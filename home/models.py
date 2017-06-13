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
	associationFee = models.CharField(max_length=200, null=True)
	associationFeeMQYN = models.CharField(max_length=200)
	associationFeeIncludes = models.CharField(max_length=1000)
	associationName = models.CharField(max_length=200)
	associationPhone = models.CharField(max_length=200)
	bathsFull = models.FloatField(null=True, blank=True)
	bathsHalf = models.FloatField(null=True, blank=True)
	bathsTotal = models.FloatField(null=True, blank=True)
	bedroomsTotalPossibleNum = models.FloatField(null=True, blank=True)
	bedsTotal = models.FloatField(null=True, blank=True)
	buildingDescription = models.CharField(max_length=200)
	closePrice = models.FloatField(null=True, blank=True)
	communityName = models.CharField(max_length=300)
	contructionDescription = models.CharField(max_length=300)
	currentPrice = models.FloatField(null=True, blank=True)
	directions = models.CharField(max_length=2000)
	dryerIncluded = models.FloatField(null=True, blank=True)
	dryerUltilities = models.CharField(max_length=200, null=True)
	financingConsidered = models.CharField(max_length=300)
	flooringDescription = models.CharField(max_length=300)
	garageDescription = models.CharField(max_length=500)
	houseFaces = models.CharField(max_length=100)
	lastListPrice = models.FloatField(null=True, blank=True)
	listAgentFullName = models.CharField(max_length=300)
	listAgentMUI = models.CharField(max_length=200, null=True)
	listOfficeName = models.CharField(max_length=300)
	listOfficePhone = models.CharField(max_length=200)
	listPrice = models.FloatField(null=True, blank=True)
	mls = models.CharField(max_length=100)
	mlsNumber = models.CharField(max_length=200, null=True)
	matrixModifiedDT = models.DateTimeField(auto_now=False, auto_now_add=False)
	matrixUniqueID = models.CharField(max_length=200, null=True)
	photoCount = models.FloatField(null=True, blank=True)
	postalCode = models.CharField(max_length=10)
	propertyCondition = models.CharField(max_length=100)
	propertySubType = models.CharField(max_length=100)
	publicAddress = models.CharField(max_length=300)
	publicRemarks = models.CharField(max_length=1000)
	sellingAgentDirectWorkPhone = models.CharField(max_length=300)
	sellingAgentFullName = models.CharField(max_length=400)
	sellingAgentMUI = models.CharField(null=True, max_length=200)
	sqftTotal = models.FloatField(null=True, blank=True)
	streetName = models.CharField(max_length=200)
	streetNumber = models.CharField(max_length=200, null=True)
	subdivisionName = models.CharField(max_length=200)
	objects = ListingManager()

class StoryManager(models.Manager):
	def create_story(self, url, text, image, summary, keywords):
		story = self.create(url=url, text=text, image=image, summary=summary, keywords=keywords)
		return story

class Story(models.Model):
	url = models.CharField(max_length=255)
	text = models.TextField()
	image = models.CharField(max_length=210)
	summary = models.TextField()
	keywords = models.TextField()
	objects = StoryManager()
	class Meta:
		unique_together = ["url"]
	
# book = Book.create("Pride and Prejudice")
