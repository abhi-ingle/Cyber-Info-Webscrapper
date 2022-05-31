from bs4 import BeautifulSoup
import requests

def get_sites():
    html_code = requests.get("https://ctfsites.github.io/").text
    soup = BeautifulSoup(html_code,'lxml')

    table=soup.find('table',id="ttable")
    td=table.find_all('td')
    site_name=[]
    site_description=[]
    site_link=[]
    count=0
    for content in td:
        if count>2:
            count=0
            site_name.append(content.text)
        elif count==0:
            site_name.append(content.text)
        elif count==1:
            site_description.append(content.text)
        elif count==2:
            site_link.append(content.a['href'])
        count+=1
    
    with open(f'Scrapped_Data/ctf_sites/siteName.txt','w') as f:
        for name in site_name:
            f.write(f'{str(name)}\n')
    with open(f'Scrapped_Data/ctf_sites/siteDescription.txt','w') as f:
        for description in site_description:
            f.write(f'{str(description)}\n')
    with open(f'Scrapped_Data/ctf_sites/siteLink.txt','w') as f:
        for link in site_link:
            f.write(f'{str(link)}\n')
     
    
    
get_sites()
