import urllib3
import json
import csv


class NewsService():
    def __init__(self):
        self.http = urllib3.PoolManager()

    def getSites(self):
        response = self.http.request(
            'GET',
            'http://localhost:5000/allSite')
        return json.loads(response.data.decode('utf-8'))

    def getNews(self, site):
        response = self.http.request(
            'GET',
            'http://localhost:5000/site/{0}/news'.format(site))
        return json.loads(response.data.decode('utf-8'))

    def to_csv(self,data):
        with open('news.csv', 'a') as csvfile:
            fieldnames = ['site','title', 'url', 'content', "target"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for news in data:
                writer.writerow(news)


ns = NewsService()
response = ns.getSites()

for site in response:
    data = ns.getNews(site['name'])
    ns.to_csv(data)
