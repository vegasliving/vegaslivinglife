from django.db import models

class ListingManager(models.Manager):
    def create_listing(self,
    	area, associationFeaturesAvailable, associationFee, associationFeeMQYN, associationFeeIncludes, associationName, associationPhone,
    	bathsFull, bathsHalf, bathsTotal, bedroomsTotalPossibleNum, bedsTotal, buildingDescription, closePrice, contructionDescription,
    	communityName, directions, dryerIncluded, financingConsidered, flooringDescription, garageDescription, houseFaces, lastListPrice, 
    	listAgentMUI, listAgentFullName, listOfficeName, listOfficePhone, listPrice, matrixUniqueID, matrixModifiedDT, mlsNumber, mls,
    	photoCount, postalCode, propertyCondition, propertySubType, publicAddress, publicRemarks, sellingAgentMUI, sellingAgentFullName, 
    	sellingAgentDirectWorkPhone, sqftTotal, streetName, streetNumber, subdivisionName):

        listing = self.create(
        area=area, associationFeaturesAvailable=associationFeaturesAvailable, associationFee=associationFee, associationFeeMQYN=associationFeeMQYN, 
        associationFeeIncludes=associationFeeIncludes, associationName=associationName, associationPhone=associationPhone,
    	bathsFull=bathsFull, bathsHalf=bathsFull, bathsTotal=bathsTotal, bedroomsTotalPossibleNum=bedroomsTotalPossibleNum, bedsTotal=bedsTotal,
    	buildingDescription=buildingDescription, closePrice=closePrice, contructionDescription=contructionDescription,communityName=communityName,
    	directions=directions,dryerIncluded=dryerIncluded, financingConsidered=financingConsidered, flooringDescription=flooringDescription,
    	garageDescription=garageDescription, houseFaces=houseFaces, lastListPrice=lastListPrice, listAgentMUI=listAgentMUI, listAgentFullName=listAgentFullName,
    	listOfficeName=listOfficeName, listOfficePhone=listOfficePhone, listPrice=listPrice, matrixUniqueID=matrixUniqueID, 
    	matrixModifiedDT=matrixModifiedDT, mlsNumber=mlsNumber, mls=mls, photoCount=photoCount, postalCode=postalCode, propertyCondition=propertyCondition,
    	propertySubType=propertySubType, publicAddress=publicAddress, publicRemarks=publicRemarks, sellingAgentMUI=sellingAgentMUI, 
    	sellingAgentFullName=sellingAgentFullName, sellingAgentDirectWorkPhone=sellingAgentDirectWorkPhone, sqftTotal=sqftTotal, streetName=streetName, streetNumber=streetNumber,
    	subdivisionName=subdivisionName)
        return listing

class Listing(models.Model):
	area = models.CharField(max_length=300)
	associationFeaturesAvailable = models.CharField(max_length=1000) 
	associationFee = models.IntegerField(null=True, blank=True)
	associationFeeMQYN = models.CharField(max_length=200)
	associationFeeIncludes = models.CharField(max_length=1000)
	associationName = models.CharField(max_length=200)
	associationPhone = models.CharField(max_length=200)
	bathsFull = models.IntegerField(null=True, blank=True)
	bathsHalf = models.IntegerField(null=True, blank=True)
	bathsTotal = models.FloatField(null=True, blank=True)
	bedroomsTotalPossibleNum = models.IntegerField(null=True, blank=True)
	bedsTotal = models.IntegerField(null=True, blank=True)
	buildingDescription = models.CharField(max_length=200)
	closePrice = models.FloatField(null=True, blank=True)
	communityName = models.CharField(max_length=300)
	contructionDescription = models.CharField(max_length=300)
	currentPrice = models.FloatField(null=True, blank=True)
	directions = models.CharField(max_length=2000)
	dryerIncluded = models.IntegerField(null=True, blank=True)
	dryerUltilities = models.CharField(max_length=200, null=True)
	financingConsidered = models.CharField(max_length=300)
	flooringDescription = models.CharField(max_length=300)
	garageDescription = models.CharField(max_length=500)
	houseFaces = models.CharField(max_length=100)
	lastListPrice = models.FloatField(null=True, blank=True)
	listAgentFullName = models.CharField(max_length=300)
	listAgentMUI = models.IntegerField(null=True, blank=True)
	listOfficeName = models.CharField(max_length=300)
	listOfficePhone = models.CharField(max_length=200)
	listPrice = models.FloatField(null=True, blank=True)
	mls = models.CharField(max_length=100)
	mlsNumber = models.IntegerField(null=True, blank=True)
	matrixModifiedDT = models.TimeField(auto_now=False, auto_now_add=False)
	matrixUniqueID = models.IntegerField(null=True, blank = True)
	photoCount = models.IntegerField(null=True, blank=True)
	postalCode = models.CharField(max_length=10)
	propertyCondition = models.CharField(max_length=100)
	propertySubType = models.CharField(max_length=100)
	publicAddress = models.CharField(max_length=300)
	publicRemarks = models.CharField(max_length=1000)
	sellingAgentDirectWorkPhone = models.CharField(max_length=300)
	sellingAgentFullName = models.CharField(max_length=400)
	sellingAgentMUI = models.IntegerField(null=True, blank=True)
	sqftTotal = models.IntegerField(null=True, blank=True)
	streetName = models.CharField(max_length=200)
	streetNumber = models.IntegerField(null=True, blank=True)
	subdivisionName = models.CharField(max_length=200)
	objects = ListingManager()

# book = Book.create("Pride and Prejudice")
