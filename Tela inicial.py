from tkinter import *
from tkinter import ttk
import tkinter.font as font

app = Tk()
app.title('Lista de itens')
app.configure(background='#0e2440')
app.geometry('205x340')
app.resizable(False, False)

#Adicionar a tela para armazenar os itens
tela_itens = Listbox(app, relief='sunken', background='#8ba2c7', border=4)
tela_itens.place(relx=0.02, rely=0.02, height=155, width=195)

#Adicionar campo para digitar o nome do item
campo_adicionar = Entry(app, width=26, relief='ridge', background='#a0a3a2', border=2)
campo_adicionar.place(relx=0.12, rely=0.5, height=25, width=150)

#Adicionar o botão de inserir item
fonte_btn_inserir = font.Font(family='Arial', size=12, weight='bold')
btn_inserir = Button(app, text="Adicionar item",background='#a0a3a2', border=1, font=fonte_btn_inserir)
btn_inserir.place(relx=0.2, rely=0.6, height=30, width=120)

#Adiconar o botão de alterar item
fonte_btn_alterar = font.Font(family='Arial', size=12, weight='bold')
btn_alterar = Button(app, text="Alterar item",background='#a0a3a2', border=1, font=fonte_btn_alterar)
btn_alterar.place(relx=0.2, rely=0.7, height=30, width=120)

#Adicionar o botão de deletar item
fonte_btn_deletar = font.Font(family='Arial', size=12, weight='bold')
btn_deletar = Button(app, text="Deletar item",background='red', fg='white',border=1, font=fonte_btn_deletar)
btn_deletar.place(relx=0.2, rely=0.8, height=30, width=120)

#Botão para imprimir a lista em um arquivo .txt ou PDF
fonte_btn_imprimir = font.Font(family='Arial', size=12, weight='bold')
btn_imprimir = Button(app, text='Imprimir Lista', background='#a0a3a2', border=1, font=fonte_btn_imprimir)
btn_imprimir.place(relx=0.2, rely=0.9, height=30, width=120)

app.mainloop()
