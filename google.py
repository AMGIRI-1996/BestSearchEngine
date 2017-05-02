from googleapiclient.discovery import build
import simplejson as json
import tldextract
#import pprint

my_api_key = "AIzaSyDrO3fpX1AMOhwBS_nTvU2sUHAgqobnrFU"
my_cse_id = "008760540502611867558:q1tp0tmtixw"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def getbase(url):
	ext = tldextract.extract(url)
	return '.'.join(ext[1:3])
results = google_search('flash', my_api_key, my_cse_id, num=10)
for result in results:
    #pprint.pprint(result)
    for key, value in result.items():
    	#print("%s -> %s"%(key,value))
    	if key.encode('utf-8').decode('utf-8') == "formattedUrl":
    		print(("%s --> %s")%(getbase(value),value))


    # res = json.loads(result.decode('utf-8'))
    # data = res['formatedurl']
    # print(data)