#Escreva um script que leia a hora atual e a converta em um tempo em horas, minutos e segundos, mais o número de dias desde a época.

import time

tempo = time.time()

dias = tempo//86400

info = time.localtime(tempo)

horas = info.tm_hour
minutos = info.tm_min
segundos = info.tm_sec

print("Hora: ",horas," Minutos: ",minutos," Segundos: ",segundos)
print('Dias: ',dias)