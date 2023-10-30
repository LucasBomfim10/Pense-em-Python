#Escreva uma função chamada eval_loop que iterativamente peça uma entrada ao usuário,a avalie usando eval e exiba o resultado. Ela deve continuar até que o usuário digite done; então deverá exibir o valor da última expressão avaliada.

def eval_loop():
    while True:
        x = input("Digite a fórmula ou termine com 'done':")
        if x == 'done':
            break
        
        y = x
        print(eval(x))
    print(y)
    
eval_loop()
