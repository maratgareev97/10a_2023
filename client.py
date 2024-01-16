import connect

def createTable(nameTable):
    con=connect.connection()
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS " + nameTable + "(id int NOT NULL AUTO_INCREMENT, name text, phone text, PRIMARY KEY (id));")
    con.commit()
    cur.close()
    con.close()

def addNewData(name, phone):
    con=connect.connection()
    cur = con.cursor()
    cur.execute("""insert into testtwo(name, phone) VALUES (%s,%s)""",(name, phone))
    con.commit() # сохранение изменений
    cur.close()
    con.close()
    print("!!!")

def getAllData():
    con=connect.connection() # вызов метода который соединяется с базой
    cur = con.cursor() # создание курсора
    cur.execute("select * from testtwo") # это сам sql запрос
    result = cur.fetchall() # сохранение объекта
    cur.close()
    con.close()
    return result

def sendNumberStringForDelete(id):
    con = connect.connection()  # вызов метода который соединяется с базой
    cur = con.cursor()  # создание курсора
    cur.execute("""DELETE FROM school.testtwo WHERE id=%s;""",(id))  # это сам sql запрос
    con.commit()  # сохранение объекта
    cur.close()
    con.close()

def getDataById(id):
    con = connect.connection()  # вызов метода который соединяется с базой
    cur = con.cursor()  # создание курсора
    cur.execute("""select * from testtwo where id=%s""",(id))  # это сам sql запрос
    result = cur.fetchall()  # сохранение объекта
    cur.close()
    con.close()
    return result

def updateGetById(id,name, phone):
    con=connect.connection()
    cur = con.cursor()
    cur.execute("""UPDATE testtwo SET name = %s, phone = %s WHERE id = %s;""",(name, phone,id))
    con.commit() # сохранение изменений
    cur.close()
    con.close()
    print("!!!")
# createTable("testtwo")
# addNewData("Петя","312")
# createTable("test")
# print(getAllData())
