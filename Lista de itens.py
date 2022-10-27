from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font

lista = []

#Função para adicionar itens na lista
def adicionarItem():
    if campo_adicionar.get() == "":
        messagebox.showwarning(title="Erro ao adicionar", message="Não é possivel adicionar itens vazios!")
    else:
        lista.append(tela_itens.insert(END, campo_adicionar.get()))
        messagebox.showinfo(title="Adicionar item", message="Item adicionado com sucesso!")

def deletarItem():
    if len(lista) == 0:
        messagebox.showwarning(title="Sem itens", message="Não há itens para deletar!")
    else:
        lista.remove(tela_itens.delete(ACTIVE))
        messagebox.showinfo(title="Item removido", message="O item foi deletado da lista!")

def alterarItem():
    global app2
    app2 = tk.Toplevel()
    app2.title("Alterar item")
    app2.geometry("250x200")
    app2.configure(background='#0e2440')
    app2.resizable(False, False)
    fonte_label_alterar = font.Font(family="Cambria", size=15, weight='bold')
    tk.Label(app2, text="Alteração de item", height=2, width=15, font=fonte_label_alterar, bg='#0e2440', fg='White').pack(padx=2, pady=2)
    fonte_label_items = font.Font(family='Cambria', size=12)
    tk.Label(app2, text="Item Atual:", bg='#0e2440', font=fonte_label_items, fg='White').pack()
    global remove_item
    remove_item = tk.Entry(app2, bd=2, highlightcolor='#0a80a1', highlightthickness=1).pack(padx=2, pady=2)
    tk.Label(app2, text="Novo Item:", bg='#0e2440', font=fonte_label_items, fg='White').pack()
    global adiciona_item
    adiciona_item = tk.Entry(app2, bd=2, highlightcolor='#0a80a1', highlightthickness=1).pack(padx=2, pady=2)
    fonte_btn = font.Font(family='Cambria', size=10, weight='bold')
    tk.Button(app2, text="Alterar", font=fonte_btn, fg="Black", justify='center', command=alterar).pack(pady=6)
    
def alterar():
    for l in lista:
        if remove_item in lista:
            tela_itens.delete(ACTIVE) and adiciona_item.insert(END, adiciona_item.get())
            app2.destroy()
        else:
            print("Algo deu errado!")


app = Tk()
app.title('Lista de itens')
app.configure(background='#0e2440')
app.geometry('205x340')
app.resizable(False, False)

#Adicionar a tela para armazenar os itens
fonte_tela_itens = font.Font(family="MV Boli", size=15)

tela_itens = Listbox(app,
                    relief='sunken', 
                    background='#8ba2c7', 
                    border=4, 
                    highlightcolor='#0a80a1', 
                    highlightthickness=2, 
                    font=fonte_tela_itens,
                    justify='center',
                    cursor='dot')
tela_itens.place(relx=0.02, rely=0.02, height=155, width=195)

#Barra de navegação lateral da lista
barra = Scrollbar(tela_itens)
barra.pack(side = RIGHT, fill = 'y')
tela_itens.config(yscrollcommand = barra.set)
barra.config(command = tela_itens.yview)

#Adicionar campo para digitar o nome do item
fonte_campo_adicionar = font.Font(family="Cambria", size=10)

campo_adicionar = Entry(app, 
                        width=26, 
                        relief='ridge', 
                        background='white', 
                        border=2, 
                        highlightcolor='black', 
                        highlightthickness=1,
                        font=fonte_campo_adicionar)
campo_adicionar.place(relx=0.12, rely=0.5, height=25, width=150)

#Adicionar o botão de inserir item
fonte_btn_inserir = font.Font(family='Cambria', size=12, weight='bold')
btn_inserir = Button(app, 
                    text="Adicionar item", 
                    background='#a0a3a2', 
                    border=1, 
                    font=fonte_btn_inserir, 
                    command=adicionarItem)
btn_inserir.place(relx=0.2, rely=0.6, height=30, width=120)

#Adicionar o botão de alterar item
fonte_btn_alterar = font.Font(family='Cambria', size=12, weight='bold')
btn_alterar = Button(app, 
                    text="Alterar item", 
                    background='#a0a3a2', 
                    border=1,
                    font=fonte_btn_alterar,
                    command=alterarItem)

btn_alterar.place(relx=0.2, rely=0.7, height=30, width=120)

#Adicionar o botão de deletar item
fonte_btn_deletar = font.Font(family='Cambria', size=12, weight='bold')
btn_deletar = Button(app, 
                    text="Deletar item", 
                    background='red', 
                    fg='white',border=1, 
                    font=fonte_btn_deletar, 
                    command=deletarItem)
btn_deletar.place(relx=0.2, rely=0.8, height=30, width=120)

#Botão para imprimir a lista em um arquivo .txt ou PDF
fonte_btn_imprimir = font.Font(family='Cambria', size=12, weight='bold')
btn_imprimir = Button(app, 
                    text='Imprimir Lista', 
                    background='#a0a3a2', 
                    border=1, 
                    font=fonte_btn_imprimir)
btn_imprimir.place(relx=0.2, rely=0.9, height=30, width=120)

app.mainloop()
