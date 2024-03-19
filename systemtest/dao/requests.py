import connect

def addNewDataOne(mainquest, var1, var2, var3,var4,result):
    con=connect.connection()
    cur = con.cursor()
    cur.execute("""insert into Questions(mainquest, var1, var2, var3,var4,result) VALUES (%s,%s,%s,%s,%s,%s)""",(mainquest, var1, var2, var3,var4,result))
    con.commit() # сохранение изменений
    cur.close()
    con.close()
    print("!!!")