from random import randint as rd
import time as t

TAMANHO1 = 100000
TAMANHO2 = 250000
TAMANHO3 = 500000

def selection_sort(lista):
    for i in range(1, len(lista)):
        k = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[k]:
                k = j
        lista[i], lista[k] = lista[k], lista[i]

def inserir_aleatoriamente(lista, t1):
    i = 0
    while i < t1:
        value = rd(1, t1)
        if value not in lista:
            lista.append(value)
        i += 1
            

def inserir_decrescente(lista, t1):
    for i in range(t1):
        lista.append(t1 - i)
            

def inserir_crescente(lista, t1):
    for i in range(1, t1):
        lista.append(i)
            

def printar_lista(lista):
    for i in range(len(lista)):
        print(lista[i], end=" ")
    print()

def menu_tamanho(lista1, lista2, lista3, tamanho):
    while True:
        print("\nEscolha uma opcao:")
        print("1. Inserir numeros aleatorios")
        print("2. Inserir numeros em ordem decrescente")
        print("3. Inserir numeros em ordem crescente")
        print("4. Ordenar lista aleatoria")
        print("5. Ordenar lista decrescente")
        print("6. Ordenar lista crescente")
        print("0. Sair")
        opcao = int(input("Digite sua opcao: "))
        
        if opcao == 1:
            inserir_aleatoriamente(lista1, tamanho)
            printar_lista(lista1)
        elif opcao == 2:
            inserir_decrescente(lista2, tamanho)
            printar_lista(lista2)
        elif opcao == 3:
            inserir_crescente(lista3, tamanho)
            printar_lista(lista3)
        elif opcao == 4:
            inicio = t.time()
            selection_sort(lista1)
            fim = t.time()
            print("Lista aleatoria apos a ordenacao:", lista1)
            print(f"Tempo de execucao: {fim - inicio:.9f} segundos")
        elif opcao == 5:
            inicio = t.time()
            selection_sort(lista2)
            fim = t.time()
            print("Lista decrescente apos a ordenacao:", lista2)
            print(f"Tempo de execucao: {fim - inicio:.9f} segundos")
        elif opcao == 6:
            inicio = t.time()
            selection_sort(lista3)
            fim = t.time()
            print("Lista crescente apos a ordenacao:", lista3)
            print(f"Tempo de execucao: {fim - inicio:.9f} segundos")
        elif opcao == 0:
            print("Saindo do submenu...")
            break
        else:
            print("Opcao invalida, tente novamente!")

def menu():
    while True:
        print("\nEscolha um tamanho:")
        print("1. Tamanho 1")
        print("2. Tamanho 2")
        print("3. Tamanho 3")
        print("0. Sair")
        opcao = int(input("Digite sua opcao: "))
        
        if opcao == 1:
            menu_tamanho(lista1, lista2, lista3, TAMANHO1)
        elif opcao == 2:
            menu_tamanho(lista1, lista2, lista3, TAMANHO2)
        elif opcao == 3:
            menu_tamanho(lista1, lista2, lista3, TAMANHO3)
        elif opcao == 0:
            print("Saindo do programa...")
            break
        else:
            print("Opcao invalida, tente novamente!")


#variaveis globais
lista1 = []
lista2 = []
lista3 = []

if __name__ == "__main__":
    menu()