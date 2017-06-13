from django.contrib.auth.decorators import login_required
from django.contrib import postgres
from django.shortcuts import render
from django.views.generic import DetailView
from properties.models import Article
from . models import Listing
from . models import Story
from blog.models import BlogPage
import googlemaps
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import re
from django.forms import ModelForm
import keys
from pprint import pprint
from . stories import getStory

auth = keys.myAuth
client = Client(auth)
gmaps = googlemaps.Client(key=keys.myGeoCodingKey)
urls = [
"https://www.reviewjournal.com/weather/monday-cool-before-dramatic-warm-up-in-las-vegas-valley/",
"https://lasvegassun.com/news/2017/jun/12/las-vegans-breaking-barriers-in-science/",
"http://www.prnewswire.com/news-releases/tropicana-las-vegas-to-host-gary-leffews-bucking-ball-december-7-16-2017-300471915.html",
"https://lasvegassun.com/news/2017/jun/12/unlv-officials-say-parking-is-adequate-but-student/"
]

def home(request):
	address_input = ""
	price_input = ""
	bedroomInput = "3 Bed(s) |"
	bathroomInput = "3 Bath(s)"
	postalCode = "89118"
	# articles = Article.objects.filter(title__icontains=address_input).filter(numberOfBeds=bedroomInput).filter(numberOfBaths=bathroomInput)[:9]
	articles = Listing.objects.filter(matrixUniqueID__startswith="11").filter(bedsTotal__icontains="3")[:9]
	for article in articles:
		article.image = ("Las%20Vegas%20Active%20Listing"+"/LargePhoto%s-0" %(article.matrixUniqueID))
	# for url in urls:
	# 	story = getStory(url)
	# 	print(len(story))
	# 	vegasStory = Story.objects.create_story(story[0], story[1], story[2], story[3], story[4])
	
	stories = Story.objects.all()
	return render(request, 'home/for-you.html',{"stories": stories, "articles": articles})

def stories(request):
	articles = Article.objects.raw('SELECT * FROM properties_article WHERE title LIKE "%%Rainbow%%"')[:3]
	blogpages = BlogPage.objects.all()
	return render(request, 'home/stories.html',{"blogpages": blogpages, "articles": articles})
	
def homes(request):
	address_input = "Las Vegas"
	price_input = ""
	bedroomInput = "2"
	bathroomInput = "3"
	articles = Article.objects.filter(title__icontains=address_input).filter(numberOfBeds__icontains=bedroomInput).filter(numberOfBaths__contains=bathroomInput)[:10]
	for article in articles:
		location = gmaps.geocode(article.title)
		if location[0] is not None:
			article.price = article.description
			article.latitude = location[0]['geometry']['location']['lat']
			article.longtitude = location[0]['geometry']['location']['lng']	
	return render(request, 'home/homes.html',{"articles": articles})
		
def places(request):
	articles = Article.objects.raw('SELECT * FROM properties_article WHERE title LIKE "%%Paradise%%"')[:5]
	blogpages = BlogPage.objects.all()
	return render(request, 'home/places.html',{"blogpages": blogpages, "articles": articles})
	
def home_detail(request, article_id):
	restaurants = {
    'term': 'food',
	}
	bars = {
	'term': 'drink',
	}
	stores = {
	'term': 'active',
	}
	articles = Listing.objects.filter(matrixUniqueID = article_id)
	# articles = Listing.objects.raw('SELECT * FROM properties_article WHERE id=%s' % (article_id))
	for article in articles:
		bedNumber = article.bedsTotal
		bathNumber = article.bathsTotal
		suggested_articles = []
		homePrice =  article.listPrice
		similar_articles = Listing.objects.filter(bedsTotal=bedNumber).filter(bathsTotal=bathNumber)
		# similar_articles = Article.objects.raw("""SELECT * FROM properties_article WHERE numberOfBeds=%(bedNumber)s AND numberOfBaths=%(bathNumber)s""",params={'bedNumber':bedNumber,'bathNumber': bathNumber})[:30]
		for similar_article in similar_articles:
			price = similar_article.listPrice
			if price < homePrice*1.1 and similar_article.id != article.id:
				suggested_articles.append(similar_article)
				# print(article.listPrice)
				# print(similar_article.listPrice)
				# print(similar_article.publicAddress)
		address = "%s, %s, Las Vegas, NV, %s" %(article.streetNumber, article.streetName, article.postalCode)
		location = gmaps.geocode(address)
		pprint(location)
		if location[0] is not None:
			# article.zipcode = location[0]['address_components'][7]['long_name']
			# print(">>>>>>>>>>>>>>>>>>>>>",article.zipcode)
			# results = findjob(article.zipcode,'')
			# for result in results:
			# 	print(result['jobtitle'],'----------',result['formattedLocation'],'----------',result['company'],'----------',result['url'])
			article.latitude = location[0]['geometry']['location']['lat']
			article.longtitude = location[0]['geometry']['location']['lng']
			# print(gmaps.reverse_geocode([article.latitude, article.longtitude]))
			
			restaurants = client.search_by_coordinates(article.latitude, article.longtitude, **restaurants)
			bars = client.search_by_coordinates(article.latitude, article.longtitude, **bars)
			stores = client.search_by_coordinates(article.latitude, article.longtitude, **stores)

			suggestedRestaurants = restaurants.businesses
			suggestedBars = bars.businesses
			suggestedStores = stores.businesses
			# Write function to pass in different cool place

			for suggestedRestaurant in suggestedRestaurants:
				suggestedRestaurant.image = re.sub(r'ms.jpg', 'ls.jpg', suggestedRestaurant.image_url)
				suggestedRestaurant.snippet_image = re.sub(r'ms.jpg', 'ls.jpg', suggestedRestaurant.snippet_image_url)
				suggestedRestaurant.address = ' '.join(suggestedRestaurant.location.display_address)
			for suggestedBar in suggestedBars:
				suggestedBar.image = re.sub(r'ms.jpg', 'ls.jpg', suggestedBar.image_url)
				suggestedBar.snippet_image = re.sub(r'ms.jpg', 'ls.jpg', suggestedBar.snippet_image_url)
				suggestedBar.address = ' '.join(suggestedBar.location.display_address)
			for suggestedStore in suggestedStores:
				if suggestedStore.image_url is not None:
					suggestedStore.image = re.sub(r'ms.jpg', 'ls.jpg', suggestedStore.image_url)
					suggestedStore.snippet_image = re.sub(r'ms.jpg', 'ls.jpg', suggestedStore.snippet_image_url)
					suggestedStore.address = ' '.join(suggestedStore.location.display_address)
					print(suggestedStore.name)
					print(suggestedStore.address)
					print(suggestedStore.image)
					print(suggestedStore.snippet_image)
					print(suggestedStore.snippet_text)
				
	return render(request, 'home/your-home.html', {"articles":articles, "suggestedRestaurants":suggestedRestaurants, "suggestedBars":suggestedBars, "suggestedStores":suggestedStores, "suggested_articles":suggested_articles})




	
	

	
	
