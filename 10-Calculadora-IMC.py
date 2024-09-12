# Iniciação da programação

print("[CALCULADORA IMC]")
peso = float(input("Diga-me seu peso: "))
altura = float(input("Diga-me sua altura: "))
print("Calculando seu IMC...")

#Calculadora
imc = peso/(altura**2)
print(f"Seu IMC é:{imc}")

#classificação
if(imc<18.5):
    print("[Você está abaixo do peso :( ]")

elif(18.5 <= imc <= 24.9):
    print("[Você está com o peso normal :D ]")

elif(25 <= imc <= 34.9):
    print("[Você está com sobrepeso...]")

else:
    print("[Você está com obesidade :( ]")