from customtkinter import *
from tkinter import ttk
import sv_ttk
from tkinter import font as tkFont

class Application:
    # window
    window = CTk()
    window.title('Alpaca Trading App')
    window.geometry('425x190')

    # style
    s = ttk.Style()
    s.configure('menu.TButton', font=('Futura', 20))
    set_appearance_mode('light')

    # title
    title_label = ttk.Label(master=window, text='Trading Bot', font=('Futura', 50, 'bold'))
    title_label.pack()

    # input field for main selections
    input_frame = ttk.Frame(master=window)

    auto_button = ttk.Button(master=input_frame, text='Automatic Mode', style='menu.TButton')
    manual_button = ttk.Button(master=input_frame, text='Manual Mode', style='menu.TButton')

    auto_button.pack(side='left', padx=10, pady=15)
    manual_button.pack(side='right', padx=10, pady=15)
    input_frame.pack()

    # run
    window.mainloop()
