import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='UMS',
    user='root',
    password='aman'
)

cur = conn.cursor()


class updated:
    
    def dptupdate(x,colname,newval,oldval):
        cur.execute(f"update department set {colname}='{newval}' where {colname} = '{oldval}'")
        conn.commit()

