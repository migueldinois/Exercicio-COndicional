# Dado os três lados de um triângulo determinar:
# a)	se estes três lados caracterizam realmente um triângulo. Para que se possa construir um triângulo é 
# necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas 
# b)	se a resposta for afirmativa determinar de que tipo de triângulo se trata:
# •	Triangulo equilátero: Todos os lados são iguais.
# •	Triangulo isósceles: Possui 2 lados iguais.
# •	Triangulo escaleno: Todos os lados são diferentes.


def equilatero():
    if (lado1 == lado2) and (lado2 == lado3):
        print("Esse triangulo é equilatero!")

def isosceles():
    if ((lado1 == lado2) or (lado2 == lado1)) or ((lado2 == lado3) or (lado3 == lado2)) or ((lado3 == lado1) or (lado1 == lado3)):
        print("Esse triangulo é isosceles!")

def escaleno():
    if ((lado1 != lado2) and (lado1 != lado3)) and ((lado2 != lado1) and (lado2 != lado3))


lado1 = int(input("Quantos metros tem o primeiro lado?"))
lado2 = int(input("Quantos metros tem o segundo lado?"))
lado3 = int(input("Quantos metros tem o terceiro lado?"))
somados2 = lado2 + lado3
valordiferenca = lado2 - lado3

if 


else:
    print("Os valores não formam um triangulo!")