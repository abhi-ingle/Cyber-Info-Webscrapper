
from bs4 import BeautifulSoup
import requests

def get_channels():
    html_code = requests.get('https://www.websiterating.com/online-security/best-youtube-channels-to-learn-cybersecurity/').text
    soup = BeautifulSoup(html_code,'lxml')

    headings = soup.find_all('h3')
    headings=headings[:10]
    
    content = soup.find_all('p',class_="color-box")
    content.pop(0)
    
       



    with open(f'Scrapped_Data/channels/heading.txt','w') as f:
        for heading in headings:
            f.write(f'{(heading.text)}\n')
    
    with open(f'Scrapped_Data/channels/content.txt','w') as f:
        for index in range(0,len(content),2):
            f.write(f'{(content[index].text)}\n')

    with open(f'Scrapped_Data/channels/link.txt','w') as f:
        for index in range(1,len(content),2):
            f.write(f'{(content[index].text)}\n')
