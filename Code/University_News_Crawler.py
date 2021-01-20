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


def get_pages_num(category):
    """
    Function for retrieving the number of pages to be scrapped for each category
    """
    soup = extract_html("https://www.birzeit.edu/ar/news/category/{}".format(category))
    stories = soup.findAll("h2", {"class": "element-invisible"})
    li = soup.findAll("li", {"class": "pager-last last"})
    num = int(li[0].find('a').attrs['href'].split("=")[1])
    return num


Categories_en = ["research", "arts-and-culture", "campus-life", "awards", "alumni", "international", 
                 "sports-and-well-being", "visits", "community-engagement", "students", "science-and-technology", 
                 "events", "feature-stories", "conferences", "bzu-community"]

Categories_ar = ["ابحاث ومشاريع", "ثقافة وفنون", "الجامعة", "جوائز ومنح", "خريجون", "دولى", "رياضة", "زيارات", "شراكة مجنمعية", "طلاب", "علوم وتكنولوجيا", "فعاليات", "قصص مميزة", "مؤتمرات", "مجتمع الجامعة"]

data = {}
data['Article'] = []
#l = 0
for i in range(14, 14):
    
    for j in range(get_pages_num(Categories_en[i])+1):    
        soup = extract_html("https://www.birzeit.edu/ar/news/category/{}?page={}".format(Categories_en[i], j))
        stories = soup.findAll("h3", {"class": "field-content"})

        for n in range(len(stories)):
            title = stories[n].text
            url = "https://www.birzeit.edu"+stories[n].find('a').attrs['href']
            soup = extract_html("https://www.birzeit.edu"+stories[n].find('a').attrs['href'])
            divs = soup.findAll("div", {"class": "field-item even"})
            category = Categories_ar[i]
            
            if len(divs) != 0:
                ps = divs[3].findAll('p')
                content = ""
                for p in ps:
                    content += p.text
                add_to_json(data, title, content, url, category)
                #l += 1
        print(l)
        
save_json(data, 'results')
df = pd.json_normalize(data['Article'])
df.to_csv("University_News.csv", index=False)
