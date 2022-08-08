from tkinter import*
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.ttk import*

ekran=Tk()
ekran.title("kuyumcu")
ekran.geometry("400x400")

tür=["yüzük","bilezik","kolye"]
ayar=["14","22"]
fiyat14=["350","400","380"]
fiyat22=["450","500","480"]

snfiy=0
üfiy=0

def hesapla():
   if atür.get()=="yüzük":
       print()

def hesapla2():
    if atür.get()=="bilezik":
        print()

def hesapla3():
    if atür.get()=="kolye":
        print()
    

atür=ttk.Combobox()
atür['values']=tür
atür.bind('<<ComboboxSelected>>',hesapla)
atür.current(1)
atür.grid(column=0,row=0)

ayar1=ttk.Combobox()
ayar1['values']=ayar
ayar1.bind('<<ComboboxSelected>>',hesapla)
ayar1.current(1)
ayar1.grid(row=0,column=1)

bfiyat14=Combobox()
bfiyat14['values']=fiyat14
bfiyat14.bind('<<ComboboxSelected>>',hesapla)
bfiyat14.current(1)
bfiyat14.grid(row=1,column=2)

bfiyat22=Combobox()
bfiyat22['values']=fiyat22
bfiyat22.bind('<<ComboboxSelected>>',hesapla)
bfiyat22.current(1)
bfiyat22.grid(row=1,column=3)



gram=Entry()
gram.grid(row=0,column=2)

hesap=Button(text="hesap",command=hesapla)
hesap.grid(row=3,column=0)

mainloop()
