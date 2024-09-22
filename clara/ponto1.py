# Quantidade de candidatos por cargo
from func import *
arquivo_cargo = open("clara/cargo.txt","r")

arqv_cargo=montar_lista(arquivo_cargo)

arquivo_cargo.close()

P='PREFEITO'
Vp='VICE-PREFEITO'
V='VEREADOR'

cont_p=0
cont_vp=0
cont_v=0

for i in arqv_cargo:
    if i==P:
        cont_p+=1
    if i==Vp:
        cont_vp+=1
    if i==V:
        cont_v+=1

print(f'Vereador: {cont_v}')
print(f'Vice-Prefeito: {cont_vp}')
print(f'Prefeito: {cont_p}')


