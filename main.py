from tkinter import *

window = Tk()
window.geometry("480x420")

centre = Frame(window, highlightbackground="black", highlightthickness=4, width=440, height=120)
centre.grid(row=2, padx=20, pady=10)

top = Frame(window, highlightbackground="black", highlightthickness=4, width=440, height=120)
top.grid(row=1, padx=20, pady=10)

bottom = Frame(window, highlightbackground="black", highlightthickness=4, width=440, height=120)
bottom.grid(row=3, padx=20,pady=10)

entry = Entry(top, width=50)
entry.insert(0, "Enter text to encrypt")
entry.pack(padx=20, pady=10)

encryption_type=1
radio = Radiobutton(centre, text="cipher1 | swaps rows and columns + applies a shift", variable=encryption_type, value=1)
radio.pack()


    














window.mainloop()
