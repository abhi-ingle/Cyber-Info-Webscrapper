import os
import telebot
import time
from datetime import date
import ctf
import ctfSites
import cyber_channels
import CyberExperts
import cybernews
import random
from dotenv import load_dotenv

load_dotenv()    
API_KEY = os.getenv("API_KEY")
bot = telebot.TeleBot(API_KEY)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~HELP COMMAND~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@bot.message_handler(commands=["Help"])
def menu(message):
    help_text = """
Following commands can be executed on the bot: \n
1)"/Greet": Greet the bot \n
2)"/TimeTable": Get the ctf TimeTable from www.ctftime.org \n
3)"/ctf": Get the list of best CTF websites\n
4)"/Channels": Get the list of Top Cybersecurity Youtube Channels\n
5)"/Experts": Get the list of most followed CyberExperts on Twitter \n
6)"/News": Get the latest Cyber News\n
7)"/Help": Display the Help Menu
"""
#    Help menu displayed
    bot.send_message(message.chat.id, help_text)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~GREET COMMAND~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@bot.message_handler(commands=["Greet"])
def greet(message):
    greetings = [
        "Hey! How's it going?",
        "Hey!",
        "Whatsup",
        "Yo!",
        "Glad to meet you!",
        "Hello!",
    ]

#   Random greeting chosen from the list and send to the user 
    bot.reply_to(message, random.choice(greetings))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~TIMETABLE COMMAND~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@bot.message_handler(commands=["TimeTable"])
def TimeTable(message):
    # TimeTable is scraped once in a month, the following code block checks for new month and scraps new timetable from the site
    current_date_format = date.today()
    with open("Scraped_Data/Track/Month1.txt") as f:
        for line in f:
            current_month = line
    if int(current_month) != current_date_format.month: # if old and current month doesn't match then the webpage is scraped
        ctf.get_timetable() # scraping function get_timetable() called from ctf module
        with open("Scraped_Data/Track/Month1.txt", "w") as f:
            f.write(f"{current_date_format.month}") # current month stored in Month1.txt file

    time.sleep(2) # wait time of 2 sec added to ensure that the webpage loads and selenium chromedriver takes the screenshot

#   Timetable Displayed

    bot.send_photo(
        message.chat.id,
        photo=open("Scraped_Data/ctf-timetable/timetable.png", "rb"),
        caption="For more information visit www.ctftime.org",
    )

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CTF COMMAND~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@bot.message_handler(commands=["ctf"])
def ctf_sites(message):
    # CTF list is scraped once in a day, the following code block checks for new day and scraps new list from the site
    current_date_format = date.today()
    with open("Scraped_Data/Track/Day2.txt") as f:
        for line in f:
            current_day = line
    if int(current_day) != current_date_format.day: # if old and current day doesn't match then the webpage is scraped
        ctfSites.get_sites() # scraping function get_sites() called from ctfSites module
        with open("Scraped_Data/Track/Day2.txt", "w") as f:
            f.write(f"{current_date_format.day}") # current date(day) stored in Day2.txt file

    site_Name = []
    site_Description = []
    site_Link = []

#  Stored Scraped data is retrieved from the respective files and organised in presentable form

    with open("Scraped_Data/ctf_sites/siteName.txt") as Names:
        for Name in Names:
            site_Name.append(Name)

    with open("Scraped_Data/ctf_sites/siteDescription.txt") as Descriptions:
        for Description in Descriptions:
            site_Description.append(Description)

    with open("Scraped_Data/ctf_sites/siteLink.txt") as Links:
        for Link in Links:
            site_Link.append(Link)

    result = f"*Here is the list of Best CTF websites*\n{'~'*20}\n"

    for i in range(len(site_Name)):
        result += f"*{i+1}: {site_Name[i]}*\n{site_Description[i]}\nLink: {site_Link[i]}\n{'~'*20}\n"

#   Top CTF website list is displayed
    bot.send_message(message.chat.id, result, parse_mode="markdown")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CHANNELS COMMAND~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@bot.message_handler(commands=["Channels"])
def Channels(message):
  # Cybersecurity Channels list is scraped once in a day, the following code block checks for new day and scraps new list from the site
  current_date_format = date.today()
  with open("Scraped_Data/Track/Day3.txt") as f:
      for line in f:
          current_day = line
  if int(current_day) != current_date_format.day: # if old and current day doesn't match then the webpage is scraped
      cyber_channels.get_channels() # scraping function get_channels() called from cyber_channels module
      with open("Scraped_Data/Track/Day3.txt", "w") as f:
          f.write(f"{current_date_format.day}") # current date(day) stored in Day3.txt file
  
  Headings=[]
  Contents=[]
  Links=[]

#  Stored Scraped data is retrieved from the respective files and organised in presentable form
  with open("Scraped_Data/channels/heading.txt") as Headings_file:
    for line in Headings_file:
      Headings.append(line)

  with open("Scraped_Data/channels/content.txt") as Contents_file:
    for line in Contents_file:
      Contents.append(line)
  with open("Scraped_Data/channels/link.txt") as Links_file:
    for line in Links_file:
      Links.append(line)

  result=f"*Here is the list of Top Cybersecurity Youtube Channels*\n{'~'*20}\n"
  for index in range(len(Headings)):
    result += f"*{Headings[index]}*\n{Contents[index]}\n*{Links[index]}*\n{'~'*20}\n"

# Top Cybersecurity Youtube Channels displayed
  bot.send_message(message.chat.id,result,parse_mode="markdown")
   
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~EXPERTS COMMAND~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@bot.message_handler(commands=["Experts"])
def Experts(message):
    # Experts list is scraped once in a month, the following code block checks for new month and scraps new timetable from the site
    current_date_format = date.today()
    with open("Scraped_Data/Track/Month2.txt") as f:
        for line in f:
            current_month = line
    if int(current_month) != current_date_format.month: # if old and current month doesn't match then the webpage is scraped
        CyberExperts.get_experts() # scraping function get_experts() called from CyberExperts module
        with open("Scraped_Data/Track/Month2.txt", "w") as f:
            f.write(f"{current_date_format.month}") # current month stored in Month2.txt file

#  Stored Scraped data is retrieved from the respective files and organised in presentable form

    Names = []
    Twitter_IDs = []
    with open("Scraped_Data/CyberExperts/ExpertName.txt", "r") as NameFile:
        for line in NameFile:
            Names.append(line)
    with open("Scraped_Data/CyberExperts/TwitterProfile.txt", "r") as ID_File:
        for line in ID_File:
            Twitter_IDs.append(line)

    result = f"*Here is the list of cybersecurity experts you can follow on Twitter*:https://twitter.com/\n{'~'*20}\n"
    for index in range(len(Names)):
        result += f"{index+1}: {Names[index]}\nLink: {Twitter_IDs[index]}\n{'~'*20}\n"

# List of Cybersecurity experts displayed
    bot.send_message(message.chat.id, result, parse_mode="markdown")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~NEWS COMMAND~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@bot.message_handler(commands=["News"])
def News(message):
# News Headlines are scraped once in a day, the following code block checks for new day and scraps new list from the site
    current_date_format = date.today()
    with open("Scraped_Data/Track/Day1.txt") as f:
        for line in f:
            current_day = line
    if int(current_day) != current_date_format.day: # if old and current day doesn't match then the webpage is scraped
        cybernews.get_news() # scraping function get_news() called from cybernews module
        with open("Scraped_Data/Track/Day1.txt", "w") as f:
            f.write(f"{current_date_format.day}")# current date(day) stored in Day1.txt file

    Headlines = []
    Description = []
    Links = []

#  Stored Scraped data is retrieved from the respective files and organised in presentable form
    with open("Scraped_Data/cybernews/Headlines.txt") as Headlines_file:
        for line in Headlines_file:
            Headlines.append(line)

    with open("Scraped_Data/cybernews/Description.txt") as Description_file:
        for line in Description_file:
            Description.append(line)

    with open("Scraped_Data/cybernews/links.txt") as links_file:
        for line in links_file:
            Links.append(line)

# Cybersecurity News Displayed
    for i in range(len(Headlines)):
        try:
            bot.send_photo(
                message.chat.id,
                photo=open(f"Scraped_Data/cybernews_cover_images/{i}.jpg", "rb"),
                caption=f"*{Headlines[i]}*\n{Description[i]}\n{Links[i]}",
                parse_mode="markdown",
            )
        except:
            continue


bot.polling()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~