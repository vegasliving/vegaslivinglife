from pypodio2 import api
from pprint import pprint
import keys

client_id = keys.production_client_id
client_secret = keys.production_client_secret
app_id = keys.app_id
app_token = keys.app_token
username = keys.username
password = keys.password

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

appID = app_id

myApp = c.Application.activate(app_id)
def createLead(firstName, lastName, phone, email, listing):
	lead = c.Item.create(appID,{'fields': {
		"first-name-2": firstName,
		"last-name-2": lastName, 
		"phone": [{ "type": "mobile", "value": phone}],
		"email": [{ "type": "work", "value": email}], 
		"listing": listing
	}})
	return lead

# createLead('Troy','Do','7027420978','partyhard@troy.do')
