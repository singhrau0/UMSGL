import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='UMS',
    user='root',
    password='aman'
)

cur = conn.cursor()


class deleted:
    def dptdelete(x,id):
        cur.execute(f"delete from department where departmentid={id}")
        conn.commit()

