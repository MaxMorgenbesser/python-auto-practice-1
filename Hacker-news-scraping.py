import imp
from urllib import response
import requests #http requests lets you interact with http
# BS4 scrapes the information
from bs4 import BeautifulSoup
#sends emails
import smtplib 

#lets you put something in an email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#gives you the date
import datetime
now = datetime.datetime.now()
#empty string 
content=''

def extract_news(url):
    print("Extracting Hacker News Stories")
    #assigns value to email body
    cnt = ''
    cnt +=('<b>HN Top Stories</b> \n' + '<br>'+'_'*50+',<br>')
    response = requests.get(url) #sends a get request to a specific url
    content=response.content # returns content of url
    soup=BeautifulSoup(content, 'html.parser') #extracts/ makes soup 
    #
    for i, tag in enumerate(soup.find_all('td', attrs={'class' : 'title', 'valign': ''})):
        cnt += ((str(i+1)+' :: ' + tag.text + "\n" + "<br>" ) if tag.text != 'More' else '')
    return cnt
#extracting everywhere where there is td in html this creates a table so extracting from the tables
#find_aLL extracts everywhere there is class and title inside of td
cnt = extract_news('https://news.ycombinator.com/')
content+=cnt
content+= '<br>------</br>'
content+= '<br><br>End of Message'
        
    