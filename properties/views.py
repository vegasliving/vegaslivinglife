from django.shortcuts import render
from .models import Article
from home.models import Listing
import googlemaps
import csv
from pprint import pprint
from django.conf import settings
from .download import downloadImage
# from django.template.defaultfilters import Listing, baseUrl

csvfile = 'vegasActiveListing.csv'
gmaps = googlemaps.Client(key='AIzaSyDhMoj3bF9Cw2PJ08_vbKZruTWLXM4X28o')

def article_list(request):
	listings = convert(csvfile)
	print(len(listings))
	# for i in range(0,4983):
	# 	listing = listings[i]
	# 	if len(listing.keys()) > 1:
	# 		print(listing)
	# 		vegasListing = Listing.objects.create_listing(
	# 		listing['Area'], listing['Association Features Available'], listing['Association Fee 1'], listing['Association Fee 1 MQYN'],
	# 		listing['Association Fee Includes'], listing['Association Name'], listing['Association Phone'], float("".join(('0',listing['Baths Full']))), float("".join(('0',listing['Baths Half']))),
	# 		float("".join(('0',listing['Baths Total']))),float("".join(('0',listing['Bedrooms Total Possible Num']))),float("".join(('0',listing['Beds Total']))),listing['Building Description'],float("".join(('0',listing['Close Price']))),
	# 		listing['Construction Description'],listing['Community Name'],listing['Directions'],float("".join(('0',listing['Dryer Included']))),listing['Financing Considered'],
	# 		listing['Flooring Description'],listing['Garage Description'],listing['House Faces'],float("".join(('0',listing['Last List Price']))),listing['List Agent MUI'],
	# 		listing['List Agent Full Name'], listing['List Office Name'], listing['List Office Phone'], float("".join(('0',listing['List Price']))), listing['Matrix Unique ID'],
	# 		listing['Matrix Modified DT'], listing['MLS Number'], listing['MLS'], float("".join(('0',listing['Photo Count']))), listing['Postal Code'],listing['Property Condition'], 
	# 		listing['Property Sub Type'], listing['Public Address'], listing['Public Remarks'], listing['Selling Agent MUI'], listing['Selling Agent Full Name'],
	# 		listing['Selling Agent Direct Work Phone'],float("".join(('0',listing['Sq Ft Total']))), listing['Street Name'], listing['Street Number'], listing['Subdivision Name'])
	# 	else:
	# 		print("69696969696969")
	# print(Listing.objects.count())
	vegasListings = Listing.objects.filter(matrixUniqueID__startswith="11")|Listing.objects.filter(matrixUniqueID__startswith="10")  #12159 #13174	#116469 #146820
	for vegasListing in vegasListings:
		print(vegasListing.matrixUniqueID, vegasListing.photoCount)
		vegasListing.image = ("Las%20Vegas%20Active%20Listing"+"/LargePhoto%s-0" %(vegasListing.matrixUniqueID))
		print(vegasListing.image)
	# 	downloadImage(vegasListing.matrixUniqueID, vegasListing.photoCount)
	# 	vegasListing.image = downloadImage(vegasListing.matrixUniqueID, vegasListing.photoCount)
	# 	vegasListing.image = []
	# 	photoCount = vegasListing.photoCount
	# 	# for count in range(0,int(i)):
	# 	for photoCount in range(1,int(photoCount)):
	# 		vegasListing.image.extend(downloadImage(vegasListing.matrixUniqueID, photoCount))

	print("-------%s--------" %(len(vegasListings)))
	articles = Article.objects.all()[:9]
	for article in articles:
		location = gmaps.geocode(article.title)
		if location[0] is not None:
			latitude = location[0]['geometry']['location']['lat']
			longtitude = location[0]['geometry']['location']['lng']		
			# print(latitude, longtitude)
			# print(article.thumbnail)
		
	return render(request, 'properties.html', {"articles": articles,"listings":vegasListings})

def convert(csvfile):
	with open(csvfile) as f:
	    reader = csv.reader(f, skipinitialspace=True)
	    header = next(reader)
	    listings = [dict(zip(header, map(str, row))) for row in reader]
	return listings


