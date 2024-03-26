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