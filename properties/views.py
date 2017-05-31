from django.shortcuts import render
from .models import Article
from home.models import Listing
import googlemaps
import csv
from pprint import pprint
from django.conf import settings


gmaps = googlemaps.Client(key='AIzaSyDhMoj3bF9Cw2PJ08_vbKZruTWLXM4X28o')

def article_list(request):
	listings = convert(csvfile)
	pprint(listings[0])
	for listing in listings:
		pprint(listing)
			listing = Listing.objects.create_listing(
			listing['Area'], listing['Association Features Available'], listing['Association Fee 1'], listing['Association Fee 1 MQYN'],
			listing['Assoctiation Fee Includes'], listing['Association Name'], listing[''], listing[''], listing[''],
			listing[''],listing[''],listing[''],listing[''],listing[''],
			listing[''],listing[''],listing[''],listing[''],listing[''],
			listing[''],listing[''],listing[''],listing[''],listing['']
	
# area, associationFeaturesAvailable, associationFee, associationFeeMQYN, associationFeeIncludes, associationName, associationPhoneNumber,
#     	bathsFull, bathsHalf, bathsTotal, bedroomsTotalPossibleNumber, bedsTotal, buildingDescription, closePrice, contructionDescription,
#     	communityName, directions, dryerIncluded, financingConsidered, flooringDescription, garageDescription, houseFaces, lastListPrice, 
#     	listAgentMUI, listAgentFullName, listAgentOfficeName, listOfficePhone, listPrice, matrixUniqueID, matrixModifiedDT, mlsNumber, mls,
#     	photoCount, postalCode, propertyCondition, propertySubType, publicAddress, publicRemarks, sellingAgentMUI, sellingAgentFullName, 
#     	sellingAgentDirectWorkPhone, streetName, streetNumber, subdivisionName, sqftTotal



	articles = Article.objects.all()[:9]
	for article in articles:
		location = gmaps.geocode(article.title)
		if location[0] is not None:
			latitude = location[0]['geometry']['location']['lat']
			longtitude = location[0]['geometry']['location']['lng']		
			# print(latitude, longtitude)
			# print(article.thumbnail)
		
	return render(request, 'properties.html', {"articles": articles})

def convert(csvfile):
	with open(csvfile) as f:
	    reader = csv.reader(f, skipinitialspace=True)
	    header = next(reader)
	    listings = [dict(zip(header, map(str, row))) for row in reader]
	return listings

csvfile = 'listings.csv'


