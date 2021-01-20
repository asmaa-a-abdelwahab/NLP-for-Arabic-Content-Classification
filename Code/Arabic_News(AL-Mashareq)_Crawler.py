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


def get_pages_num(soup):
    """
    Function for retrieving the number of pages to be scrapped for each category
    """
    num = int(soup.find("div", {"class": "pagination"}).findAll("a")[-2].text)
    return num


data = {}
data['Article'] = []
soup = extract_html("https://almashareq.com/ar/archives")
stories = soup.findAll("div", {"class": "article--listing"})

for n in range(len(stories)):
    soup = extract_html("https://almashareq.com"+stories[n].find("div", {"class": "article--listing__text"}).find("a").attrs['href'])
    
    for m in range(get_pages_num(soup)):
        #Access each category page
        soup1 = extract_html("https://almashareq.com"+stories[n].find("div", {"class": "article--listing__text"}).find("a").attrs['href']+"?page={}".format(m))
        sub_stories = soup1.findAll("div", {"class": "article--block"})
        
        for k in range(len(sub_stories)):
            title = sub_stories[k].find('h5', {"class": "article__title"}).text
            url = "https://almashareq.com"+sub_stories[k].find('a').attrs['href']
            category = sub_stories[k].find('a', {"class", "article__keyword"}).text
            soup2 = extract_html("https://almashareq.com"+sub_stories[k].find('a').attrs['href'])
            divs = soup2.find("div", {"class": "article__content"})
            
            if len(divs) != 0:
                ps = divs.findAll('p', {"class": "article__p"})
                content = ""
                for p in ps:
                    content += p.text
                add_to_json(data, title, content, url, category)
        
save_json(data, 'results')
df = pd.json_normalize(data['Article'])
df.to_csv("Arabic_News_AL-Mashareq.csv", index=False)

