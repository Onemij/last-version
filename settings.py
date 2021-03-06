from tkinter import ttk

#----Fonts----#
FONT_FAMILY = "Arial Bold"
FONT_SIZE = 12

#----Paddings----#
LABEL_PADDING = 5

#----Colors----#
BACKGROUND_COLOR = "#8cce7c"
PROGRESSBAR_COLOR = "#006400"

#----Styles----#
def define_styles():
    '''Define los estilos'''

    style = ttk.Style()
    style.theme_use('clam')
    
    #Configura el estilo de las progressbar de ingresos y gastos
    style.configure(
        "TProgressbar",
        troughcolor=BACKGROUND_COLOR,
        background=PROGRESSBAR_COLOR,
        bordercolor=BACKGROUND_COLOR,
        darkcolor=PROGRESSBAR_COLOR,
        lightcolor=PROGRESSBAR_COLOR
    )
    style.configure(
        "Onemij.TButton",
        troughcolor=BACKGROUND_COLOR,
        background=PROGRESSBAR_COLOR,
        bordercolor=BACKGROUND_COLOR,
        darkcolor=PROGRESSBAR_COLOR,
        lightcolor=PROGRESSBAR_COLOR,
        width=25
    )
    style.configure(
        "Back.Onemij.TButton",
        troughcolor="white",
        background="red",
        bordercolor="red",
        darkcolor="red",
        lightcolor="red"
    )
    style.configure(
        "Onemij.TLabel",
        background="yellow",
        width=15,
        padding=(5,5,5,5),
        anchor="center"
    )

categories_list = [
    "Nómina",
    "Ingresos no nómina",
    "Transportes y viajes",
    "Seguros",
    "Salud",
    "Ocio",
    "Casa",
    "Efectivo y pagos",
    "Educación",
    "Compras",
    "Otros",
]
sub_categories_list = {
    "Nómina" : ["Nómina"],
    "Ingresos no nómina" : ["Ingresos no nómina"],
    "Transportes y viajes" : ["Combustible", "Avión, tren o barco", "Hoteles", "Peajes", "Viajes"],
    "Seguros" : ["Salud", "Coche", "Otros"],
    "Salud" : ["Farmacia", "Consultas y hospitales", "Otros"],
    "Ocio" : ["Bares y restaurantes", "Espectáculos", "Otros"],
    "Casa" : ["Electricidad", "Teléfono e internet", "Otros"],
    "Efectivo y pagos" : ["Retirada de cajero", "Pagos Bizum", "Otros"],
    "Educación" : ["Cursos", "Otros"],
    "Compras" : ["Alimentación", "Decoración", "Electrónica", "Ropa", "Belleza", "Otros"],
    "Otros" : ["Otros"],
}

switch_categories = {
    1 : "Nómina",
    2 : "Ingresos no nómina",
    3 : "Transportes y viajes",
    4 : "Seguros",
    5 : "Salud",
    6 : "Ocio",
    7 : "Casa",
    8 : "Efectivo y pagos",
    9 : "Educación",
    10 : "Compras",
    0 : "Otros",
}
switch_subcategories = [
    {},
    {},
    {1 : "Combustible", 2 : "Avión, tren o barco", 3 : "Hoteles", 4 : "Peajes", 5 : "Viajes",},
    {1 : "Salud", 2 : "Coche", 3 : "Otros",},
    {1 : "Farmacia", 2 : "Consultas y hospitales", 3 : "Otros",},
    {1 : "Bares y restaurantes", 2 : "Espectáculos", 3 : "Otros",},
    {1 : "Electricidad", 2 : "Teléfono e internet", 3 : "Otros",},
    {1 : "Retirada de cajero", 2 : "Pagos Bizum", 3 : "Otros",},
    {1 : "Cursos", 2 : "Otros",},
    {1 : "Alimentación", 2 : "Decoración", 3 : "Electrónica", 4 : "Ropa", 5 : "Belleza", 6 : "Otros"},
]

def translate_month(month):
    months = {
        "January": "Enero",
        "February": "Febrero",
        "March": "Marzo",
        "April": "Abril",
        "May": "Mayo",
        "June": "Junio",
        "July": "Julio",
        "August": "Agosto",
        "September": "Septiembre",
        "October": "Octubre",
        "November": "Noviembre",
        "December": "Diciembre",
    }
    return months[month]