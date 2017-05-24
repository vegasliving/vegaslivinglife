from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models as gismodels

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
    	FieldPanel('body', classname="full"),
    ]

class ListingManager(models.Manager):
    def create_Listing(
    	area, association, associationFee, associationFeeMQYN, associationFeeIncludes, associationName, associationPhoneNumber,
    	bathsFull, bathsHalf, bathsTotal, bedroomsTotalPossibleNumber, bedsTotal, buildingDescription, closePrice, contructionDescription,
    	communityName, directions, dryerIncluded, financingConsidered, flooringDescription, garageDescription, houseFaces, lastListPrice, 
    	listAgentMUI, listAgentFullName, listAgentOfficeName, listOfficePhone, listPrice, matrixUniqueID, matrixModifiedDT, mlsNumber, mls,
    	photoCount, postalCode, propertyCondition, propertySubType, publicAddress, publicRemarks, sellingAgentMUI, sellingAgentFullName, 
    	sellingAgentDirectWorkPhone, streetName, streetNumber, subdivisionName, sqftTotal):

        Listing = self.create(
        area=area, association=association, associationFee=associationFee, associationFeeMQYN=associationFeeMQYN, 
        associationFeeIncludes=associationFeeIncludes, associationName=associationName, associationPhoneNumber=associationPhoneNumber,
    	bathsFull=bathsFull, bathsHalf=bathsFull, bathsTotal=bathsTotal, bedroomsTotalPossibleNumber=bedroomsTotalPossibleNumber, bedsTotal=bedsTotal,
    	buildingDescription=buildingDescription, closePrice=closePrice, contructionDescription=contructionDescription,communityName=communityName,
    	directions=directions,dryerIncluded=dryerIncluded, financingConsidered=financingConsidered, flooringDescription=flooringDescription,
    	garageDescription=garageDescription, houseFaces=houseFaces, lastListPrice=lastListPrice, listAgentMUI=listAgentMUI, listAgentFullName=listAgentFullName,
    	listAgentOfficeName=listAgentOfficeName, listOfficePhone=listOfficePhone, listPrice=listPrice, matrixUniqueID=matrixUniqueID, 
    	matrixModifiedDT=matrixModifiedDT, mlsNumber=mlsNumber, mls=mls, photoCount=photoCount, postalCode=postalCode, propertyCondition=propertyCondition,
    	propertySubType=propertySubType, publicAddress=publicAddress, publicRemarks=publicRemarks, sellingAgentMUI=sellingAgentMUI, 
    	sellingAgentFullName=sellingAgentFullName, sellingAgentDirectWorkPhone=sellingAgentDirectWorkPhone, streetName=streetName, streetNumber=streetNumber,
    	subdivisionName=subdivisionName, sqftTotal=sqftTotal)
        return Listing

class Listing(models.Model):
	area = models.CharField(max_length=300)
	associationFeaturesAvailable = models.CharField(max_length=1000) 
	associationFee = models.IntegerField(null=True, blank=True)
	associationFeeMQYN = models.CharField(max_length=200)
	associationFeeIncludes = models.CharField(max_length=1000)
	associationName = models.CharField(max_length=200)
	associationPhoneNumber = models.CharField(max_length=200)
	bathsFull = models.IntegerField(null=True, blank=True)
	bathsHalf = models.IntegerField(null=True, blank=True)
	bathsTotal = models.IntegerField(null=True, blank=True)
	bedroomsTotalPossibleNumber = models.IntegerField(null=True, blank=True)
	bedsTotal = models.IntegerField(null=True, blank=True)
	buildingDescription = models.CharField(max_length=200)
	closePrice = models.IntegerField(null=True, blank=True)
	contructionDescription = models.CharField(max_length=300)
	communityName = models.CharField(max_length=300)
	directions = models.CharField(max_length=2000)
	dryerIncluded = models.IntegerField(null=True, blank=True)
	financingConsidered = models.CharField(max_length=300)
	flooringDescription = models.CharField(max_length=300)
	garageDescription = models.CharField(max_length=500)
	houseFaces = models.CharField(max_length=100)
	lastListPrice = models.IntegerField(null=True, blank=True)
	listAgentMUI = models.IntegerField(null=True, blank=True)
	listAgentFullName = models.CharField(max_length=300)
	listOfficeName = models.CharField(max_length=300)
	listOfficePhone = models.CharField(max_length=200)
	matrixUniqueID = models.IntegerField(null=True, blank = True)
	matrixModifiedDT = models.TimeField(auto_now=False, auto_now_add=False)
	mlsNumber = models.IntegerField(null=True, blank=True)
	mls = models.CharField(max_length=100)
	photoCount = models.IntegerField(null=True, blank=True)
	postalCode = models.CharField(max_length=10)
	propertyCondition = models.CharField(max_length=100)
	propertySubType = models.CharField(max_length=100)
	publicAddress = models.CharField(max_length=300)
	publicRemarks = models.CharField(max_length=1000)
	sellingAgentMUI = models.IntegerField(null=True, blank=True)
	sellingAgentFullName = models.CharField(max_length=400)
	sellingAgentDirectWorkPhone = models.CharField(max_length=300)
	streetName = models.CharField(max_length=200)
	streetNumber = models.IntegerField(null=True, blank=True)
	subdivisionName = models.CharField(max_length=200)
	sqftTotal = models.IntegerField(null=True, blank=True)
	objects = ListingManager()

# fieldnames = ("Area","Association Features Available", "Association Fee 1", "Association Fee 1 MQYN",
# 	"Association Fee Includes","Association Name","Association Phone","Baths Full","Baths Half","Baths Total",
# 	"Bedrooms Total Possible Num","Beds Total","Building Description","Close Price","Construction Description",
# 	"Community Name","Current Price","Directions","Dryer Included","Dryer Utilities","Financing Considered",
# 	"Flooring Description","Garage Description","House Faces","Last List Price","List Agent MUI","List Agent Full Name",
# 	"List Office Name","List Office Phone","List Price","Matrix Unique ID","Matrix Modified DT","MLS Number","MLS","MLS Photo Count",
# 	"Postal Code","Property Condition","Property Sub Type","Public Address","Public Remarks","Selling Agent MUI",
# 	"Selling Agent Full Name","Selling Agent Direct Work Phone","Street Name","Street Number","Subdivision Name","Sq Ft Total")

# Area 303 - South
# Association Features Available CC&RS
# Association Fee 1 
# Association Fee 1 MQYN 
# Association Fee Includes 
# Association Name 
# Association Phone 
# Baths Full 2
# Baths Half 1
# Baths Total 3.00
# Bedrooms Total Possible Num 4
# Beds Total 4
# Building Description 2  Stories
# Close Price 
# Construction Description Frame & Stucco
# Community Name Silverado Ranch
# Current Price 1650.00
# Directions FROM PEBBLE SOUTH ON MARYLAND PKWY, RIGHT ON STORMY VALLEY.
# Dryer Included 
# Dryer Utilities Gas
# Financing Considered 
# Flooring Description 
# Garage Description Attached
# House Faces West
# Last List Price 
# List Agent MUI 9630716
# List Agent Full Name Kimberly Kingham
# List Office Name American Homes 4 Rent
# List Office Phone 702-703-5296
# List Price 1650.00
# Matrix Unique ID 129022325
# Matrix Modified DT 2017-05-22T16:48:25.723
# MLS Number 1899553
# MLS LAS
# Photo Count 20
# Postal Code 89123
# Property Condition 
# Property Sub Type 
# Public Address 
# Public Remarks GREAT 4 BEDROOM HOME IN SILVERADO RANCH AREA, VERY CLEAN AND RENT READY NOW.
# Selling Agent MUI 
# Selling Agent Full Name 
# Selling Agent Direct Work Phone 
# Street Name STORMY VALLEY
# Street Number 1153
# Subdivision Name MOONDANCE AT SILVERADO RANCH
# Sq Ft Total 1915
# Area 301 - South
# Association Features Available None
# Association Fee 1 
# Association Fee 1 MQYN 
# Association Fee Includes 
# Association Name 
# Association Phone 
# Baths Full 2
# Baths Half 0
# Baths Total 2.00
# Bedrooms Total Possible Num 3
# Beds Total 3
# Building Description 1  Story
# Close Price 
# Construction Description Frame & Stucco
# Community Name None
# Current Price 1300.00
# Directions From Eastern & Sahara; West on Sahara to Mariposa; Right on Mariposa to 2308 on Left.
# Dryer Included 
# Dryer Utilities Gas
# Financing Considered 
# Flooring Description 
# Garage Description Attached,Entryto House
# House Faces East
# Last List Price 
# List Agent MUI 9624220
# List Agent Full Name Debra Ballard
# List Office Name Ballard Realty Group
# List Office Phone 702-570-6400
# List Price 1300.00
# Matrix Unique ID 129022449
# Matrix Modified DT 2017-05-22T16:54:27.003
# MLS Number 1899554
# MLS LAS
# Photo Count 0
# Postal Code 89104
# Property Condition 
# Property Sub Type 
# Public Address 
# Public Remarks Comfortable open floor plan.  Neutral colors.  Refrigerator, washer an dryer are included.  Conveniently located to shopping, schools and the Las Vegas strip.  Two car attached garage.
# Selling Agent MUI 
# Selling Agent Full Name 
# Selling Agent Direct Work Phone 
# Street Name MARIPOSA
# Street Number 2308
# Subdivision Name METROPOLITAN ADD AMD
# Sq Ft Total 1316