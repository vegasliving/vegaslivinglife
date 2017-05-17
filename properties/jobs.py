# from indeed import IndeedClient

# client = IndeedClient("779356190786663")

# params =  {
# 	# Query term 
# 	'q': "accounting", 
# 	'l':"",
# 	'userip':'69.194.135.243',
# 	'useragent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2)',
# 	'sort':'',
# 	'latlong':'1',
# 	'limit': '25'
# 	# Location. Use a postal code or a "city, state/province/region" combination.
	
# }

# search_response = client.search(**params)

# results = search_response['results']

# jobKeys = []

# for result in results:
# 	# print(result['jobtitle'],'----------',result['formattedLocation'],'----------',result['company'],'----------',result['url'])
# 	# print(result['jobkey'])
# 	jobKeys.append(result['jobkey'])


# job_response = client.jobs(jobkeys=('a624c87a4f419230', '84bc3bb5a4f98938'))
# job_results = job_response['results']

# for job_result in job_results:
# 	print(job_result)	
