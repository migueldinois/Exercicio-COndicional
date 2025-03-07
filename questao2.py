# Leia 2 números e informe qual deles é o maior ou se eles são iguais.

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 > numero2:
    print("O número 1 é maior que o número 2")
elif numero1 < numero2:
    print("O número 2 é maior que o número 1")
elif numero1 == numero2:
    print("Os números são iguais!")