import pymysql
import connect

def createTable(nameTable):
    cur = connect.connection.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS " + nameTable + "(id int NOT NULL AUTO_INCREMENT, name text, phone text, PRIMARY KEY (id));")
    connect.connection.commit()
    cur.close()
    connect.connection.close()

def addNewData(name, phone):
    cur = connect.connection.cursor()
    cur.execute("""insert into primer(name, phone) VALUES (%s,%s)""",(name, phone))
    connect.connection.commit()
    cur.close()
    connect.connection.close()
    print("!!!")

addNewData("вася","123")
# createTable("test")
