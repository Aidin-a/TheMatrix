import os
import sys
import game
from time import sleep
import db


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def say(string):
    sys.stdout.write(string)


def sayLine():
    say("\n/*\n")
    say(" *        Matrix VR Game          *\n")
    say(" * Getting Ready For Installation *\n")
    say(" *      Preparing Data Base       *\n")
    say(" *      Getting Dependencies      *\n")
    say(" *      Starting Game Setup       *\n")
    say(" */\n\n")


def startGame():
    sleep(0.25)
    say("> Hello?...")
    sleep(1.5)
    say("\n> Is There Any One Answer Me?...")
    sleep(1.5)
    say("\n> I Need Help!...")
    sleep(1.5)
    say("\n> I Have Been Robbed By A Thief!...")
    sleep(1.5)
    say("\n> He Is Going To Kill Me!...")
    sleep(1.5)
    say("\n> Help Me Please!...")
    sleep(1.5)
    say("\n> Help Me Please!...")
    sleep(1.5)
    say("\n> Help Me Please!...")
    sleep(1.5)
    say("\n> NoNoNoNoNoNoNoNoNoOoOoOoOoOoOoOoO!...")
    sleep(2.5)
    say("\n> Press Enter To Start The Game Setup!...")
    input()
    sleep(0.25)
    gameSetup()


def setupFinished():
    say("> Press Any Key To Start The Game!...")
    DB = db.getDB()
    DB["isInstalled"] = True
    db.setDB(DB)
    input()
    runGame()


def checkSetupInputs(inpt, txt):
    for i in range(1000):
        if i < 1000 and inpt == "":
            say(txt)
            inpt = input()
        elif i > 1000 and inpt == "":
            quit()


def gameSetup():
    sayLine()
    say("> Enter Your Name: ")
    name = input()
    checkSetupInputs(name, "> Enter Your Name: ")
    say("> Enter Your Email: ")
    email = input()
    checkSetupInputs(email, "> Enter Your Email: ")
    say("> Enter Game Password: ")
    password = input()
    checkSetupInputs(password, "> Enter Game Password: ")
    say("> Congratulations!...\n")
    say("> Game Setup Finished Successfully!...\n")
    setupFinished()


def runGame():
    game.start()
