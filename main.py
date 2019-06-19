# /usr/bin/env python3
#
# modulo para manipular recursos sobre protocolo http(s)
import requests
import json

import test.test_json.test_decode
from bs4 import BeautifulSoup
from pymongo import MongoClient
# define a client
client = MongoClient()
# define a database
db = client.jobbag
# define a collection
collection = db.results

# solicitar el sitio web con un get
# use Beautiful Soup
webpage = requests.get(
    "https://www.indeed.nl/jobs?q=javascript&l&vjk=646b25ca0fb38fc8&advn=3944699374646158").text

# make soup
soup = BeautifulSoup(webpage, "lxml")

# imprimir solo links
# un for que recorra el html y extraiga links
counter = 0

# crear lista para guardar avisos
listofJobs = []

# crea json con las ofertas encontradas
for link in soup.find_all('a'):
    websites = link.get('href')
    try:
        if websites.startswith('/pagead'):
            counter += 1
            urljob = "https://www.indeed.nl" + websites
            # print(urljob)
            jobs = dict()
            jobs["url"] = urljob
            # print(jobs)
            listofJobs.append(jobs)

    except AttributeError:
        pass

# print("Avisos en total: %s" % counter)
# print("Avisos en total: %s" % len(jobs))
# print("inserto documentos a mongodb:")

result = collection.insert_many(listofJobs)
