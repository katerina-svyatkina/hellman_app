from tkinter import *
from tkinter import messagebox
import hellmanAlgorithm

root = Tk()

def clickOnInfo():
    messagebox.showinfo(title="Краткая информация", message = 'Программа была реализована для ознакомительных целей в рамках учебной работы.\n'
                                                              ' Для корректной работы:\n '
                                                              '\n'
                                                              '1. Чтобы зашифровать введите сообщение в поле "Текста".\n'
                                                              'Ключ вводить в формате : Последовательность чисел открытого ключа, число открытого ключа.\n'
                                                              '\n'
                                                              '2. Чтобы расшифровать введите сообщение в поле "Текста".\n'
                                                              'Ключ вводить в формате : Последовательность чисел закрытого ключа, число открытого ключа, число закрытого ключа.\n')

def clickDeCr():
    n=8 #произвольное количество элементов последовательности
    textOutput.configure(state="normal")
    textOutput.delete('1.0', END)
    textFromKeyboard = str(textInput.get(1.0, 'end-1c'))
    textNew=[int(x) for x in textFromKeyboard.split()]
    keyFromKeyboard = str(labelInput.get())
    print(textNew)

    if((textFromKeyboard == '' and keyFromKeyboard == '') or textFromKeyboard == '' or keyFromKeyboard == ''   ):
        messagebox.showerror(title='ОШИБКА!', message='Поле текст должно содержать хотя бы один символ.')
    else:
        key = [int(x) for x in keyFromKeyboard.split()]
        keyM = key[-2]
        keyW=key[-1]
        key.pop()
        key.pop()
        print(keyM, keyW, key)
        newMess = hellmanAlgorithm.deCryptMessage(textNew, key, keyW, keyM)  # расшифрованное сообщение
        textOutput.insert(1.0,newMess )
        textOutput.configure(state="disabled")

    textOutput.configure(state="disabled")

def clickCrypt():
    n=8 #произвольное количество элементов последовательности
    textOutput.configure(state="normal")
    textOutput.delete('1.0', END)
    textFromKeyboard = str(textInput.get(1.0, 'end-1c'))
    keyFromKeyboard = str(labelInput.get())

    if((textFromKeyboard == '' and keyFromKeyboard == '') or textFromKeyboard == '' or keyFromKeyboard == ''   ):
        messagebox.showerror(title='ОШИБКА!', message='Поле текст должно содержать хотя бы один символ.')
    else:
        key = [int(x) for x in keyFromKeyboard.split()]
        keyW = key[-1]
        key.pop()

        chipMess = hellmanAlgorithm.cryptMessage(textFromKeyboard, key, keyW)  # зашифрованное сообщение
       # newMess = str(hellmanAlgorithm.deCryptMessage(textFromKeyboard, key, keyW, M))  # расшифрованное сообщение
       # print(newMess)
        textOutput.insert(1.0,chipMess )
        textOutput.configure(state="disabled")
def clickGenerate():
    generatePrKey = hellmanAlgorithm.generatePrivateKey(8)
    M = hellmanAlgorithm.generateMOpen(generatePrKey)
    w = hellmanAlgorithm.generateWClose(M)
    generateOpenKey = hellmanAlgorithm.generateOpenKey(8, generatePrKey, w, M)
    messagebox.showinfo(title="Сгенерированные ключи",
                        message='Для дешифрования:'+ str(generatePrKey) + ' ' + str(M) + ' ' + str( w) +'\n'
                        '\n'
                        'Для шифрования: ' + str(generateOpenKey)+ str( M ) + '\n'
                        )

root['bg'] = '#fafafa'
root.title('Алгоритм шифрования/дешифррования DES.')
root.geometry('850x700')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=600, width=850 )
canvas.pack()

frame = Frame(root, bg='#6899D3')
frame.place(x=10, y = 100, width = 825, height = 550)

title = Label(canvas, text='Добро пожаловать!', font = ("Nihonium113", 40), fg = '#4284D3', anchor="e" )
title.place(x=10, y=10)

titleInfo = Label(canvas, text='В этой программе используется алгоритм шифрования DES.', font = ("Humaroid",16), fg='#04346C', anchor="e")
titleInfo.place(x=10,y=55)

buttonInfo = Button(canvas, text = "Узнать больше", font = ("Humaroid",13), bg='#4284D3', command=clickOnInfo)
buttonInfo.place(x=600, y=50)

titleAboutInput = Label(frame, text ='Введите ваше сообщение ниже: ', font = ("Humaroid", 16), fg='#04346C', anchor="e")
titleAboutInput.place(x = 10, y =10)

textInput = Text(frame, bg='white', width = 48, height=23)
textInput.place(x=10, y=45)

titleKey = Label(frame,text ='Введите ключ: ', font = ("Humaroid", 12), fg='#04346C', anchor="e" )
titleKey.place(x = 10, y= 430)

labelInput = Entry(frame, bg = 'white', width=63)
labelInput.place(x=10, y=460)

buttonCr = Button(frame, text = "ТЫК (Зашифровать)", font = ("Humaroid",13), bg='#4284D3', command = clickCrypt )
buttonCr.place(x = 60, y = 500)

buttonDeCr = Button(frame, text = "ТЫК (Дешифровать)", font = ("Humaroid",13), bg='#4284D3', command= clickDeCr )
buttonDeCr.place(x = 200, y = 500)

buttonGenerate= Button(frame, text= "Сгенерировать ключи", font = ("Humaroid", 13), bg='#4284D3', command= clickGenerate)
buttonGenerate.place(x = 550, y = 500)

titleOutput = Label(frame, bg = 'white',text= 'Результат алгоритма ниже:', font = ("Humaroid", 16), fg='#04346C', anchor="e" )
titleOutput.place(x=425, y = 10)


textOutput = Text(frame, bg='white', width = 48, height=23 )
textOutput.configure(state="disabled")
textOutput.place(x = 425, y = 45 )

root.mainloop()