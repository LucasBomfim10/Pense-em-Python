#Exercício 10.3 Escreva uma função chamada middle que receba uma lista e retorne uma nova lista com todos os elementos originais, exceto os primeiros e os últimos elementos.


def middle(t):
    t.pop(0)
    t.pop(-1)
    return t

t = [1,2,3,4,5,6]
print(middle(t))