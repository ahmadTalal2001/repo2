import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
now = datetime.datetime.now()

content = ''
#step1
def extract_news(url):
    print('extracting Hacker news Stories ...')
    cnt = ''
    cnt +=('<b> HN Top Stories:</b>\n' + '<br>'+'-'*50+'br')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += (str(i+1)+ '::' + '<a href="'+tag.a.get('href')+'">'+tag.text +'</a>' + "\n" + '<br>' if tag.text != 'more' else '')

    return(cnt)


cnt = extract_news('https://news.ycombinator.com/')
content += cnt #the out side content
content += ('<br>------<br>')
content +=('<br><br>End of Message')


#---------------------------------
#step2
print('composing Email')

SERVER = 'smtp.gmail.com'
PORT = 587
FROM ='ahmdalmghny5@gmail.com'
TO ='aalmoghany@smail.ucas.edu.ps'
PASS= 'ah.67.123'

msg=MIMEMultipart()

msg['subject']='Top News Stories HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(
    now.year)

msg['From']= FROM
msg['To']=TO

msg.attach(MIMEText(content,'html'))

#-----------------------------------------
#step 3 start connect with server
server = smtplib.SMTP(SERVER, PORT )
server.set_debuglevel(1) # if find give me it
server.ehlo() # every thing ok start connect
server.starttls() # which method to connect (start TLS)
server.login(FROM ,PASS) #ok we are connect which email and pass need to login
server.sendmail(FROM ,TO ,msg.as_string()) # good Im in your email start sending from to and the content

print('email Sent')
server.quit()






