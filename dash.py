from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk,ImageDraw,ImageFont
from tkinter import messagebox
import datetime as dt
import sqlite3

ntwo=0
nfour=0
nother=0

def logout():
    dash.destroy()
    import login

def profile():
    global prof
    prof=Toplevel()
    prof.geometry("200x220+1330+80")
    prof.title("Profile")
    prof.config(bg="#EEA842")
    Label(prof,text="3AD\nGroup",font=("Aerial",20),bg="#EEA842").pack(pady=40)
    Button(prof,text="Log Out",font=("poppins",20),bg="#2A3473",command=logout).pack(side=BOTTOM)
    prof.mainloop()


date=dt.datetime.now()
def pressed(e):
    search.delete(0,END)
def unpress1(e):
    deleterecipten.insert(0,"Receipt No:")
def pressed1(e):
    deleterecipten.delete(0,END)


def udt():
    conn=sqlite3.connect("parking.db")
    c=conn.cursor()
    c.execute("""UPDATE add_customer SET 
                full_name=:full,
                vehicle_no=:veh,
                phone_no=:phn,
                slot_no=:sn
                WHERE vehicle_no= :veh_param""",
          {"full": entry11.get(),
           "veh": entry22.get(),
           "phn": entry33.get(),
           "sn": entry44.get(),
           "veh_param": search.get()
           }
          )

    search.delete(0,END)
    conn.commit()   
    conn.close()
    upp.destroy()

def update():
    global entry11
    global entry22
    global entry33
    global entry44
    global upp
    if search.index("end")!=0:
        upp=Tk()
        upp.title("Update Page")
        upp.geometry("500x500")
        upp.config(bg="#2A3473")
        conn=sqlite3.connect("parking.db")
        c=conn.cursor()
        c.execute("SELECT*FROM add_customer WHERE vehicle_no=?",(search.get(),))
        records=c.fetchall()

        label=Label(upp,text='Full Name',bg="#2A3473",font=("poppins",10),fg="white")
        label.place(x=0,y=10)
        label1=Label(upp,text="Vehicle no",bg="#2A3473",font=("poppins",10),fg="white")
        label1.place(x=0,y=40)
        label2=Label(upp,text="Phone No",bg="#2A3473",font=("poppins",10),fg="white")
        label2.place(x=0,y=80)
        label3=Label(upp,text="Slot no",bg="#2A3473",font=("poppins",10),fg="white")
        label3.place(x=0,y=120)

        entry11=Entry(upp,width=40)
        entry22=Entry(upp,width=40)
        entry33=Entry(upp,width=40)
        entry44=Entry(upp,width=40)
        entry11.place(x=80,y=10)
        entry22.place(x=80,y=40)
        entry33.place(x=80,y=80)
        entry44.place(x=80,y=120)
        sv=Button(upp,text="Update",command=udt,width=21,font=("poppins"))
        sv.place(x=80,y=150)
            
        for record in records:
                entry11.insert(0,record[0])
                entry22.insert(0,record[1])
                entry33.insert(0,record[2])
                entry44.insert(0,record[4])
            
        upp.mainloop()
    else:
        messagebox.showwarning("Alert!","Please fill all the details")

def deleterec():
    if deleterecipten.index("end")!=0:
        try:
            conn=sqlite3.connect("parking.db")
            c=conn.cursor()

            c.execute("DELETE from receipt WHERE oid= ?",(deleterecipten.get(),))
            deleterecipten.delete(0,END)
            conn.commit()
            conn.close()
        except conn.Error:
            messagebox.showerror("ALert","Error Occured")
            c.execute("rollback")
    else:
            messagebox.showwarning("Alert!","Please fill all the details")


def dell():
    if veh_no_en.index("end")!=0 and rate_en.index("end")!=0 and exit_en.index("end")!=0: 
        try:
            connect=sqlite3.connect("parking.db")
            cc=connect.cursor()
            ab=cc.execute("SELECT time from add_customer WHERE vehicle_no= ?",(veh_no_en.get(),))
            ex_t=ab.fetchone()
            exit1=float(ex_t[0])
            connect.commit()
            connect.close()
        except connect.Error:
            messagebox.showerror("ALert","Error Occured")
            cc.execute("rollback")

        try:
            connect1=sqlite3.connect("parking.db")
            cc1=connect1.cursor()
            abc=cc1.execute("SELECT full_name from add_customer WHERE vehicle_no= ?",(veh_no_en.get(),))
            ab_c=abc.fetchone()
            abc1=str(ab_c[0])
            connect1.commit()
            connect1.close()
        except connect1.Error:
            messagebox.showerror("ALert","Error Occured")
            cc1.execute("rollback")

        try:
            connect11=sqlite3.connect("parking.db")
            cc11=connect11.cursor()
            abcd=cc11.execute("SELECT vehicle_no from add_customer WHERE vehicle_no= ?",(veh_no_en.get(),))
            ab_d=abcd.fetchone()
            abcd1=int(ab_d[0])
            connect11.commit()
            connect11.close()
        except connect11.Error:
            messagebox.showerror("ALert","Error Occured")
            cc11.execute("rollback")

        try:
            connect111=sqlite3.connect("parking.db")
            cc111=connect111.cursor()
            abcde=cc111.execute("SELECT date from add_customer WHERE vehicle_no= ?",(veh_no_en.get(),))
            ab_de=abcde.fetchone()
            abcd11=str(ab_de[0])
            connect111.commit()
            connect111.close()
        except connect111.Error:
            messagebox.showerror("ALert","Error Occured")
            cc111.execute("rollback")


        try:
            connect1112=sqlite3.connect("parking.db")
            cc1112=connect1112.cursor()
            abcdef=cc1112.execute("SELECT vehicle_type from add_customer WHERE vehicle_no= ?",(veh_no_en.get(),))
            ab_def=abcdef.fetchone()
            abcd112=ab_def[0]
            connect1112.commit()
            connect1112.close()
        except connect1112.Error:
            messagebox.showerror("ALert","Error Occured")
            cc1112.execute("rollback")

        try:
            conn=sqlite3.connect("parking.db")
            c=conn.cursor()
            c.execute("DELETE from add_customer WHERE vehicle_no= ?",(veh_no_en.get(),))
            print("Deleted Sucessfully")
            veh_no_en.delete(0,END)
            conn.commit()
            conn.close()
        except conn.Error:
            messagebox.showerror("ALert","Error Occured")
            c.execute("rollback")

            

        if abcd112=="Two Wheelers":
            global ntwo
            ntwo=ntwo-1
        elif abcd112=="Four Wheelers":
            global nfour
            nfour=nfour-1
        elif abcd112=="        Other":
            global nother
            nother=nother-1
        receipt=Toplevel()

        receipt.geometry("300x300")
        receipt.title("Receipt Invoice")
        receipt.config(bg="pink")
        rate=rate_en.get()
        exx_time=exit_en.get()
        print(type(exx_time))
        ex_time=float(exit_en.get())-exit1
        amount=int(rate)*ex_time
        roundamount=round(amount,2)
        rate_en.delete(0,END)

        com_label=Label(receipt,text="Parking\n ORG",font=("poppins",12),bg="pink")
        com_label.pack(side=TOP)

        name_label=Label(receipt,text="Name   :",font=("poppins",12),bg="pink")
        name_label.place(x=0,y=40)
        fullname_label=Label(receipt,text=abc1,font=("poppins",12),bg="pink")
        fullname_label.place(x=170,y=40)

        vehic_label=Label(receipt,text="Vehicle No:",font=("poppins",12),bg="pink")
        vehic_label.place(x=0,y=70)
        vehicno_label=Label(receipt,text=abcd1,font=("poppins",12),bg="pink")
        vehicno_label.place(x=200,y=70)

        entry_label=Label(receipt,text="Enter Time:",font=("poppins",12),bg="pink")
        entry_label.place(x=0,y=100)
        entryy_label=Label(receipt,text=exit1,font=("poppins",12),bg="pink")
        entryy_label.place(x=200,y=100)

        exit_label=Label(receipt,text="Exit Time:",font=("poppins",12),bg="pink")
        exit_label.place(x=0,y=130)
        exitt_label=Label(receipt,text=exx_time,font=("poppins",12),bg="pink")
        exitt_label.place(x=200,y=130)

        rate_label=Label(receipt,text="Rate     :",font=("poppins",12),bg="pink")
        rate_label.place(x=0,y=160)
        ratee_label=Label(receipt,text=rate,font=("poppins",12),bg="pink")
        ratee_label.place(x=200,y=160)

        date_label=Label(receipt,text="Date     :",font=("poppins",12),bg="pink")
        date_label.place(x=0,y=190)
        dat_label=Label(receipt,text=abcd11,font=("poppins",12),bg="pink")
        dat_label.place(x=200,y=190)


        amountabel=Label(receipt,text="TOTAL  :",font=("poppins",15),bg="pink")
        amountabel.place(x=0,y=240)
        amountlabel=Label(receipt,text=roundamount,font=("poppins",12),bg="pink")
        amountlabel.place(x=200,y=240)
        
        try:
            connt=sqlite3.connect('parking.db')
            cy=connt.cursor()
            cy.execute("INSERT INTO receipt VALUES(:date,:name,:vehicle_no,:total)",{
                "date":abcd11,
                "name":abc1,
                "vehicle_no":abcd1,
                "total":roundamount



            })
            connt.commit()
            connt.close()
        except connt.Error:
            messagebox.showerror("ALert","Error Occured")
            cy.execute("rollback")
    else:
        messagebox.showwarning("Alert!","Please fill all the details")




def submit():
    if customer_entry.index("end")!=0 and vehicle_no_en.index('end')!=0 and phone_entry.index("end")!=0 and slot_entry.index("end")!=0 :
        try:
            conn=sqlite3.connect('parking.db')
            c=conn.cursor()
            c.execute("INSERT INTO add_customer VALUES(:full_name,:vehicle_no,:phone_no,:time,:slot_no,:date,:vehicle_type)",{
                "full_name":customer_entry.get(),
                "vehicle_no":vehicle_no_en.get(),
                "phone_no":phone_entry.get(),
                "time":timeentry.get(),
                "slot_no":slot_entry.get(),
                "date":date_entry.get(),
                "vehicle_type":valueinside.get()
                })
            conn.commit()
            conn.close()
        except conn.Error:
            messagebox.showerror("ALert","Error Occured")
            c.execute("rollback")
        if valueinside.get()=="Two Wheelers":
            global ntwo
            ntwo=ntwo+1
        if valueinside.get()=="Four Wheelers":
            global nfour
            nfour=nfour+1
        if valueinside.get()=="        Other":
            global nother
            nother=nother+1
  
        newwin=Toplevel()
        newwin.geometry("200x200")
        newwin.config(bg="light green")
        vvv=vehicle_no_en.get()
        nnn=customer_entry.get()
        timeeee=timeentry.get()
        ssss=slot_entry.get()
        Label(newwin,text="____Ticket____\nParking Org",bg="light green").pack()
        Label(newwin,text=nnn,font=("poppins",10),bg="light green").pack()
        Label(newwin,text=vvv,font=("poppins",10),bg="light green").pack()
        Label(newwin,text=timeeee,font=("poppins",10),bg="light green").pack()
        Label(newwin,text=ssss,font=("poppins",10),bg="light green").pack()


        customer_entry.delete(0,END)
        vehicle_no_en.delete(0,END)
        phone_entry.delete(0,END)
        slot_entry.delete(0,END)
        newwin.mainloop()

    else:
        messagebox.showwarning("Alert!","Please fill all the details")

    
    
    
def showcustomer():
    try:
        conn=sqlite3.connect("parking.db")
        c=conn.cursor()
        c.execute("SELECT*,oid FROM add_customer")
        records=c.fetchall()
        print_record=""
        for record in records:
            print_record+=(record[0])+"\t \t"+str(record[1])+"\t \t"+str(record[2])+"\t \t"+str(record[3])+"\t \t"+str(record[4])+"\t \t"+str(record[5])+"\t \t"+str(record[6])+"\n"
        query_label=Label(customerinframe,text=print_record,width=120,font=("poppins",11))
        query_label.place(x=80,y=50)
        conn.commit()
        conn.close()
    except conn.Error:
        messagebox.showerror("Alert","Error Occured")
        c.execute("rollback")

    



def landpage():
# for dashboard frame and heading________________________________


    land=Frame(dash,width=1200,bg="#E5E5E5")
    land.place(x=350,y=60,height=850)
    heading=Label(land,text="Dashboard",fg="black",bg="#E5E5E5",font=("poppins",40))
    heading.place(x=0,y=0)


    twowheelerlabel=Label(land,width=50,bg="#2A3473")
    twowheelerlabel.place(x=15,y=100,height=300)
    twowheeler_label1=Label(land,width=20,bg="#2A3473",text="Two Wheelers",font=("poppins",20),fg="white")
    twowheeler_label1.place(x=30,y=100)

    fourwheelerlabel=Label(land,width=50,bg="#2A3473")
    fourwheelerlabel.place(x=415,y=100,height=300)
    fourwheeler_label1=Label(land,width=20,bg="#2A3473",text="Four Wheelers",font=("poppins",20),fg="white")
    fourwheeler_label1.place(x=435,y=100)

    otherlabel=Label(land,width=50,bg="#2A3473")
    otherlabel.place(x=815,y=100,height=300)
    other_label1=Label(land,width=20,bg="#2A3473",text="Other Vehicles",font=("poppins",20),fg="white")
    other_label1.place(x=835,y=100)

    twowheeler_quant=Label(land,text=ntwo,font=("poppins",120),fg="white",bg="#2A3473")
    twowheeler_quant.place(x=150,y=150)
    fourwheeler_quant=Label(land,text=nfour,font=("poppins",120),fg="white",bg="#2A3473")
    fourwheeler_quant.place(x=550,y=150)
    other_quant=Label(land,text=nother,font=("poppins",120),fg="white",bg="#2A3473")
    other_quant.place(x=950,y=150)
    
    # _____________________________________________________
def parkingslot():
    park=Frame(dash,width=1200,bg="#2A3473")
    park.place(x=350,y=60,height=850)
    global date
    date=dt.datetime.now()
    exit_time=f"{date: %H.%M }"

    vehicleNoLabel=Label(park,width=30,bg="#2A3473",text="Enter Vehicle Number:",fg="white",font=("poppins",20))
    vehicleNoLabel.place(x=120)
    global veh_no_en
    veh_no_en=Entry(park,width=50,font=("poppins",20))
    veh_no_en.place(x=225,y=50,height=30)

    exit=Label(park,width=30,bg="#2A3473",text="Enter Exit Time:",fg="white",font=("poppins",20))
    exit.place(x=80,y=100)
    global exit_en
    exit_en=Entry(park,width=50,font=("poppins",20))
    exit_en.insert(END,exit_time)
    exit_en.place(x=225,y=150,height=30)
   
    rate_lb=Label(park,width=30,bg="#2A3473",text="Rate:",fg="white",font=("poppins",20))
    rate_lb.place(x=20,y=200)
    global rate_en
    rate_en=Entry(park,width=50,font=("poppins",20))
    rate_en.place(x=225,y=250,height=30)

    submitbutton=Button(park,width=30,command=dell,text="Submit",font=("poppins",10))
    submitbutton.place(x=480,y=300)



def addcustomerfunc():
    addcus=Frame(dash,width=1200,bg="#2A3473")
    addcus.place(x=350,y=60,height=850)
    
    global customer_entry
    customer_name=Label(addcus,bg="#2A3473",width=30,text="Enter Customer Full Name:",fg="white",font=("poppins",20))
    customer_name.place(x=150)
    customer_entry=Entry(addcus,width=50,font=("poppins",20))
    customer_entry.place(x=225,y=50,height=30)

    global vehicle_no_en
    vehicle_no=Label(addcus,width=30,bg="#2A3473",text="Enter Vehicle Number:",fg="white",font=("poppins",20))
    vehicle_no.place(x=120,y=100)
    vehicle_no_en=Entry(addcus,width=50,font=("poppins",20))
    vehicle_no_en.place(x=225,y=150,height=30)
    
    global phone_entry
    phone_no=Label(addcus,width=30,bg="#2A3473",text="Enter Phone Number:",fg="white",font=("poppins",20))
    phone_no.place(x=115,y=200)
    phone_entry=Entry(addcus,width=50,font=("poppins",20))
    phone_entry.place(x=225,y=250,height=30)

    enter_time=Label(addcus,width=30,bg="#2A3473",text="Entered Time:",fg="white",font=("poppins",20))
    enter_time.place(x=70,y=300)
    #/Current Date and Time Code_____________
    global date
    date=dt.datetime.now() 
    format_date=f"{date: %H.%M }"
    date_format=f"{date: %m/%d/%Y}"
    global timeentry
    timeentry=Entry(addcus,width=50,font=("poppins",20))
    timeentry.insert(END,format_date)
    timeentry.place(x=225,y=350,height=30)#___________________________/

    global slot_entry
    rate=Label(addcus,width=30,bg="#2A3473",text="Slot No:",fg="white",font=("poppins",20))
    rate.place(x=35,y=400)
    slot_entry=Entry(addcus,width=50,font=("poppins",20))
    slot_entry.place(x=225,y=450,height=30)

    current_date=Label(addcus,width=30,bg="#2A3473",text="Date:",fg="white",font=("poppins",20))
    current_date.place(x=20,y=500)
    global date_entry
    date_entry=Entry(addcus,width=50,font=("poppins",20))
    date_entry.insert(END,date_format)
    date_entry.place(x=225,y=550,height=30)

    selectveh=Label(addcus,width=30,bg="#2A3473",text="Select Vehicle",fg="white",font=("poppins",20))
    selectveh.place(x=70,y=600)
    global valueinside
    valueinside=StringVar(addcus)
    valueinside.set("Select An Option")
    global question
    question=OptionMenu(addcus,valueinside,"Two Wheelers","Four Wheelers","        Other")
    question.config(width=30,font=("poppins",15))
    question.place(x=225,y=650,height=30)

    addcustomer_button=Button(addcus,width=30,text="Add Customer",command=submit,font=("poppins",10))
    addcustomer_button.place(x=730,y=650,height=30)



    #Refresh button__________________________________
    global refreshbutton
    refreshbutton=Button(addcus,width=10,text="Refresh",command=addcustomerfunc,font=("poppins",10))
    refreshbutton.place(x=890,y=600,height=40)
    

    

def receiphisfunc():
    receipthis=Frame(dash,width=1200,bg="#2A3473")
    receipthis.place(x=350,y=60,height=850)
    scrollbar=Scrollbar(receipthis,orient="vertical")
    scrollbar.place(x=1170,y=0)

    conn=sqlite3.connect("parking.db")
    c=conn.cursor()
    c.execute("SELECT*,oid FROM receipt")
    records=c.fetchall()
    print_record=""
    for record in records:
        print_record+=(record[0])+"\t\t"+str(record[1])+"\t\t"+str(record[2])+"\t\t"+str(record[3])+"\t\t"+str(record[4])+"\n"
    query_label=Label(receipthis,text=print_record,font=("poppins",15))
    query_label.place(x=150,y=50)
    conn.commit()
    conn.close()

    fullnamelabel=Label(receipthis,text="Date                        Name                 VH No      Total Amt    R.No",font=("poppins",23),bg="#2A3473",fg="white")
    fullnamelabel.place(x=150,y=0,height=45)

    global deleterecipten
    deleterecipten=Entry(receipthis,width=30,font=("poppins",20))
    deleterecipten.insert(0,"Receipt No:")
    deleterecipten.bind("<Button-1>",pressed1)
    deleterecipten.bind("<FocusOut>",unpress1)
    deleterecipten.place(x=10,y=690)
    deletereciptenbutton=Button(receipthis,width=15,command=deleterec,text="Delete Receipt",font=("poppins",10))
    deletereciptenbutton.place(x=480,y=690,height=40)

    global refreshbutton1
    refreshbutton1=Button(receipthis,width=10,text="Refresh",command=receiphisfunc,font=("poppins",10))
    refreshbutton1.place(x=1100,y=680,height=40)

def customerinfo():
    global customerinframe
    customerinframe=Frame(dash,width=1200,bg="#2A3473")
    customerinframe.place(x=350,y=60,height=850)
    showcustomer()
    fullnamelabel=Label(customerinframe,text="Name          VH No       Phn No      Enter Time  Slot no     Date            VH Type",font=("poppins",23),bg="#2A3473",fg="white")
    fullnamelabel.place(x=80,y=0,height=45)
    global refreshbutton11
    refreshbutton11=Button(customerinframe,width=10,text="Refresh",command=customerinfo,font=("poppins",10))
    refreshbutton11.place(x=1100,y=680,height=40)
    
     

    


   
    
 








dash=Tk()

# For window size and window size_________________
dash.title("LOG IN")
dash.geometry("1920x1080")
dash.resizable(1,1)
windowwidth=400
windowheight=300
screenwidth=dash.winfo_screenmmwidth()
screenheight=dash.winfo_screenheight()
x=(screenwidth//2)-(windowwidth//2)
y=(screenheight//2)-(windowheight//2)
dash.geometry(f"{windowwidth}x{windowheight}+{x}+{y}")
dash.state("zoomed")
landpage()
# for top bar frame and search and profile______________________________________
topbar=Frame(dash, width=1200,height=60,bg="#EEA842")
topbar.place(x =350,y=0)
search=Entry(topbar,width=35,fg="black",border=0,font=("poppins",12))
search.insert(0,"Search with Vehicle No")
search.bind("<Button-1>",pressed)
search.place(x=50,y=13,height=35)
searchbutton=Button(topbar,command=update,width=10,text="search",font=("poppins",12))
searchbutton.place(x=370,y=13,height=35)
pro = Button(topbar,text="Profile",command=profile,fg="black",bg="#EEA842",bd=0,activebackground='white', activeforeground="black",
                      font=("bold",20))
pro.place(x=1050,y=5)

img4=Image.open("pro.png")
img4=img4.resize((40,40))
img4=ImageTk.PhotoImage(img4)
label4=Label(dash,image=img4,bg="#EEA842")
label4.place(x=1350,y=9)
# ___________________________________________________

# For sidebar frame and other buttons_______________________
sidebar=Frame(dash,bg="white",width=350)
sidebar.place(x=0,y=0,height=850)

# For side bar image__________________________________________
my=Image.open("buss.png")
my=my.resize((350,150))
img=ImageTk.PhotoImage(my)
label=Label(sidebar,image=img)
label.place(x=0,y=0)

# For dashboard button________________________________________
dash_button = Button(sidebar,text="Dashboard",fg="darkblue",command=landpage,bg="white",bd=0,activebackground='white', activeforeground="darkblue",
                      font=("bold",20),width=20)
dash_button.place(x=0,y=200)
img1=Image.open("dashboardicon.png")
img1=img1.resize((40,30))
img1=ImageTk.PhotoImage(img1)
label1=Label(sidebar,image=img1,bg= "white")
label1.place(x=50,y=210)

# For parking slot button_________________________________
parkslot_button = Button(sidebar,text="Withdraw Customer",command=parkingslot,fg="darkblue",bg="white",bd=0,activebackground='white', activeforeground="darkblue",
                      font=("bold",20),width=20)
parkslot_button.place(x=55,y=290)
img2=Image.open("parkingicon.png")
img2=img2.resize((40,40))
img2=ImageTk.PhotoImage(img2)
label2=Label(sidebar,image=img2,bg= "white")
label2.place(x=50,y=295)

# For adding customer buttton___________________
addcustomer = Button(sidebar,text="Add customer",command=addcustomerfunc,fg="darkblue",bg="white",bd=0,activebackground='white', activeforeground="darkblue",
                      font=("bold",20),width=20)
addcustomer.place(x=25,y=390)
img3=Image.open("addcustomer.png")
img3=img3.resize((40,40))
img3=ImageTk.PhotoImage(img3)
label3=Label(sidebar,image=img3,bg= "white")
label3.place(x=50,y=390)

# For receipt history________________________________
rhistory = Button(sidebar,text="Receipt history",command=receiphisfunc,fg="darkblue",bg="white",bd=0,activebackground='white', activeforeground="darkblue",
                      font=("bold",20),width=20)
rhistory.place(x=25,y=485)
img5=Image.open("receipthistory.png")
img5=img5.resize((40,40))
img5=ImageTk.PhotoImage(img5)
label5=Label(sidebar,image=img5,bg= "white")
label5.place(x=50,y=490)

#For Customer details_________________________
customer_detail=Button(sidebar,text="Customer info",command=customerinfo,fg="darkblue",bg="white",bd=0,activebackground='white', activeforeground="darkblue",
                       font=("bold",20),width=20)
customer_detail.place(x=25,y=575)
img6=Image.open("receipthistory.png")
img6=img6.resize((40,40))
img6=ImageTk.PhotoImage(img6)
label6=Label(sidebar,image=img6,bg= "white")
label6.place(x=50,y=580)







dash.mainloop()