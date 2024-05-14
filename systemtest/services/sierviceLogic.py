# import sys
from systemtest.dao.requests import *
import systemtest.dao

import systemtest

def  addNewDataService(textquestion, question1,question2,
                question3, question4, selectQuestion):
    addNewDataDao(textquestion, question1,question2,
               question3, question4, selectQuestion)
def getAllDataService():
    return getAllDataDao()

def sendNumberStringForDeleteService(id):
    if id != None:
        sendNumberStringForDeleteDao(id)

def updateByIdServices(id,textquestion, question1,question2,
                question3, question4, selectQuestion):
    updateById(id,textquestion, question1,question2,
                question3, question4, selectQuestion)


def getDataByIdService(id):
    dataById=getDataById(id)
    return dataById

def equalsPasswordAndDataBaseService(login,password):
    user = getUserDao(login)
    if user != False and list(user[0].items())[-1][-1] == password:
        return True