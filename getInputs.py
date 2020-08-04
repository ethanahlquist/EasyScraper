#!/usr/bin/env python3

from bs4 import BeautifulSoup
import urllib.request as urlRequest
import urllib.parse as urlParse
import json
import sys

def main(argv):
    Scraper = InputScraper()
    openUrl = Scraper.makeRequest()
    soup = BeautifulSoup(openUrl, "lxml")
    inputDict = Scraper.getInputs(soup)
    print(inputDict)


class InputScraper:
    def __init__(self):
        self.URL = 'https://www.intemag.com/magnet-pull-calculations-disc-magnet-with-steel-plate'

        # pretend to be a chrome 47 browser on a windows 10 machine
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}

        # This is the dictionary that holds the input fields
        self.values = {}

        self.CLUBS_API = 'http://0.0.0.0:8080/new_data/clubs'
        self.TOP_LINK = 'https://www.asi.calpoly.edu/club_directories/listing_bs/'
        # Doesn't contain 'Contact Email' because that name is used for two different fields.
        # Workaround in scrape method.
        self.INFO_ENTRY_PAIRS = {
            'Contact Person:': 'CONTACT_PERSON',
            'Contact Phone:': 'CONTACT_PHONE',
            'Advisor:': 'ADVISOR',
            'Advisor Phone:': 'ADVISOR_PHONE',
            'Advisor Email:': 'ADVISOR_EMAIL',
            'Box:': 'BOX',
            'Affiliation:': 'AFFILIATION',
            'Type(s):': 'TYPES',
            'Description:': 'DESCRIPTION'
        }


    def makeRequest(self):
        params = urlParse.urlencode(self.values).encode("utf-8")
        # create the url
        targetUrl = urlRequest.Request(url=self.URL, data=params, headers=self.headers)
        # open the url
        fp  = urlRequest.urlopen(targetUrl)
        return fp



    def getInputs(self, soup):

        d = {e['name']: e.get('value', '') for e in soup.find_all('input', {'name': True})}
        d['fat'] = "dumb"

        return json.dumps(d, indent=4)


    def getSelection(self, soup):

        d = {e['name']: e.get('value', '') for e in soup.find_all('input', {'name': True})}
        return json.dumps(d, indent=4)

if __name__ == "__main__":
   main(sys.argv[1:])
