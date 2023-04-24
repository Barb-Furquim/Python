# Project convert file HTML in file PDF

import pdfkit
from tkinter import *

def covert():
  
    pdfkit.from_url("https://www.google.com.br/", "google.pdf")
    
convert()

janela = Tk()

janela.mainloop()
