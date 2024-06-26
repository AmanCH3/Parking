
from tkinter import*
from PIL import Image,ImageTk,ImageDraw,ImageFont
import sqlite3
from tkinter import messagebox
store_password = "passw"

def login():
    conn=sqlite3.connect("parking.db")
    c=conn.cursor()
    c.execute("SELECT*,oid FROM admin_profile")
    records=c.fetchall()
    us=records[0]
    data=list(us)
    user=data[0]
    print(user)
    passw=data[1]
    print(passw)
    
    if username.get()==user and passwordd.get()==passw :
        a.destroy()
        import dash
    else:
        messagebox.showinfo("Alert","Check your username and password")


a = Tk()
a.title("LOG IN")
a.geometry("1920x1080")
a.resizable(1,1)
a.configure(bg="white")
windowwidth=400
windowheight=300
screenwidth=a.winfo_screenmmwidth()
screenheight=a.winfo_screenheight()
x=(screenwidth//2)-(windowwidth//2)
y=(screenheight//2)-(windowheight//2)
a.geometry(f"{windowwidth}x{windowheight}+{x}+{y}")
a.state("zoomed")

frame=Frame(a, width=1000,height=999,bg="white").place(x = 900,y=1)



def toggle_password_visibility():
    if passwordd.get():
        passwordd.config(show="")
    else:
        passwordd.config(show="*")

my=Image.open("l.png")
my=my.resize((1550,830))
img=ImageTk.PhotoImage(my)
label=Label(a,image=img)
label.place(x=-7,y=0)


main_heading=Label(a,text="PARKING MANAGEMENT SYSTEM",fg="grey",font=("poppins",30,"bold"))
main_heading.place(x=430,y=100)
def on_enter(e):
    username.delete(0,"end")
def on_leave(e):
    name=username.get()
    if name=="":
        username.insert(0,"username")

# ========username edit=======
username=Entry(frame,width=25,fg="black",border=0,font=("poppins",12))
username.place(x=667,y=350) # x-axis and y-axis
username.insert(0,"username")
username.bind('<FocusIn>',on_enter)
username.bind('<FocusOut>',on_leave)


  
# =======forgot password=====
def forgot_password():
    global win
    win = Toplevel()
    win.geometry("350x400+450+150")
    win.title('Forgot password')
    win.configure(background='#f8f8f8')
    win.resizable(1,1)
    def update_pas():
        global win
        conn = sqlite3.connect('parking.db')
        c = conn.cursor()

        # The correct syntax for the UPDATE statement should be as follows:
        c.execute("""UPDATE admin_profile 
                    SET "password" = :new_pass 
                    WHERE "username" = :user""",
                {
                    'new_pass':new_password_entry.get(),
                    'user':username_entry.get(),
                })

        conn.commit()
        conn.close()
        win.destroy()
 
        #====================username =========
    username_entry = Entry(win,fg='#a7a7a7', font =('yu gothic ui semibold',12),show = '*',highlightthickness=2)
    username_entry.place(x=40, y =30, width=256, height=34)
    username_entry.config(highlightbackground='black', highlightcolor='black')
    username_label = Label(win, text='New Username',fg='#89898b',bg='#f8f8f8', font=('yu gothic ui', 11, 'bold'))
    username_label.place(x=40, y =0)



        # ====new password====
    new_password_entry = Entry(win,fg='#a7a7a7', font =('yu gothic ui semibold',12),show = '*',highlightthickness=2)
    new_password_entry.place(x=40, y =110, width=256, height=34)
    new_password_entry.config(highlightbackground='black', highlightcolor='black')
    new_password_label = Label(win, text='New password',fg='#89898b',bg='#f8f8f8', font=('yu gothic ui', 11, 'bold'))
    new_password_label.place(x=40, y =80)


        # =======conform passowrd====
    conform_password_entry = Entry(win,fg='#a7a7a7', font =('yu gothic ui semibold',12),show = '*',highlightthickness=2)
    conform_password_entry.place(x=40, y =190, width=256, height=34)
    conform_password_entry.config(highlightbackground='black', highlightcolor='black')
    conform_password_label = Label(win, text='Confirm password',fg='#89898b',bg='#f8f8f8', font=('yu gothic ui', 11, 'bold'))
    conform_password_label.place(x=40, y =160)

       

         

        # #====update password button =====
    update_pass = Button(win, fg='black', text ='update Password', font =('yu gothic ui bold',14), cursor =' hand2', activebackground='#1b87d2',command=update_pas)
    update_pass.place(x = 40, y = 240, width = 256, height=50)
    
    win.mainloop()

    
# =====password cursor===
def on_enter(a):
    passwordd.delete(0,"end")

def on_leave(a):
    if passwordd.get() == "":
        passwordd.insert(0, "Password")

# =========password edit==
passwordd=Entry(frame,width=25,fg="black",border=0,font=("poppins",12),show='*')
passwordd.place(x=667,y=450)
passwordd.insert(0,"Password")
passwordd.bind("<FocusIn>",on_enter)
passwordd.bind("<FocusOut>",on_leave)


# ===========Button==============
login_button = Button(a,activebackground="#CDF0EA",command=login,bg="#0079FF",text="login",fg="white",border=1,width= 20,font=("Comic Sans MS",10),padx=30,
                   pady=6,)
login_button.place(x=667,y=520)

show_password_var = BooleanVar()
show_password_checkbutton = Checkbutton(a, text="Show Password", variable=show_password_var,command=toggle_password_visibility,fg="black",bg = "gray")
show_password_checkbutton.place(x=783, y=475)


# ==== forgot Button==
forgot_password_button = Button(a, text="forgot password",font =('yu gothic ui',8,'bold underline'),fg='black',bg='gray' ,borderwidth = 0,command= forgot_password,cursor='hand2')

forgot_password_button.place(x=660,y=475)
a.mainloop()