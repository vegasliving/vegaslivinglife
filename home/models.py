from django.db import models

class ListingManager(models.Manager):
    def create_listing(self,
    	area, associationFeaturesAvailable, associationFee, associationFeeMQYN, associationFeeIncludes, associationName, associationPhoneNumber,
    	bathsFull, bathsHalf, bathsTotal, bedroomsTotalPossibleNumber, bedsTotal, buildingDescription, closePrice, contructionDescription,
    	communityName, directions, dryerIncluded, financingConsidered, flooringDescription, garageDescription, houseFaces, lastListPrice, 
    	listAgentMUI, listAgentFullName, listAgentOfficeName, listOfficePhone, listPrice, matrixUniqueID, matrixModifiedDT, mlsNumber, mls,
    	photoCount, postalCode, propertyCondition, propertySubType, publicAddress, publicRemarks, sellingAgentMUI, sellingAgentFullName, 
    	sellingAgentDirectWorkPhone, streetName, streetNumber, subdivisionName, sqftTotal):

        listing = self.create(
        area=area, associationFeaturesAvailable=associationFeaturesAvailable, associationFee=associationFee, associationFeeMQYN=associationFeeMQYN, 
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
        return listing

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

# book = Book.create("Pride and Prejudice")
