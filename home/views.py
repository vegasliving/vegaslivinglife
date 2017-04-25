from django.contrib.auth.decorators import login_required
from django.contrib import postgres
from django.shortcuts import render
from properties.models import Article
from blog.models import BlogPage

def home(request):
	articles = Article.objects.raw('SELECT * FROM properties_article WHERE title LIKE "%%Rainbow%%"')[:3]
	blogpages = BlogPage.objects.all()
	for post in blogpages:
		print(post.title, post.intro, post.main_image())
	for article in articles:
		print(article)
	return render(request, 'home/home.html',{"blogpages": blogpages, "articles": articles})

# def logout(request):
# 	return render(request, 'home/home_page.html')

	
	
