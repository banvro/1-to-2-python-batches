# Tkinter() 
# 1) pack()
# 2) grid()


import tkinter as tk

app = tk.Tk()
app.geometry("400x300")

lblspace = tk.Label(app, text = " ", bg = "green")

lbl1 = tk.Label(app, text = "Username : ", font = ("robort", 10, "bold"))
lbl2 = tk.Label(app, text = "Number : ", font = ("robort", 10, "bold"))

en1 = tk.Entry(app, font = ("robort", 10, "italic"))
en2 = tk.Entry(app, font = ("robort", 10, "italic"))

lblspace.grid(row = 0, column = 0, padx=30, pady=30)

lbl1.grid(row = 1, column = 1)
en1.grid(row = 1, column = 2)

lbl2.grid(row = 2, column = 1)
en2.grid(row = 2, column = 2)
# 


# lbl1.pack()
# en1.pack()
# lbl2.pack()
# en2.pack()


app.mainloop()