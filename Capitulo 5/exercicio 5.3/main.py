# 1. Escreva uma função chamada is_triangle que receba três números inteiros como argumentos, e que imprima “Yes” ou “No”, dependendo da possibilidade de formar ou não um triângulo de gravetos com os comprimentos dados.

def is_triangle(x, y, z):

    if (z > (x+y) or x > (z+y) or y > (x+z)):
        print("no")

    else:
        print("yes")


def pergunta():

    x = int(input("x:"))
    y = int(input("y:"))
    z = int(input("z:"))
    is_triangle(x, y, z)


pergunta()
