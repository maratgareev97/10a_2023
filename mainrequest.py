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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
