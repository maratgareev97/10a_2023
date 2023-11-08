from flask import Flask, render_template, request, redirect
import math

app = Flask(__name__)


@app.route('/<a>&<b>&<c>')
def index(a, b, c):
    s = str(a) + " " + str(b) + " " + str(c)
    return s


@app.route('/kv', methods=['GET'])
def kvUr():
    print("Ax^2 + Bx + C = 0")
    otvet = ""
    a = request.args.get("aaa")
    b = request.args.get("bbb")
    c = request.args.get("ccc")
    print(a, b, c)
    if a != None and b != None and c != None:
        try:
            a=int(a)
            b=int(b)
            c=int(c)
            d = b * b - 4 * a * c
            if d > 0:
                x1 = (-b + math.sqrt(d)) / (2 * a)
                x2 = (-b - math.sqrt(d)) / (2 * a)
                otvet = str(x1) + ", " + str(x2)
            if d == 0:
                x = (-b) / (2 * a)
                otvet = str(x)
            if d < 0:
                otvet = "нет корней"
        except:
            otvet="Сам дурак"

    return render_template("kvadrurav.html", o=otvet)

@app.route('/post_z')
def postZ():
    return render_template("post.html")

@app.route('/post_zz', methods=['POST'])
def postZZ():
    print(request.form['first'])
    print(request.form['second'])
    return redirect("/post_z")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
