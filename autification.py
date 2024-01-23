from flask import Flask, render_template, redirect, session, request, l

app = Flask(__name__)
app.secret_key="1234567890"

password="1234"
@app.route('/')
def index():
    if "user" in session and session["user"]==password:
        return "Привет"
    return "Доступ запрещен"

@app.route('/login', methods=['GET','POST'])
def index1():
    if request.method == "POST":
        p=request.form['pw']
        if p==password:
            session["user"]=p
            return redirect("/")
    return render_template("login.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
