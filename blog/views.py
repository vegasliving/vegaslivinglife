from django.shortcuts import render
from properties.models import Article
from blog.models import BlogIndexPage

def properties_list(request):
	articles = Article.objects.all()
	blogpage = BlogIndexPage.objects.all()
	for article in articles:
		print(article.thumbnail)
	return render(request, 'properties.html', {"articles": articles})

