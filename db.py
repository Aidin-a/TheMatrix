import json


def getDB():
    DBFile = open("./DB.json", "r")
    DBTxt = DBFile.read()
    DBObj = json.loads(DBTxt)
    return DBObj


def setDB(DB):
    DBJson = json.dumps(DB)
    DBFileW = open("./DB.json", "w")
    setStatus = DBFileW.write(DBJson)
    return setStatus
