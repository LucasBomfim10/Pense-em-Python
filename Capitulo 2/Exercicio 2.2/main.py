
# 1. O volume de uma esfera com raio r é . Qual é o volume de uma esfera com raio 5?

raio = 5

volume = (4/3)*3.14*raio**3

print(volume)

# 2. Suponha que o preço de capa de um livro seja R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?

preco = ((24.95 - (24.95*40/100))*60+3+(59*0.75))

print(preco)

#3. Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro lugar, que horas chego em casa para o café da manhã?

horas = ((6*60+52)+(8+15/60)+(3*(7+15/60)))/60
print(horas)