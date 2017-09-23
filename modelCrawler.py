from bs4 import BeautifulSoup as bs
from Logger import Logger
from lxml import html
import requests

Log = Logger()
class Crawler():
	def __init__(self, url, method, item):
		self.url = url
		self.method = method
		self.item = item
		self.data = []

	def crawl(self):
		status_code = requests.get(self.url).status_code
		if (status_code != 200):
			Log.err('Status code : ' + status_code + ' - url : ' + self.url + ' is unreacheable')
			raise(e)
		source_code = requests.get(self.url).text
		# html_doc = html.fromstring(source_code)
		tree = bs(source_code, 'html.parser')
		if self.method == 'find':
			self.data = tree.find(self.item)
		elif self.method == 'find_all':
			self.data = tree.find_all(self.item)


		# self.data = tree.xpath(self.xpathSelector)
		return

	def getData(self):
		return(self.data)
