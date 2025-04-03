from datetime import datetime


data_namoro = datetime (2025, 3, 22).date()
data_atual = datetime.today().date()

data_usuario = input ("Quando Pedro e Monyke começaram a namorar?")
data_usuario = datetime.strptime(data_usuario, "%d/%m/%Y").date()

if data_usuario == data_namoro:
   print ("Parabéns Você acertou!!!")

else:
    print ("Voce Errou!!!")