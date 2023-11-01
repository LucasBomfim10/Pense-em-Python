#Escreva uma função chamada nested_sum que receba uma lista de listas de números inteiros e adicione os elementos de todas as listas aninhadas. Por exemplo:

def  nested_sum (lista):
    total = 0
    c = 0
    for i in range (len(lista)):
        for c in lista[i-1]:
           total += c

    return total


t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))
