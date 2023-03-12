from tkinter import *
from datetime import datetime
from tkinter import messagebox

###### Cores usadas #######
cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul

app = Tk()
app.geometry("480x200")
app.resizable(False, False)
app.title("Relógio Inteligente")
icon = PhotoImage(file='imagens/icon.png')
app.iconphoto(True, icon)
app.config(bg=cor1)

def relogio():
    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_semana =  tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.month
    ano = tempo.year
    
    #adicionando um zero
    dia_str = str(dia).zfill(2)
    mes_str = str(mes).zfill(2)
    
    hora_label["text"]= hora
    hora_label.after(200, relogio)
    
    dia_label["text"] = dia_semana
    
    data_label["text"]=  dia_str + "/" + mes_str + "/" + str(ano)

hora_label = Label(app, text="", font=("jetbrains Mono", 60, 'bold'), fg=cor2, bg="#121212")
hora_label.pack(pady=10)

dia_label = Label(app, text="", font=("jetbrains Mono", 10, 'bold'), fg=cor2, bg="#121212")
dia_label.place(x=45, y=150)

data_label = Label(app, text="", font=("jetbrains Mono", 10, 'bold'), fg=cor2, bg="#121212")
data_label.place(x=150, y=150)


relogio()
mainloop()