from django.db import models
import requests
from bs4 import BeautifulSoup
import os
import csv
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy


class TodoItem(models.Model):
    item_text = models.CharField(max_length=200)
    def __str__(self):
        return self.item_text


class Market(models.Model):
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
        for string in soup.tbody.strings:
            if string != '\n':
                temp = string.replace('\n', '')
                if '*' in temp:
                    continue
                body.append(temp)

        lines = []
        imgtag = soup.tbody.findAll('img')
        f = 0
        for anchor in imgtag:
            if f == 1:
                lines.append(anchor['src'])
                f = 0
            else:
                f = 1
        rows = []
        i = 9
        k = 0
        rows.append(header)
        while i < len(body):
            sublist = body[i - 9:i]
            sublist.append(lines[k])
            rows.append(sublist)
            i += 9
            k += 1
        with open(stats_file_path + 'Market.csv', 'w', newline='') as myFile:
            writer = csv.writer(myFile, dialect='excel')
            # print(rows)
            writer.writerows(rows)
    def marketcap(pdmkt):
        reviews = pd.read_csv(pdmkt)
        df1 = reviews.head(10).copy()
        df1['capint'] = df1['Market Cap'].str.replace(',', '')
        df1['capint'] = df1['capint'].str.replace('$', '')
        df1['capint'] = df1['capint'].astype(float)
        plt.barh(df1['Name'], df1['capint'])
        plt.savefig('marketcap.png')
    downloadMarketInfo("static/csv/")
    marketcap("static/csv/Market.csv")
    reviews = pd.read_csv("static/csv/Market.csv")
    pd.set_option('display.max_colwidth', -1)
    df1 = reviews.head(10).copy()
    form_text = reviews.head(10).to_html(escape=False)