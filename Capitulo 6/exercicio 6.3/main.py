#Escreva uma função chamada is_palindrome que receba uma string como argumento e retorne True se for um palíndromo e False se não for. Lembre-se de que você pode usar a função integrada len para verificar o comprimento de uma string.



def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]




def is_palindrome(s) :
    if(len(s)>1):
        if (first(s) == last(s)) :
            print(first(s),last(s),middle(s))
            return is_palindrome(middle(s))            
        else :
            return 0
    else:
        return 1
    
palavra = "teste"   

print(is_palindrome(palavra))
    
    
    
    