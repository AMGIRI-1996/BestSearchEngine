
import http.client, urllib.request, urllib.parse, urllib.error, base64
import simplejson as json
import search
headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '6ead8834e97a4447b4108490ba6cd6dd',
}

def search(query):
	params = urllib.parse.urlencode({'q': query,'count': '10','offset': '0','mkt': 'en-us','safesearch': 'Moderate',})
	try:
		conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
		conn.request("GET", "/bing/v5.0/search?%s" % params, "{body}", headers)
		response = conn.getresponse()
		data = response.read()
		
		results = json.loads(data)
		data = results['value']
		for key, value in data.items():
			if key.encode('utf-8').decode('utf-8') == "url":
				print(("%s --> %s")%(search.getbase(value),value))
		# print(data)
		print(data)
		conn.close()
	except Exception as e:
		#print("[Errno {0}] {1}".format(e.errno, e.strerror))
		return

search("flash")