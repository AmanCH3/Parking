import sqlite3
conn=sqlite3.connect("parking.db")
c=conn.cursor()
c.execute(''' CREATE TABLE addcustomer(
          full_name,
          vehicel_no,
          phone_no,
          enter_time,
          slot_no,
          date,
          vehicle_type
          
)''')
conn.commit()