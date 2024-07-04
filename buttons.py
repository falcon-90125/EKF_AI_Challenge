from tkinter import *
from events_handler import process_pdf_file, process_png_file, selectNomenclature, сommercialOffer, co_to_pdf

button_bg="lightgrey"
button_fg="blue"
button_font=('Calibri', 15, 'bold')
button_width=25
button_height=2
relx=525

def btnProcessPDF(parent, canvas):
    btn_increase = Button(                                   # Создание виджета кнопки
        master=parent,
        text="Обработать PDF",
        command=process_pdf_file,
        bg=button_bg,
        fg=button_fg,
        font=button_font,
        width=button_width,
        height=button_height
    )
    canvas.create_window(
        relx,
        110, 
        anchor = "w",
        window = btn_increase
        )

def btnDnldPNG(parent, canvas):
    btn_increase = Button(                                   # Создание виджета кнопки
        master=parent,
        text="Загрузить и распознать PNG",
        command=process_png_file,
        bg=button_bg,
        fg=button_fg,
        font=button_font,
        width=button_width,
        height=button_height
    )
    canvas.create_window(
        relx,
        220, 
        anchor = "w",
        window = btn_increase
        )

def btnSelectNomenclature(parent, canvas):
    btn_increase = Button(                                   # Создание виджета кнопки
        master=parent,
        text="Подобрать номенклатуру",
        command=selectNomenclature,
        bg=button_bg,
        fg=button_fg,
        font=button_font,
        width=button_width,
        height=button_height
    )
    canvas.create_window(
        relx,
        330, 
        anchor = "w",
        window = btn_increase
        )

def btnCommercialOffer(parent, canvas):
    btn_increase = Button(                                   # Создание виджета кнопки
        master=parent,
        text="Сформировать КП",
        command=сommercialOffer,
        bg=button_bg,
        fg=button_fg,
        font=button_font,
        width=button_width,
        height=button_height
    )
    canvas.create_window(
        relx,
        440, 
        anchor = "w",
        window = btn_increase
        )

def btnCOToPDF(parent, canvas):
    btn_increase = Button(                                   # Создание виджета кнопки
        master=parent,
        text="Выгрузть КП в PDF",
        command=co_to_pdf,
        bg=button_bg,
        fg=button_fg,
        font=button_font,
        width=button_width,
        height=button_height
    )
    canvas.create_window(
        relx,
        550, 
        anchor = "w",
        window = btn_increase
        )
