from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from codigo import organizar


def perguntar_pasta():
    global path
    path = filedialog.askdirectory()
    mostra_pasta['text'] = path


def botao():
    global path
    try:
        organizar(path)
    except FileNotFoundError:
        messagebox.showerror(
            title="ERRO", message=f'O caminho "{path}" não foi encontrado.')
    else:
        messagebox.showinfo(
            title='SUCESSO', message=f'O caminho {path} foi organizado com sucesso ou já está organizado')


path = 'Ainda não foi adicionado nenhum path'
# GUI
janela = Tk()
janela.geometry('200x80')
janela.resizable(0, 0)
janela.title('Organizador de arquivos')

mostra_pasta = Label(text=path, font=('ARIAL', 7))
mostra_pasta.pack()

perguntar_pasta = Button(text='Selecionar pasta', command=perguntar_pasta)
perguntar_pasta.pack()


botao = Button(text='Organizar', bg='blue',
               font=('ARIAL', 13), command=botao)
botao.pack()


janela.mainloop()
