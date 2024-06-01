from tkinter import *

class PaginaAgendamentos(Frame):
    def __init__(self, master):
        super().__init__(master, bg="#2E8B57", width=600, height=400, padx=50, pady=50)
        self.title = Label(self, text="Agendamentos", bg="#2E8B57", fg = "#FFFAFA")
        self.title["font"] = ("Verdana", "30", "italic", "bold")
        self.title.pack()