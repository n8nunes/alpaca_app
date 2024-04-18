import tkinter as tk
from tkinter import ttk
import sv_ttk

# window
window = tk.Tk()
window.title('Alpaca Trading App')
window.geometry('300x150')

# style
sv_ttk.set_theme('dark')

# title
title_label = ttk.Label(master=window, text='Trading Bot', font='Futura')
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
auto_button = ttk.Button(master=input_frame, text='Automatic Mode')
manual_button = ttk.Button(master=input_frame, text='Manual Mode')
auto_button.pack(side='left')
manual_button.pack(side='right')
input_frame.pack()

# run
window.mainloop()
