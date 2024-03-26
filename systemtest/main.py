from flask import Flask, render_template, request, redirect
from services.sierviceLogic import *


app = Flask(__name__)

@app.route("/edit")
def edit():
    return render_template("edit.html")
@app.route("/editquestion", methods=['POST'])
def editquestion():
    if request.method=='POST':
        textquestion=request.form['textquestion']
        question1 = request.form['question1']
        question2 = request.form['question2']
        question3 = request.form['question3']
        question4 = request.form['question4']
        selectQuestion = request.form['select_question']

        addNewDataService(textquestion,question1,question2,
                            question3,question4,selectQuestion)
    return redirect("/edit")

@app.route("/allquestions")
def allQuestions():
    allData = getAllDataService()
    return render_template("allquestion.html", allData=allData)

@app.route("/delete")
def deleteQuestions():
    id = request.args.get("answer")
    sendNumberStringForDeleteService(id)
    return redirect("/allquestions")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
