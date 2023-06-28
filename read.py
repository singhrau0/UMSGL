import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='UMS',
    user='root',
    password='aman'
)

cur = conn.cursor()


class readed:
    def readdpt(x,id):
        cur.execute(f"select * from department where departmentid={id}")
        print(cur.fetchall())