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

auth = Oauth1Authenticator(
    consumer_key="xj49H3XgGKqHkKfdBrpYOA",
    consumer_secret="2TMHAvDUGv-mMOzCcZ_X_rFLoJY",
    token="b1jtqbsJIi2K4EAJVzvNWUMs4SPjfTo8",
    token_secret="y5hM7tC3e9GiltBaO4o432Z4m8Q"
)

client = Client(auth)
gmaps = googlemaps.Client(key='AIzaSyCTLthxG3Gaj12OcGK_EYU6bXXUSqDvcyg')

def home(request):
	articles = Article.objects.raw('SELECT * FROM properties_article WHERE title LIKE "%%Las Vegas%%"')[:6]
	blogpages = BlogPage.objects.all()
	return render(request, 'home/for-you.html',{"blogpages": blogpages, "articles": articles})

def stories(request):
	articles = Article.objects.raw('SELECT * FROM properties_article WHERE title LIKE "%%Rainbow%%"')[:3]
	blogpages = BlogPage.objects.all()
	return render(request, 'home/stories.html',{"blogpages": blogpages, "articles": articles})
	
def homes(request):
	articles = Article.objects.raw('SELECT * FROM properties_article WHERE title LIKE "%%Las Vegas%%"')[:20]
	blogpages = BlogPage.objects.all()
	for post in blogpages:
		print(post.title, post.intro, post.main_image())
	for article in articles:
		location = gmaps.geocode(article.title)
		if location[0] is not None:
			article.latitude = location[0]['geometry']['location']['lat']
			article.longtitude = location[0]['geometry']['location']['lng']		

	return render(request, 'home/homes.html',{"blogpages": blogpages, "articles": articles})
		
def places(request):
	articles = Article.objects.raw('SELECT * FROM properties_article WHERE title LIKE "%%Paradise%%"')[:5]
	blogpages = BlogPage.objects.all()
	return render(request, 'home/places.html',{"blogpages": blogpages, "articles": articles})
	
def home_detail(request, article_id):
	params = {
    'term': 'drink',
	}
	articles = Article.objects.raw('SELECT * FROM properties_article WHERE id=%s' % (article_id))
	for article in articles:
		bedNumber = article.numberOfBeds
		bathNumber = article.numberOfBaths
		suggested_articles = []
		homePrice =  int(re.sub("[^\d\.]", "", article.description))
		similar_articles = Article.objects.raw("""SELECT * FROM properties_article WHERE numberOfBeds=%(bedNumber)s AND numberOfBaths=%(bathNumber)s""",params={'bedNumber':bedNumber,'bathNumber': bathNumber})
		for similar_article in similar_articles:
			price = int(re.sub("[^\d\.]", "", similar_article.description))
			if price < homePrice:
				suggested_articles.append(similar_article)
				print(article.description)
				print(similar_article.description)
				print(similar_article.title)
		location = gmaps.geocode(article.title)
		if location[0] is not None:
			article.latitude = location[0]['geometry']['location']['lat']
			article.longtitude = location[0]['geometry']['location']['lng']
			responses = client.search_by_coordinates(article.latitude, article.longtitude, **params)
			places = responses.businesses
			for place in places:
				place.image = re.sub(r'ms.jpg', 'ls.jpg', place.image_url)
				place.snippet_image = re.sub(r'ms.jpg', 'ls.jpg', place.snippet_image_url)
				place.address = ' '.join(place.location.display_address)
	return render(request, 'home/your-home.html', {"articles":articles, "places":places, "suggested_articles":suggested_articles})






	
	

	
	
