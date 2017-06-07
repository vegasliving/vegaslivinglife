from pypodio2 import api
from pprint import pprint

client_id = "vegas-living-33m2bp"
client_secret = "INOPZocrCMZzAv9VbkqS2rVlBrIuHTqkKc2ysV1I8H0KGsVMnhVEfOB56b9YTMOm"
app_id = "18725351"
app_token = "d7b6a16beb71476abefeefb8b468abe5"
username = "hoangdov@gmail.com"
password = "milkyway42"

### Oauth for Org
c = api.OAuthClient(
    client_id,
    client_secret,
    username,
   	password,    
)

spaces = c.Org.get_all()[0]['spaces']
for space in spaces:
	print(space['name'],space['space_id'], space['url'])
	# print(space['name'], space['space'], space['url'])

myApp = c.Application.activate('18725351')
appID = 18725351

def createLead(name, phone, email):
	lead = c.Item.create(appID,{'fields': {"title": name,"phone": [{ "type": "mobile", "value": phone}],"email": [{ "type": "work", "value": email}]}})
	return lead

createLead('T','7027420978','partyhard@troy.do')
