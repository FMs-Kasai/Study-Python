import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

html = urlopen("http://www.dq-8.com/monstername.html")
bsObj = BeautifulSoup(html, "html.parser")

table = bsObj.findAll("table",{"class":"sml"})[0]
rows = table.findAll("tr")

with open("dq8_monster.csv", "w", encoding='utf-8') as file:
    writer = csv.writer(file)
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td']):
            csvRow.append(cell.get_text())

        writer.writerow(csvRow)