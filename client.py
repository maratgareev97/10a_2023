import connect

def createTable(nameTable):
    con=connect.connection()
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS " + nameTable + "(id int NOT NULL AUTO_INCREMENT, name text, phone text, PRIMARY KEY (id));")
    connect.connection.commit()
    cur.close()
    con.close()

def addNewData(name, phone):
    con=connect.connection()
    cur = con.cursor()
    cur.execute("""insert into primer(name, phone) VALUES (%s,%s)""",(name, phone))
    connect.connection.commit() # сохранение изменений
    cur.close()
    con.close()
    print("!!!")

def getAllData():
    con=connect.connection() # вызов метода который соединяется с базой
    cur = con.cursor() # создание курсора
    cur.execute("select * from primer") # это сам sql запрос
    result = cur.fetchall() # сохранение объекта
    cur.close()
    con.close()
    return result

# addNewData("вася","123")
# createTable("test")
# print(getAllData())
