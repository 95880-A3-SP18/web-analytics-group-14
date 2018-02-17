import requests
from bs4 import BeautifulSoup
import os
import csv
import sys


def downloadMarketInfo(stats_file_path):
    exist = os.path.exists(stats_file_path)
    if not exist:
        os.makedirs(stats_file_path)
    page = requests.get("https://coinmarketcap.com/")
    soup = BeautifulSoup(page.content, 'html.parser')
    header = []
    body = []
    for string in soup.thead.strings:
        if string != '\n':
            header.append(string)
    header.insert(1, 'abbr')
    header.insert(7, 'abbr')
    header.pop()
    for string in soup.tbody.strings:
        if string != '\n':
            temp = string.replace('\n', '')
            if '*' in temp:
                continue
            body.append(temp)
    i = 9
    rows = []
    rows.append(header)
    while i < len(body):
        rows.append(body[i-9:i])
        i += 9
    with open(stats_file_path + 'Market.csv', 'w') as myFile:
        writer = csv.writer(myFile, dialect= 'excel')
        writer.writerows(rows)


def downloadBTCInfo(stats_file_path):
    exist = os.path.exists(stats_file_path)
    if not exist:
        os.makedirs(stats_file_path)
    page = requests.get("https://coinmarketcap.com/currencies/bitcoin/#markets")
    soup = BeautifulSoup(page.content, 'html.parser')
    header = []
    body = []
    for string in soup.thead.strings:
        if string != '\n':
            header.append(string)
    for string in soup.tbody.strings:
        if string != '\n':
            temp = string.replace('\n', '')
            if '*' in temp:
                continue
            body.append(temp)
    header.insert(6, '%')
    rows = []
    rows.append(header)
    i = 8
    while i < len(body):
        rows.append(body[i - 8:i])
        i += 8
    with open(stats_file_path + 'BitCoin.csv', 'w') as myFile:
        writer = csv.writer(myFile, dialect='excel')
        writer.writerows(rows)


if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0]))
    downloadMarketInfo("downloads\\")
    downloadBTCInfo("downloads\\")