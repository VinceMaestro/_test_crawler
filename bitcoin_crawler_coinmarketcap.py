# from lxml import html
import requests	#Handle : POST GET ... requests

class TableClassCrawler:
	def __init__(self, starting_url):
		self.starting_url = starting_url
		self.data = []

	def crawl(self):
		self.data = requests.get(self.starting_url)
		print self.data.text
		return

class DataProcessor:
	def __init__(self, data, file_path):
		self.data = data
		self.file_path = file_path

	def process_data(self):

		return

	def save_to_file(self):

		return

crawler = TableClassCrawler('https://coinmarketcap.com/currencies/bitcoin/historical-data/')
crawler.crawl()
# data = DataProcessor(crawler.data)
# data.process_data()
# data.save_to_file()
