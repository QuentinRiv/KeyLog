# A simple keylogger for Windows, Linux and Mac

[Keylogger wiki](https://en.wikipedia.org/wiki/Keystroke_logging)


Welcome to the simple keylogger repo! A keylogger is a program that records your keystrokes, and this program saves them in a log file on your local computer, before sending them to me.

Check out below to learn how to install them. These keyloggers are simple and bare bones, however they work great! Feel free to fork and improve it if you want. Be sure to check out the [issues](https://github.com/QuentinRiv/KeyLog/issues) or [pull requests](https://github.com/QuentinRiv/KeyLog/pulls) to see if your problem has been fixed, or to help out others.

Currently, there are three keylogger programs for the major operating systems; Windows, Mac and Linux.


## Linux

### Installation


The following instructions will install Keylogger using pip3 .

```
  pip3 install -r requirements.txt
```

## How to run it

By running `nohup python3 KeyLog.py &` command, it'll start to log your strokes.

The Keylogger is now running! It will log your strokes to a file .
Stop it by typing the command `fg` then hitting `CTRL+C`

or

`kill {PID}` for example `kill 12529`


---

---
#### Uses

Some uses of a keylogger are:

- Business Administration: Monitor what employees are doing.
- School/Institutions: Track keystrokes and log banned words in a file.
- Personal Control and File Backup: Make sure no one is using your computer when you are away.
- Parental Control: Track what your children are doing.
- Self analysis

---

Feel free to contribute to fix any problems, or to submit an issue!

Please note, this repo is for educational purposes only. No contributors, major or minor, are to fault for any actions done by this program.

This README was inspired from GiacomoLaw's repo. Click [here](https://github.com/GiacomoLaw/Keylogger/blob/master/README.md) for more detail.
