from newsapi.articles import Articles
from .abstract.Widget import Widget

class NewsWidget(Widget):

	# Abstract functions inherited
	def get(self):
		return self.__get_news()

	def get_script(self):
		return self.__get_news_script()

	# Get n amount of news headlines
	def get_news(self, limit=5):
		'''
		Get dictionary of news headlines
		'''
		# Authorize the news api
		apikey = '1a4e2bcd0c2b40e48786ccdbf916959a'

		# Get article information
		a = Articles(API_KEY=apikey)
		articles = a.get(source="cnn", sort_by='popular')

		headlines = {}
		# Loop and create headlines 
		for index, article in enumerate(articles['articles'], start=1):
			headlines[article['title']] = article['description']  # Populate dictionary
			if index == limit:  # Once limit is reached, end the loop
				break

		return headlines  # Return headlines dictionary

	def get_news_script(self):
		'''
		Return script for headlines for the Voice to read
		'''
		script = "Here are the news headlines for today: "
		for headline, description in self.__get_news().items():
			script += " {};".format(headline)
		return script


if __name__ == '__main__':
	news = NewsWidget()
	print(news.get_script())
