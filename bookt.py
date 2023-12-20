from flask import Flask, render_template, request
app = Flask(__name__)
spisok = []

@app.route('/', methods=['GET'])
def book():
    newName = str(request.args.get("newName"))
    newNumber = str(request.args.get('newNumber'))
    print(newName,type(newName))
    if newName !='None' and newNumber!='None' and newName !='' and newNumber!='':
        print("1111")
        spisok.append({'name':newName, 'number': newNumber})
        return render_template("book.html", spisok=spisok)
    return render_template("book.html", spisok=spisok)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)