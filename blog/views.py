from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from properties.models import Article
from blog.models import BlogPage

def properties_list(request):
	articles = Article.objects.all()
	blogpages = BlogPage.objects.all()
	for post in blogpages:
		print(post.title, post.intro, post.main_image())
	return render(request, 'blog/main.html', {"blogpages": blogpages, "articles": articles})

