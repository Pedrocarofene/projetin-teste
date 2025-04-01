
print ("monyke")
nome = "monyke thifany"
idade = 18
altura =1.65
data_de_nascimento = 21/10/2006


from datetime import datetime

data_de_namoro = datetime(2025, 3, 22).date()
data_atual = datetime.today().date()    

data_usuario = input("Qual a data de namoro de Pedro e Monyke?")
data_usuario = datetime.strptime(data_usuario, "%d/%m/%Y").date()

if data_usuario == data_de_namoro:
    print("Parabéns, você acertou!")
else:
    print("Você errou!!")