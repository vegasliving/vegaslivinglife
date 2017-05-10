from indeed import IndeedClient

def findjob(location, job):
	client = IndeedClient("779356190786663")

	params =  {
		# Query term 
		'q': job, 
		'l': location,
		'userip':'69.194.135.243',
		'useragent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)',
		'sort':'',
		'radius':'1',
		'latlong':'1',
		'limit': '9'
		# Location. Use a postal code or a "city, state/province/region" combination.
		
	}

	search_response = client.search(**params)

	results = search_response['results']

	jobKeys = []

	for result in results:
		jobKeys.append(result['jobkey'])
	return(results)
# findjob('san francisco','engineer')