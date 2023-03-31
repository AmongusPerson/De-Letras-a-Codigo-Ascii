from tkinter import *
ola = Tk()
ola.title("Convertidor")
ola.geometry("500x500")
ola.configure(background="#f4a261")
titulo = Label(ola, text="De Letras a Codigo Ascii", bg="#2a9d8f", fg="white")
titulo.place(relx=0.5, rely=0.03, anchor=CENTER,)
inpu = Entry(ola, bg="#e9c46a")
inpu.place(relx=0.5, rely=0.09, anchor=CENTER,)
resultado = Label(ola, text="Resultado = ", bg="#e76f51", fg="white")
resultado.place(relx=0.5, rely=0.22, anchor=CENTER,)
def xd():
    hola = inpu.get()
    for letter in hola:
        resultado["text"] += str(ord(letter))+" "

bton = Button(ola, text="Convertir", bg="#264653", fg="white", command=xd)
bton.place(relx=0.5, rely=0.15, anchor=CENTER)


ola.mainloop()