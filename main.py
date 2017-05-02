
import urllib.request
import simplejson as json
def search(search_string):
  query = urllib.parse.urlencode({'q': search_string})
  i=0
  cx='008760540502611867558:q1tp0tmtixw'

  while i<1:
  	#url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&rsz=large&%s&start=%d' % (query, i)
  	#url= 'http://googlecustomsearch.appspot.com/elementv2/results-only_url_v2.html?q=%s' % query
  	url='http://www.google.com/cse/cse.js?cx=%s' % cx
  	search_response = urllib.request.urlopen(url)
  	search_results = search_response.read().decode("utf8")
  	print(search_results)
  	# results = json.loads(search_results)
  	# data = results['responseData']
  	# print(data)
  	i+=1
  # print('Total results: %s' % data['cursor']['estimatedResultCount'])
  # hits = data['results']
  # print('Top %d hits:' % len(hits))
  # for h in hits: print(' ', h['url'])
  # print('For more results, see %s' % data['cursor']['moreResultsUrl'])
  #return hits

search("hi")