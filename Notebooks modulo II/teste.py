arquivo = open('daily_IBM.csv', 'r')
planilha = list(csv.reader(arquivo, delimiter=',', lineterminator='\n'))
arquivo.close()
print(planilha)
variação = 0

for linha,indice in enumerate(planilha[1:]):
    variação = float(linha[2])-float(linha[3])
    planilha[indice].append(variação)

print(planilha)
