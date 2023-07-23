# realizando importações de bibliotecas
# por padrao, elas serão importadas no começo
# dos arquivos/programas.py

import os
import time

#.system serve para mandar coamandos para o terminal entre outras funções
os.system('cls')
os.system('dir')

# o taskkilll serve para parar o aplicativo executável
# responsável por rodar uma aplicação ou sistema

os.system('taskkill /f /im chome.exe')


#os.system('taskkill /f /im cmd.exe')

#tipos de dados em python
numero_inteiro_1: int = 5
numero_inteiro_2: int = 5500
numero_inteiro_3: int = 100

print(f'Dados das variáveis do tipo int: {numero_inteiro_1}, {numero_inteiro_2}, {numero_inteiro_3}')

nome: str = 'Caue'
sobrenome: str = 'Oliveira'
texto_aleatorio: str = 'hahahaha'
print(f'\nDados das variáveis do tipo str: {numero_inteiro_1}, {numero_inteiro_2}, {numero_inteiro_3}')

salario_dev: float = 1.545
nota_aluno: float = 7.5
temperatura: float = 35.9
print(f'\nDados das variáveis do tipo float: {salario_dev}, {nota_aluno}, {temperatura}')

eh_verdade: bool = True
eh_mentira: bool = False
numero_inteiro_1_eh_maior_que_numero_2: bool = numero_inteiro_1 > numero_inteiro_2
print(f'\nDados das variáveis do tipo bool: {eh_verdade}, {eh_mentira}, {numero_inteiro_1_eh_maior_que_numero_2}')

lista_de_dados: list = [
    numero_inteiro_1,
    numero_inteiro_2,
    numero_inteiro_3,
    nome,
    sobrenome,
    texto_aleatorio,
    salario_dev,
    nota_aluno,
    temperatura,
    eh_verdade,
    eh_mentira,
    numero_inteiro_1_eh_maior_que_numero_2
]

print(f'\nMostrando o dado da posição 0: {lista_de_dados[0]}')
print(f'\nMostrando o dado da posição 3: {lista_de_dados[3]}')
print(f'\nMostrando o dado da posição 7: {lista_de_dados[7]}')

print('esperando...')
time.sleep(5)
os.system('cls')

#for item in lista_de_dados


