from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from properties.models import Article
from blog.models import BlogPage

@login_required
def login(request):
	word = "rainbow"
	articles = Article.objects.raw('SELECT * FROM properties_article WHERE title LIKE "%%Rainbow%%"')[:100]
	blogpages = BlogPage.objects.all()
	for post in blogpages:
		print(post.title, post.intro, post.main_image())
	for article in articles:
		print(article)
	return render(request, 'home/home_page.html')

def logout(request):
	return render(request, 'home/home_page.html')

	
	
