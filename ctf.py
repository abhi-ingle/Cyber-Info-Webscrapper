from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ get_timetable takes the calendar screenshot from ctftime.org ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_timetable():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  
  driver = webdriver.Chrome(options=chrome_options)
  driver.get('https://calendar.google.com/calendar/embed?showTitle=0&showNav=0&showPrint=0&showCalendars=0&height=600&wkst=2&bgcolor=%23FFFFFF&src=ctftime%40gmail.com&color=%232952A3&ctz=Africa%2FAbidjan')
  
  time.sleep(3)
  
# Screenshot of the calendar taken and saved in the ctf-timetable directory

  driver.get_screenshot_as_file("Scraped_Data/ctf-timetable/timetable.png")
  driver.quit()

#For more info visit https://ctftime.org/calendar/

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~