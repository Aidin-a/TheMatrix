import lib
from db import db

if not db.isInstalled:
    lib.startGame()
else:
    lib.runGame()

quit(input())