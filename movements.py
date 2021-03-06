import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from babel.dates import format_date
from tkcalendar import Calendar
import settings
import data_base as db

class MovementFrame(tk.Frame):
    def __init__(self, parent, mov_type, update_labels, **kwargs) -> None:
        super().__init__(parent, **kwargs)
        self.mov_type = mov_type
        self.update_labels = update_labels

        self.calendar = Calendar(self, date_pattern="yyyy-mm-dd")
        self.quantity_entry = tk.Entry(self, width=20)

        self.combo_categories = ttk.Combobox(self, state="readonly", values=settings.categories_list)
        self.combo_categories.current(0)
        self.combo_categories.bind('<<ComboboxSelected>>', self.select_subcategory)

        self.combo_sub_categories = ttk.Combobox(self, state="readonly", values=settings.sub_categories_list["Nómina"])
        self.combo_sub_categories.current(0)

        self.movement_button = ttk.Button(
            self, 
            style="TButton",
            text=self.mov_type.capitalize(),
            command= self.movimiento_clicked
        )

        self.quantity_entry.grid(row=0, column=0)
        self.combo_categories.grid(row=1,column=0)
        self.combo_sub_categories.grid(row=2,column=0)
        self.movement_button.grid(row=3, column=0)

    def select_subcategory(self, e=None):
        '''Cambia la lista de valores del combo de subcategorías en función del valor que tenga seleccionado
            el combo de categorías.'''

        self.combo_sub_categories.config(values=settings.sub_categories_list[self.combo_categories.get()])
        self.combo_sub_categories.current(0)

    def movimiento_clicked(self):
        '''Introduce un movimiento en la base de datos con la fecha seleccionada en el calendario, la cantidad del
            Entry y la categoría y subcategoría del combo respectivo, si se le da a aceptar al messagebox que sale.
            Si se cancela el messagebox no hace nada. En caso de que haya un error durante la inserción del movimiento
            muestra un aviso de error. Utiliza el método data_entry() de data_base.py para introducir el movimiento.'''

        date = self.calendar.get_date()
        quantity = self.quantity_entry.get()
        category = self.combo_categories.get()
        subcategory = self.combo_sub_categories.get()
        confirmation = messagebox.askyesno(message=f"¿Confirmar {self.mov_type} de {quantity} €?\n\n\nCategoría: {category}\nSubcategoría: {subcategory}", title="Añadir movimiento")

        if confirmation:
            try:   
                quantity_float = float(quantity.replace(",","."))
                db.data_entry(date, self.mov_type, quantity_float, category, subcategory)
                self.update_labels()
                #self.lbl_movimiento.grid(row=4, column=1, pady=10)
                #self.lbl_movimiento.after(750, self.lbl_movimiento.grid_forget)
                self.quantity_entry.delete(0,"end")
        
            except:
                tk.messagebox.showwarning(message="El valor no es correcto", title="Error")
