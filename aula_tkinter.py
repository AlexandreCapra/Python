import tkinter as tk


def clicado():
    print("O botão foi clicado")


janela = tk.Tk()
# janela.iconbitmap("raposa.png")
janela.title("Tkinter o início!")
janela.geometry("800x600")
janela.minsize(width=400, height=250)
janela.maxsize(width=1200, height=1050)
janela.resizable(width=True, height=True)
janela.config(bg='gray', cursor='hand1')

botao = tk.Button(janela, text="Clica em Mim!", bg="black",
                  fg="white", activebackground="orange", activeforeground="blue", font=("Roboto", 20), command=clicado())
botao.pack()

label = tk.Label(janela, text="Aqui está o Label",
                 bg="red", fg="white", font=("Roboto", 20))
label.pack()

entrada = tk.Entry(janela, show="=")
entrada.pack()
janela.mainloop()
