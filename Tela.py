from tkinter import*
from tkinter import Tk, ttk
import requests
import json
import string
from ttkbootstrap import Style
from ttkbootstrap.widgets import Button, Combobox, Label


from ttkthemes import ThemedStyle

azul = '#2778FF'
azul_escuro  = '#2778FF'
branco = '#ffffff'

janela = Tk()
janela.title("Currenty Converter")
janela.geometry('900x550')
janela.resizable(False, False)
janela.configure(bg=azul)
style = ttk.Style(janela)



#funcoes
#flags

#dinheiro!!!!!!
def cotacao_dinheiro(event):
    if combo1.get() == 'EUR' and combo2.get() == 'BRL':
        param = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": "EUR",
        "to_currency": "BRL",
        "apikey": "SUA_CHAVE_DE_API"
}

        #pegar a cotacao
        response = requests.get("https://www.alphavantage.co/query", params=param)
        dados = response.json()
        cotacion = float(dados['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        coti = (f"R${cotacion:.2f}")
        atu = coti
        moedinha.config(text=atu)

        
        horario_completo = dados['Realtime Currency Exchange Rate']['6. Last Refreshed']
        horas = (f"Last update : {horario_completo}")
        atual = horas
        att.config(text=atual)
        moedinha.after(1000, cotacao_dinheiro)
        att.after(1000,cotacao_dinheiro)

    if combo1.get() == 'USD' and combo2.get() == 'BRL':
        param = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": "USD",
        "to_currency": "BRL",
        "apikey": "SUA_CHAVE_DE_API"
}

        #pegar a cotacao
        response = requests.get("https://www.alphavantage.co/query", params=param)
        dados = response.json()
        cotacion = float(dados['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        coti = (f"R${cotacion:.2f}")
        atu = coti
        moedinha.config(text=atu)
        horario_completo = dados['Realtime Currency Exchange Rate']['6. Last Refreshed']
        horas = (f"Last update : {horario_completo}")
        atual = horas
        att.config(text=atual)
        moedinha.after(1000, cotacao_dinheiro)
        att.after(1000,cotacao_dinheiro)
    if combo1.get() == 'USD' and combo2.get() == 'EUR':
        param = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": "USD",
        "to_currency": "EUR",
        "apikey": "SUA_CHAVE_DE_API"
}

        #pegar a cotacao
        response = requests.get("https://www.alphavantage.co/query", params=param)
        dados = response.json()
        cotacion = float(dados['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        coti = (f"€{cotacion:.2f}")
        atu = coti
        moedinha.config(text=atu)
        horario_completo = dados['Realtime Currency Exchange Rate']['6. Last Refreshed']
        horas = (f"Last update : {horario_completo}")
        atual = horas
        att.config(text=atual)
        moedinha.after(1000, cotacao_dinheiro)
        att.after(1000,cotacao_dinheiro)
    
    if combo1.get() == 'BRL' and combo2.get() == 'USD':
        param = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": "BRL",
        "to_currency": "USD",
        "apikey": "SUA_CHAVE_DE_API"
}

        #pegar a cotacao
        response = requests.get("https://www.alphavantage.co/query", params=param)
        dados = response.json()
        cotacion = float(dados['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        coti = (f"${cotacion:.2f}")
        atu = coti
        moedinha.config(text=atu)
        horario_completo = dados['Realtime Currency Exchange Rate']['6. Last Refreshed']
        horas = (f"Last update : {horario_completo}")
        atual = horas
        att.config(text=atual)
        moedinha.after(1000, cotacao_dinheiro)
        att.after(1000,cotacao_dinheiro)
    if combo1.get() == 'BRL' and combo2.get() == 'EUR':
        param = {
        "function": "CURRENCY_EXCHANGE_RATE",
        "from_currency": "BRL",
        "to_currency": "EUR",
        "apikey": "SUA_CHAVE_DE_API"
}

        #pegar a cotacao
        response = requests.get("https://www.alphavantage.co/query", params=param)
        dados = response.json()
        cotacion = float(dados['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        coti = (f"€{cotacion:.2f}")
        atu = coti
        moedinha.config(text=atu)
        horario_completo = dados['Realtime Currency Exchange Rate']['6. Last Refreshed']
        horas = (f"Last update : {horario_completo}")
        atual = horas
        att.config(text=atual)
        moedinha.after(1000, cotacao_dinheiro)
        att.after(1000, cotacao_dinheiro)
    


#combox
style= ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground= branco, background= branco, selectbackground= azul)


frame_photo1 = PhotoImage(file='principal.png')
frame_label1 = Label(janela,border=0,background=azul, image=frame_photo1)
frame_label1.pack(fill=BOTH,expand=True)



#titulo
titulo = Label(frame_label1,text="Conversor de moedas", background=azul, foreground=branco, font=('Roboto', 12, 'bold'))
titulo.place(x=100,y=10)
#moeda
moedinha = Label(text="",background=azul_escuro,foreground=branco, font=('Roboto', 68, 'bold'))
moedinha.place(x=100,y=40)

#att
att = Label(text="",background= azul_escuro,foreground=branco, font=('Montserat', 10, 'bold'))
att.place(x=100, y=150)





moeda = ['BRL', 'EUR', 'USD']


#frame
frame = Frame(janela, width=583, height=287,background =azul)
frame.place(x=100,y=200)

frame_photo = PhotoImage(file='Frame 1.png')
frame_principal = Label(frame,border=0,background=azul, image=frame_photo)
frame_principal.pack(fill=BOTH,expand=True)

#aba
frameaba = Frame(janela, width=541, height=77,background=azul_escuro)
frameaba.place(x=170,y=230)
frame_photo2 = PhotoImage(file='aba.png')
aba = Label(frameaba,border=0,background=branco, image=frame_photo2)
aba.pack(fill=BOTH,expand=True)

De = Label(text="From",foreground='#2C2F34', background=branco, font=('Montserat', 14, 'bold'))
De.place(x=200, y=200)
#frametest1 para a moeda
frametest1 = Frame(janela, width=100, height=50,bg=branco)
frametest1.place(x=200,y=250)
#comobobox


combo1 = ttk.Combobox(frametest1, font=(10),state="readonly")
combo1['values'] = (moeda)
combo1.pack()
combo1.bind('<<ComboboxSelected>>', lambda event: cotacao_dinheiro(event))






to = Label(text="To",foreground='#2C2F34', background=branco, font=('Montserat', 14, 'bold'))
to.place(x=600, y=200)
#frametest1 para a moeda
frametest2 = Frame(janela, width=100, height=50,background=branco)
frametest2.place(x=500,y=250)
#combobox
combo2 = ttk.Combobox(frametest2, values= moeda, font=(10),state="readonly",style='info.TCombobox')
combo2.pack()
combo2.bind('<<ComboboxSelected>>', lambda event:  cotacao_dinheiro(event))


#get_value()
#tempo()
janela.mainloop()

