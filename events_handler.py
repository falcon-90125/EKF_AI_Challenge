from tkinter import *
from tkinter import filedialog
from PIL import Image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import PIL.ImageOps #модуль для инверсии цветов
import numpy as np
import fitz

model = load_model('app_exchenge/model.h5')

# Параметры лейблов
lebel_size_w=500
lebel_size_h=65
lebel_place_x = 0.328
lebel_place_y = 0.182
lebel_text_size = 13
lebel_text_color = 'blue'
lebel_text_font = 'Calibri'

# Преобразование PDF в PNG
def process_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF", "*.pdf")])  # Открываем диалоговое окно выбора файла
    if file_path:  # Если файл был выбран
        file_name = file_path[[index for index, slesh in enumerate(file_path) if slesh == '/'][-1]+1:] # Имя файла для уведомления
        doc = fitz.open(file_path) # Открыть документ
        dpi = 500 # Указать разрешение DPI для сохранения с высоким разрешением

        for i, page in enumerate(doc):
            pix = page.get_pixmap(matrix=fitz.Matrix(dpi/72, dpi/72))
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            output_path = f"app_exchenge/processed_files/page_{i + 1}.png"
            img.save(output_path, format="PNG")

        doc.close()

    Label(text=f'Файл {file_name} успешно загружен.\nКонвертировано в PNG листов: {i+1}',
            fg=lebel_text_color, font=(lebel_text_font, lebel_text_size, 'bold'))\
                .place(relx=lebel_place_x, rely=lebel_place_y, anchor="center", width=lebel_size_w, height=lebel_size_h)


def process_png_file():
    global image_data
    file_path = filedialog.askopenfilename(filetypes=[("PNG", "*.png")])  # Открываем диалоговое окно выбора файла
    if file_path:  # Если файл был выбран
        # image = Image.open(file_path)
        # image_data = image.tobytes()
        file_name = file_path[[index for index, slesh in enumerate(file_path) if slesh == '/'][-1]+1:] # Имя файла для уведомления
        image_test = image.load_img(file_path, target_size=(28, 28), color_mode = 'grayscale')
        image_inv = PIL.ImageOps.invert(image_test) #инверсия цветов
        image_test_np = image.img_to_array(image_inv) #преобразуем изображение в numpy-массив
        image_test_resh = image_test_np.reshape(1, 784) #Меняем формат тестовой картинки с 28х28 на 784х1
        image_test_fin = image_test_resh / 255 # Нормализуем входную картинку, делим на 255, чтобы диапазон был от 0 до 1
        prediction = model.predict(image_test_fin) #Распознаём наш пример
        pred = np.argmax(prediction) # Получаем индекс самого большого элемента (это итоговая цифра, которую распознала сеть)

        n = 12
        v = 54

        Label(text=f'Файл {file_name} успешно обработан.\nНайдено элементов - {n}, общее количество - {v}, в том числе:',
                fg=lebel_text_color, font=(lebel_text_font, lebel_text_size, 'bold'))\
                    .place(relx=lebel_place_x, rely=lebel_place_y, anchor="center", width=lebel_size_w, height=lebel_size_h)
        
        Label(text=f'Распознана цифра: {pred}',
                fg=lebel_text_color, font=(lebel_text_font, lebel_text_size, 'bold'), anchor="nw")\
                    .place(relx=lebel_place_x, rely=lebel_place_y+0.435, anchor="center", width=lebel_size_w, height=lebel_size_h+363)


def selectNomenclature():
    Label(text='Сработала selectNomenclature',
        fg=lebel_text_color, font=(lebel_text_font, lebel_text_size, 'bold'))\
            .place(relx=lebel_place_x, rely=lebel_place_y, anchor="center", width=lebel_size_w, height=lebel_size_h)


def сommercialOffer():
    Label(text='Сработала сommercialOffer',
    fg=lebel_text_color, font=(lebel_text_font, lebel_text_size, 'bold'))\
        .place(relx=lebel_place_x, rely=lebel_place_y, anchor="center", width=lebel_size_w, height=lebel_size_h)


def co_to_pdf():
    Label(text='Сработала co_to_pdf',
    fg=lebel_text_color, font=(lebel_text_font, lebel_text_size, 'bold'))\
        .place(relx=lebel_place_x, rely=lebel_place_y, anchor="center", width=lebel_size_w, height=lebel_size_h)