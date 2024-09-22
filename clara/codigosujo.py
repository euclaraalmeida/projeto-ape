# Percentual de candidatos por cargo, considerando:
# Grau de instrução;
# Gênero;
# Estado civil.

from func import *

with open("clara/arquivo_juntos.txt", "r") as arquivo_juntos:
    arqv_todos = montar_lista(arquivo_juntos)

contadores= {
    # civil
    'SOLTEIRO(A)': 0,
    'CASADO(A)': 0,
    'DIVORCIADO(A)': 0,
    'VIÚVO(A)': 0,
    # genero
    'FEMININO':0,
    'MASCULINO':0,
}

contadores_grau= {

'LÊ E ESCREVE':0,
'ENSINO FUNDAMENTAL INCOMPLETO':0,
'ENSINO FUNDAMENTAL COMPLETO':0,
'ENSINO MÉDIO INCOMPLETO':0,
'ENSINO MÉDIO COMPLETO':0,
'SUPERIOR INCOMPLETO':0,
'SUPERIOR COMPLETO':0,
}


total=len(arqv_todos)

for i in arqv_todos:
    dados = i.strip().split(";")
    cargos = dados[3].strip() 

    if cargos == 'VEREADOR':
        estado_civil = dados[1].strip() 
        genero = dados[2].strip()
        escolaridade = dados[0].strip()

        if estado_civil in contadores:
            contadores[estado_civil] += 1

        if genero in contadores:
            contadores[genero]+=1
        
        if escolaridade in contadores_grau:
            contadores_grau[escolaridade]+=1


print('% Vereadores')

print(f'{(contadores["SOLTEIRO(A)"]/total)*100:.2f}% de solteiros')
print(f'{(contadores["CASADO(A)"]/total)*100:.2f}% de casados')
print(f'{(contadores["DIVORCIADO(A)"]/total)*100:.2f}% de Divorciados')
print(f'{(contadores["VIÚVO(A)"]/total)*100:.2f}% de viuvos')

print(f'porcentagem de mulheres{(contadores['FEMININO']/total)*100:.2f}')

print(f'porcenatgem de homens{(contadores['MASCULINO']/total)*100:.2f}')

print(f'{(contadores_grau["LÊ E ESCREVE"]/total)*100:.2f}% ')
print(f'{(contadores_grau["ENSINO FUNDAMENTAL INCOMPLETO"]/total)*100:.2f}% ')
print(f'{(contadores_grau["ENSINO FUNDAMENTAL COMPLETO"]/total)*100:.2f}% ')
print(f'{(contadores_grau["ENSINO MÉDIO INCOMPLETO"]/total)*100:.2f}% ')
print(f'{(contadores_grau["ENSINO MÉDIO COMPLETO"]*total)*100:.2f}% ')
print(f'{(contadores_grau["SUPERIOR INCOMPLETO"]/total)*100:.2f}% ')
print(f'{(contadores_grau["SUPERIOR COMPLETO"]/total)*100:.2f}% ')


for i in arqv_todos:
    dados = i.strip().split(";")
    cargos = dados[3].strip() 

    if cargos == 'PREFEITO':
        estado_civil = dados[1].strip() 
        genero = dados[2].strip()
        escolaridade = dados[0].strip()

        if estado_civil in contadores:
            contadores[estado_civil] += 1

        if genero in contadores:
            contadores[genero]+=1
        
        if escolaridade in contadores_grau:
            contadores_grau[escolaridade]+=1


print('% Prefeito')

print(f'{(contadores["SOLTEIRO(A)"]/total)*100:.2f}% de solteiros')
print(f'{(contadores["CASADO(A)"]/total)*100:.2f}% de casados')
print(f'{(contadores["DIVORCIADO(A)"]/total)*100:.2f}% de Divorciados')
print(f'{(contadores["VIÚVO(A)"]/total)*100:.2f}% de viuvos')

print(f'porcentagem de mulheres{(contadores['FEMININO']/total)*100:.2f}')

print(f'porcenatgem de homens{(contadores['MASCULINO']/total)*100:.2f}')

print(f'{(contadores_grau["LÊ E ESCREVE"]/total)*100:.2f}% ')
print(f'{(contadores_grau["ENSINO FUNDAMENTAL INCOMPLETO"]/total)*100:.2f}% ')
print(f'{(contadores_grau["ENSINO FUNDAMENTAL COMPLETO"]/total)*100:.2f}% ')
print(f'{(contadores_grau["ENSINO MÉDIO INCOMPLETO"]/total)*100:.2f}% ')
print(f'{(contadores_grau["ENSINO MÉDIO COMPLETO"]*total)*100:.2f}% ')
print(f'{(contadores_grau["SUPERIOR INCOMPLETO"]/total)*100:.2f}% ')
print(f'{(contadores_grau["SUPERIOR COMPLETO"]/total)*100:.2f}% ')



for i in arqv_todos:
    dados = i.strip().split(";")
    cargos = dados[3].strip() 

    if cargos == 'VICE-PREFEITO':
        estado_civil = dados[1].strip() 
        genero = dados[2].strip()
        escolaridade = dados[0].strip()

        if estado_civil in contadores:
            contadores[estado_civil] += 1

        if genero in contadores:
            contadores[genero]+=1
        
        if escolaridade in contadores_grau:
            contadores_grau[escolaridade]+=1


print('% VICE-PREFEITO')

print(f'{(contadores["SOLTEIRO(A)"]/total)*100:.2f}% de solteiros')
print(f'{(contadores["CASADO(A)"]/total)*100:.2f}% de casados')
print(f'{(contadores["DIVORCIADO(A)"]/total)*100:.2f}% de Divorciados')
print(f'{(contadores["VIÚVO(A)"]/total)*100:.2f}% de viuvos')

print(f'porcentagem de mulheres{(contadores['FEMININO']/total)*100:.2f}')

print(f'porcenatgem de homens{(contadores['MASCULINO']/total)*100:.2f}')

print(f'{(contadores_grau["LÊ E ESCREVE"]/total)*100:.2f}% ')
print(f'{(contadores_grau["ENSINO FUNDAMENTAL INCOMPLETO"]/total)*100:.2f}% ')
print(f'{(contadores_grau["ENSINO FUNDAMENTAL COMPLETO"]/total)*100:.2f}% ')
print(f'{(contadores_grau["ENSINO MÉDIO INCOMPLETO"]/total)*100:.2f}% ')
print(f'{(contadores_grau["ENSINO MÉDIO COMPLETO"]*total)*100:.2f}% ')
print(f'{(contadores_grau["SUPERIOR INCOMPLETO"]/total)*100:.2f}% ')
print(f'{(contadores_grau["SUPERIOR COMPLETO"]/total)*100:.2f}% ')


