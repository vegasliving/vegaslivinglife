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
		listing['Association Fee Includes'], listing['Association Name'], listing['Association Phone'], listing['Baths Full'], listing['Baths Half'],
		listing['Baths Total'],listing['Bedrooms Total Possible Num'],listing['Beds Total'],listing['Building Description'],listing['Close Price'],
		listing['Construction Description'],listing['Community Name'],listing['Directions'],listing['Dryer Included'],listing['Financing Considered'],
		listing['Flooring Description'],listing['Garage Description'],listing['House Faces'],listing['Last List Price'],listing['List Agent MUI'],
		listing['List Agent Full Name'], listing['List Office Name'], listing['List Office Phone'], listing['List Price'], listing['Matrix Unique ID'],
		listing['Matrix Modified DT'], listing['MLS Number'], listing['MLS'], listing['Photo Count'], listing['Postal Code'],listing['Property Condition'], 
		listing['Property Sub Type'], listing['Public Address'], listing['Public Remarks'], listing['Selling Agent MUI'], listing['Selling Agent Full Name'],
		listing['Selling Agent Direct Work Phone'],listing['Sq Ft Total'], listing['Street Name'], listing['Street Number'], listing['Subdivision Name'])
	
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


