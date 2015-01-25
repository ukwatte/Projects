import feedparser
from tabulate import tabulate
from dateutil.parser import parse as date_parse
import sys
url = sys.argv[1]
feed = feedparser.parse(url)
table = [['title','author','link','published']]
for entry in  feed['entries']:
    table.append([entry['title'][:30], entry['author'][:30], entry['link'], date_parse(entry['published']).strftime('%Y-%m-%d')])

print tabulate(table, headers="firstrow")

## Example usage
## python rss.py "http://yesteapea.com/blog/feed"
## Prints title, author, link, published date
