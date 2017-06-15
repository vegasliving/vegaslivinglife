from django.contrib.auth.decorators import login_required
from django.contrib import postgres
from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from properties.models import Article
from . models import Listing, Story, Lead
from blog.models import BlogPage
import googlemaps
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import re
from django.forms import ModelForm
import keys
from pprint import pprint
from . stories import getStory
from . forms import PodioForm
from . podio import createLead
from pypodio2 import api

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
	coolSpots = findCoolSpot(articles[1])
	pprint(coolSpots)
	suggestedRestaurants = coolSpots[0]
	suggestedBars = coolSpots[1]
	suggestedStores = coolSpots[2]
	suggestedPlays = coolSpots[3]

	# print(suggestedRestaurants[0], suggestedBars[0], suggestedStores[0], suggestedPlays[0])
	# print(suggestedPlays[0])

	# for url in urls:
	# 	story = getStory(url)
	# 	print(len(story))
	# 	vegasStory = Story.objects.create_story(story[0], story[1], story[2], story[3], story[4])
	
	stories = Story.objects.all()
	return render(request, 'home/for-you.html',{
		"stories": stories, 
		"articles": articles,
		"suggestedRestaurants":suggestedRestaurants,
		"suggestedBars":suggestedBars,
		"suggestedStores":suggestedStores,
		"suggestedPlays":suggestedPlays
	})

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

	plays = {
	'term': 'active',
	}

	articles = Listing.objects.filter(matrixUniqueID="%s"%(article_id))
	# articles = Listing.objects.raw('SELECT * FROM properties_article WHERE id=%s' % (article_id))
	for article in articles:
	# 	area, associationFeaturesAvailable, associationFee, associationFeeMQYN, associationFeeIncludes, associationName, associationPhone,
  #   	bathsFull, bathsHalf, bathsTotal, bedroomsTotalPossibleNum, bedsTotal, buildingDescription, closePrice, contructionDescription,
  #   	communityName, directions, dryerIncluded, financingConsidered, flooringDescription, garageDescription, houseFaces, lastListPrice, 
  #   	listAgentMUI, listAgentFullName, listOfficeName, listOfficePhone, listPrice, matrixUniqueID, matrixModifiedDT, mlsNumber, mls,
  #   	photoCount, postalCode, propertyCondition, propertySubType, publicAddress, publicRemarks, sellingAgentMUI, sellingAgentFullName, 
  #   	sellingAgentDirectWorkPhone, sqftTotal, streetName, streetNumber, subdivisionName
		form = PodioForm()
		if request.method == 'POST':
			form = PodioForm(request.POST)
			if form.is_valid():
				data = form.cleaned_data
				print(data)
				createLead(data['firstName'], data['lastName'],str(data['phone']), data['email'], article.matrixUniqueID)
				Lead.objects.create_lead(data['firstName'], data['lastName'],data['phone'], data['email'], article.matrixUniqueID)
				return HttpResponseRedirect('/home-%s'%(article.matrixUniqueID))
		pprint(vars(article))
		article.image = ("Las%20Vegas%20Active%20Listing"+"/LargePhoto%s-0" %(article.matrixUniqueID))
		bedNumber = article.bedsTotal
		bathNumber = article.bathsTotal
		suggested_articles = []
		homePrice =  article.listPrice
		similar_articles = Listing.objects.filter(bedsTotal=bedNumber).filter(bathsTotal=bathNumber).filter(matrixUniqueID__startswith="11")
		# similar_articles = Article.objects.raw("""SELECT * FROM properties_article WHERE numberOfBeds=%(bedNumber)s AND numberOfBaths=%(bathNumber)s""",params={'bedNumber':bedNumber,'bathNumber': bathNumber})[:30]
		for similar_article in similar_articles:
			price = similar_article.listPrice
			if price < homePrice*1.1 and similar_article.matrixUniqueID != article.matrixUniqueID:
				similar_article.image = ("Las%20Vegas%20Active%20Listing"+"/LargePhoto%s-0" %(similar_article.matrixUniqueID))
				suggested_articles.append(similar_article)
				# print(article.listPrice)
				# print(similar_article.listPrice)
				# print(similar_article.publicAddress)
		address = "%s %s, Las Vegas, NV, %s" %(article.streetNumber, article.streetName, article.postalCode)
		location = gmaps.geocode(address)
		# pprint(location)
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
			plays = client.search_by_coordinates(article.latitude,article.longtitude, **plays)

			suggestedRestaurants = restaurants.businesses
			suggestedBars = bars.businesses
			suggestedStores = stores.businesses
			suggestedPlays = plays.businesses

			# REMEMBER TO REFACTOR AND REWRITE FUNCTION to pass in different cool places

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
					# print(suggestedStore.name)    
					# print(suggestedStore.address)
					# print(suggestedStore.image)
					# print(suggestedStore.snippet_image)
					# print(suggestedStore.snippet_text)

			for suggestedPlay in suggestedPlays:
				if suggestedPlay.image_url is not None:
					suggestedPlay.image = re.sub(r'ms.jpg', 'ls.jpg', suggestedPlay.image_url)
					suggestedPlay.snippet_image = re.sub(r'ms.jpg', 'ls.jpg', suggestedPlay.snippet_image_url)
					suggestedPlay.address = ' '.join(suggestedPlay.location.display_address)
					# print(suggestedPlay.name)
					print(suggestedPlay.address)
					print(suggestedPlay.image)
					print(suggestedPlay.snippet_image)
					print(suggestedPlay.snippet_text)
				
	return render(
		request, 'home/your-home.html', 
		{"articles":articles, "form":form, "suggestedRestaurants":suggestedRestaurants, "suggestedBars":suggestedBars, 
		"suggestedStores":suggestedStores, "suggestedPlays":suggestedPlays, "suggested_articles":suggested_articles}
	)

def newLead(request): 
	leads = Lead.objects.all()
	for lead in leads:
		pprint(vars(lead))
	return render(request, 'home/leads.html', {"leads":leads})

def findCoolSpot(article):
	restaurants = {'term': 'food',}
	bars = {'term': 'drink',}
	stores = {'term': 'shopping',}
	plays = {'term': 'active',}
	address = "%s %s, Las Vegas, NV, %s" %(article.streetNumber, article.streetName, article.postalCode)
	print(address)
	location = gmaps.geocode(address)
	if location[0] is not None:
		article.latitude = location[0]['geometry']['location']['lat']
		article.longtitude = location[0]['geometry']['location']['lng'] 

		restaurants = client.search_by_coordinates(article.latitude, article.longtitude, **restaurants)
		bars = client.search_by_coordinates(article.latitude, article.longtitude, **bars)
		stores = client.search_by_coordinates(article.latitude, article.longtitude, **stores)
		plays = client.search_by_coordinates(article.latitude,article.longtitude, **plays)

		suggestedRestaurants = restaurants.businesses
		suggestedBars = bars.businesses
		suggestedStores = stores.businesses
		suggestedPlays = plays.businesses

		for suggestedRestaurant in suggestedRestaurants:
					suggestedRestaurant.image = re.sub(r'ms.jpg', 'ls.jpg', suggestedRestaurant.image_url)
					suggestedRestaurant.snippet_image = re.sub(r'ms.jpg', 'ls.jpg', suggestedRestaurant.snippet_image_url)
					suggestedRestaurant.address = ' '.join(suggestedRestaurant.location.display_address)
					# print(suggestedRestaurant.address)

		for suggestedBar in suggestedBars:
			suggestedBar.image = re.sub(r'ms.jpg', 'ls.jpg', suggestedBar.image_url)
			suggestedBar.snippet_image = re.sub(r'ms.jpg', 'ls.jpg', suggestedBar.snippet_image_url)
			suggestedBar.address = ' '.join(suggestedBar.location.display_address)
			# print(suggestedBar.address)
		
		for suggestedStore in suggestedStores:
			if suggestedStore.image_url is not None:
				suggestedStore.image = re.sub(r'ms.jpg', 'ls.jpg', suggestedStore.image_url)
				suggestedStore.snippet_image = re.sub(r'ms.jpg', 'ls.jpg', suggestedStore.snippet_image_url)
				suggestedStore.address = ' '.join(suggestedStore.location.display_address)
				# print(suggestedStore.address)

		for suggestedPlay in suggestedPlays:
			if suggestedPlay.image_url is not None:
				suggestedPlay.image = re.sub(r'ms.jpg', 'ls.jpg', suggestedPlay.image_url)
				suggestedPlay.snippet_image = re.sub(r'ms.jpg', 'ls.jpg', suggestedPlay.snippet_image_url)
				suggestedPlay.address = ' '.join(suggestedPlay.location.display_address)
				# print(suggestedPlay.name) 

	return suggestedRestaurants, suggestedBars, suggestedStores, suggestedPlays
	
	

	
	
