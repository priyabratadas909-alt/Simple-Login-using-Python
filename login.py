from tkinter import *
import mysql.connector
from PIL import Image, ImageTk
from tkinter import messagebox

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Your_DB_PASSWORD",
    database="login"
)

cursor = con.cursor()

win = Tk()

image = Image.open(r"C:\Users\JAYATRI DAS\Downloads\IMG_20260711_20583797.jpeg")
image = image.resize((715, 500))
bg_photo = ImageTk.PhotoImage(image)
bg_label = Label(win, image=bg_photo)
bg_label.place(x=0, y=0)

def login():
    u = user.get()
    p = passwd.get()

    status.delete(0, END)

    if u == "" or p == "":
        messagebox.showerror("Error", "Please Enter Username and Password")
    else:
        sql = "SELECT * FROM login WHERE username=%s AND password=%s"
        values = (u, p)

        cursor.execute(sql, values)
        result = cursor.fetchone()

        if result:
            status.insert(0, "Present")
            messagebox.showinfo("Success", f"Login Succesful\nWelcome {u}")
        else:
            status.insert(0, "Absent")
            messagebox.showerror("Error", "Login unsuccess")


def register():
    u = user.get()
    p = passwd.get()
    p_again = c_pass.get()

    status.delete(0, END)

    if p != p_again:
        messagebox.showerror("Error", "Please Enter Same Password in both field")
    elif u == "" or p == "" or p_again == "":
        messagebox.showerror("Error", "Please fill all the fields")
    else:
        cursor.execute("SELECT * FROM login WHERE username=%s", (u,))
        existing = cursor.fetchone()

        if existing:
            status.insert(0, "Failed")
            messagebox.showerror("Error", "Username already exists, choose a different one")
        else:
            sql = "INSERT INTO LOGIN (username,password) VALUES (%s,%s)"
            values = (u, p)

            cursor.execute(sql, values)
            con.commit()

            status.insert(0, "Successfull")
            messagebox.showinfo("Success", f"Registration Successfull\nWelcome {u}!!")

def change():
    lbl_npass.place(x=130, y=180)
    n_pass.place(x=370, y=183)
    lbl_opass.place(x=130, y=125)
    o_pass.place(x=370, y=128)

    lbl_change.place(x=900, y=440)
    btn_change.place(x=900, y=442)

    lbl_back.place(x=250, y=440)
    btn_back.place(x=377, y=442)

    lbl_pass.place(x=900, y=125)
    passwd.place(x=900, y=128)
    lbl_status.place(x=130, y=230)
    status.place(x=370, y=233)

    btn_newuser.place(x=900, y=350)
    lbl_newuser.place(x=900, y=350)

    btn_login.place(x=800, y=300)
    btn_set.place(x=380, y=300)


def change_pass():
    u = user.get()
    p = o_pass.get()
    p_new = n_pass.get()

    status.delete(0, END)

    if u == "" or p == "":
        messagebox.showerror("Error", "Please enter Fields")
    else:
        cursor.execute("SELECT * FROM login WHERE username=%s", (u,))
        existing = cursor.fetchone()

        if not existing:
            status.insert(0, "Failed")
            messagebox.showerror("Error", "Username does not exist")
        else:
            sql = "UPDATE login SET password=%s WHERE username=%s"
            values = (p_new, u)
            cursor.execute(sql, values)
            con.commit()

            status.insert(0, "Success")
            messagebox.showinfo("Success", "Your Password Successfully Changed\nTry Login with new Password")


def login_again():
    lbl_newuser.place(x=257, y=350)
    btn_newuser.place(x=350, y=350)

    lbl_cpass.place(x=800, y=180)
    c_pass.place(x=800, y=183)
    lbl_status.place(x=130, y=180)
    status.place(x=370, y=183)

    lbl_olduser.place(x=800, y=340)
    btn_olduser.place(x=800, y=340)

    btn_login.place(x=380, y=300)
    btn_register.place(x=800, y=300)

    lbl_pass.place(x=130, y=125)
    passwd.place(x=370, y=128)

    lbl_change.place(x=250, y=440)
    btn_change.place(x=377, y=442)

    lbl_back.place(x=900, y=440)
    btn_back.place(x=900, y=442)

    lbl_npass.place(x=900, y=180)
    n_pass.place(x=900, y=183)
    lbl_opass.place(x=900, y=125)
    o_pass.place(x=900, y=128)

    btn_set.place(x=800, y=300)
    btn_login.place(x=380, y=300)


def newuser():
    lbl_status.place(x=130, y=230)
    status.place(x=370, y=233)
    lbl_cpass.place(x=130, y=180)
    c_pass.place(x=370, y=183)

    lbl_newuser.place(x=800, y=340)
    btn_newuser.place(x=800, y=337)

    lbl_olduser.place(x=250, y=350)
    btn_olduser.place(x=380, y=350)

    btn_login.place(x=800, y=290)
    btn_register.place(x=380, y=300)


def clear():
    user.delete(0, END)
    passwd.delete(0, END)
    status.delete(0, END)
    c_pass.delete(0, END)


win.title("LOGIN FORM")

lbl_title = Label(win, text="LOG IN", fg="black", font=("Instrument serif", 24, "bold underline"))
lbl_title.place(x=330, y=0)

lbl_user = Label(win, text="Enter Your Username:", fg="black", font=("Instrument serif", 18))
lbl_user.place(x=130, y=70)
user = Entry(win, bg="white", fg="black", font=(12), bd=3, width=24)
user.place(x=370, y=73)

lbl_pass = Label(win, text="Enter Your Password:", fg="black", font=("Instrument serif", 18))
lbl_pass.place(x=130, y=125)
passwd = Entry(win, bg="white", fg="black", font=(12), bd=3, width=24, show='*')
passwd.place(x=370, y=128)

lbl_status = Label(win, text="Status:", fg="black", font=("Instrument serif", 20, "bold"))
lbl_status.place(x=130, y=180)
status = Entry(win, bg="white", fg="green", font=("Instrument serif", 15, "bold"), bd=3, width=20)
status.place(x=370, y=183)

lbl_newuser = Label(win, text="New User?", fg="black", font=("Instrument serif", 15, "bold"))
lbl_newuser.place(x=257, y=350)
btn_newuser = Button(win, text="REGISTER", command=newuser, bg="black", font=("Times", 9, "bold"), fg="white")
btn_newuser.place(x=350, y=350)

lbl_cpass = Label(win, text="Enter you Password again:", fg="black", font=("Instrument serif", 18))
c_pass = Entry(win, bg="white", fg="black", font=("Instrument serif", 15), bd=3, width=32, show="*")

lbl_olduser = Label(win, text="Already a User?", fg="black", font=("Instrument serif", 15, "bold"))
btn_olduser = Button(win, text="Log In", command=login_again, bg="black", font=("Times", 9, "bold"), fg="white")

btn_register = Button(win, text="REGISTER", command=register, bg="black", font=("Times", 13, "bold"), fg="white")

btn_login = Button(win, text="LOG IN", command=login, bg="black", font=("Times", 13, "bold"), fg="white")
btn_login.place(x=380, y=300)
btn_clear = Button(win, text="CLEAR", command=clear, bg="black", font=("Times", 13, "bold"), fg="white")
btn_clear.place(x=257, y=300)
btn_set = Button(win, text="SET", command=change_pass, bg="black", font=("Times", 13, "bold"), fg="white")

lbl_change = Label(win, text="Change Password:", fg="black", font=("Instrument serif", 13, "bold"))
btn_change = Button(win, text="CHANGE", command=change, bg="black", font=("Times", 8, "bold"), fg="white")
lbl_change.place(x=250, y=440)
btn_change.place(x=377, y=442)
lbl_back = Label(win, text="Back To Login:", fg="black", font=("Instrument serif", 13, "bold"))

btn_back = Button(win, text="Login", command=login_again, bg="black", font=("Times", 8, "bold"), fg="white")


lbl_npass = Label(win, text="Enter your new Password:", fg="black", font=("Instrument serif", 18))
n_pass = Entry(win, bg="white", fg="black", font=("Instrument serif", 15), bd=3, width=32, show="*")
lbl_opass = Label(win, text="Enter Your old Password:", fg="black", font=("Instrument serif", 18))
o_pass = Entry(win, bg="white", fg="black", font=(12), bd=3, width=24, show='*')


win.geometry("715x500+300+150")
win.resizable(False, False)
win.mainloop()
