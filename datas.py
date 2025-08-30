#Programa que mostra a data e a hora atual.
from datetime import datetime
hoje=datetime.now() #Lê a data de hoje
ano=hoje.strftime("%y")
mes=hoje.strftime("%m")
dia=hoje.strftime("%d")
hora=hoje.strftime("%H")
min=hoje.strftime("%M")
print("{}/{}/{}".format(dia,mes,ano))
print("{}:{}".format(hora,min))