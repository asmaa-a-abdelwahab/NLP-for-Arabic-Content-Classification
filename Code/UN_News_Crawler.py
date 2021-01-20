#!/usr/bin/env python
# coding: utf-8
import json
import pandas as pd    
from requests import get
from bs4 import BeautifulSoup


def extract_html(url):
    """
    Function for extracting html content using BeautifulSoup
    """
    response = get(url, allow_redirects=False)
    html = response.text
    soup = BeautifulSoup(html, "lxml-xml")
    return(soup)


def add_to_json(data, title, summary, url, category):
    """
    Function for adding data contents to a json file
    """
    data['Article'].append({
        'Title': title,
        'Content': summary,
        'Link': url,
        'Category': category
    })
    return(data['Article'])


def save_json(data, fname):
    """
    Function for saving json file
    """
    with open('{}.json'.format(fname), 'w') as outfile:
        json.dump(data, outfile)


data = {}
data['Article'] = []
#l = 0
for i in range(1000):
    
    soup = extract_html("https://news.un.org/ar/news/date/2018?page={}".format(i))
    stories = soup.findAll("h1", {"class": "story-title"})
    
    for n in range(len(stories)):
        title = stories[n].text
        url = "https://news.un.org"+stories[n].find('a').attrs['href']
        soup = extract_html("https://news.un.org/"+stories[n].find('a').attrs['href'])
        div = soup.findAll("div", {"class": "field-item even"})
        if len(div) > 4:
            ps = div[4].findAll('p')
            content = ""
            for p in ps:
                content += p.text
            category = div[1].text
            if content != "" and category != "":
                add_to_json(data, title, content, url, category)
                #l += 1
    #print(l)
        
save_json(data, 'results')
df = pd.json_normalize(data['Article'])
df.to_csv("UN_News.csv", index=False)

