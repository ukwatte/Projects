import urllib
import sys
import json

url = 'http://query.yahooapis.com/v1/public/yql?{0}&format=json'
query = '''select LastTradePriceOnly,symbol,Name 
           from yahoo.finance.quotes 
           where symbol in ({0})'''

quotes = sys.argv[1]
quotes = ','.join(('"' + q.strip() + '"' for q in quotes.split(',')))
query = query.format(quotes)
query = urllib.urlencode({'q':query,'env':'http://datatables.org/alltables.env'})
url = url.format(query)

res = urllib.urlopen(url).read()
print url
res = json.loads(res)['query']['results']

print json.dumps(res, indent=4, sort_keys=True)

## Example usage 
## python quotes.py "FUEL,GOOG, MSFT"
## output : 
## {
##     "quote": [
##         {
##             "LastTradePriceOnly": "13.83",
##             "Name": "Rocket Fuel Inc.",
##             "symbol": "FUEL"
##         },
##         {
##             "LastTradePriceOnly": "539.95",
##             "Name": "Google Inc.",
##             "symbol": "GOOG"
##         },
##         {
##             "LastTradePriceOnly": "47.18",
##             "Name": "Microsoft Corpora",
##             "symbol": "MSFT"
##         }
##     ]
## }
