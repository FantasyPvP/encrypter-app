import tkinter as tk
from tkinter import ttk
import sv_ttk
import matplotlib.pyplot as graph

import encrypt
import encrypt2
import encrypt3







class Encrypter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("encrypter app")
        self.geometry("420x720")
    





        layer1 = tk.Label(self, width=380, height=120)
        layer1.place(x=20, y=10)

        self.description_text = "Welcome to my encryption app!\nto use all of the features, simply select the type of encryption you want to use, select whether to encrypt or decrypt and press confirm!"

        top_text = ttk.Label(layer1, text = self.description_text, wraplength="360", padding="20")
        top_text.pack()





        self.type_ = tk.StringVar()
        self.encrypt = tk.StringVar()
        self.text = tk.StringVar()
        self.key = tk.StringVar()
        self.output = ""
        
        # left set of radio buttons for the encrypter

        layer2L = ttk.LabelFrame(self, text="encryption type", width=300, height=300)
        layer2L["labelanchor"] = "n"
        layer2L.place(x=40, y=160)

        label = tk.Label(layer2L, width=15, height=1)
        label.grid(column=0, row=0, ipadx=5, ipady=5)
        radio = ttk.Radiobutton(layer2L, text="cipher1", variable=self.type_, value=1)
        radio.grid(column=0, row=1, ipadx=5, ipady=5)
        radio = ttk.Radiobutton(layer2L, text="cipher2", variable=self.type_, value=2)
        radio.grid(column=0, row=2, ipadx=5, ipady=5)
        radio = ttk.Radiobutton(layer2L, text="cipher3", variable=self.type_, value=3)
        radio.grid(column=0, row=3, ipadx=5, ipady=5)
        label = tk.Label(layer2L, width=20, height=1)
        label.grid(column=0, row=4, ipadx=5, ipady=5)



        layer3 = ttk.LabelFrame(self, text="text input and output", width=380, height=100)
        layer3["labelanchor"] = "n"
        layer3.place(x=20, y=420)




        label = tk.Label(layer3, width=45, height=1)
        label.grid(column=0, row=0, ipadx=5, ipady=10)

        self.text = ttk.Entry(layer3, width=40, text="enter message to be encrypted") #2E2C2F
        self.text.grid(column=0, row=1, ipadx=5, ipady=5)


        label = tk.Label(layer3, width=45, height=1)
        label.grid(column=0, row=2, ipadx=5, ipady=5)

        self.key = ttk.Entry(layer3, width=40, text="enter decryption or encryption key") #2E2C2F
        self.key.grid(column=0, row=3, ipadx=5, ipady=5)

        label = tk.Label(layer3, width=45, height=1)
        label.grid(column=0, row=4, ipadx=5, ipady=5)
        
        self.output = tk.Label(layer3, width=40, bg="#292929", wraplength="300", text="")
        self.output.grid(column=0, row=5, ipadx=5, ipady=5)

        label = tk.Label(layer3, width=50, height=1)
        label.grid(column=0, row=6, ipadx=5, ipady=5)




        # rightn set of options that allow you to select encrypt / decrypt and confirm

        layer2R = ttk.LabelFrame(self, text="encrypt or decrypt", width=300, height=300)
        layer2R["labelanchor"] = "n"
        layer2R.place(x=220, y=160)

        label = tk.Label(layer2R, width=15, height=1)
        label.grid(column=0, row=0, ipadx=5, ipady=5)
        radio = ttk.Radiobutton(layer2R, text="encrypt", variable=self.encrypt, value=1)
        radio.grid(column=0, row=1, ipadx=5, ipady=5)
        radio = ttk.Radiobutton(layer2R, text="decrypt", variable=self.encrypt, value=0)
        radio.grid(column=0, row=2, ipadx=5, ipady=5)
        label = tk.Label(layer2R, width=15, height=1)
        label.grid(column=0, row=3, ipadx=5, ipady=5)
        button = ttk.Button(layer2R, text="confirm", command=self.process)
        button.grid(column=0, row=4, ipadx=5, ipady=0)
        label = tk.Label(layer2R, width=20, height=1)
        label.grid(column=0, row=5, ipadx=5, ipady=5)



    def process(self):
        text = self.text.get()
        key = int(self.key.get())
        type_ = self.type_.get()
        encrypt_ = self.encrypt.get()

        self.charfreq = {
            "a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0, "i" : 0, "j" : 0, 
            "k" : 0, "l" : 0, "m" : 0, "n" : 0, "o" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0, "t" : 0,
            "u" : 0, "v" : 0, "w" : 0, "x" : 0, "y" : 0, "z" : 0, "0" : 0, "1" : 0, "2" : 0, "3" : 0, 
            "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0
        }


        for char in text:
            if char in self.charfreq:
                self.charfreq[char] += 1

        self.draw_graph()


        (output, key) = encrypt.cipher(text, key, encrypt_)

        print(output, key)

        self.output.config(text=output)

        

        #match self.type_:
        #    case 1:
        #        encrypt.


        #self.output.config(text = encryption_result)
    
    def draw_graph(self):

        print(self.charfreq.keys(), self.charfreq.values())

        x = [y for y in self.charfreq.keys()]
        for key in x:
            if self.charfreq[key] == 0:
                del self.charfreq[key]


        print(self.charfreq.keys(), self.charfreq.values())

        graph.bar(self.charfreq.keys(), self.charfreq.values(), label="character frequency chart")
        graph.show()

        print("ok")
























            

if __name__ == "__main__":
    window = Encrypter()
    sv_ttk.set_theme("dark")
    window.mainloop()
