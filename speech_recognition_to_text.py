# Основной файл программы
# Здесь создается окно программы и её виджеты
# Вызываются функции работы программы


# Библиотека для создания графического интерфейса
from tkinter import Tk, Button, Label, scrolledtext, END


# Библиотека для работы с изображениями
from PIL import ImageTk


# Функции для распознования речи в текст и текста в речь
# Функции для вывода знаков препинания
from program_functions import recognition, speech, dot, comma, colon, semicolon
from program_functions import quotes, left_parenthesis, right_parenthesis
from program_functions import question_mark, exclamation_mark


def working():
    '''Функция запуска работы программы.'''
    output.configure(state='normal')  # Разрешаем ввод
    output.insert(END, recognition())
    output.yview(END)  # Включаем автоскроллинг


def press_dot():
    '''Функция, выводящая "." при нажатии кнопки.'''
    output.configure(state='normal')
    output.insert(END, dot())
    output.yview(END)


def press_comma():
    '''Функция, выводящая "," при нажатии кнопки.'''
    output.configure(state='normal')
    output.insert(END, comma())
    output.yview(END)


def press_colon():
    '''Функция, выводящая ":" при нажатии кнопки.'''
    output.configure(state='normal')
    output.insert(END, colon())
    output.yview(END)


def press_semicolon():
    '''Функция, выводящая ";" при нажатии кнопки.'''
    output.configure(state='normal')
    output.insert(END, semicolon())
    output.yview(END)


def press_quotes():
    '''Функция, выводящая кавычки при нажатии кнопки.'''
    output.configure(state='normal')
    output.insert(END, quotes())
    output.yview(END)


def press_left_parenthesis():
    '''Функция, выводящая "(" при нажатии кнопки.'''
    output.configure(state='normal')
    output.insert(END, left_parenthesis())
    output.yview(END)


def press_right_parenthesis():
    '''Функция, выводящая ")" при нажатии кнопки.'''
    output.configure(state='normal')
    output.insert(END, right_parenthesis())
    output.yview(END)


def press_question_mark():
    '''Функция, выводящая "?" при нажатии кнопки.'''
    output.configure(state='normal')
    output.insert(END, question_mark())
    output.yview(END)


def press_exclamation_mark():
    '''Функция, выводящая "!" при нажатии кнопки.'''
    output.configure(state='normal')
    output.insert(END, exclamation_mark())
    output.yview(END)


# Создаем окно для программы
window = Tk()
# Заголовок программы
window.title('Speech Recognition to Text')
# Задаем размер окна
window.geometry('920x480')
# Задаем цвет окна
window['bg'] = 'LightSkyBlue1'


# Создаем надпись
lb1 = Label(window, text='Здравствуйте, эта программа преобразует вашу речь в текст. '
                         'Нажмите на кнопу "Распознование речи" и говорите в ')
# Задаем расположение надписи
lb1.place(x=10, y=10)
# Задаем цвет надписи
lb1['bg'] = 'LightSkyBlue1'


lb2 = Label(window, text='микрофон, программа начнет работать. Если вам нужно отредактировать '
                         'полученный текст, можете воспользоваться ')
lb2.place(x=10, y=30)
lb2['bg'] = 'LightSkyBlue1'


lb3 = Label(window, text='кнопками или клавиатурой. Вы так же можете '
                         'скопировать полученный вами результат в какой-либо текстовый файл.')
lb3.place(x=10, y=50)
lb3['bg'] = 'LightSkyBlue1'


# Создаем кнопку
btn1 = Button(window, text='Распознование речи', height=2, width=20, command=working)
# Задаем расположение кнопки
btn1.place(x=718, y=275)


btn2 = Button(window, text='.', height=2, width=10, command=press_dot)
btn2.place(x=675, y=335)


btn3 = Button(window, text=',', height=2, width=10, command=press_comma)
btn3.place(x=755, y=335)


btn4 = Button(window, text=':', height=2, width=10, command=press_colon)
btn4.place(x=835, y=335)


btn5 = Button(window, text=';', height=2, width=10, command=press_semicolon)
btn5.place(x=675, y=375)


btn6 = Button(window, text='"', height=2, width=10, command=press_quotes)
btn6.place(x=755, y=375)


btn7 = Button(window, text='(', height=2, width=10, command=press_left_parenthesis)
btn7.place(x=835, y=375)


btn8 = Button(window, text=')', height=2, width=10, command=press_right_parenthesis)
btn8.place(x=675, y=415)


btn9 = Button(window, text='?', height=2, width=10, command=press_question_mark)
btn9.place(x=755, y=415)


btn10 = Button(window, text='!', height=2, width=10, command=press_exclamation_mark)
btn10.place(x=835, y=415)


# Создаем поле для вывода текста
output = scrolledtext.ScrolledText(window, state='normal')
# Задаем расположение поля вывода
output.place(x=10, y=70)


# Открываем изображение
image = ImageTk.PhotoImage(file='images\mikrofon.png')
# Помещаем изображение в tkinter
picture = Label(window, image=image)
# Задаем расположение картинки
picture.place(x=680, y=20)
# Задаем цвет вокруг изображения
picture['bg'] = 'LightSkyBlue1'


# Приветствуем пользователя
speech("Здравствуйте, я вас слушаю")


# Создаем бесконечный цикл для отображения окна программы
window.mainloop()


# Прощаемся с пользователем, если он выходит из программы
speech("До свидания")