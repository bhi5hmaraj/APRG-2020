import requests,os

base_url = 'https://www.hackerrank.com/rest/contests/{}/challenges/{}/hackers/{}/download_solution'
contests = ['cmi-aprg-2020-assign-1', 'cmi-aprg-assignment-4']
challenges = [["minsweeper"], ["the-journey", "second-shortest-path"]]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

ids = open('cmi-ids.txt', 'r')

ids = ids.readlines()

for c in range(len(contests)):
	for challs in challenges[c]:		
		curr = 0	
		for ID in ids:
			ID = ID.strip()
			url = base_url.format(contests[c], challs, ID)
			print("url ", url)
			code = requests.get(url, headers=headers).text
			
			if len(code) == 0: continue

			path = './{}/{}/{}/'.format(contests[c], challs, ID)
			print("path ", path)

			os.makedirs(path)
			fout = open('./{}/{}/{}/{}.py'.format(contests[c], challs, ID, ID), 'w')
			
			print(code, file=fout)
			fout.close()

			curr += 1
			print("progress ", (curr * 100.0) / len(ids))