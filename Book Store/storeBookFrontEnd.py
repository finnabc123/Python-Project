from tkinter import *
from storeBookBackEnd import Database

database = Database()

def getSelectedRow(event):
    try:
        global selectedTupple
        index = list1.curselection()[0]
        selectedTupple = list1.get(index)
        e1.delete(0,END)
        e1.insert(0,selectedTupple[1])
        e2.delete(0,END)
        e2.insert(END,selectedTupple[2])
        e3.delete(0,END)
        e3.insert(END,selectedTupple[3])
        e4.delete(0,END)
        e4.insert(END,selectedTupple[4])
    except IndexError:
        pass
def viewAllCommand():
    list1.delete(0, END)
    for row in database.view():
        list1.insert(END, row)

def searchCommand():
    list1.delete(0, END)
    for row in database.search(titleText.get(), authorText.get(), yearText.get(), isbnText.get()):
        list1.insert(END, row)

def addCommand():
    database.insert(titleText.get(), authorText.get(), yearText.get(), isbnText.get())
    list1.delete(0, END)
    list1.insert(END, (titleText.get(), authorText.get(), yearText.get(), isbnText.get()))

def deleteCommand():
    database.delete(selectedTupple[0])

def updateCommand():
    database.update(selectedTupple[0],titleText.get(), authorText.get(), yearText.get(), isbnText.get())

window = Tk()
window.wm_title('Book Store')

l1 = Label(window, text='Title')
l1.grid(row = 0, column = 0)

l2 = Label(window, text='Author')
l2.grid(row = 0, column = 2)

l3 = Label(window, text='Year')
l3.grid(row = 1, column = 0)

l4 = Label(window, text='ISBN')
l4.grid(row = 1, column = 2)

titleText = StringVar()
e1 = Entry(window, textvariable = titleText)
e1.grid(row = 0, column = 1)

authorText = StringVar()
e2 = Entry(window, textvariable = authorText)
e2.grid(row = 0, column = 3)

yearText = StringVar()
e3 = Entry(window, textvariable = yearText)
e3.grid(row = 1, column = 1)

isbnText = StringVar()
e4 = Entry(window, textvariable = isbnText)
e4.grid(row = 1, column = 3)

list1 = Listbox(window, height = 6, width = 35)
list1.grid(row =2, column = 0, rowspan = 6, columnspan = 2)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>', getSelectedRow)

b1 = Button(window, text = 'View All', width = 12, command= viewAllCommand)
b1.grid(row = 2, column = 3)

b2 = Button(window, text = 'Search Entry', width = 12, command = searchCommand)
b2.grid(row = 3, column = 3)

b3 = Button(window, text = 'Add Entry', width = 12, command = addCommand)
b3.grid(row = 4, column = 3)

b4 = Button(window, text = 'Update Entry', width = 12, command = updateCommand)
b4.grid(row = 5, column = 3)

b5 = Button(window, text = 'Delete Entry', width = 12, command = deleteCommand)
b5.grid(row = 6, column = 3)

b6 = Button(window, text = 'Close', width = 12, command = window.destroy)
b6.grid(row = 7, column = 3)

window.mainloop()