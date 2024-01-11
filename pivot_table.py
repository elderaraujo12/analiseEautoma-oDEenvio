import pandas as pd

data = pd.read_excel('VendaCarros.xlsx')
print(type(data))

# selecionando colunas
print(data["Estado"])

#selecionando colunas especificas do dataframe
df = data[['Fabricante','ValorVenda','Ano']]
print(df)

#criando tabela pivo

pivot_table = df.pivot_table(
    index = 'Ano',
    columns = 'Fabricante',
    values='ValorVenda',
    aggfunc='sum'
)
print(pivot_table)

#exportando tabela em excel 
pivot_table.to_excel("pivot_table.xlsx", 'Relatorio') 
