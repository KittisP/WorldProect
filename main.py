import tkinter.ttk as ttk
import tkinter
from tkinter import *
import sqlite3
from Mass import x

#Создали файл базы данных и подключились к нему
base = sqlite3.connect('bases.db')
cur = base.cursor()


win = Tk()                                      # Создаем окошко
win.geometry('1000x500+250+250')                # задаем размеры окна и коорд где будет выскакивать
win.title('Глобус!')                            # Называем наше приложение
win.resizable(False, False)                     # Запрещаем менять размеры окна
win["bg"] = "#0096E1"                           # Задаем цвет фона окна

# Выводим базу данных в окно приложения
table= ttk.Treeview(win, column=("column1", "column2", "column3"), show='headings')
table.heading("#1", text="Страна")
table.heading("#2", text="Столица")
table.heading("#3", text="Национальная валюта")
table.place(x=100, y=170, width=800, height=200)

# Добавляем икноку окна глобус
Logo = PhotoImage(file='glob.png')
win.iconphoto(False, Logo)



# Делаем окно ввода

vvod = Entry()
vvod.place(x=350, y=80, width=300, height=30)


# Функция для кнопки Отразить всё

def View():
    cur.execute("SELECT * FROM globe")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        table.insert("", tkinter.END, values=row)

# Функция для кнопки Поиска. Связываем поисковик и кнопку поиска

def Search():
    word = vvod.get()
    result = ('%' + word + '%',)
    cur.execute('''SELECT * FROM globe WHERE Country LIKE ?''',result)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    table.insert("", tkinter.END, values=row)


# Функция для кнопки Очистить
def Delete():
    [table.delete(i) for i in table.get_children()]


#Создаем наши кнопки
b1 = Button(win, text= "Показать всё", command=View,bg="#6B96E1", font =("Times New Roman",15),fg='#000000' )
b1.place(x=150, y=400, width=150, height=30)

b2 = Button(win, text= "Найти столицу", command=Search,bg="#6B96E1", font =("Times New Roman",15),fg='#000000' )
b2.place(x=400, y=400, width=200, height=50)

b3 = Button(win, text= "Очистить", command=Delete,bg="#6B96E1", font =("Times New Roman",15),fg='#000000' )
b3.place(x=680, y=400, width=150, height=30)

#Создаем надпись сверху
advice = tkinter.Label(win, text="Введите название страны", font =("Times New Roman",17, 'bold'),fg='#000000', bg ="#0096E1")
advice.place(x=350, y=30, width=300, height=50)



# Создаем нашу базу данных с использованием массива под назваением x из файла Mass
'''
base.execute('CREATE TABLE IF NOT EXISTS {}(Country PRIMARY KEY,Capital,National currency)'.format('globe'))
base.commit()

cur.executemany('INSERT INTO globe VALUES(?, ?, ?)', (x))
base.commit()
'''
# Проверка запросов
'''
open = cur.execute('SELECT * FROM globe').fetchall()
print(open)

open = cur.execute('SELECT Country FROM globe').fetchall()
print(open)

open = cur.execute('SELECT Capital FROM globe').fetchall()
print(open)

open = cur.execute('SELECT National currency FROM globe').fetchall()
print(open)

open = cur.execute('SELECT Capital, National currency FROM globe WHERE Country ==?', ('США',)).fetchone()
print(open)
'''

win.mainloop() # запускает приложение