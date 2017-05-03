from django.shortcuts import render
from .models import Article
import googlemaps
from django.conf import settings

gmaps = googlemaps.Client(key='AIzaSyCTLthxG3Gaj12OcGK_EYU6bXXUSqDvcyg')

def article_list(request):
	articles = Article.objects.all()
	for article in articles:
		location = gmaps.geocode(article.title)
		if location[0] is not None:
			latitude = location[0]['geometry']['location']['lat']
			longtitude = location[0]['geometry']['location']['lng']		
			print(latitude, longtitude)
			print(article.thumbnail)
		
	return render(request, 'properties.html', {"articles": articles})

