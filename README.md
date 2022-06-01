<pre>
   ______      __                 ____      ____    
  / ____/_  __/ /_  ___  _____   /  _/___  / __/___ 
 / /   / / / / __ \/ _ \/ ___/   / // __ \/ /_/ __ \
/ /___/ /_/ / /_/ /  __/ /     _/ // / / / __/ /_/ /
\____/\__, /_.___/\___/_/     /___/_/ /_/_/  \____/ 
     /____/                                         
</pre>
</br>
BOT LINK: https://t.me/CyberInf0_bot
</br>

# WORKING OF THE BOT

### Help Menu: 
Displays the commands which can be executed on the bot
![ezgif-2-609b638928](https://user-images.githubusercontent.com/88927842/171376432-b228ebe1-b4d6-4432-a879-8b13dee67860.gif)

## Following data can be scraped using Cyber Info:

### 1) Cybersecurity News:
Top Headlines are scraped daily from https://cybernews.com/news/ </br> 
Then from the individual news-links description and cover-image is grabed, all this data is organised in a presentable form and displayed to the user.
![News](https://user-images.githubusercontent.com/88927842/171376461-35b784fa-dd39-450e-aca5-9ceb9449d5f4.JPG)

### 2) CTF-TimeTable
Screenshot of TimeTable of Capture the flag events is scraped monthly from www.ctftime.org.</br>
Selenium Webdriver is used for this purpose.
![TimeTable](https://user-images.githubusercontent.com/88927842/171376487-64009b86-251b-4895-9935-f4592cb3365e.JPG)

### 3) CTF-Websites
Data of top websites to play CTFs is scraped and the list is displayed to the user.
![ctf-websites](https://user-images.githubusercontent.com/88927842/171378979-8d3cb041-f5b0-4b40-8cfa-c89332912fe5.JPG)

### 4) Cybersecurity Youtube Channels
Data of Cybersecurity YouTube channels is scrapped containing the channel name, frequent topics posted on channel and the channel link, all this data is organised in presentable form and displayed to the user.
![Channels](https://user-images.githubusercontent.com/88927842/171378995-a58fbb98-8b3d-4094-a1b0-05afe531a25e.JPG)

### 5) Cybersecurity Experts on Twitter
Profile links of Top Cybersecurity Experts on Twitter is scaped and the list is displayed to the user.
![Experts](https://user-images.githubusercontent.com/88927842/171379010-5140cd10-d7bc-4888-a7ea-8996d8966539.JPG)

#### <i>NOTE: The data is not scraped for each request as too many requests may cause unintentional Denial of Servive (DoS) Attack on the sites.</br>The sites are scraped periodically and the scraped data is stored in files(Cyber-Info v1 later versions may use databases).</br>Example: for CTF-TimeTable the bot scraps the site monthly and stores the new time-table for each month, for news the bot scraps the site once in a day and stores the news of each new day.</i>
