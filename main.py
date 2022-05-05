import os
import telebot
import time
from datetime import date
import ctf
import CyberExperts
import cybernews

API_KEY = os.environ['API_KEY']
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Help'])
def menu(message):
  help_text="""
The following commands can be executed on the bot: \n
1)"\\Greet": Greet the bot \n
2)"\\Hi": Say Hi to the bot \n
3)"\\TimeTable": Get the ctf TimeTable from www.ctftime.org \n
4)"\\Experts": Get the list of most followed CyberExperts on Twitter \n
5)"\\News" : Get the latest Cyber News
"""
  
  bot.send_message(message.chat.id,help_text)

  

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message,"Hey! How is it going?")

@bot.message_handler(commands=['Hi'])
def hello(message):
  bot.send_message(message.chat.id,"Hello!")
  
@bot.message_handler(commands=['TimeTable'])
def TimeTable(message):
  current_date_formate=date.today()
  current_month=5 #at time of writing the program
  if current_month!=current_date_formate.month:
    ctf.get_timetable()
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
  result="https://twitter.com/\n\n"
  for index in range(len(Names)):
    result += f"{index+1}: {Names[index]}:{Twitter_IDs[index]}\n"
  bot.send_message(message.chat.id,result)
  
  
@bot.message_handler(commands=['News'])
def News(message):
  headlines,description=cybernews.py
  for i in range(len())



bot.polling()

