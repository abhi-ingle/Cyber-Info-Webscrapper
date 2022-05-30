import os
import telebot
import time
from datetime import date
import ctf
import ctfSites
import CyberExperts
import cybernews
import random
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Help'])
def menu(message):
  help_text="""
The following commands can be executed on the bot: \n
1)"/Greet": Greet the bot \n
2)"/TimeTable": Get the ctf TimeTable from www.ctftime.org \n
3)"/ctf": Get  the list of best CTF websites\n
4)"/Experts": Get the list of most followed CyberExperts on Twitter \n
5)"/News": Get the latest Cyber News\n
6)"/Help": Display the Help Menu
"""
  
  bot.send_message(message.chat.id,help_text)

  

@bot.message_handler(commands=['Greet'])
def greet(message):
    greetings=["Hey! How's it going?",'Hey!','Whatsup','Yo!','Glad to meet you!','Hello!']
    bot.reply_to(message,random.choice(greetings))


@bot.message_handler(commands=['TimeTable'])
def TimeTable(message):
  current_date_format=date.today()
  with open('Track/Month.txt') as f:
    for line in f:
      current_month=line
  if int(current_month)!=current_date_format.month:
    ctf.get_timetable()
    with open('Track/Month.txt','w') as f:
        f.write(f'{current_date_format.month}')
  time.sleep(2)
  bot.send_photo(message.chat.id,photo=open('ctf-timetable/timetable.png', 'rb'),caption="For more information visit www.ctftime.org")

@bot.message_handler(commands=['Experts'])
def Experts(message):
  CyberExperts.get_experts()
  Names=[]
  Twitter_IDs=[]
  with open("CyberExperts/ExpertName.txt","r") as NameFile:
    for line in NameFile:
      Names.append(line)
  with open("CyberExperts/TwitterProfile.txt","r") as ID_File:
    for line in ID_File:
      Twitter_IDs.append(line)
  
  result=f"*Here is the list of cybersecurity experts you can follow on Twitter*:https://twitter.com/\n{'~'*20}\n"
  for index in range(len(Names)):
    result += f"{index+1}: {Names[index]}\nLink: {Twitter_IDs[index]}\n{'~'*20}\n"
  
  bot.send_message(message.chat.id,result,parse_mode="markdown")
  
  
@bot.message_handler(commands=['News'])
def News(message):
  current_date_format=date.today()
  with open('Track/Day1.txt') as f:
    for line in f:
      current_day=line
  if int(current_day)!=current_date_format.day:
    cybernews.get_news()
    with open('Track/Day1.txt','w') as f:
      f.write(f'{current_date_format.day}')
  Headlines=[]
  Description=[]
  Links=[]
  with open("cybernews/Headlines.txt") as Headlines_file:
    for line in Headlines_file:
      Headlines.append(line)
  with open("cybernews/Description.txt") as Description_file:
    for line in Description_file:
      Description.append(line)

  with open("cybernews/links.txt") as links_file:
    for line in links_file:
      Links.append(line)
      
      
  for i in range(len(Headlines)):
    try:
      bot.send_photo(message.chat.id,photo=open(f'cybernews_cover_images/{i}.jpg', 'rb'),caption=f"*{Headlines[i]}*\n{Description[i]}\n{Links[i]}",parse_mode="markdown")
    except:
      continue

@bot.message_handler(commands=['ctf'])
def ctf_sites(message):
  current_date_format=date.today()
  with open('Track/Day2.txt') as f:
    for line in f:
      current_day=line
  if int(current_day)!=current_date_format.day:
    ctfSites.get_sites()
    with open('Track/Day2.txt','w') as f:
      f.write(f'{current_date_format.day}')
  


  site_Name=[]
  site_Description=[]
  site_Link=[]

  with open('ctf_sites/siteName.txt') as Names:
    for Name in Names:
      site_Name.append(Name)

  with open('ctf_sites/siteDescription.txt') as Descriptions:
    for Description in Descriptions:
      site_Description.append(Description)

  with open('ctf_sites/siteLink.txt') as Links:
    for Link in Links:
      site_Link.append(Link)
  result=f"*Here is the list of Best CTF websites*\n{'~'*20}\n"
  for i in range(len(site_Name)):
    result+=f"*{i+1}: {site_Name[i]}*\n{site_Description[i]}\nLink: {site_Link[i]}\n{'~'*20}\n"
  bot.send_message(message.chat.id,result,parse_mode="markdown")

  print("Done")

bot.polling()

