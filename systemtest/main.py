from flask import Flask, render_template, request, redirect, session
from services.sierviceLogic import *


app = Flask(__name__)
app.secret_key="1234567890"

@app.route("/edit")
def edit():

    return render_template("addquestion.html")
@app.route("/editquestion", methods=['POST'])
def editquestion():
    if request.method=='POST':
        textquestion=request.form['textquestion']
        question1 = request.form['question1']
        question2 = request.form['question2']
        question3 = request.form['question3']
        question4 = request.form['question4']
        selectQuestion = request.form['select_question']
        print("55555")

        addNewDataService(textquestion,question1,question2,
                            question3,question4,selectQuestion)
    return redirect("/allquestions")

@app.route("/allquestions")
def allQuestions():
    print("nnnnn")
    allData = getAllDataService()
    return render_template("allquestion.html", allData=allData)

@app.route("/delete")
def deleteQuestions():
    id = request.args.get("answer")
    print('id ',id)
    sendNumberStringForDeleteService(id)
    return redirect("/allquestions")

@app.route('/update/<id>')
def updateById(id):
    dataById=getDataByIdService(id)
    return render_template("editquestion.html",dataById=dataById)

@app.route('/update',methods=['POST'])
def updateByIdPost():
    id = request.form['id']
    textquestion = request.form['textquestion']
    question1 = request.form['question1']
    question2 = request.form['question2']
    question3 = request.form['question3']
    question4 = request.form['question4']
    selectQuestion = request.form['select_question']
    updateByIdServices(id, textquestion, question1, question2, question3, question4, selectQuestion)
    return redirect("/allquestions")
@app.route('/',methods=['GET','POST'])
def register():
    return render_template("login.html")

@app.route('/login',methods=['GET','POST'])
def check():
    if request.method=='POST':
        login = request.form['log']
        password = request.form['pw']
        if equalsPasswordAndDataBaseService(login,password)==True:
            session[login] = password
        # print(type(user[0]))
        # if user == 'NoneType':
        #     return False
        # mas = [{'test2': 'test'},
        #        {'пользователь2': 'пароль'}]
        # masLog = list()
        # for i in mas:
        #     masLog.append(list(i)[0])
        # for login in session.items():
        #     if login[0] in masLog:
        #         print('Хорошо!')
                # if login in session and session[login] == password:
    return render_template("login.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
