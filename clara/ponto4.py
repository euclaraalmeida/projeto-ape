# Percentual de candidatos por cargo, considerando:
# Grau de instrução;
# Gênero;
# Estado civil.

from func import *

def contar_dados(arqv_todos, cargo_alvo):
    contadores = {
        'SOLTEIRO(A)':0,
        'CASADO(A)': 0,
        'DIVORCIADO(A)':0,
        'VIÚVO(A)': 0,
        'FEMININO': 0,
        'MASCULINO': 0,
    }

    contadores_grau = {
        'LÊ E ESCREVE': 0,
        'ENSINO FUNDAMENTAL INCOMPLETO': 0,
        'ENSINO FUNDAMENTAL COMPLETO': 0,
        'ENSINO MÉDIO INCOMPLETO': 0,
        'ENSINO MÉDIO COMPLETO': 0,
        'SUPERIOR INCOMPLETO': 0,
        'SUPERIOR COMPLETO': 0,
    }

    total_cargo = 0

    # Contagem por cargo
    for i in arqv_todos:
        dados = i.strip().split(";")
        cargos = dados[3].strip()

        if cargos == cargo_alvo:
            total_cargo += 1
            estado_civil = dados[1].strip()
            genero = dados[2].strip()
            escolaridade = dados[0].strip()

            if estado_civil in contadores:
                contadores[estado_civil] += 1

            if genero in contadores:
                contadores[genero] += 1

            if escolaridade in contadores_grau:
                contadores_grau[escolaridade] += 1

    return total_cargo, contadores, contadores_grau

def imprimir_percentuais(total, contadores, contadores_grau, cargo):
    if total > 0:
        print(f'% {cargo}')
        print(f'{(contadores["SOLTEIRO(A)"] / total) * 100:.2f}% de solteiros')
        print(f'{(contadores["CASADO(A)"] / total) * 100:.2f}% de casados')
        print(f'{(contadores["DIVORCIADO(A)"] / total) * 100:.2f}% de divorciados')
        print(f'{(contadores["VIÚVO(A)"] / total) * 100:.2f}% de viúvos')
        print()

        print(f'{(contadores["FEMININO"] / total) * 100:.2f}% de mulheres')
        print(f'{(contadores["MASCULINO"] / total) * 100:.2f}% de homens')
        print()
        
        print(f'{(contadores_grau["LÊ E ESCREVE"] / total) * 100:.2f}% com "Lê e escreve"')
        print(f'{(contadores_grau["ENSINO FUNDAMENTAL INCOMPLETO"] / total) * 100:.2f}% com Ensino Fundamental Incompleto')
        print(f'{(contadores_grau["ENSINO FUNDAMENTAL COMPLETO"] / total) * 100:.2f}% com Ensino Fundamental Completo')
        print(f'{(contadores_grau["ENSINO MÉDIO INCOMPLETO"] / total) * 100:.2f}% com Ensino Médio Incompleto')
        print(f'{(contadores_grau["ENSINO MÉDIO COMPLETO"] / total) * 100:.2f}% com Ensino Médio Completo')
        print(f'{(contadores_grau["SUPERIOR INCOMPLETO"] / total) * 100:.2f}% com Superior Incompleto')
        print(f'{(contadores_grau["SUPERIOR COMPLETO"] / total) * 100:.2f}% com Superior Completo')
        print()
    
with open("clara/arquivo_juntos.txt", "r",encoding="utf-8") as arquivo_juntos:
    arqv_todos = montar_lista(arquivo_juntos)

# Contando e imprimindo dados para cada cargo
for cargo in ["VEREADOR", "PREFEITO", "VICE-PREFEITO"]:
    total, contadores, contadores_grau = contar_dados(arqv_todos, cargo)
    imprimir_percentuais(total, contadores, contadores_grau, cargo)