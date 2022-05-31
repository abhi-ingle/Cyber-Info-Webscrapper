from bs4 import BeautifulSoup
import requests

# ~~~~~~~~~~~~~~~~~~~~~~~~~~get_experts() method scraps data about top cybersecurity exprests on twitter from https://www.purevpn.com/blog/top-cybersecurity-experts/~~~~~~~~~~~~~

def get_experts():
  html_code = requests.get('https://www.purevpn.com/blog/top-cybersecurity-experts/').text
  soup = BeautifulSoup(html_code, 'lxml')
  
  names = soup.find_all('a',rel="noopener")
  names.pop() # irrelevant Scraped data removed

  name_titles=[]
  twitter_Profiles=[]
  for name in names:
      name_titles.append(name.text)
      twitter_Profiles.append(name['href'])
  
# Scraped data stored on CyberExperts directory

  with open(f'Scraped_Data/CyberExperts/ExpertName.txt','w') as f:
      for name_title in name_titles:
          f.write(f'{str(name_title)}\n') 
  
  with open(f'Scraped_Data/CyberExperts/TwitterProfile.txt','w') as f:
      for twitter_Profile in twitter_Profiles: 
          f.write(f'{str(twitter_Profile)}\n') 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~