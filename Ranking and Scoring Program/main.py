import customtkinter as ctk
import openpyxl
import ranking_module
import config
import scoring_module
from tkinter.filedialog import *

def sub9load():
    app.destroy
    ranking_module.start('9sub')
def sub5load():
    app.destroy
    ranking_module.start('5sub')
def scoring():
    app.destroy
    scoring_module.start()
def setting():
    config.main()

global app
def start():
    global app
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    app = ctk.CTk()
    app.geometry("500x300")
    app.minsize(width=500, height=300)
    app.title("Ranking Program By Anansit")

    label = ctk.CTkLabel(master=app, text="Ranking Program", font=('Arial', 20))
    label.pack()

    frame = ctk.CTkFrame(master=app, height=200)
    frame.pack(padx=100, pady=10, fill='both')

    rank9 = ctk.CTkButton(master=frame, text="9 วิชา", font=('Arial', 20), command=sub9load)
    rank9.grid(column=0,row=0)

    rank5 = ctk.CTkButton(master=frame, text="5 วิชา", font=('Arial', 20), command=sub5load)
    rank5.grid(column=1,row=0,padx=20)
    
    score = ctk.CTkButton(master=app, text='โปรแกรมทำคะแนน', font=('Arial', 20), command=scoring)
    score.pack(pady=10)
    
    set_config = ctk.CTkButton(master=app, text='Setting', font=('Arial', 20), command=setting)
    set_config.pack(pady=25)

    Exit = ctk.CTkButton(master=app, text='Exit', font=('Arial', 25), command=app.destroy)
    Exit.pack(pady=10)
    app.mainloop()
start()