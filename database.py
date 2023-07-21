import sqlite3
conn=sqlite3.connect("parking.db")
c=conn.cursor()
c.execute(''' CREATE TABLE receipt(
        date,
        name,
        vehicle_no,
        total  
         ) ''')
conn.commit()

