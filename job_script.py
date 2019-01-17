import urllib.request
import json

stuff = urllib.request.Request('https://jobs.github.com/positions.json?description=ruby&page=1')
data = urllib.request.urlopen(stuff).read().decode('utf-8')
json_data = json.loads(data)
url = 'http://localhost:8000/api/v1/jobs/'


for job in json_data:
	company = job['company']
	title = job['title']
	description = job['description']
	link = job['how_to_apply']
	location = job['location']

	
	data = {'company': company,  'title': title, 'description': description, 'appLink': link, 'location':location}
	data = bytes( urllib.parse.urlencode( data ).encode() )
	handler = urllib.request.urlopen(url, data);


	

	# post_feedback = handler.read().decode('utf-8')
	# resp = json.loads(post_feedback)