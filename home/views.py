from django.contrib.auth.decorators import login_required
from django.contrib import postgres
from django.shortcuts import render
from django.views.generic import DetailView
from properties.models import Article
from blog.models import BlogPage
import googlemaps
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import re
from django.forms import ModelForm
import keys


auth = keys.myAuth
client = Client(auth)
gmaps = googlemaps.Client(key=keys.myGeoCodingKey)

def home(request):
	address_input = ""
	price_input = ""
	bedroomInput = "3 Bed(s) |"
	bathroomInput = "3 Bath(s)"
	articles = Article.objects.filter(title__icontains=address_input).filter(numberOfBeds=bedroomInput).filter(numberOfBaths=bathroomInput)[:9]
	blogpages = BlogPage.objects.all()
	return render(request, 'home/for-you.html',{"blogpages": blogpages, "articles": articles})

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
	'term': 'shopping',
	}

	articles = Article.objects.raw('SELECT * FROM properties_article WHERE id=%s' % (article_id))
	for article in articles:
		bedNumber = article.numberOfBeds
		bathNumber = article.numberOfBaths
		suggested_articles = []
		homePrice =  int(re.sub("[^\d\.]", "", article.description))
		similar_articles = Article.objects.raw("""SELECT * FROM properties_article WHERE numberOfBeds=%(bedNumber)s AND numberOfBaths=%(bathNumber)s""",params={'bedNumber':bedNumber,'bathNumber': bathNumber})[:30]
		for similar_article in similar_articles:
			price = int(re.sub("[^\d\.]", "", similar_article.description))
			if price < homePrice*1.1 and similar_article.id != article.id:
				suggested_articles.append(similar_article)
				print(article.description)
				print(similar_article.description)
				print(similar_article.title)
		location = gmaps.geocode(article.title)
		if location[0] is not None:
			article.zipcode = location[0]['address_components'][8]['long_name']
			print(">>>>>>>>>>>>>>>>>>>>>",article.zipcode)
			# results = findjob(article.zipcode,'')
			# for result in results:
			# 	print(result['jobtitle'],'----------',result['formattedLocation'],'----------',result['company'],'----------',result['url'])
			article.latitude = location[0]['geometry']['location']['lat']
			article.longtitude = location[0]['geometry']['location']['lng']
			print(gmaps.reverse_geocode([article.latitude, article.longtitude]))
			
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
				suggestedStore.image = re.sub(r'ms.jpg', 'ls.jpg', suggestedStore.image_url)
				suggestedStore.snippet_image = re.sub(r'ms.jpg', 'ls.jpg', suggestedStore.snippet_image_url)
				suggestedStore.address = ' '.join(suggestedStore.location.display_address)
	return render(request, 'home/your-home.html', {"articles":articles, "suggestedRestaurants":suggestedRestaurants, "suggestedBars":suggestedBars, "suggestedStores":suggestedStores, "suggested_articles":suggested_articles})




	
	

	
	
