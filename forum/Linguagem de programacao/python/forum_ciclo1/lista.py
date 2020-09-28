# coding: utf-8

# Programa escrito em python por Rodrigo Moraes para o forum do
# curso de analise e desenvolvimento de sistemas 
# Anhanguera 2020.2
# 
# Esse programa consiste em 3 funcoes que pegam valores digitados no prompt
# armazena-los em um array, usam o laço "for" para lista-los
# e depois excluem os dados se necessarios.
# 
# 2020/09/28 - Rodrigo Moraes
# 
# 
# 


# um cabeçalho simples
print("Criação de listas")
print("Escolha uma opção")

# criação de um array vazio
lista = []


# essa função é a responsavel por receber os valores digitados
# e popular o array
def criaLista(pnome, snome, tnome):
    lista.append(pnome)
    lista.append(snome)
    lista.append(tnome)

# Essa fn é o que o forum pede: eu usei o laço "for" para listar os valores do array 
def mostraLista():
    for l in lista:
        print(l)
# Essa fn é responsável por excluir um valor do array,
# tmb fiz um tratamento de erro
def excluiDado(nome):

    if nome not in lista:
        print("Não há dados que combinam com " + nome )
        print("Nenhum dado foi alterado.")
    else:
        lista.remove(nome)
        print("Dado excluido com sucesso! Carregue a lista para ver as alterações.")

#esse bloco abaixo é responsavel pelo menu
option = 0
while option != 4:
    print('''
[1] Criar Lista
[2] Carregar lista
[3] Excluir um dado
[4] Sair
        ''')
    option = int(input("Selecione uma opção: "))
    if option == 1:
        print("Digite 3 nomes quaisquer")
        pnome = str(input("Digite o primeiro nome: "))
        snome = str(input("Digite o segundo nome: "))
        tnome = str(input("Digite o terceiro nome: "))

        criaLista(pnome, snome, tnome)

        print("Lista criada com sucesso! Selecione uma opção desejada abaixo:")
    elif option == 2:
        
        mostraLista()
        print("Lista carregada com sucesso! Selecione uma opção desejada abaixo:")
    elif option == 3:
        nome = str(input("Digite o nome que deseja excluir:"))
        excluiDado(nome)
        
    elif option == 4:
        print("Fechando o programa!")
        print("Bye")
    else:
        print("Opção incorreta!")
