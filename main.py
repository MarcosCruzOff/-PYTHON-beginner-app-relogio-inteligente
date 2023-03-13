from tkinter import *
import locale
from datetime import datetime

###### Cores usadas #######
cor1 = "#3d3d3d"  #cinza
cor2 = "#fafcff"  #branca
cor3 = "#15181C"  #preta     

app = Tk()
app.geometry("480x200")
app.resizable(False, False)
app.title("Relógio Inteligente")
icon = PhotoImage(file='imagens/icon.png')
app.iconphoto(True, icon)
app.config(bg=cor1)

def relogio():
    #Definir o idioma para português do Brasil
    locale.setlocale(locale.LC_ALL, "pt_BR.utf-8")
    
    agora = datetime.now()
    hora = agora.strftime("%H:%M:%S")    
    
    dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    nome_dia_semana = dias_semana[agora.weekday()]
    dia = agora.day
    
    mes = agora.month
    meses = [
        "Janeiro", 
        "Fevereiro", 
        "Março", 
        "Abril", 
        "Maio", 
        "Junho", 
        "Julho", 
        "Agosto", 
        "Setembro", 
        "Outubro", 
        "Novembro", 
        "Dezembro"
    ]
    nome_mes = meses[mes-1]
    
    ano = agora.year
    
    #adicionando um zero
    dia_str = str(dia).zfill(2)
    # mes_str = str(mes).zfill(2)
    
    hora_label["text"]= hora
    hora_label.after(200, relogio)
    
    dia_label["text"] = dia_str
    nome_dia_label["text"] = nome_dia_semana
    mes_label["text"] = nome_mes
    ano_label["text"] = ano
    
    # data_label["text"]=  dia_str + "/" + mes_str + "/" + str(ano)

#Frame_data
frame_data = Frame(height=150, width=150, bg=cor3, highlightthickness=0)
frame_data.place(x=10, y=10)

dia_label = Label(frame_data, text="", font=("jetbrains Mono", 40, 'bold'), fg=cor2, bg=cor3, highlightthickness=0)
dia_label.place(x=10, y=30 )

mes_label = Label(frame_data, text="", font=("jetbrains Mono", 15, 'bold'), fg=cor2, bg=cor3, highlightthickness=0)
mes_label.place(x=10 ,y=95)

ano_label = Label(frame_data, text="", font=("jetbrains Mono", 10, 'bold'), fg=cor2, bg=cor3, highlightthickness=0)
ano_label.place(x=105 ,y=10)

nome_dia_label = Label(app, text="", font=("jetbrains Mono", 10, 'bold'), fg=cor2, bg=cor1, highlightthickness=0)
nome_dia_label.place(x=10 ,y=160)

#Frame_hora
frame_hora = Frame(height=150, width=305, bg=cor2, highlightthickness=0)
frame_hora.place(x=165, y=10)

hora_label = Label(frame_hora, text="", font=("jetbrains Mono", 45, 'bold'), fg=cor1, bg=cor2, highlightthickness=0)
hora_label.place(x=5, y=25)


# data_label = Label(app, text="", font=("jetbrains Mono", 10, 'bold'), fg=cor2, bg="#121212")
# data_label.place(x=150, y=150)


relogio()
mainloop()