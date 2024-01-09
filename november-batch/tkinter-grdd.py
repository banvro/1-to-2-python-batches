import tkinter as tk
import mysql.connector

conn = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "amazon")

cuser = conn.cursor()

def savethis():
    name = en1.get()
    age = en2.get()
    email = en3.get()
    number = en4.get()

    cuser.execute(f"insert into sturec values('{name}', {age}, '{email}', '{number}')")
    conn.commit()

    lbl10.config(text = "Data Saved Sucessfully...!")

    en1.delete(0, tk.END)
    en2.delete(0, tk.END)
    en3.delete(0, tk.END)
    en4.delete(0, tk.END)

app = tk.Tk()

app.geometry("600x500")
app.title("Students Records")
app.config(background = "yellow")

lbl1 = tk.Label(app, text = "")
lbl2 = tk.Label(app, text = "Name", font = ("robort", 25, "bold"), bg = "yellow")
lbl3 = tk.Label(app, text = "Age", font = ("robort", 25, "bold"), bg = "yellow")
lbl4 = tk.Label(app, text = "Email", font = ("robort", 25, "bold"), bg = "yellow")
lbl5 = tk.Label(app, text = "Number", font = ("robort", 25, "bold"), bg = "yellow")

lbl6 = tk.Label(app, text = ":", font = ("robort", 25, "bold"), bg = "yellow")
lbl7 = tk.Label(app, text = ":", font = ("robort", 25, "bold"), bg = "yellow")
lbl8 = tk.Label(app, text = ":", font = ("robort", 25, "bold"), bg = "yellow")
lbl9 = tk.Label(app, text = ":", font = ("robort", 25, "bold"), bg = "yellow")

lbl10 = tk.Label(app, text = "", font = ("robort", 25, "italic"), bg = "yellow", fg = "green")

btn = tk.Button(app, text = "Save Data", font = ("robort", 25, "bold"), bg = "#34ebc9", command = savethis)

en1 = tk.Entry(app, font = ("robort", 25, "italic"))
en2 = tk.Entry(app, font = ("robort", 25, "italic"))
en3 = tk.Entry(app, font = ("robort", 25, "italic"))
en4 = tk.Entry(app, font = ("robort", 25, "italic"))

lbl1.grid(row = 0, column = 0, padx = 20, pady = 20)
lbl2.grid(row = 1, column = 1, pady = 8)
lbl3.grid(row = 2, column = 1, pady = 8)
lbl4.grid(row = 3, column = 1, pady = 8)
lbl5.grid(row = 4, column = 1, pady = 8)

lbl6.grid(row = 1, column = 2, padx = 7)
lbl7.grid(row = 2, column = 2, padx = 7)
lbl8.grid(row = 3, column = 2, padx = 7)
lbl9.grid(row = 4, column = 2, padx = 7)

en1.grid(row = 1, column = 3)
en2.grid(row = 2, column = 3)
en3.grid(row = 3, column = 3)
en4.grid(row = 4, column = 3)

btn.grid(row = 5, column = 3, pady = 20)

lbl10.grid(row = 6, column = 3)

app.mainloop()