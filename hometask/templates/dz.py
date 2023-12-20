from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/dz', methods=['GET'])
def dz():
    otvet = ""
    a = request.args.get("aaa")
    b = request.args.get("bbb")
    c = request.args.get("ccc")
    d = request.args.get("ddd")
    e = request.args.get("eee")
    if a != None and b != None and c != None and d != None and e != None:

        try:
            a=int(a)
            b=int(b)
            c=int(c)
            d=int(d)
            e=int(e)
        except:
            return render_template("dz.html", o="Сам дурак")
        mas=[a,b,c,d,e]
        otvet = 1
        for i in range(len(mas)):
            if mas[i] % 2 == 0 and mas[i] % 10 != 0:
                otvet = otvet * mas[i]
        if otvet==1:
            return render_template("dz.html", o=0)
    return render_template("dz.html", o=otvet)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)