import pymysql

def connection():
    connection = pymysql.connect(host='82.146.35.88',
                                 user='school',
                                 password='Q1w2e3r4',
                                 db='school',
                                 charset='cp1251',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection
