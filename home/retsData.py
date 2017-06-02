import csv
from rets.client import RetsClient
from pprint import pprint
import urllib3
import xmltodict

csvfile = 'listings.csv'

with open(csvfile) as f:
	reader = csv.reader(f, skipinitialspace=True)
	header = next(reader)
	listings = [dict(zip(header, map(str, row))) for row in reader]
	for key in listings[0].items():
		print(key)
	# for listing in listings:
	# 	# for key, value in listing.items():
	# 	# 	print(key, value)

#### Using rets-python



def getdata():
	client = RetsClient(
    login_url='http://rets.las.mlsmatrix.com/rets/login.ashx',
    # logout_url='Logout=http://rets.las.mlsmatrix.com/rets/Logout.ashx',
    username='tinoco',
    password='lv360',)
	http = urllib3.PoolManager()
	r = http.request(
		'GET',
		'http://rets.las.mlsmatrix.com/rets/login.ashx',fields={
		'username':'tinoco',
		'password':'lv360',
		})
	mydata = r.data
	print(mydata[0])
	return mydata

getdata()



# http://rets.las.mlsmatrix.com/rets/search.ashx?CLASS=Listing&searchtype=Property&querytype=DMQL2&Query=(BedsTotal=2%2B)



# http://rets.las.mlsmatrix.com/rets/login.ashx
 	
# user ID – tinoco
# Psw – lv360

# MemberName= User=tinoco,NULL,NULL,tinoco Broker= MetadataVersion=1.00.04817 MetadataTimestamp=2017-05-10T19:59:59Z MinMetadataTimestamp=2017-05-10T19:59:59Z 
# Login=http://rets.las.mlsmatrix.com/rets/Login.ashx 
# Logout=http://rets.las.mlsmatrix.com/rets/Logout.ashx 
# Search=http://rets.las.mlsmatrix.com/rets/Search.ashx 



# GetMetadata=http://rets.las.mlsmatrix.com/rets/GetMetadata.ashx 
# http://rets.las.mlsmatrix.com/rets/GetMetaData.ashx?TYPE=METADATA-RESOURCE&ID=0&Format=COMPACT
# <RETS ReplyCode="0" ReplyText="Operation Success.">
# <METADATA-RESOURCE Version="1.00.04815" Date="2017-05-10T19:59:59Z">
# <COLUMNS>
# ResourceID	StandardName	VisibleName	Description	KeyField	ClassCount	TableName	ClassVersion	ClassDate	ObjectVersion	ObjectDate	SearchHelpVersion	SearchHelpDate	EditMaskVersion EditMaskDate	LookupVersion	LookupDate	UpdateHelpVersion	UpdateHelpDate	ValidationExpressionVersion	ValidationExpressionDate	ValidationLookupVersion	ValidationLookupDate ValidationExternalVersion	ValidationExternalDate
# </COLUMNS>
# <DATA>
# Agent	Agent	Agent	Agent	Matrix_Unique_ID	1	Agent	1.00.00087	2017-02-15T17:34:55Z	1.00.00001	2015-04-16T21:39:51Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z 1.00.00152	2017-02-17T00:05:48Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z
# </DATA>
# <DATA>
# Office	Office	Office	Office	Matrix_Unique_ID	1	Office	1.00.00078	2016-06-02T15:21:29Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00052	2016-02-02T19:23:49Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z
# </DATA>
# <DATA>
# OpenHouse	OpenHouse	Openhouse	Openhouse	matrix_unique_id	1	OpenHouse	1.00.00030	2016-11-10T12:44:07Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000 2015-04-16T21:39:40Z	1.00.00018	2016-02-02T19:23:49Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z
# </DATA>
# <DATA>
# Property	Property	Listing	Listing	Matrix_Unique_ID	1	Listing	1.00.01344	2016-12-14T00:02:24Z	1.00.00002	2016-05-11T18:03:24Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z	1.00.01733	2017-05-10T19:59:59Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z
# </DATA>
# <DATA>
# PropertySubTable	Listing Sub Table	Listing Sub Table	matrix_unique_id	2	Unit	1.00.00027	2016-02-04T18:44:55Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z 1.00.00000	2015-04-16T21:39:40Z	1.00.00320	2017-04-07T15:58:16Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z	1.00.00000	2015-04-16T21:39:40Z
# </DATA>
# </METADATA-RESOURCE>
# </RETS>


# GetObject=http://rets.las.mlsmatrix.com/rets/GetObject.ashx 
# Update=http://rets.las.mlsmatrix.com/rets/Update.ashx 
# PostObject=http://rets.las.mlsmatrix.com/rets/PostObject.ashx'


# http://rets.las.mlsmatrix.com/rets/GetMetaData.ashx?TYPE=METADATA-CLASS&ID=0&Format=COMPACT
# <RETS ReplyCode="0" ReplyText="Operation Success.">
# <METADATA-CLASS Resource="Property" Version="1.00.01344" Date="2016-12-14T00:02:24Z">
# <COLUMNS>
# ClassName	StandardName	VisibleName	Description	TableVersion	TableDate	UpdateVersion	UpdateDate
# </COLUMNS>
# <DATA>
# Listing	Cross Property	Cross Property	1.00.01339	2016-12-14T00:02:24Z	1.00.00000	2015-04-16T21:39:45Z
# </DATA>
# </METADATA-CLASS>
# <METADATA-CLASS Resource="Agent" Version="1.00.00087" Date="2017-02-15T17:34:55Z">
# <COLUMNS>
# ClassName	StandardName	VisibleName	Description	TableVersion	TableDate	UpdateVersion	UpdateDate
# </COLUMNS>
# <DATA>
# Agent	Agent	Agent	1.00.00083	2017-02-15T17:34:55Z	1.00.00000	2015-04-16T21:39:45Z
# </DATA>
# </METADATA-CLASS>
# <METADATA-CLASS Resource="Office" Version="1.00.00078" Date="2016-06-02T15:21:29Z">
# <COLUMNS>
# ClassName	StandardName	VisibleName	Description	TableVersion	TableDate	UpdateVersion	UpdateDate
# </COLUMNS>
# <DATA>
# Office	Office	Office	1.00.00074	2016-06-02T15:21:29Z	1.00.00000	2015-04-16T21:39:45Z
# </DATA>
# </METADATA-CLASS>
# <METADATA-CLASS Resource="PropertySubTable" Version="1.00.00027" Date="2016-02-04T18:44:55Z">
# <COLUMNS>
# ClassName	StandardName	VisibleName	Description	TableVersion	TableDate	UpdateVersion	UpdateDate
# </COLUMNS>
# <DATA>
# Room	Rooms	Rooms	1.00.00008	2016-02-04T18:44:55Z	1.00.00000	2015-04-16T21:39:45Z
# </DATA>
# <DATA>
# Unit	Units	Units	1.00.00015	2015-11-02T14:08:14Z	1.00.00000	2015-04-16T21:39:45Z
# </DATA>
# </METADATA-CLASS>
# <METADATA-CLASS Resource="OpenHouse" Version="1.00.00030" Date="2016-11-10T12:44:07Z">
# <COLUMNS>
# ClassName	StandardName	VisibleName	Description	TableVersion	TableDate	UpdateVersion	UpdateDate
# </COLUMNS>
# <DATA>
# OpenHouse	Open House	Open House	1.00.00024	2016-11-10T12:44:07Z	1.00.00000	2015-04-16T21:39:45Z
# </DATA>
# </METADATA-CLASS>
# </RETS>








## Using rets
# from rets import Session
# from pprint import pprint

# login_url = "http://rets.las.mlsmatrix.com/rets/GetObject.ashx"
# username = 'tinoco'
# password = 'lv360'
# rets_client = Session(login_url, username, password)
# rets_client.login()
# system_data = rets_client.get_system_metadata()
# pprint(system_data)

# resources = rets_client.get_resource('Property')
# pprint(resources)

# import urllib.request
# from bs4 import BeautifulSoup
# import json

# company = "Space X"
# yourID = ""
# yourKey = ""
# url = "http://rets.las.mlsmatrix.com/rets/Search.ashx(matrix_unique_id = 0+)&Limit=1" 
# hdr = {
# 	'User-Agent': 'Mozilla/5.0',
# 	'username':'tinoco',
# 	'password':'lv360',
# }
# req = urllib.request.Request(url,headers=hdr)
# response = urllib.request.urlopen(req)
# # soup = BeautifulSoup(response, 'lxml')
# # data = json.loads(soup.p.get_text())
# # print(data)


# # fieldnames = ("Area","Association Features Available", "Association Fee 1", "Association Fee 1 MQYN",
# # 	"Association Fee Includes","Association Name","Association Phone","Baths Full","Baths Half","Baths Total",
# # 	"Bedrooms Total Possible Num","Beds Total","Building Description","Close Price","Construction Description",
# # 	"Community Name","Current Price","Directions","Dryer Included","Dryer Utilities","Financing Considered",
# # 	"Flooring Description","Garage Description","House Faces","Last List Price","List Agent MUI","List Agent Full Name",
# # 	"List Office Name","List Office Phone","List Price","Matrix Unique ID","Matrix Modified DT","MLS Number","MLS","MLS Photo Count",
# # 	"Postal Code","Property Condition","Property Sub Type","Public Address","Public Remarks","Selling Agent MUI",
# # 	"Selling Agent Full Name","Selling Agent Direct Work Phone","Street Name","Street Number","Subdivision Name","Sq Ft Total")
