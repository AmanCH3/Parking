from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk,ImageDraw,ImageFont
from tkinter import messagebox
import datetime as dt
import sqlite3

date=dt.datetime.now()

    


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
    
    # _____________________________________________________
def parkingslot():
    park=Frame(dash,width=1200,bg="#2A3473")
    park.place(x=350,y=60,height=850)
    global date
    date=dt.datetime.now()
    exit_time=f"{date: %H.%M }"

    vehicleNoLabel=Label(park,width=30,bg="#2A3473",text="Enter Vehicle Number:",fg="white",font=("poppins",20))
    vehicleNoLabel.place(x=120)
    veh_no_en=Entry(park,width=50,font=("poppins",20))
    veh_no_en.place(x=225,y=50,height=30)

    exit=Label(park,width=30,bg="#2A3473",text="Enter Exit Time:",fg="white",font=("poppins",20))
    exit.place(x=80,y=100)
    exit_en=Entry(park,width=50,font=("poppins",20))
    exit_en.insert(END,exit_time)
    exit_en.place(x=225,y=150,height=30)
   
    rate_lb=Label(park,width=30,bg="#2A3473",text="Rate:",fg="white",font=("poppins",20))
    rate_lb.place(x=20,y=200)
    rate_en=Entry(park,width=50,font=("poppins",20))
    rate_en.place(x=225,y=250,height=30)

    submitbutton=Button(park,width=30,text="Submit",font=("poppins",10))
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
    question=OptionMenu(addcus,valueinside,"Two Wheelers","Four Wheelers","Other")
    question.config(width=30,font=("poppins",15))
    question.place(x=225,y=650,height=30)

    addcustomer_button=Button(addcus,width=30,text="Add Customer",font=("poppins",10))
    addcustomer_button.place(x=730,y=650,height=30)



    #Refresh button__________________________________
    global refreshbutton
    refreshbutton=Button(addcus,width=10,text="Refresh",command=addcustomerfunc,font=("poppins",10))
    refreshbutton.place(x=890,y=600,height=40)
    

    

def receiphisfunc():
    receipthis=Frame(dash,width=1200,bg="green")
    receipthis.place(x=350,y=60,height=850)
    scrollbar=Scrollbar(receipthis,orient="vertical")
    scrollbar.place(x=1170,y=0)

def customerinfo():
    customerinframe=Frame(dash,width=1200,bg="yellow")
    customerinframe.place(x=350,y=60,height=850)
    
     

    


   
    
 








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
search.place(x=50,y=13,height=35)
searchbutton=Button(topbar,width=10,text="search",font=("poppins",12))
searchbutton.place(x=370,y=13,height=35)
pro = Button(topbar,text="Profile",fg="black",bg="#EEA842",bd=0,activebackground='white', activeforeground="black",
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