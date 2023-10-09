#Exercício 3.2 - Objeto de funcao


def do_twice(f,t):
    f(t)
    f(t)
    
def print_spam(t):
    print(t)

t = 't'
do_twice(print_spam,t)