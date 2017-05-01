from django.contrib.auth.decorators import login_required
from django.contrib import postgres
from django.shortcuts import render
from properties.models import Article
from blog.models import BlogPage

def home(request):
	articles = Article.objects.raw('SELECT * FROM properties_article WHERE title LIKE "%%Las Vegas%%"')[:6]
	blogpages = BlogPage.objects.all()
	for post in blogpages:
		print(post.title, post.intro, post.main_image())
	for article in articles:
		print(article)
	return render(request, 'home/for-you.html',{"blogpages": blogpages, "articles": articles})

def stories(request):
	articles = Article.objects.raw('SELECT * FROM properties_article WHERE title LIKE "%%Rainbow%%"')[:3]
	blogpages = BlogPage.objects.all()
	for post in blogpages:
		print(post.title, post.intro, post.main_image())
	for article in articles:
		print(article)
	return render(request, 'home/stories.html',{"blogpages": blogpages, "articles": articles})
	
def homes(request):
	articles = Article.objects.raw('SELECT * FROM properties_article WHERE title LIKE "%%Henderson%%"')[:10]
	blogpages = BlogPage.objects.all()
	for post in blogpages:
		print(post.title, post.intro, post.main_image())
	for article in articles:
		print(article)
	return render(request, 'home/homes.html',{"blogpages": blogpages, "articles": articles})
	
def places(request):
	articles = Article.objects.raw('SELECT * FROM properties_article WHERE title LIKE "%%Paradise%%"')[:5]
	blogpages = BlogPage.objects.all()
	for post in blogpages:
		print(post.title, post.intro, post.main_image())
	for article in articles:
		print(article)
	return render(request, 'home/places.html',{"blogpages": blogpages, "articles": articles})
	



	
	


	
	

	
	
