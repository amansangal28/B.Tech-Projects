import socket
import sys
import RPi.GPIO as GPIO
from thread import *
import datetime
import random
import requests
import os
import time
import smtplib
from gpiozero import Buzzer
from time import sleep
import picamera
import picamera
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
from email.mime.image import MIMEImage
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import Adafruit_DHT
from email.mime.image import MIMEImage
GPIO.setmode(GPIO.BCM)

button1=19
toaddr = "aditiagarwal34550@gmail.com"
fromaddr = "iotworkshop88@gmail.com"
#GPIO.setup(8,GPIO.OUT)
mail = MIMEMultipart()

mail['From'] = fromaddr
mail['To'] = toaddr
mail['Subject'] = "Attachment"
body = "Please find the attachment"
HIGH=1
LOW=0
GPIO.setwarnings(False)

GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
data=""
def sendMail(data):
    mail.attach(MIMEText(body, 'plain'))
    #print (data)
    dat='%s.jpg'%data
    #print (dat)
    time.sleep(5)
    attachment = open(dat,'rb')
    image=MIMEImage(attachment.read())
    attachment.close()
    time.sleep(2)
    mail.attach(image)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "cloud@123")
    text = mail.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def capture_image():
    data= time.strftime("%d_%b_%Y|%h:%mm:%ss")
    camera.start_preview()
    time.sleep(5)
   # print (data)
    camera.capture('%s.jpg'%data)
    camera.stop_preview()
    time.sleep(1)
    sendMail(data)
camera = picamera.PiCamera()
camera.rotation=180
camera.awb_mode= 'auto'
camera.brightness=55
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)


#camera=picamera.PiCamera()
#camera.rotation=180
#camera.awb_mode='auto'
#camera.brightness=55
#toaddr = "aditiagarwal34550@gmail.com"
#fromaddr = "iotworkshop88@gmail.com"
#mail=MIMEMultipart()
#mail['From']=fromaddr
#mail['To']=toaddr
#mail['Subject']="attachment"
#body="attachment"
#HIGH=1
#LOW=0
#GPIO.setwarnings(False)
#GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_UP)
#data=""
host = ''
port = 8269
address = (host, port)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
server_socket.listen(5)
numbOfConn = 0
addressList = []
clients = set()
##############################################################################
#small database of our bot
greetings = ['hola', 'hello', 'hi', 'hey']
questions = ['how are you', 'how are you doing']
responses = ['okay', 'i am fine']
database={
    'Ninja':'hello,sir how can i help you',
    'name':'Ninja',
    'what is your name':'my name is Ninja',
    'hello Ninja':'hello,sir how can i help you',
    'what can you do for me':'i can do many things..'
}
print ("Listening for client . . .")
###############################################################################
#chatbot code here

def mail(content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "cloud@123")
    text = mail.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
#GPIO.setwarnings(False)
#GPIO.setup(12, GPIO.OUT)

def distance():
    GPIO.output(12, True)
    time.sleep(0.00001)
    GPIO.output(12, False)
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(16) == 0:
        StartTime = time.time()
    while GPIO.input(16) == 1:
        StopTime = time.time()
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
    return distance
def chatboat(data):
    if data in database:
        print(database[data])
        sclient(database[data])
    elif data in questions:
        random_response = random.choice(responses)
        print(random_response)
        sclient(random_response)
    elif data in greetings:
        random_greeting = random.choice(greetings)
        print(random_greeting)
        sclient(random_greeting)
        #os.system("flite -t '"+ random_greeting +"'")
    elif 'fan one on'in data or 'fan one on' in data:
        sclient("fan turn on")
        #os.system("flite -t 'light turn on'")
        GPIO.output(2,False)
        print("fan on")
    elif 'fan one off' in data or 'led one off' in data:
        sclient("fan turn off")
        #os.system("flite -t 'light turn off'")
        GPIO.output(2,True)
        print("fan Off")
    elif 'light two on'in data or 'light to on' in data:
        sclient("light turn on")
        #os.system("flite -t 'light turn on'")
        GPIO.output(3,False)
        print("Light on")
    elif 'light two off' in data or 'light to off' in data:
        sclient("light turn off")
        #os.system("flite -t 'light turn off'")
        GPIO.output(3,True)
        print("Light Off")
    elif 'fan one on'in data:
        sclient("fan turn on")
        #os.system("flite -t 'light turn on'")
        GPIO.output(18,False)
        print("fan on")
    elif 'fan one off' in data or 'fan one off' in data:
        sclient("fan turn off")
        #os.system("flite -t 'light turn off'")
        GPIO.output(18,True)
        print("fan Off")
    elif 'fan two on' in data or 'fan to on' in data:
        sclient("fan turn on")
        #os.system("flite -t 'light turn off'")
        GPIO.output(23,False)
        print("fan On")
    elif 'fan two off' in data or 'fan to off' in data:
        sclient("fan turn off")
        #os.system("flite -t 'light turn off'")
        GPIO.output(23,False)
        print("fan Off")
    elif 'time' in data:
        now = datetime.datetime.now()
        time=str(now.hour)+str(":")+str(now.minute)
        print(time)
        #os.system("flite -t '"+ time+"'")
        sclient(time)
    elif 'temperature' in data:
        humidity, temperature = Adafruit_DHT.read_retry(11, 24)
        sclient(" Temperature = {} C".format(temperature))
        print (" Temperature = {} C".format(temperature))
    elif 'humidity' in data:
        humidity, temperature = Adafruit_DHT.read_retry(11, 24)  #
GPIO27 (BCM notation)
        sclient("Humidity = {} % ".format(humidity))
        print ("Humidity = {} % ".format(humidity))
    elif 'humidity and temperature' in data:
        humidity, temperature = Adafruit_DHT.read_retry(11, 24)  #
GPIO27 (BCM notation)
        sclient("Humidity = {} %; Temperature = {} C".format(humidity,
temperature))
        print ("Humidity = {} %; Temperature = {} C".format(humidity,
temperature))
    elif 'enable lock' in data:
        sclient("lock enable")
        buzzer=Buzzer(8)
        if GPIO.input(button1)==1:
            capture_image()
            while 1:
                buzzer.on()
                sleep(1)
                buzzer.off()
                sleep(1)
            while(GPIO.input(button1)==1):
                time.sleep(1)
        else:
            time.sleep(0.01)
    elif 'disable lock' in data:
        buzzer=Buzzer(8)
        buzzer.off()
    elif 'date'in data:
        now = datetime.datetime.now()
        date=str("%s/%s/%s" % (now.month,now.day,now.year))
        print(date)
        #os.system("flite -t '"+date+"'")
        sclient(date)
    else:
        conn.send("sorry please repeat..")
        add_data = open("newdata.txt", 'a')
        add_data.write("\n")
        add_data.write(data)
        add_data.close()
###############################################################################
#Sending Reply to all clients
def sclient(mess):
    for c in clients:
        try:
            c.send(mess)
        except:
            c.close()
##############################################################################
#server code here
def clientthread(conn,addressList):
#infinite loop so that function do not terminate and thread do not end.
    while True:
        output = conn.recv(2048);
        if output.strip() == "disconnect":
            conn.close()
            sys.exit("Received disconnect message.  Shutting down.")
            conn.send("connection loss")
        elif output:
            print ("Message received from client:")
            data=str(output).lower()
            print (data)
            print("Reply from the server:")
            chatboat(data)

while True:
#Accepting incoming connections
    conn, address = server_socket.accept()
    print ("Connected to client at ", address)
    clients.add(conn)
#Creating new thread. Calling clientthread function for this function
and passing conn as argument.
    start_new_thread(clientthread,(conn,addressList)) #start new
thread takes 1st argument as a function name to be run, second is the
tuple of arguments to the function.

conn.close()
sock.close()
