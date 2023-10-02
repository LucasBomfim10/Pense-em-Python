
#Quantos segundos há em 42 minutos e 42 segundos?

minToSeg = (42*60)+42
print(minToSeg)


#Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.

kmToMi = 10/1.61
print(kmToMi)

#Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?

passoMedio = (42+(42/60))/kmToMi
velocidadeMedia= kmToMi/(passoMedio/60)
print(passoMedio)
print(velocidadeMedia)