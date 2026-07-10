from tkinter import*
import mysql.connector
from tkinter import messagebox

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="T202514921",
    database="login"
)

cursor=con.cursor()

window= Tk()

def login():

    u= t1.get()
    p= t2.get()

    t3.delete(0,END)    

    if u=="" or p=="":
        messagebox.showerror("Error","Please Enter Username and Password")

    else:
        sql="SELECT * FROM login WHERE username=%s AND password=%s"
        values=(u,p)

        cursor.execute(sql, values)
        result= cursor.fetchone()

        if result:
            t3.insert(0, "Present")
            messagebox.showinfo("Success","Login Succesful")
        else:
            t3.insert(0, "Absent")
            messagebox.showerror("Error","Login unsuccess")

def register():
    u= t1.get()
    p= t2.get()
    p_again=t4.get()

    t3.delete(0,END)    

    if p != p_again:
        messagebox.showerror("Error","Please Enter Same Password in both field")

    elif u=="" or p=="" or p_again=="":
        messagebox.showerror("Error","Please fill all the fields")

    else:
        sql="INSERT INTO LOGIN (username,password) VALUES (%s,%s)"
        values=(u,p)

        cursor.execute(sql, values)
        con.commit()

        t3.insert(0,"Successfull")
        messagebox.showinfo("Success","Registration Successfull")


def login_again():

    lbl4.place(x=57, y= 300)
    btn3.place(x=147,y=303)

    lbl5.place(x=700, y= 170)
    t4.place(x=700, y=175)
    lbl3.place(x=30, y= 200)
    t3.place(x=110, y=205)

    lbl6.place(x=700, y= 300)
    btn4.place(x=700,y=303)

    btn1.place(x=380,y=290)
    btn5.place(x=700,y=290)


def newuser():

    lbl3.place(x=30, y= 220)
    t3.place(x=110, y=225)
    lbl5.place(x=30, y= 170)
    t4.place(x=260, y=175)

    lbl4.place(x=700, y= 300)
    btn3.place(x=700,y=303)
              
    lbl6.place(x=57, y= 300)
    btn4.place(x=180,y=303)

    btn1.place(x=700,y=290)
    btn5.place(x=380,y=290)
    
def clear():
    t1.delete(0,END)
    t2.delete(0,END)
    t3.delete(0,END)
    t4.delete(0,END)

window.title("LOGIN FORM")
lbl=Label(window, text="LOG IN", fg="black", font=("Instrument serif", 24, "bold underline"))      #title
lbl.place(x=190, y=10)
lbl1=Label(window, text="Enter Your Username:", fg="black", font=("Instrument serif", 18))          #username
lbl1.place(x=30, y= 70)
t1=Entry(window, bg="cyan", fg="black",font=(12),bd=3)
t1.place(x=220, y=75)
lbl2=Label(window, text="Enter Your Password:", fg="black", font=("Instrument serif", 18))          #password
lbl2.place(x=30, y= 125)
t2=Entry(window, bg="cyan", fg="black",font=(12),bd=3,show='*')
t2.place(x=220, y=128)
lbl3=Label(window, text="Status:", fg="black", font=("Instrument serif", 20 ,"bold"))               #status
lbl3.place(x=30, y= 200)
t3=Entry(window, bg="white", fg="green",font=("Instrument serif", 15 ,"bold"),bd=3, width=25)
t3.place(x=110, y=205)

lbl4=Label(window, text="New User?", fg="black", font=("Instrument serif", 15 ,"bold"))               #status
lbl4.place(x=57, y= 300)
btn3=Button(window, text="REGISTER", command=newuser, bg="blue", font=("Times", 9 ,"bold"), fg="white")
btn3.place(x=147,y=303)

lbl5=Label(window, text="Enter you Password again:", fg="black", font=("Instrument serif", 18))               #status
t4=Entry(window, bg="cyan", fg="black",font=("Instrument serif", 14 ),bd=3,width=22,show="*")

lbl6=Label(window, text="Already a User?", fg="black", font=("Instrument serif", 15 ,"bold"))               
btn4=Button(window, text="Log In", command=login_again , bg="blue", font=("Times", 9 ,"bold"), fg="white")

btn5=Button(window, text="REGISTER", command=register ,bg="blue",font=("Times", 13 ,"bold"), fg="white")

btn1=Button(window, text="LOG IN", command=login ,bg="blue",font=("Times", 13 ,"bold"), fg="white")
btn1.place(x=400,y=290)
btn2=Button(window, text="CLEAR", command=clear, bg="blue", font=("Times", 13 ,"bold"), fg="white")
btn2.place(x=300,y=290)
window.geometry("500x500+900+80")
window.resizable(False,False)
window.mainloop()