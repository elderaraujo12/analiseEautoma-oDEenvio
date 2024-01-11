import pandas as pd 

#importando dados 
data = pd.read_excel('VendaCarros.xlsx')
print(data)

# listar os primeiros registros

print(data.head())

#mostrar os ultimos registros

print(data.tail())

#contagem de valores por fabricante 
print(data["Fabricante"].value_counts())