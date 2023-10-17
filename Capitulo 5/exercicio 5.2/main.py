#Escreva uma função chamada check_fermat que receba quatro parâmetros – a, b, c e n – e verifique se o teorema de Fermat se mantém. Se n for maior que 2 e a**n + b**n == c**n o programa deve imprimir, “Holy smokes, Fermat was wrong!” Senão o programa deve exibir “No, that doesn’t work.”

def check_format(a,b,c,n) :
    if n > 2 and a**n+b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else :
        print("No, that doesn’t work.")
        

a = int(input("a:\n"))
b = int(input("b:\n"))
c = int(input("c:\n"))
n = int(input("n:\n"))

check_format(a,b,c,n)