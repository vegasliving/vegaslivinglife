from django.contrib.auth.decorators import login_required
from django.contrib import postgres
from django.shortcuts import render
from properties.models import Article
from blog.models import BlogPage

def properties_list(request):
	word = "rainbow"
	articles = Article.objects.raw('SELECT * FROM properties_article WHERE title LIKE "%%Rainbow%%"')[:100]
	blogpages = BlogPage.objects.all()
	for post in blogpages:
		print(post.title, post.intro, post.main_image())
	for article in articles:
		print(article)
	return render(request, 'blog/main.html', {"blogpages": blogpages, "articles": articles})

