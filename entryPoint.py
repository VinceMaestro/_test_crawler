from modelCrawler import Crawler
from bs4 import BeautifulSoup
from Logger import Logger
from lxml import html
import traceback

url = 'https://profile.intra.42.fr/#'

method_list = dir(BeautifulSoup)

# print(method_list)

# xpathSelector = '//span/text()'
Log = Logger()

method = 'find_all'

item = '/15'

try:
	crawler = Crawler(url, method, item)
	crawler.crawl()

	data = crawler.getData()
	print(data)
except KeyboardInterrupt:
	Log.info('KeyboardInterrupt')
except (SystemExit):
	Log.info('SystemExit')
except Exception as e:
	Log.err('Caught Exception in child process:')
	traceback.print_exc()

def fon(fun, *args):
	fun(*args)
