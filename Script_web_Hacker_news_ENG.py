################################################################# beautifulsoup #################################################################
#                               
#           INSTAL:             pip3 install beautifulsoup4                       
#           DEFINITION:         
#           DOCUMENTATION:      https://www.crummy.com/software/BeautifulSoup/bs4/doc/#calling-a-tag-is-like-calling-find-all
#              
##################################################################################################################################################

################################################################# Request ########################################################################
#                               
#           INSTAL:             pip3 install Request                      
#           DEFINITION:         
#           DOCUMENTATION:              
#
##################################################################################################################################################

################################################################# Selectors ######################################################################
#                               
#           INSTAL:                                  
#           DEFINITION:         
#           DOCUMENTATION:    https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors          
#
##################################################################################################################################################

################################################################# pprint #########################################################################
#                               
#           INSTAL:                                  
#           DEFINITION:         
#           DOCUMENTATION:    https://docs.python.org/3/library/pprint.html        
#
##################################################################################################################################################

################################################################# Scrapy #########################################################################
#                               
#           INSTAL:                                  
#           DEFINITION:         
#           DOCUMENTATION:    https://scrapy.org/                
#
##################################################################################################################################################


import requests
from bs4 import BeautifulSoup
import pprint #to print beautiful
import time

#to get connected
response = requests.get('https://news.ycombinator.com/news')
response2 = requests.get('https://news.ycombinator.com/news?p=2')

soup = BeautifulSoup(response.text, 'html.parser')
soup2 = BeautifulSoup(response2.text, 'html.parser')

#To take a score
links = soup.select('.storylink')
links2 = soup2.select('.storylink')

#How not everyone has a score instead of going for points let's go to the other class
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

#to join the links on the first and second pages
mega_links = links + links2
mega_subtext = subtext + subtext2

def create_custom_hacker_news (links, subtext):
    new_hn = []
    for idx, item in enumerate(links):
        
        #A Biblio Soup tem o getText() par pegar só no texto
        title = item.getText()
        href = item.get('href', None)
        score = subtext[idx].select('.score')
        if len(score):
            points = int(score[0].getText().replace(' points', ''))
            if points > 99:
                new_hn.append({'Title: ': title, 'Link: ': href, 'Vote: ': points})

    return sort_stories_by_votes(new_hn)

def sort_stories_by_votes(Hacker_new_list):
    #Lambda 
    return sorted(Hacker_new_list, key= lambda k:k['Vote: '], reverse=True) 

pprint.pprint(create_custom_hacker_news(mega_links,mega_subtext))
