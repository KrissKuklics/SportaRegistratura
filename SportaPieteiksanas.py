import psycopg2
import psycopg2.extras
from tkinter import *
from tkinter.ttk import *

DB_HOST="mouse.db.elephantsql.com"
DB_NAME="qikaguov"
DB_USER="qikaguov"
DB_PASS="kzKs5VsB-YTS4K0ECtxMUUl-vRpXUSnH"

conn=psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()


window = Tk()
window.geometry('350x250')
window.title("Sporta reģistratūra")

"""
sql = '''CREATE TABLE Dati(Vārds varchar, Uzvārds varchar, SportaVeids varchar); '''
cur.execute(sql)
"""
def delete():
    txt0.delete(0, "")
    txt2.delete(0, "")
    combo.current(0)
    
def submit():
    vards=txt0.get()
    uzvards=txt2.get()
    sports=combo.get()
    
    cur.execute('INSERT INTO Dati VALUES (%s,%s,%s)', (vards,uzvards,sports))
    conn.commit()
    cur.close()
    conn.close()
    
emptylbl0 = Label(window, text="        ")
emptylbl0.grid(column=0, row=0)
emptylbl1 = Label(window, text="        ")
emptylbl1.grid(column=0, row=1)
emptylbl2 = Label(window, text="        ")
emptylbl2.grid(column=0, row=2)
emptylbl3 = Label(window, text="        ")
emptylbl3.grid(column=0, row=3)
emptylbl4 = Label(window, text="        ")
emptylbl4.grid(column=0, row=4)
emptylbl5 = Label(window, text="        ")
emptylbl5.grid(column=1, row=6)
emptylbl6 = Label(window, text="        ")
emptylbl6.grid(column=2, row=6)
emptylbl7 = Label(window, text="        ")
emptylbl7.grid(column=3, row=6)
emptylbl8 = Label(window, text="        ")
emptylbl8.grid(column=1, row=7)
emptylbl9 = Label(window, text="        ")
emptylbl9.grid(column=2, row=7)
emptylbl10 = Label(window, text="        ")
emptylbl10.grid(column=3, row=7)

lbl0 = Label(window, text="Vārds")
lbl0.grid(column=1, row=0)
lbl1 = Label(window, text="")
lbl1.grid(column=1, row=1)
lbl2 = Label(window, text="Uzvārds")
lbl2.grid(column=1, row=2)
lbl3 = Label(window, text="")
lbl3.grid(column=1, row=3)
lbl4 = Label(window, text="Sporta veids")
lbl4.grid(column=1, row=4)

txt0 = Entry(window,width=20)
txt0.grid(column=2, row=0)
txt2 = Entry(window,width=20)
txt2.grid(column=2, row=2)

combo = Combobox(window)

combo['values']= ("Izvēlies sporta veidu", "Basketbols", "Futbols", "Volejbols")
combo.current(0) 
combo.grid(column=2, row=4)

btn0 = Button(window, text="Apstiprināt", command=submit)
btn0.grid(column=1, row=8)
btn2 = Button(window, text="Nodzēst", command=delete)
btn2.grid(column=2, row=8)
btn4 = Button(window, text="Iziet", command=window.destroy)
btn4.grid(column=3, row=8)


window.mainloop()

