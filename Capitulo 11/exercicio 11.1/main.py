#Escreva uma função que leia as palavras em words.txt e guarde-as como chaves em um dicionário. Não importa quais são os valores. Então você pode usar o operador in como uma forma rápida de verificar se uma string está no dicionário. Fiz uma variacão de word como variavel


words = ["teste","bola","casco","flamengo","chuveiro","chuveiro"]

chest = dict()

def contador(words):
    for w in words:
        if w not in chest :
            chest[w] = 1
        else:
            chest[w] +=1
            
    return chest         
        
print(contador(words))