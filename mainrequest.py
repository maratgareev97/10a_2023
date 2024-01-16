from flask import Flask, render_template, request, redirect
import client

app = Flask(__name__)


@app.route('/')
def main():
    rezult = client.getAllData()
    print(rezult)
    return render_template("mainrequest.html", rezult=rezult)

@app.route('/add', methods=['POST'])
def addData():
    if request.method=="POST":
        name=request.form['name']
        phone=request.form['phone']
        print(name,phone)
        client.addNewData(name,phone)
        print("!!!!!!")
    return redirect("/")

@app.route('/delete', methods=['POST'])
def deleteData():
    if request.method=="POST":
        id=request.form['answer']
        print(request.form['delete'])
        client.sendNumberStringForDelete(int(id))
    return redirect("/")

@app.route('/<id>')
def updateData(id):
    result=client.getDataById(id)
    print(result)
    return render_template("update.html",idNumber=result)

@app.route('/update', methods=['POST'])
def update():
    if request.method=="POST":
        id=request.form["id"]
        name = request.form["name"]
        phone = request.form["phone"]
        client.updateGetById(id,name,phone)
    return redirect("/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
