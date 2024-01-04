# Tkinter 

# pygame 

# pyqts5


import tkinter as tk

window = tk.Tk()

window.geometry("500x300")
window.title("this is a title")
window.config(background = "#3ed6b3")

lbl = tk.Label(window, text = "Hellow world", font = ("robort", 30, "bold"), fg = "white", bg = "#973ed6")
lbl.pack(fill="x", padx = 30, pady = 20, ipady = 10, side ="top")

en = tk.Entry(window, font = ("robort", 20, "italic"))
en.pack()

btn = tk.Button(window, text = "Click Me", font = ("robort", 20, "bold"))
btn.pack(pady=20)

window.mainloop()


# 1) pack()
# 2) grid()
# 3) place()