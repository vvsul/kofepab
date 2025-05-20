from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import psycopg2

#Функция подключения к БД

#Функция создания окна просмотра Клиентов
def wclients():
    window = tk.Tk()
    window.title("Клиенты")
    window.geometry("900x300")
    tree = ttk.Treeview(window, column=("c1", "c2", "c3","C4","C5"), show='headings')
    tree.column("#1", anchor=tk.CENTER, width=40)
    tree.heading("#1", text="ID")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Имя")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Фамилия")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Телефон")
    tree.column("#5", anchor=tk.CENTER)
    tree.heading("#5", text="'Эл. почта")
    tree.pack()
    
    button_frame = tk.Frame(window, width=200) 
    button_frame.pack(pady=10) 
    button1 = tk.Button(button_frame,text="Добавить",command=wclientsadd)
    button1.grid(row=1, column=0)
    
    button2 = tk.Button(button_frame,text="Удалить")
    
    button2.grid(row=1, column=1)

   
    
    con=psycopg2.connect(
		host = "81.94.155.134", 
		database = "infuse",
		user = "admin",
		password = "083Hdwd3", 
		port = "5432",
		)
    cur1 = con.cursor()
    cur1.execute("SELECT * FROM clients")
    rows = cur1.fetchall()    
    for row in rows:
        print(row)
        tree.insert("", 'end', values=(row[0],row[1],row[2],row[3],row[4]))        

    con.close()
#функции CRUD для клиента

#функция создания окна добавления клиента
def wclientsadd():
    
    
    windowcladd = tk.Tk()
    windowcladd.title("Добавление клиента")
    windowcladd.geometry("500x400") 
    windowcladd.title("Добавление клиента")
    id = Label(windowcladd, text="ID:", font=("verdana 15"))
    id.place(x=50, y=30)
    id_entry = Entry(windowcladd, font=("verdana 15"))
    id_entry.place(x=150, y=30)
  
    def Insert():
        con=psycopg2.connect(
		host = "81.94.155.134", 
		database = "infuse",
		user = "admin",
		password = "083Hdwd3", 
		port = "5432",
		)
        id = id_entry.get()
        last_name = lname_entry.get()
        first_name= name_entry.get()
        phone = phone_entry.get()
        mal=mail_entry.get()
  
        if(id == "" or name == "" or phone == ""):
            messagebox.showinfo("ALERT", "Заполните все поля!")
        else:
           
            cursor = con.cursor()
            cursor.execute("insert into clients values('" + id +"', '"+ last_name +"', '" + first_name +"', '" + phone +"','" + mal +"')")
            cursor.execute("commit")
  
            messagebox.showinfo("Status", "Запись вставлена")
            con.close();
  
  
    lastname = Label(windowcladd, text="Фамилия:", font=("verdana 15"))
    lastname.place(x=50, y=80)
    lname_entry = Entry(windowcladd, font=("verdana 15"))
    lname_entry.place(x=150, y=80)
    name = Label(windowcladd, text="Имя:", font=("verdana 15"))
    name.place(x=50, y=130)
    name_entry= Entry(windowcladd, font=("verdana 15"))
    name_entry.place(x=150, y=130)
    phone = Label(windowcladd, text="Телефон:", font=("verdana 15"))
    phone.place(x=50, y=180)
    phone_entry= Entry(windowcladd, font=("verdana 15"))
    phone_entry.place(x=150, y=180)
    mail = Label(windowcladd, text="Эл. почта:", font=("verdana 15"))
    mail.place(x=50, y=230)
    mail_entry= Entry(windowcladd, font=("verdana 15"))
    mail_entry.place(x=150, y=230)
    btnInsert = Button(windowcladd, text="Добавить", command=Insert, font=("verdana 15")).place(x=60, y=280)
    btnDelete = Button(windowcladd, text="Удалить",  font=("verdana 15")).place(x=200, y=280)
    btnUpdate = Button(windowcladd, text="Обновить",  font=("verdana 15")).place(x=320, y=280)
    btnSelect= Button(windowcladd, text="Выбрать",  font=("verdana 15")).place(x=200, y=340)
HEIGHT = 300
WIDTH = 500

ws = tk.Tk()
ws.title("Кофейня")
canvas = tk.Canvas(ws, height=HEIGHT, width=WIDTH)
canvas.pack()
main_menu = tk.Menu()
file_menu = tk.Menu()
file_menu.add_command(label="Создать")
file_menu.add_command(label="Сохранить")
file_menu.add_command(label="Открыть")
file_menu.add_separator()
file_menu.add_command(label="Закрыть",command=lambda: ws.destroy())
sprav_menu = tk.Menu()
sprav_menu.add_command(label="Клиенты",command=lambda: wclients())
sprav_menu.add_command(label="Сотрудники")
sprav_menu.add_command(label="Продукты")
sprav_menu.add_separator()
sprav_menu.add_command(label="Скидки")
main_menu.add_cascade(label="Файл",menu=file_menu)

main_menu.add_cascade(label="Справочники",menu=sprav_menu)
main_menu.add_cascade(label="Операции")
main_menu.add_cascade(label="Отчеты")
main_menu.add_cascade(label="Помощь")

ws.config(menu=main_menu)
# определяем данные для отображения

    
ws.mainloop()