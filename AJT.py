from tkinter import *
import sqlite3
root=Tk()
root.title('gere_voiture')
root.geometry("1400x750")
root.iconbitmap("car_23773.ico")
conn = sqlite3.connect('voiture.db')


def createVoitur():
    cur = conn.cursor
    req1 = "CREATE TABLE IF NOT EXIST voitures(id_v INTEGER PRIMARY KEY AUTOINCREMENT, marque TEXT NOT NULL\
    ,model integer NOT NULL ,type_carb TEXT NOT NULL, nb_place INTEGER NOT NULL,transmission TEXT NOT NULL,disponibilite TEXT NOT NULL)"
    cur.execute(req1) 
    conn.commit()
    conn.close()

def createuser():
    curr = conn.cursor
    req2 = "CREATE TABLE user(login text NOT NULL, mote_de_pass text NOT NULL)"
    curr.execute(req2)
    conn.commit()
    conn.close()

def ajtuser():
    c = conn.cursor
    req3 = "INSERT INTO user values (:login , :mote_de_pass )"{
        'login':'ismail',
        'mote_de_pass':'zbair'
        }
    c.execute(req3)
    conn.commit()
    conn.close()



conn.commit()
conn.close()

root.mainloop()