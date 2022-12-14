import tkinter as tk
from tkinter import ttk
import sv_ttk
import matplotlib.pyplot as graph
from tkinter import messagebox

import encrypt1
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


        self.render_sections()

        # left set of radio buttons for the encrypter




    def process(self):
        text = self.text.get()
        key = self.key.get()
        cipher = self.type_.get()
        encrypt_ = int(self.encrypt.get())

        # int(key.get())




        if text.endswith(".txt"):
            file = True
            try:
                filename = text
                with open(text, "r") as filehandle:
                    text = filehandle.read()
            except:
                pass
        else:
            file = False


        encrypt = False
        if encrypt_:
            encrypt = True
            # key is not strictly necessary here. None will be passed to functions
            if key == "":
                key = None

        # sends text to cipher algorithms

        match cipher:
            case "caesar":
                (stat, output, key, other) = encrypt1.cipher(text, key, encrypt)
            case "transpos":
                (stat, output, key, other) = encrypt2.scramble(text.rstrip())
            case "atbash":
                (stat, output, key, other) = encrypt3.process(text)

        # outputs

        if stat != "err":
            if key:
                if file:
                    with open(f"{filename[:-4]}_.txt", "w") as file:
                        file.write(output)
                    self.output.config(text=f"check {filename}\nKey: {key}")
                else:
                    self.output.config(text=f"Output : {output}\nKey : {key}")
            else:
                if file:
                    with open(f"{filename[:-4]}_.txt", "w") as file:
                        file.write(output)
                    self.output.config(text=f"check {filename}")
                else:
                    self.output.config(text=f"Output : {output}")

        if other:
            self.status.config(text=f"{stat} : {other}")
        else:
            self.status.config(text=f"{stat}")

        # character frequency graphs

        box = messagebox.askyesno("would you like to see graphs of character frequencies in your message?")

        if box == True:
            self.draw_graph(text)
            self.draw_graph(output)









    def draw_graph(self, text):

        self.charfreq = {
            "a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0, "i" : 0, "j" : 0,
            "k" : 0, "l" : 0, "m" : 0, "n" : 0, "o" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0, "t" : 0,
            "u" : 0, "v" : 0, "w" : 0, "x" : 0, "y" : 0, "z" : 0, "0" : 0, "1" : 0, "2" : 0, "3" : 0,
            "4" : 0, "5" : 0, "6" : 0, "7" : 0, "8" : 0, "9" : 0
        }

        for char in text:
            if char in self.charfreq:
                self.charfreq[char] += 1


        x = [y for y in self.charfreq.keys()]
        for key in x:
            if self.charfreq[key] == 0:
                del self.charfreq[key]


        graph.style.use('dark_background')
        graph.bar(self.charfreq.keys(), self.charfreq.values(), label="character frequency chart")
        graph.show()





    def render_sections(self):

        self.layer2l = Layer(self, text="encryption type", width=300, height=300, x=40, y=160)

        self.layer2l.label1 = tk.Label(self.layer2l, width=15, height=1)
        self.layer2l.label1.grid(column=0, row=0, ipadx=5, ipady=5)
        self.layer2l.radio1 = ttk.Radiobutton(self.layer2l, text="caesar", variable=self.type_, value="caesar")
        self.layer2l.radio1.grid(column=0, row=1, ipadx=5, ipady=5)
        self.layer2l.radio2 = ttk.Radiobutton(self.layer2l, text="transpos", variable=self.type_, value="transpos")
        self.layer2l.radio2.grid(column=0, row=2, ipadx=5, ipady=5)
        self.layer2l.radio3 = ttk.Radiobutton(self.layer2l, text="atbash", variable=self.type_, value="atbash")
        self.layer2l.radio3.grid(column=0, row=3, ipadx=5, ipady=5)
        self.layer2l.label2 = tk.Label(self.layer2l, width=20, height=1)
        self.layer2l.label2.grid(column=0, row=4, ipadx=5, ipady=5)


        self.layer2r = Layer(self, text="encrypt or decrypt", width=300, height=300, x=220, y=160)

        self.layer2r.label1 = tk.Label(self.layer2r, width=15, height=1)
        self.layer2r.label1.grid(column=0, row=0, ipadx=5, ipady=5)
        self.layer2r.radio1 = ttk.Radiobutton(self.layer2r, text="encrypt", variable=self.encrypt, value=1)
        self.layer2r.radio1.grid(column=0, row=1, ipadx=5, ipady=5)
        self.layer2r.radio2 = ttk.Radiobutton(self.layer2r, text="decrypt", variable=self.encrypt, value=0)
        self.layer2r.radio2.grid(column=0, row=2, ipadx=5, ipady=5)
        self.layer2r.label2 = tk.Label(self.layer2r, width=15, height=1)
        self.layer2r.label2.grid(column=0, row=3, ipadx=5, ipady=5)
        self.layer2r.button1 = ttk.Button(self.layer2r, text="confirm", command=self.process)
        self.layer2r.button1.grid(column=0, row=4, ipadx=5, ipady=0)
        self.layer2r.label3 = tk.Label(self.layer2r, width=20, height=1)
        self.layer2r.label3.grid(column=0, row=5, ipadx=5, ipady=5)



        self.layer3 = Layer(self, text="text input and output", width=380, height=100, x=20, y=420)

        self.layer3.label1 = tk.Label(self.layer3, width=45, height=1)
        self.layer3.label1.grid(column=0, row=0, ipadx=5, ipady=10)
        self.text = ttk.Entry(self.layer3, width=40, text="enter message to be encrypted") #2E2C2F
        self.text.grid(column=0, row=1, ipadx=5, ipady=5)
        self.layer3.label2 = tk.Label(self.layer3, width=45, height=1)
        self.layer3.label2.grid(column=0, row=2, ipadx=5, ipady=5)
        self.key = ttk.Entry(self.layer3, width=40, text="enter decryption or encryption key") #2E2C2F
        self.key.grid(column=0, row=3, ipadx=5, ipady=5)
        self.layer3.label3 = tk.Label(self.layer3, width=45, height=1)
        self.layer3.label3.grid(column=0, row=4, ipadx=5, ipady=5)
        self.output = tk.Label(self.layer3, width=40, bg="#292929", wraplength="300", text="")
        self.output.grid(column=0, row=5, ipadx=5, ipady=5)
        self.status = tk.Label(self.layer3, width=40, bg="#292929", wraplength="300", text="")
        self.status.grid(column=0, row=6, ipadx=5, ipady=5)
        self.layer3.label4 = tk.Label(self.layer3, width=50, height=1)
        self.layer3.label4.grid(column=0, row=7, ipadx=5, ipady=5)




        # rightn set of options that allow you to select encrypt / decrypt and confirm















class Layer(ttk.Labelframe):
    def __init__(self, root, text=None, width=300, height=300, x=0, y=0):
        super().__init__(root, text=text, width=300, height=300)

        self.anchor = "n"
        self.place(x=x, y=y)





















if __name__ == "__main__":
    window = Encrypter()
    sv_ttk.set_theme("dark")
    window.mainloop()
