# Faça um programaQue informe se um dado ano é ou não bissexto. Obs: um ano é bissexto se ele for divisível por 400 ou se ele for divisível por 4 e não por 100


ano = int(input("Diga um ano: "))

if (ano % 4 == 0) and ano % 100 > 0:
    print("Esse ano é bissexto")
else: 
    print("Esse ano não é bissexto!")