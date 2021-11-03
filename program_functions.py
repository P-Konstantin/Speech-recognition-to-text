# Библиотека для распознования речи
import speech_recognition as sr


# Библиотека для перевода текста в речь
import pyttsx3


def speech(phrase):
    '''Функция общения с пользователем.'''

    # Инициализация модуля
    engine = pyttsx3.init()
    # Функция воспроизвоит фразу для пользователя
    engine.say(phrase)
    # Функция запускаетя и переходит в режим ожидания
    engine.runAndWait()


def recognition():
    '''Функция распознования речи в текст.'''

    # Объект класса Recognizer для преобразования звука в текст
    recog = sr.Recognizer()

    # Объект класса Microphone для захвата звука с микрофона
    mic = sr.Microphone()

    # Делаем микрофон источником звука
    with mic as source:
        # Применяем метод adjust_for_ambient_noise() класса Recognizer для уменьшения шума
        recog.adjust_for_ambient_noise(source)
        # Захватываем звук с источника звука(микрофона)
        audio = recog.listen(source)
        # Распознаем речь из источника(микрофона)
        text = recog.recognize_google(audio, language="ru-Ru")

    return text


def dot():
    '''Функция, возвращающая точку.'''
    dot = '.'
    return dot


def comma():
    '''Функция, возвращающая запятую.'''
    comma = ','
    return comma


def colon():
    '''Функция, возвращающая двоеточие.'''
    colon = ':'
    return colon


def semicolon():
    '''Функция, возвращающая точку с запятой.'''
    semicolon = ';'
    return semicolon


def quotes():
    '''Функция, возвращающая кавычки.'''
    quotes = '"'
    return quotes


def left_parenthesis():
    '''Функция, возвращающая левую скобку.'''
    left_parenthesis = '('
    return left_parenthesis


def right_parenthesis():
    '''Функция, возвращающая правую скобку.'''
    right_parenthesis = ')'
    return right_parenthesis


def question_mark():
    '''Функция, возвращающая "?".'''
    question_mark = '?'
    return question_mark


def exclamation_mark():
    '''Функция, возвращающая "!".'''
    exclamation_mark = '!'
    return exclamation_mark