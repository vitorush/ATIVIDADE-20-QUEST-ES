peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))
imc = peso/altura
if imc <18.5:
    print("Abaixo do peso.")
elif imc >=18.5 and imc <=24.9:
    print("Peso normal.")
elif imc >=25 and imc <30:
    print("Sobrepeso")
else:
    ("Obesidade")