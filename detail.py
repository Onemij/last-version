import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from typing import Collection
from babel.dates import format_date
from tkcalendar import Calendar
import settings
import data_base as db

class DetailButtonsFrame(tk.Frame):
    def __init__(self, master, mov_type) -> None:
        super().__init__()
        category_buttons = {}
        category_total_labels = {}
        self.master = master
        self.mov_type = mov_type
        back_button = ttk.Button(self, text="Atrás", style='Back.Onemij.TButton', command=self.back)
        back_button.grid(row=0, column=0)

        for category in settings.categories_list:
            category_buttons[category] = ttk.Button(self,
                                                    text=category,
                                                    style='Onemij.TButton',
                                                    command=lambda cat=category: self.view_category_detail(cat))
            category_total_labels[category] = ttk.Label(self,
                                                        text=db.get_total(self.mov_type, category=category, currency_symbol=True),
                                                        style='Onemij.TLabel')
            if db.get_total(self.mov_type, category=category):
                category_buttons[category].grid(row=len(category_buttons), column=0)
                category_total_labels[category].grid(row=len(category_buttons), column=1)
    
    def back(self):
        self.destroy()
        self.master.grid_widgets_master_frame_init()
    
    def view_category_detail(self, category):
        detail_frame = DetailFrame(self, mov_type=self.mov_type, category=category)
        self.grid_forget()
        detail_frame.grid(row=0, column=0)

class DetailFrame(tk.Frame):
    def __init__(self, master, mov_type, category) -> None:
        super().__init__()
        
        self.master = master

        back_button = ttk.Button(self, text="Atrás", style='Back.Onemij.TButton', command=self.back)
        back_button.grid(row=0, column=0)
        lbl = ttk.Label(self, text=category)
        lbl2 = ttk.Label(self, text=db.get_total(mov_type=mov_type, category=category,currency_symbol=True))
        lbl.grid(row=1, column=0)
        lbl2.grid(row=2, column=0)

        
    def back(self):
        self.destroy()
        self.master.grid(row=0, column=0)