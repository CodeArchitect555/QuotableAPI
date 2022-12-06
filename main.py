import requests
import tkinter as tk
from tkinter import END, Text
from tkinter.ttk import Button

class Main(tk.Frame):
    def __init__(self, master):
        self.text_box = Text(master, height=10, width=50)
        self.get_button = Button(text="Get Quote", command=self.get_quote)
        self.text_box.pack()
        self.get_button.pack()

        
    def get_quote(self):
        r = requests.get('https://api.quotable.io/random') 
        data = r.json()
        quote = data['content'] + " -" + data['author']

        #deletes all the text that is currently in the 
        #TextBox
        self.text_box.delete('1.0', END)

        #inserts new data into the TextBox
        self.text_box.insert(END, quote)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Random Quotes')
        self.geometry('410x215')

if __name__ == "__main__":
    app = App()
    Main(app)
    app.mainloop()