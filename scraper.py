# Forked from Joel Eastwood's Globe Headlines (https://classic.scraperwiki.com/scrapers/bbc_headlines_8/) on Dec. 23, 2015
# Modified by Aaron Jacklin
# Additional commenting added as I figure out how the code works.

# Import the ScraperWiki library, which is used to crawl the web.
# This library will be used to store data to the SQL database.
import scraperwiki

# Import the urllib2 module, which is used to open URLs
# (https://docs.python.org/2/library/urllib2.html).
# (Library vs module: http://stackoverflow.com/questions/19198166/whats-the-difference-between-a-module-and-a-library-in-python)
import urllib2

# Import the urlparse module, which breaks up and remakes URLs (https://docs.python.org/2/library/urlparse.html)
import urlparse

# Import the re module, which deals with regular expressions (https://docs.python.org/2/library/re.html)
import re

# Import the datetime module, which is used to manipulate dates and times (https://docs.python.org/2/library/datetime.html)
import datetime

site = 'http://www.thestar.com/#/section/latestnews/'
        
html = urllib2.urlopen(site).read()

# To limit the number of headlines, find the "Top Headlines" section of the latest news page. N.B. This only applies to the Toronto Star website as it's currently coded.
topheadlines = re.findall('"Top Headlines"(.*?)"more-headlines"', html, re.DOTALL) #(.*?)<ul class="more-headlines"', html, re.DOTALL)

# Return all "non-overlapping matches" of the pattern in topheadlines as a list of strings assigned to everyheadline 
everyheadline = re.findall('<a.*?href="(.*?)" class="headline">(.*?)</a>', topheadlines[0])

# Create an empty dictionary called 'data'.
data = {}

for i in range(len(everyheadline)-1):
	link = everyheadline[i][0]
	headline = everyheadline[i][1]
	data['headline'] = headline
	data['URL'] = link
	data['date'] = datetime.datetime.today().ctime()
	scraperwiki.sqlite.save(unique_keys=['URL'], data=data)
