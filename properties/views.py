from django.shortcuts import render
from .models import Article

def article_list(request):
	articles = Article.objects.all()
	for article in articles:
		print(article.thumbnail)
	return render(request, 'properties.html', {"articles": articles})

