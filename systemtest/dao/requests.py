import connect


def addNewDataDao(mainquest, var1, var2, var3, var4, result):
    print("!!!!")
    con = connect.connection()
    cur = con.cursor()
    cur.execute("""insert into Questions(mainquest, var1, var2, var3,var4,result) VALUES (%s,%s,%s,%s,%s,%s)""",
                (mainquest, var1, var2, var3, var4, result))
    con.commit()  # сохранение изменений
    cur.close()
    con.close()
    print("!!!")


def getAllDataDao():
    print("!!")
    con = connect.connection()  # вызов метода который соединяется с базой
    print("@@@@")
    cur = con.cursor()  # создание курсора
    cur.execute("select * from Questions")  # это сам sql запрods=['POST'])ос
    result = cur.fetchall()  # сохранение объекта
    cur.close()
    con.close()
    return result


def sendNumberStringForDeleteDao(id):
    con = connect.connection()  # вызов метода который соединяется с базой
    cur = con.cursor()  # создание курсора
    cur.execute("""DELETE FROM Questions WHERE id=%s;""", (id))  # это сам sql запрос
    con.commit()  # сохранение объекта
    cur.close()
    con.close()


def updateById(id, mainquest, var1, var2, var3, var4, result):
    con = connect.connection()
    cur = con.cursor()
    cur.execute("""UPDATE Questions SET mainquest=%s,
    var1=%s,var2=%s,
    var3=%s,var4=%s,
    result=%s WHERE id=%s""",
                (mainquest, var1, var2, var3, var4, result, id))
    con.commit()
    cur.close()
    con.close()

def getDataById(id):
    con = connect.connection()  # вызов метода который соединяется с базой
    cur = con.cursor()  # создание курсора
    cur.execute("""select * from Questions where id=%s""",(id))  # это сам sql запрос
    result = cur.fetchall()  # сохранение объекта
    cur.close()
    con.close()
    return result

def getUserDao(login):
    con = connect.connection()  # вызов метода который соединяется с базой
    cur = con.cursor()  # создание курсора
    cur.execute("""select * from users where login=%s""", (login))  # это сам sql запрос
    result = cur.fetchall()  # сохранение объекта
    print(result,'DAO')
    cur.close()
    con.close()
    return result