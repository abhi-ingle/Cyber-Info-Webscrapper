@bot.message_handler(commands=['Hi'])
# def hello(message):
#   bot.send_message(message.chat.id,"Hello!")
  
# @bot.message_handler(commands=['TimeTable'])
# def TimeTable(message):
#   current_date_format=date.today()
#   with open('Track/Month.txt') as f:
#     for line in f:
#       current_month=line
#   if int(current_month)!=current_date_format.month:
#     ctf.get_timetable()
#     with open('Track/Month.txt','w') as f:
#         f.write(f'{current_date_format.month}')
#   time.sleep(2)
#   bot.send_photo(message.chat.id,photo=open('ctf-timetable/timetable.png', 'rb'),caption="For more information visit www.ctftime.org")

# @bot.message_handler(commands=['Experts'])
# def Experts(message):
#   CyberExperts.get_experts()
#   Names=[]
#   Twitter_IDs=[]
#   with open("CyberExperts/ExpertName.txt","r") as NameFile:
#     for line in NameFile:
#       Names.append(line)
#   with open("CyberExperts/TwitterProfile.txt","r") as ID_File:
#     for line in ID_File:
#       Twitter_IDs.append(line)
#   result="https://twitter.com/\n\n"
#   for index in range(len(Names)):
#     result += f"{index+1}: {Names[index]}:{Twitter_IDs[index]}\n"
#   bot.send_message(message.chat.id,result)
  
  
# @bot.message_handler(commands=['News'])
# def News(message):
#   current_date_format=date.today()
#   with open('Track/Day.txt') as f:
#     for line in f:
#       current_day=line
#   if int(current_day)!=current_date_format.day:
#     cybernews.get_news()
#     with open('Track/Day.txt','w') as f:
#       f.write(f'{current_date_format.day}')
#   Headlines=[]
#   Description=[]
#   Links=[]
#   with open("cybernews/Headlines.txt") as Headlines_file:
#     for line in Headlines_file:
#       Headlines.append(line)
#   with open("cybernews/Description.txt") as Description_file:
#     for line in Description_file:
#       Description.append(line)

#   with open("cybernews/links.txt") as links_file:
#     for line in links_file:
#       Links.append(line)
      
      
#   for i in range(len(Headlines)):
#     bot.send_photo(message.chat.id,photo=open(f'cyb