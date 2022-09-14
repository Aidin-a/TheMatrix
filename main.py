import lib
import db

if db.getDB()["isInstalled"]:
    lib.runGame()
else:
    lib.startGame()

quit(input())
