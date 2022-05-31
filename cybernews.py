from bs4 import BeautifulSoup
import requests

# ~~~~~~~~~~~~~~~~~~~get_news() method scraps the top headlines and news link from https://cybernews.com/news/ ~~~~~~~~~~~~~~

def get_news():
  
  html_code = requests.get('https://cybernews.com/news/').text
  soup = BeautifulSoup(html_code, 'lxml')
  
  headlines = soup.find_all('h3', class_='heading heading_size_4') # individual headlines Scraped from main-page
  
  links = soup.find_all('a', class_='button space space_direction_vertical space_size_m display_block')
  descriptions = []
  
  cover_images = []
  
  for link in links:

#   Next individual webpage is scraped for description and cover_image
    try:
      html_code2 = requests.get(link['href']).text
      soup2 = BeautifulSoup(html_code2,'lxml')
      description = soup2.find('div', class_='content')
      descriptions.append(description.em.text) 
      cover_image = soup2.find('figure')
      cover_images.append(cover_image.img)
    except:
      continue

# Scraped data is stored in cybernews directory

  with open(f'Scraped_Data/cybernews/Headlines.txt','w') as f:
    for headline in headlines:
      f.write(f'{headline.text.strip()}\n')
  
  with open(f'Scraped_Data/cybernews/Description.txt','w') as f:
    for description in descriptions:
      f.write(f'{description}\n')

  with open(f'Scraped_Data/cybernews/links.txt','w') as f:
    for link in links:
      n_link=link['href']
      f.write(f'{n_link}\n')

# Scraped Cover-images stored in cybernews_cover_images directory 

  for index,image in enumerate(cover_images):
      try:
        name, src_link = image['alt'], image['data-src']
        with open(f'Scraped_Data/cybernews_cover_images/{index}.jpg','wb') as f:
            image_file = requests.get(src_link)
            f.write(image_file.content)
      except:
        continue

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 


    



      
