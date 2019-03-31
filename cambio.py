import requests
import json

url = "http://data.fixer.io/api/latest?access_key=5d0eb200bb9fb42872430c207728160f"
print("Acessando base de dados...")
response = requests.get(url)
print(response)
if response.status_code == 200:
    print("Conseguiu acessar base de dados!")
    print("Buscando informações das moedas...")
    dados = response.json()
    day = dados['date']
    print("Acessando dados do dia %s/%s/%s" % (day[8:], day[5:7], day[0:4]))
    euro_real = dados['rates']['BRL'] / dados['rates']['EUR']
    dollar_real = dados['rates']['BRL'] / dados['rates']['USD']
    btc_real = dados['rates']['BRL'] / dados['rates']['BTC']
    print("%.2f" % euro_real)
    print("%.2f" % dollar_real)
    print("%.2f" % btc_real)
else:
    print("Site com problemas!")