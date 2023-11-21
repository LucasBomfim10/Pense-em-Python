#Exercício 10.2 Escreva uma função chamada cumsum que receba uma lista de números e retorne a soma cumulativa; isto é, uma nova lista onde o i-ésimo elemento é a soma dos primeiros i+1 elementos da lista original.


def cumsum(t):
    elemento = len(t)
    soma = 0
    temp = 0
    
    for i in range(elemento):
        temp = t[i]
        t[i] = t[i] + soma
        soma+=temp
        
        
    return t
    
t = [1,2,3]
print(cumsum(t))
    