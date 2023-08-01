import sqlite3
# conn=sqlite3.connect("parking.db")
# c=conn.cursor()
# c.execute(''' CREATE TABLE add_customer(
#           full_name,
#           vehicle_no,
#           phone_no,
#           time,
#           slot_no,
#           date,
#           vehicle_type

          
   
#          ) ''')
# conn.commit()
a="parking"
b="parking123"
conn=sqlite3.connect('parking.db')
c=conn.cursor()
c.execute("INSERT INTO admin_profile VALUES(:username,:passowrd)",{
        "username":a,
        "passowrd":b
        })
conn.commit()
conn.close()


