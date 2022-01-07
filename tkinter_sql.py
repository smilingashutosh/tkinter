# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 12:07:46 2021

@author: ashutosh
"""

from tkinter import *
from tkinter import messagebox
import sqlite3

with sqlite3.connect("movies.db") as db:
    cursor=db.cursor()
    
cursor.execute("""CREATE TABLE IF NOT EXISTS movies
               ( 
                 title text PRIMARY KEY,
                 genre text NOT NULL,
                 year text NOT NULL,
                 directorname text NOT NULL
               );
               """)
               
def clear():
    data_list1.delete(0,END)
    data_list2.delete(0,END)
    textbox1.delete(0,END)
    textbox2.delete(0,END)
    textbox3.delete(0,END)
    textbox4.delete(0,END)    
    
def savetodb():
    title = textbox1.get()
    genre = textbox2.get()
    year = textbox3.get()
    name = textbox4.get()
    
                
    result = cursor.execute("""SELECT title FROM movies""") 
    for i in result:
        if i[0] == title:
            messagebox.showerror("Error","This movie or series already exists in the database") 
            window.destroy()
            
    cursor.execute("""INSERT INTO movies(title, genre, year, directorname)
                   VALUES(?,?,?,?)""",(title, genre, year, name))
    db.commit()

def showallfromdb():           
            cursor.execute("""SELECT title,"-", genre,"-", year,"-", directorname FROM movies""") 
            for i in cursor.fetchall():
                data_list1.insert(END, i)
   
def savetofiledb():
    title = textbox1.get()
    name = textbox4.get()
    
    outfile = open("movies.txt","a")
    outfile.write(title+"-"+name+"\n")


def showallfromfiledb():
    dispfile = open("movies.txt","r")
    lines = dispfile.readlines()
    for i in lines:
        data_list2.insert(END, i+"\n")
    dispfile.close()
    
window = Tk()
window.geometry("600x800")
window.title("Movies and Series Wish List 2021")

label1 = Label(text = "Enter the title of series or movie:")
label1.place(x = 105, y = 20, width = 200, height = 25)

textbox1 = Entry(text="")
textbox1.place(x = 150, y = 50, width = 200, height = 25)
textbox1.focus()


label2 = Label(text = "Enter the movies/series genre (e.g action,fiction,comedy,etc:")
label2.place(x = 105, y = 80, width = 350, height = 25)

textbox2 = Entry(text="")
textbox2.place(x = 150, y = 110, width = 200, height = 25)

label3 = Label(text = "Enter the year the movie/series was released:")
label3.place(x = 105, y = 140, width = 250, height = 25)

textbox3 = Entry(text="")
textbox3.place(x = 150, y = 170, width = 200, height = 25)

label4 = Label(text = "Enter the full name of the movie/series director:")
label4.place(x = 100, y = 200, width = 280, height = 25)

textbox4 = Entry(text="")
textbox4.place(x = 150, y = 230, width = 200, height = 25)

button1 = Button(text = "Save to DB", command = savetodb)
button1.place(x = 105, y = 260, width = 70, height = 20)

button2 = Button(text = "Save to file", command = savetofiledb)
button2.place(x = 200, y = 260, width = 70, height = 20)

button3 = Button(text = "Clear", command = clear)
button3.place(x = 295, y = 260, width = 70, height = 20)

button4 = Button(text = "Display Movies", command = showallfromdb)
button4.place(x = 30, y = 340, width = 120, height = 20)

label5 = Label(text = "Display all movies/series title,genre and year from the database: ")
label5.place(x = 150, y = 290, width = 350, height = 25)

data_list1 = Listbox()
data_list1.place(x = 150 , y = 310, width = 350, height = 150)

button5 = Button(text = "Display Directors", command = showallfromfiledb)
button5.place(x = 30, y = 550, width = 120, height = 20)

label6 = Label(text = "Display all movies/series' directors from the list: ")
label6.place(x = 150, y = 490, width = 350, height = 25)
data_list2 = Listbox()
data_list2.place(x = 150 , y = 510, width = 350, height = 150)

window.mainloop()

