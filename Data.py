from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import sqlite3
root=Tk()
root.title('gere_voiture')
root.geometry("1400x750")
root.iconbitmap("car_23773.ico")
my_img = ImageTk.PhotoImage(Image.open("c1.png"))
l1 = Label(root,image=my_img).place(x=0,y=0)

def Ajouter():
    # récupération des données du formulaire
    marque = entrymarque.get()
    model   =  entry_model.get() 
    type_carb     =  entry_type_carb.get() 
    nb_place = entry_nb_place.get()
    transmission = entry_transmission.get()
    disponibilite = entry_disponibilite.get()
    conn = sqlite3.connect('voiture.db')
    cur = conn.cursor()   
    req2 = "INSERT INTO voitures (marque , model, type_carb,nb_place,transmission,disponibilite) values (?, ?, ?,?,?,?)"
    cur.execute(req2 , (marque, model, type_carb,nb_place,transmission , disponibilite))
    conn.commit()
    conn.close()
    
def supprimer():
    conn = sqlite3("voiture.db")
    c = conn.cursor()
    c.execute("DELETE from voitures WHERE id_v = "+ entry_id_v.get())
    entry_id_v.delete(0 , END)
    conn.commit()
    conn.close()


# Label & Entry marque
lblmarque = Label(root , text = "marque :")
lblmarque.place( x = 10 , y = 40 ) 
entrymarque = Entry(root)
entrymarque.place( x = 100 , y = 40 , width = 200)
 
# Label & Entry model
lbl_model = Label(root , text = "model :")
lbl_model.place( x = 10 , y = 100 ) 
entry_model = Entry(root)
entry_model.place( x = 100 , y = 100 , width = 200)

# Label & Entry type_carb
lbl_type_carb = Label(root , text = "type_carb :")
lbl_type_carb.place( x = 10 , y = 130 ) 
entry_type_carb = Entry(root)
entry_type_carb.place( x = 100 , y = 130 , width = 200)


# Label & Entry nb_place
lbl_nb_place = Label(root , text = "nb_place :")
lbl_nb_place.place( x = 10 , y = 160 ) 
entry_nb_place = Entry(root)
entry_nb_place.place( x = 100 , y = 160 , width = 200)

# Label & Entry transmission
lbl_transmission = Label(root , text = "transmission :")
lbl_transmission.place( x = 10 , y = 190 ) 
entry_transmission = Entry(root)
entry_transmission.place( x = 100 , y = 190 , width = 200)

# Label & Entry disponibilite
lbl_disponibilite = Label(root , text = "disponibilite :")
lbl_disponibilite.place( x = 10 , y = 220 ) 
entry_disponibilite = Entry(root)
entry_disponibilite.place( x = 100 , y = 220 , width = 200)

# Label & Entry id_v
lbl_id_v = Label(root , text = "id_v :")
lbl_id_v.place( x = 10 , y = 250 ) 
entry_id_v = Entry(root)
entry_id_v.place( x = 100 , y = 250 , width = 200)

 
# Button Ajouter
btnAjouter = Button(root , text = "Ajouter" ,bg="#72b884", command = Ajouter)
btnAjouter.place(x = 50 , y = 300, width = 90 , height = 35)

# Button Supprimer
btnsupprimer = Button(root , text = "supprimer" ,bg="#72b884")
btnsupprimer.place(x = 170 , y = 300, width = 90 , height = 35)



btn = Button(root,text="Exit Programe",command=root.quit,bg="red")
btn.place(x=270,y=300,width = 90 , height = 35)

tree = ttk.Treeview(root , columns = (1,2,3,4,5,6,7) , heigh=5, show='headings')
tree.place(x = 150,y = 350 , width=1200 , height=320)

tree.heading(1 , text = "Id")
tree.heading(2 , text = "marque")
tree.heading(3 , text = "model")
tree.heading(4 , text = "type_carb")
tree.heading(5 , text = "nb_place")
tree.heading(6 , text = "transmission")
tree.heading(7 , text = "disponibilite")
tree.column(1 , width = 180)
tree.column(1 , width = 180)
tree.column(1 , width = 180)
tree.column(1 , width = 180)
tree.column(1 , width = 180)
tree.column(1 , width = 180)
#afficher les donner
con = sqlite3.connect("voiture.db")
cur = con.cursor()
req =  "CREATE TABLE IF NOT EXISTS voitures(id_v INTEGER PRIMARY KEY AUTOINCREMENT, marque TEXT NOT NULL\
    ,model integer NOT NULL ,type_carb TEXT NOT NULL, nb_place INTEGER NOT NULL,transmission TEXT NOT NULL,disponibilite TEXT NOT NULL)"
cur.execute(req)
selectt = cur.execute("select * from voitures")
for row in selectt:
    tree.insert('' , END , values = row)
root.mainloop()