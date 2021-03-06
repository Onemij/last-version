from datetime import date
import tkinter as tk
from tkinter import Button, ttk
import data_base as db
import settings, movements, detail


class FinancesApplication(tk.Tk):
    '''Aplicación de control de finanzas personales.'''
    def __init__(self):
        super().__init__()
        #Se crea, si no existe ya, la base de datos.
        db.create_table()

        #Se crean las variables que muestran el total de ingresos o gastos del mes
        self.income = tk.StringVar(value=db.get_total("ingreso", currency_symbol=True))
        self.expense = tk.StringVar(value=db.get_total("gasto", currency_symbol=True))
        
        self.define_widgets()
        settings.define_styles()
        self.grid_widgets_master_frame_init()
        self.bind_widgets()
  
    def define_widgets(self):
        '''Inicializa todos los widgets que utiliza la aplicación'''

        #Frames principales de la aplicación
        self.master_frame = tk.Frame(self)
        self.master_income_frame = tk.Frame(self.master_frame)
        self.master_expense_frame = tk.Frame(self.master_frame)


        #Etiqueta con el mes actual
        self.month_label = tk.Label(self.master_frame, font=(settings.FONT_FAMILY, settings.FONT_SIZE), text=str(settings.translate_month(date.today().strftime("%B"))))
        
        #Etiquetas de ingresos y gastos: título y valor de los del mes actual obtenidos con db.get_total()
        self.income_label = tk.Label(self.master_income_frame, font=(settings.FONT_FAMILY, settings.FONT_SIZE), text='Ingresos')
        self.income_number_label = tk.Label(self.master_income_frame, 
                                            font=(settings.FONT_FAMILY, settings.FONT_SIZE),
                                            textvariable=self.income)
        self.expense_label =  tk.Label(self.master_expense_frame, font=(settings.FONT_FAMILY, settings.FONT_SIZE), text='Gastos')
        self.expense_number_label = tk.Label(self.master_expense_frame,
                                             font=(settings.FONT_FAMILY,
                                             settings.FONT_SIZE),
                                             textvariable=self.expense)
        #Progress bar de ingresos y gastos, la de gastos muestra el porcentaje de ingresos gastados este mes
        self.income_bar = ttk.Progressbar(self.master_income_frame, style="TProgressbar", orient ="horizontal", length=480, mode="determinate")    
        self.expense_bar = ttk.Progressbar(self.master_expense_frame, style="TProgressbar", orient ="horizontal", length=480, mode="determinate")
        #Si no hay ingresos, las inicializa a cero para evitar la división por cero del cálculo del porcentaje de la barra de gastos.
        if db.get_total("ingreso") == 0:
            self.income_bar.config(value=0)
            self.expense_bar.config(value=0)
        else:
            self.income_bar.config(value=100)    
            self.expense_bar.config(value=db.get_total("gasto")/db.get_total("ingreso")*100)

        #Panel de pestañas para introducir un nuevo movimiento. Utiliza un frame (MovementFrame) diferente para cada tipo de movimiento
        self.notebook = ttk.Notebook(self)
        self.income_frame = movements.MovementFrame(parent=self.notebook, mov_type="ingreso", update_labels=self.update_labels)
        self.expense_frame = movements.MovementFrame(parent=self.notebook, mov_type="gasto", update_labels=self.update_labels)
        self.refund_frame = movements.MovementFrame(parent=self.notebook, mov_type="devolucion", update_labels=self.update_labels)
        #Se añaden los frames al panel de pestañas
        self.notebook.add(self.income_frame, text="Ingreso", padding=20)
        self.notebook.add(self.expense_frame, text="Gasto", padding=20)
        self.notebook.add(self.refund_frame, text="Devolución", padding=20)

    def grid_widgets_master_frame_init(self):
        '''Coloca los widgets en el frame master en la forma inicial del programa'''

        #Frames principales, master_income master_expense están dentro de master_frame
        self.master_frame.grid(row=0, column=0)

        #En la row 0 de master_frame va month_label, por eso empiezan en 1
        self.master_income_frame.grid(row=1, column=0, padx=20, pady=5)
        self.master_expense_frame.grid(row=2, column=0, padx=20, pady=5)

        #Row 0 de master_frame
        self.month_label.grid(row=0, column=0, columnspan=2, pady=15)

        #Row 0 de master_income_frame
        self.income_label.grid(row=0, column=0)
        self.income_number_label.grid(row=0, column=1)
        #Row 1 de master_income_frame
        self.income_bar.grid(row=1, column=0, columnspan=2)

        #Row 0 de master_expense_frame
        self.expense_label.grid(row=0, column=0)
        self.expense_number_label.grid(row=0, column=1)
        #Row 1 de master_expense_frame
        self.expense_bar.grid(row=1, column=0, columnspan=2)

        #Row 3 de master_frame
        self.notebook.grid(row=3, column=0, columnspan=2, pady=30)


    def update_labels(self):
        self.income.set(db.get_total("ingreso", currency_symbol=True))
        self.expense.set(db.get_total("gasto", currency_symbol=True))
        self.income_bar.config(value=100)    
        self.expense_bar.config(value=db.get_total("gasto")/db.get_total("ingreso")*100)

    def detail_window(self, e=None, mov_type=""):
        self.master_frame.grid_forget()
        self.notebook.grid_forget()
        detail_frame = detail.DetailButtonsFrame(self, mov_type)
        detail_frame.grid(row=0, column=0)

    def bind_widgets(self):
        self.master_income_frame.bind('<Button-1>', lambda e: self.detail_window(e=e, mov_type="ingreso"))
        self.master_expense_frame.bind('<Button-1>', lambda e: self.detail_window(e=e, mov_type="gasto"))

        for widget in self.master_income_frame.winfo_children():
            widget.bind('<Button-1>', lambda e: self.detail_window(e=e, mov_type="ingreso"))
            
        for widget in self.master_expense_frame.winfo_children():
            widget.bind('<Button-1>', lambda e: self.detail_window(e=e, mov_type="gasto"))



if __name__ == "__main__":
    finances_app = FinancesApplication()
    finances_app.mainloop()