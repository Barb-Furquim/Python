# script for convert file HTML in file PDF 
# script in progress

import pdfkit
from tkinter import *

def html_pdf():

    htmlpdf = pdfkit.from_url("https://www.google.com.br/", "google.pdf")

html_pdf()

janela = Tk()
janela.title("Converter HTML para PDF")

# criação do texto dentro da janela
texto_orientacao = Label(janela, text="Clique no botão para selecionar o arquivo HTML: ")

# posição do texto
texto_orientacao.grid(column=0, row=0)

botao = Button(janela, text="Carregar arquivo HTML", command=html_pdf)
botao.grid(column=0, row=1)

janela.mainloop()
