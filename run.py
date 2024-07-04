from tkinter import *
from PIL import ImageTk, Image
from buttons import btnProcessPDF, btnDnldPNG, btnSelectNomenclature, btnCommercialOffer, btnCOToPDF
from events_handler import lebel_text_color, lebel_text_font


root = Tk()  # Создание объекта Tk()
root.title("Нейросервис: формирование коммерческого предложения на основе электрических схем")
root.geometry('800x600')
root.resizable(width=False, height=False)

# Фон
bg = ImageTk.PhotoImage(Image.open("app_exchenge/image_app/background.png"))
canvas1 = Canvas(root, width = 800, height = 600)
canvas1.pack()
canvas1.create_image(0, 0, image = bg, anchor = "nw")

# Логотип EKF
logo = ImageTk.PhotoImage(Image.open("app_exchenge/image_app/logo_ekf.png"))
canvas1.pack()
canvas1.create_image(7, 5, image = logo, anchor = "nw")

# Описание
Label(text='''Нейросервис обрабатывает файлы электрических схем в формате PNG,\nс возможностью предобработки файлов проектной документации в формате PDF.\nФормирует коммерческое предложение на основании обнаруженных данных''',
      fg=lebel_text_color, font=(lebel_text_font, 11, 'bold')).place(relx=0.63, rely=0.058, anchor="center", width=557, height=57)


# Кнопки
btnProcessPDF(root, canvas1)
btnDnldPNG(root, canvas1)
btnSelectNomenclature(root, canvas1)
btnCommercialOffer(root, canvas1)
btnCOToPDF(root, canvas1)



# Запускаем главный цикл обработки событий
root.mainloop()