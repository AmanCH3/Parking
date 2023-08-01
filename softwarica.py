from tkinter import *
import sqlite3
root=Tk()
root.title("Registration")
root.geometry("600x600")
# conn=sqlite3.connect("softwarica.db")
# c=conn.cursor()
# c.execute(''' CREATE TABLE addresses(
#         first_name,
#         last_name,
#         age,
#         email,
#         father_name,
#         mother_name,
#         mobile_number
#          ) ''')
# conn.commit()
def submit():
    conn=sqlite3.connect('softwarica.db')
    c=conn.cursor()
    c.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:age,:email,:fathername,:mothername,:mobileno)",{
        "f_name":entry1.get(),
        "l_name":entry2.get(),
        "age":entry3.get(),
        "email":entry4.get(),
        "fathername":entry5.get(),
        "mothername":entry6.get(),
        "mobileno":entry7.get()



    })
    conn.commit()
    conn.close()
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
    entry5.delete(0,END)
    entry6.delete(0,END)
    entry7.delete(0,END)

def query():
    conn=sqlite3.connect("softwarica.db")
    c=conn.cursor()
    c.execute("SELECT*,oid FROM addresses")
    records=c.fetchall()
    print_record=""
    for record in records:
        print_record+=(record[0])+" "+(record[1])+" "+(record[2])+" "+(record[3])+"\t"+str(record[7])+"\n"
    query_label=Label(root,text=print_record)
    query_label.place(x=120,y=500)
    conn.commit()
    conn.close()

def dell():
    conn=sqlite3.connect("softwarica.db")
    c=conn.cursor()

    c.execute("DELETE from addresses WHERE email= ?",(delete.get(),))
    print("Deleted Sucessfully")
    delete.delete(0,END)
    conn.commit()
    conn.close()

def udt():
    conn=sqlite3.connect("softwarica.db")
    c=conn.cursor()
    record_id=up.get()
    c.execute(""" UPDATE addresses SET 
        first_name=:first,
        last_name=:last,
        age=:ag,
        email=:ema,
        father_name=:fat_nam,
        mother_name=:mot_nam,
        mobile_number=:mob
        WHERE oid =:oid""",
        {"first":entry11.get(),
         "last":entry22.get(),
         "ag":entry33.get(),
         "ema":entry44.get(),
         "fat_nam":entry55.get(),
         "mot_nam":entry66.get(),
         "mob":entry77.get(),
         "oid":record_id

        }
        )
    conn.commit()   
    conn.close()
    u.destroy()
    
    


def upd():
    global entry11
    global entry22
    global entry33
    global entry44
    global entry55
    global entry66
    global entry77
    global u
    u=Tk()
    u.geometry("500x500")
    
    conn=sqlite3.connect("softwarica.db")
    c=conn.cursor()

    record_id=up.get()

    c.execute("SELECT*FROM addresses WHERE oid="+record_id)
    records=c.fetchall()

    label=Label(u,text='First name')
    label.place(x=0,y=10)
    label1=Label(u,text="Last Name")
    label1.place(x=0,y=40)
    label2=Label(u,text="Age")
    label2.place(x=0,y=80)
    label3=Label(u,text="Email")
    label3.place(x=0,y=120)
    label4=Label(u,text="Father Name")
    label4.place(x=0,y=160)
    label5=Label(u,text="Mother Name")
    label5.place(x=0,y=200)
    label6=Label(u,text="Mobile no")
    label6.place(x=0,y=240)

    entry11=Entry(u)
    entry22=Entry(u)
    entry33=Entry(u)
    entry44=Entry(u)
    entry55=Entry(u)
    entry66=Entry(u)
    entry77=Entry(u)
    entry11.place(x=80,y=10)
    entry22.place(x=80,y=40)
    entry33.place(x=80,y=80)
    entry44.place(x=80,y=120)
    entry55.place(x=80,y=160)
    entry66.place(x=80,y=200)
    entry77.place(x=80,y=240)
    sv=Button(u,text="save",command=udt)
    sv.place(x=80,y=270)
    
    for record in records:
        entry11.insert(0,record[0])
        entry22.insert(0,record[1])
        entry33.insert(0,record[2])
        entry44.insert(0,record[3])
        entry55.insert(0,record[4])
        entry66.insert(0,record[5])
        entry77.insert(0,record[6])
    
    u.mainloop()
     




    

label=Label(root,text='First name')
label.place(x=0,y=10)
label1=Label(root,text="Last Name")
label1.place(x=0,y=40)
label2=Label(root,text="Age")
label2.place(x=0,y=80)
label3=Label(root,text="Email")
label3.place(x=0,y=120)
label4=Label(root,text="Father Name")
label4.place(x=0,y=160)
label5=Label(root,text="Mother Name")
label5.place(x=0,y=200)
label6=Label(root,text="Mobile no")
label6.place(x=0,y=240)


entry1=Entry(root)
entry2=Entry(root)
entry3=Entry(root)
entry4=Entry(root)
entry5=Entry(root)
entry6=Entry(root)
entry7=Entry(root)
entry1.place(x=80,y=10)
entry2.place(x=80,y=40)
entry3.place(x=80,y=80)
entry4.place(x=80,y=120)
entry5.place(x=80,y=160)
entry6.place(x=80,y=200)
entry7.place(x=80,y=240)
delete=Entry(root)
delete.place(x=70,y=300)
up=Entry(root)
up.place(x=80,y=420)

button1=Button(root,text="Add records",command=submit)
button2=Button(root,text="Show records",command=query)
button1.place(x=70,y=270)
button2.place(x=70,y=330)
deletebtn=Button(root,text="delete",command=dell)
deletebtn.place(x=70,y=370)
updatebtn=Button(root,text="update",command=upd)
updatebtn.place(x=80,y=450)
root.mainloop()