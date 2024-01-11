from openpyxl import load_workbook

# lê pasta de trabalho e planilha

wb= load_workbook("pivot_table.xlsx")
sheet = wb["Relatorio"]

#acessando um valor especifico

print(sheet["B3"].value)

#interando valores atraves deloop

for i in range(2, 6):
    ano = sheet["A%s" %i] .value
    am = sheet["B%s" %i] .value
    bt = sheet["C%s" %i] .value
    print("{0} o Maycon esta vendendo {1} e o Bently vendeu {2}".format(ano, am, bt))