from newspaper import Article

def getStory(url):
	story = Article(url)
	story.download()
	story.parse()
	print("==============================================================")
	top_image = story.top_image
	text = story.text
	link = url
	
	# nltk.download()
	story.nlp()

	print(story.keywords)
	keywords = story.keywords
	summary = story.summary
	print(story.summary)
	return(link, text, top_image, summary, keywords)
		



