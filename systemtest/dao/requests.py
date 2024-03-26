import connect

def addNewDataDao(mainquest, var1, var2, var3,var4,result):
    con=connect.connection()
    cur = con.cursor()
    cur.execute("""insert into Questions(allquestions, var1, var2, var3,var4,result) VALUES (%s,%s,%s,%s,%s,%s)""",(mainquest, var1, var2, var3,var4,result))
    con.commit() # сохранение изменений
    cur.close()
    con.close()
    print("!!!")
def getAllDataDao():
    con=connect.connection() # вызов метода который соединяется с базой
    cur = con.cursor() # создание курсора
    cur.execute("select * from Questions") # это сам sql запрос
    result = cur.fetchall() # сохранение объекта
    cur.close()
    con.close()
    return result

def sendNumberStringForDeleteDao(id):
    con = connect.connection()  # вызов метода который соединяется с базой
    cur = con.cursor()  # создание курсора
    cur.execute("""DELETE FROM Questions WHERE id=%s;""",(id))  # это сам sql запрос
    con.commit()  # сохранение объекта
    cur.close()
    con.close()