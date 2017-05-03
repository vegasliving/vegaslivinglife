from django.contrib.auth.decorators import login_required
from django.contrib import postgres
from django.shortcuts import render
from django.views.generic import DetailView
from properties.models import Article
from blog.models import BlogPage
import googlemaps

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
	articles = Article.objects.raw('SELECT * FROM properties_article WHERE id=%s' % (article_id))
	for article in articles:
		print(article.size)
	return render(request, 'home/your-home.html', {"articles":articles})




	
	


	
	

	
	
