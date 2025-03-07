# Ler 3 valores e determinar o maior dentre eles ou se eles são iguais.

numero1 = int(input("Digite o primeiro valor: "))
numero2 = int(input("Digite o segundo valor: "))
numero3 = int(input("Digite o terceiro valor: "))

if (numero1 > numero2) and (numero1 > numero3):
    print(f"O número {numero1} é maior que todos os outros números!")
elif (numero2 > numero1) and (numero2 > numero3):
    print(f"O número {numero2} é maior que todos os outros números!")
elif (numero3 > numero1) and (numero3 > numero2):
    print(f"O número {numero3} é maior que todos os outros números!")

if numero1 == numero2 and numero2 == numero3:
    print("Todos os numeros sao iguais!")