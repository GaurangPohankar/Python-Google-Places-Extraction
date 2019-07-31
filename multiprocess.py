import tkinter as tk
from tkinter import ttk


class dictionary(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.fields = []
        self.createWidgets()
        self.grid(column=0, sticky="NEWS")

    def createWidgets(self):        
        self.add_field()
        self.add_lang = ttk.Button(self, text="add language", command=self.add_field)
        self.add_lang.bind("<Return>", self.add_field)
        self.add_lang.grid(row=len(self.fields), column=3, padx=4, pady=6, sticky="W")


    def add_field(self):
        self.fields.append({})
        n = len(self.fields)-1
        self.fields[n]['var'] = tk.StringVar(self)
        self.fields[n]['field'] = ttk.Entry(self, textvariable=self.fields[n]['var'])
        self.fields[n]['field'].grid(row=n, column=0, columnspan=2, padx=4, pady=6, sticky="NEWS")
        if n:
            self.add_lang.grid(row=n + 1, column=3, padx=4, pady=6, sticky="W")



if __name__ == '__main__':
    root = tk.Tk()
    app = dictionary(master=root)
    app.mainloop()
