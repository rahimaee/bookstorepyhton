from tkinter import *
import back
def Clear_ls1():
    ls1.delete(0,END)

def Fill_ls1(books):
    for book in books:
        ls1.insert(END,book)


Window = Tk("BookStore")
# Labels
l1 = Label(Window, text="title")
l1.grid(row=0, column=0)
l2 = Label(Window, text="Author")
l2.grid(row=0, column=2)
l3 = Label(Window, text="Year")
l3.grid(row=1, column=0)
l4 = Label(Window, text="ISBN")
l4.grid(row=1, column=2)

# Entries
title_text = StringVar()
e1 = Entry(Window, textvariable=title_text)
e1.grid(row=0, column=1)

Author_text = StringVar()
e2 = Entry(Window, textvariable=Author_text)
e2.grid(row=0, column=3)

Year_text = StringVar()
e3 = Entry(Window, textvariable=Year_text)
e3.grid(row=1, column=1)

ISBN_text = StringVar()
e4 = Entry(Window, textvariable=ISBN_text)
e4.grid(row=1, column=3)

ls1 = Listbox(Window, width=35, height=6)
ls1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(Window)
sb1.grid(row=2, column=2, rowspan=6)

ls1.configure(yscrollcommand=sb1.set)
sb1.configure(command=ls1.yview)
#Event list

def get_select_row(event):
    global select_book
    if len(ls1.curselection())>0:
        index_Iteam = ls1.curselection()[0]
        select_book = ls1.get(index_Iteam)
        # title
        e1.delete(0, END)
        e1.insert(END, select_book[1])
        # author
        e2.delete(0, END)
        e2.insert(END, select_book[2])
        # year
        e3.delete(0, END)
        e3.insert(END, select_book[3])
        # isbn
        e4.delete(0, END)
        e4.insert(END, select_book[4])

ls1.bind("<<ListboxSelect>>",get_select_row)

def view_command():
    Clear_ls1()
    books = back.view()
    Fill_ls1(books)

btn1 = Button(Window, text="View All", width=12,command = lambda :view_command())
btn1.grid(row=2, column=3)

def Search_command():
    Clear_ls1()
    books = back.Search(title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get())
    Fill_ls1(books)

btn2 = Button(Window, text="Search Entry", width=12,command=Search_command)
btn2.grid(row=3, column=3)

def Add_command():
    back.insert(title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get())
    view_command()

btn3 = Button(Window, text="Add Entry", width=12,command=Add_command)
btn3.grid(row=4, column=3)

def Update_command():
    back.Update(select_book[0],title_text.get(),Author_text.get(),Year_text.get(),ISBN_text.get())
    view_command()
btn4 = Button(Window, text="Update selected", width=12,command=Update_command)
btn4.grid(row=5, column=3)

def Delete_command():
    back.Delete(select_book[0])
    view_command()

btn5 = Button(Window, text="Delete Book", width=12,command=Delete_command)
btn5.grid(row=6, column=3)

def Exit_command():
    Window.destroy()

btn6 = Button(Window, text="Exit", width=12,command=Exit_command)
btn6.grid(row=7, column=3)

#app
view_command()
Window.mainloop()