import requests
import json
import pandas as pd
import decimal

url = "http://data.fixer.io/api/latest?access_key=5d0eb200bb9fb42872430c207728160f"
print("Acessando base de dados...")
response = requests.get(url)
print(response)
if response.status_code == 200:
    print("Conseguiu acessar base de dados!")
    print("Buscando informações das moedas...")
    dados = response.json()
    day = dados['date']
    day = day[8:10]+"/"+day[5:7]+"/"+day[0:4]
    print("Acessando dados do dia %s" % day) 
    euro_real = round(dados['rates']['BRL'] / dados['rates']['EUR'], 2)
    dollar_real = round(dados['rates']['BRL'] / dados['rates']['USD'], 2)
    btc_real = round(dados['rates']['BRL'] / dados['rates']['BTC'], 2)
    print("%.2f" % euro_real)
    print("%.2f" % dollar_real)
    print("%.2f" % btc_real)
    print("Gerando o arquivo CSV...")
    df = pd.DataFrame({'Moedas': ['Euro', 'Dollar', 'Bitcoin'], 'Valores':[euro_real, dollar_real, btc_real], 'Dia de Acesso':[day, '', '']})
    df.to_csv("valores.csv", index=False, sep=";", decimal=",")
    print("Arquivo gerado e exportado com sucesso para a pasta do projeto!")
else:
    print("Site com problemas!")