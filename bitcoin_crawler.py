# Here import from coinmarketcap

from lxml import html		# Handle html parsing
import requests				# Handle POST GET ... requests

class TableClassCrawler:
	def __init__(self, starting_url):
		self.starting_url = starting_url
		self.tree = []
		self.data = []
		self.processed_data = []

	def crawl(self):
		# Recupere le code source de la page en utilisant la lib requests
		source_code = requests.get(self.starting_url).text

		# Recreer l'arborescence du code source permettant ensuite de chercher certains elements
		self.tree = html.fromstring(source_code)

		# Recupere le contenu du header
		self.header = self.tree.xpath('//table[@class="table"]//th/text()')

		# Recupere le contenu du tableau
		self.data = self.tree.xpath('//tr[@class="text-right"]//td/text()')

		# Concatene les deux
		self.processed_data = self.header + self.data
		return

	def modify_data(self, new_data):
		self.processed_data = new_data
		return

	def save_to_file(self, file_path):
		# On peut imaginer un fonction qui sauvegarde ca dans un fichier
		return

# On creer un nouvel objet: crawler, qui a la class TableClassCrawler
crawler = TableClassCrawler('https://coinmarketcap.com/currencies/bitcoin/historical-data/')

# On appelle la fonction crawl() de l'objet crawler
crawler.crawl()

print(crawler.processed_data)

# On peut modifier les valeurs des elements d'un objet
crawler.modify_data('Hahaha I\'ve just errased all processed_data =) ')

print(crawler.processed_data)

# data.save_to_file('/path')
