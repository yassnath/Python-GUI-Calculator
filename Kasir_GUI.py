from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('Kasir')

# Variabel
burger = StringVar()
rotibakar = StringVar()
kentanggoreng = StringVar()
cireng = StringVar()
brownsugarmilk = StringVar()
machalatte = StringVar()
chocomilk = StringVar()
americano = StringVar()
teh = StringVar()
icecream = StringVar()
total = 0
tax = 0.11

# Function
def totalbeli():
    global burger, rotibakar, kentanggoreng, cireng, brownsugarmilk, machalatte, chocomilk, americano, teh, icecream, total
    hburger = int(burger.get()) * 18000 
    hrotibakar = int(rotibakar.get()) * 20000 
    hkentanggoreng = int(kentanggoreng.get()) * 15000
    hcireng = int(cireng.get()) * 15000
    hbrownsugarmilk = int(brownsugarmilk.get()) * 12000 
    hmachalatte = int(machalatte.get()) * 12000
    hchocomilk = int(chocomilk.get()) * 10000
    hamericano = int(americano.get()) * 8000 
    hteh = int(teh.get()) * 5000
    hicecream = int(icecream.get()) * 8000 
    total = (hburger + (hburger * tax)) + (hrotibakar + (hrotibakar * tax)) + + (hcireng + (hcireng * tax)) + (hkentanggoreng + (hkentanggoreng * tax)) + (hmachalatte + (hmachalatte * tax)) + (hchocomilk + (hchocomilk * tax)) + (hbrownsugarmilk + (hbrownsugarmilk * tax)) + (hamericano + (hamericano* tax)) + (hteh + (hteh * tax)) + (hicecream + (hicecream * tax))

def totalharga():
    global total
    if total == 0:
       messagebox.showerror(message='Silahkan masukkan jumlah terlebih dahulu!')
    
    elif total >= 0 :
        messagebox.showinfo(message='Total belanja anda Rp {},-'.format(int(total)))

def clear():
    burger.set('0')
    rotibakar.set('0')
    kentanggoreng.set('0')
    cireng.set('0')
    brownsugarmilk.set('0')
    machalatte.set('0')
    chocomilk.set('0')
    americano.set('0')
    teh.set('0')
    icecream.set('0')
    
    if total == 0:
        messagebox.showerror(message='Silahkan masukkan jumlah terlebih dahulu!')

app.geometry('750x600') # Membuat ukuran
app.configure(bg='black') # Membuat background warna
app.resizable(0,0)

# Membuat tulisan title
Label(app, text='PabloLodonz Coffee', bg='black', foreground='#fef5ac', font='Algerian 14 bold').place(x=260,y=30)
Label(app, text='_' * 68, bg='black', foreground='#fef5ac', font='arial 14').place(x=0,y=65)
Label(app, text='Our Menu', bg='black', foreground='#fef5ac', font='Georgia 13 bold').place(x=317,y=107)

# membuat label nama menu (snack) 
Label(app, text='Snack', bg='black', foreground='#fef5ac', font='Georgia 12 bold').place(x=145,y=160)
Label(app, text='Burger', bg='black', foreground='#fef5ac', font='Georgia 12 bold').place(x=40,y=195)
Label(app, text='Toast', bg='black', foreground='#fef5ac', font='Georgia 12 bold').place(x=40,y=235)
Label(app, text='French Fries', bg='black', foreground='#fef5ac', font='Georgia 12 bold').place(x=40,y=275)
Label(app, text='Cireng', bg='black', foreground='#fef5ac', font='Georgia 12 bold').place(x=40,y=315)
Label(app, text='Ice Cream', bg='black', foreground='#fef5ac', font='Georgia 12 bold').place(x=40,y=355)

# membuat garis pemisah antara drink dan snack
Label(app, text='''
|
|
|
|
|
|
|
|
|
|
|''', bg='black', foreground='#fef5ac', font='Georgia 12 bold').place(x=360,y=165)

# Membuat label nama menu (drink)
Label(app, text='Drink', bg='black', foreground='#fef5ac', font='Georgia 12 bold').place(x=498,y=160)
Label(app, text='Brown Sugar Milk', bg='black', foreground='#fef5ac', font='Georgia 12 bold').place(x=400,y=195)
Label(app, text='Machalatte', bg='black', foreground='#fef5ac', font='Georgia 12 bold').place(x=400,y=235)
Label(app, text='Chocomilk', bg='black', foreground='#fef5ac', font='Georgia 12 bold').place(x=400,y=275)
Label(app, text='Americano', bg='black', foreground='#fef5ac', font='Georgia 12 bold').place(x=400,y=315)
Label(app, text='Teh', bg='black', foreground='#fef5ac', font='Georgia 12 bold').place(x=400,y=355)

# Membuat label wifi
Label(app, text='Password Wifi: senggoldongs', bg='black', foreground='#fef5ac', font='arial 11').place(x=268,y=450)
Label(app, text='Kritik & Saran hubungi: +6281234567890', bg='black', foreground='#fef5ac', font='Timesnewroman 8').place(x=268,y=471)
Label(app, text='_' * 68, bg='black', foreground='#fef5ac', font='arial 14').place(x=0,y=488)

# Membuat label harga
Label(app, text='Rp 18000', bg='black', foreground='#fef5ac', font='Cambria 12 bold').place(x=200,y=195) 
Label(app, text='Rp 20000', bg='black', foreground='#fef5ac', font='Cambria 12 bold').place(x=200,y=235)
Label(app, text='Rp 15000', bg='black', foreground='#fef5ac', font='Cambria 12 bold').place(x=200,y=275)
Label(app, text='Rp 15000', bg='black', foreground='#fef5ac', font='Cambria 12 bold').place(x=200,y=315)
Label(app, text='Rp  8000', bg='black', foreground='#fef5ac', font='Cambria 12 bold').place(x=200,y=355)
Label(app, text='Rp 12000', bg='black', foreground='#fef5ac', font='Cambria 12 bold').place(x=570,y=195)
Label(app, text='Rp 12000', bg='black', foreground='#fef5ac', font='Cambria 12 bold').place(x=570,y=235)
Label(app, text='Rp 10000', bg='black', foreground='#fef5ac', font='Cambria 12 bold').place(x=570,y=275)
Label(app, text='Rp  8000', bg='black', foreground='#fef5ac', font='Cambria 12 bold').place(x=570,y=315)
Label(app, text='Rp  5000', bg='black', foreground='#fef5ac', font='Cambria 12 bold').place(x=570,y=355)

# Membuat spinbox
Spinbox(app, from_=0, to=100, width=3, textvariable=burger, command=totalbeli).place(x=290,y=195)
Spinbox(app, from_=0, to=100, width=3, textvariable=rotibakar, command=totalbeli).place(x=290,y=235)
Spinbox(app, from_=0, to=100, width=3, textvariable=kentanggoreng, command=totalbeli).place(x=290,y=275)
Spinbox(app, from_=0, to=100, width=3, textvariable=cireng, command=totalbeli).place(x=290,y=315)
Spinbox(app, from_=0, to=100, width=3, textvariable=icecream, command=totalbeli).place(x=290,y=355)
Spinbox(app, from_=0, to=100, width=3, textvariable=brownsugarmilk, command=totalbeli).place(x=660,y=195)
Spinbox(app, from_=0, to=100, width=3, textvariable=machalatte, command=totalbeli).place(x=660,y=235)
Spinbox(app, from_=0, to=100, width=3, textvariable=chocomilk, command=totalbeli).place(x=660,y=275)
Spinbox(app, from_=0, to=100, width=3, textvariable=americano, command=totalbeli).place(x=660,y=315)
Spinbox(app, from_=0, to=100, width=3, textvariable=teh, command=totalbeli).place(x=660,y=355)

# Membuat tombol
Button(app, text='Total', foreground='white', bg='green', width=10, command=totalharga).place(x=270,y=535)
Button(app, text='Clear', foreground='white', bg='red', width=10, command=clear).place(x=390,y=535)

app.mainloop() 