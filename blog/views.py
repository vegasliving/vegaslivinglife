from django.shortcuts import render
from properties.models import Article
from blog.models import BlogPage

def properties_list(request):
	articles = Article.objects.all()
	blogpages = BlogPage.objects.all()
	for article in articles:
		print(article.thumbnail)
	for blogpage in blogpages:
		print(blogpage.main_image)
	return render(request, 'blog/main.html', {"articles": articles}, {"blogpages": blogpages})

