from nations import nations
import requests
from bs4 import BeautifulSoup as bs
import csv



for nation in nations:
	r = requests.get(nation['url'])
	soup = bs(r.text)
	ref_str = str(soup.find(id='References'))
	new_text = r.text.split(ref_str)[0]
	nation['connections'] = []

	for nation2 in nations:
		if nation2['name'] == nation['name']:
			continue

		if nation2['name'] in new_text:	
			count = new_text.count(nation2['name'])
			nation['connections'].append([nation2['name'], count])



# create nodes csv
with open('nations2.csv', 'w+') as csvfile:
	cwriter = csv.writer(csvfile)
	cwriter.writerow(['Id', 'Label', 'Url'])

	for nation in nations:
	    
	    cwriter.writerow([nation['name'].encode('utf8'), nation['name'].encode('utf8'), nation['url'].encode('utf8')])

# create rels csv
with open('nation_rels2.csv', 'w+') as csvfile:
	cwriter = csv.writer(csvfile)
	cwriter.writerow(['Source', 'Target', 'Weight'])

	for nation in nations:

		for connected_nation in nation['connections']:
			if connected_nation[0] != nation['name']:
				cwriter.writerow([nation['name'].encode('utf8'), connected_nation[0].encode('utf8'), connected_nation[1]])



