from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3
root=Tk()
root.title('Connexion')
root.geometry("1400x750")
root.iconbitmap("car_23773.ico")
my_img = ImageTk.PhotoImage(Image.open("c1.png"))
l1 = Label(root,image=my_img).place(x=0,y=0)


def Verifier():
    try:
        conn = sqlite3.connect('voiture.db')
        cur = conn.cursor()
       
        for row in cur.execute("select * from user"):
           username = row[0]
           passw = row[1]
    except Exception as ep:
        messagebox.showerror('',ep)

    userr = entrylogin.get()
    passs = entry_pass.get()
    if (userr != "" or passs != ""):
         if (userr == username and passs == passw ):
              messagebox.showinfo('login status','successfuly')
              root.destroy()
              import Data
         else:
              messagebox.showinfo('login status','password or login  not correct')   
    else:
            warn ="login or password can't be empty"
            messagebox.showerror('',warn)
         

# Label & Entry login
lbllogin = Label(root , text = "Login")
lbllogin.place( x = 10 , y = 40 ) 
entrylogin = Entry(root)
entrylogin.place( x = 100 , y = 40 , width = 200)
 
# Label & Entry mot_de_passe
lbl_pass= Label(root , text = "Password")
lbl_pass.place( x = 10 , y = 70 ) 
entry_pass = Entry(root)
entry_pass.place( x = 100 , y = 70 , width = 200)

# Button Action
btnVerif = Button(root , text = "Connexion" ,bg='#72b884',command=Verifier)
btnVerif.place(x = 100 , y = 100, width = 200 , height = 25)

btn = Button(root,text="Exit Programe",bg='red',command=root.quit)
btn.place(x=130,y=150)
root.mainloop()