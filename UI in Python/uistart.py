from tkinter import *

window = Tk()
def convertUnit():
    print(input1Value.get())
    kgToGrams = float(input1Value.get())*1000
    text1.delete('1.0', END)
    text1.insert(END, kgToGrams)
    kgToPound = float(input1Value.get())*2.20462
    text2.delete('1.0', END)
    text2.insert(END, kgToPound)
    kgToOnce = float(input1Value.get())*35.274
    text3.delete('1.0', END)
    text3.insert(END, kgToOnce)

label1 = Label(window, text ='Kg')
label1.grid(row = 0, column = 0)

button1 = Button(window, text = 'Execute', command = convertUnit)
button1.grid(row = 0, column= 2)

input1Value = StringVar()
input1 = Entry(window, textvariable = input1Value)
input1.grid(row = 0, column = 1)

text1 = Text(window, height = 1, width = 21)
text1.grid(row = 1, column = 1)

text2 = Text(window, height = 1, width = 21)
text2.grid(row = 1, column = 2)

text3 = Text(window, height = 1, width= 21)
text3.grid(row = 1, column = 3)
 
window.mainloop()
