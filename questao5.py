# Construa um algoritmo que, a partir de duas cores primárias fornecidas pelo usuário determine qual cor seria obtida pela mistura delas.
# Para tanto, considere as informações fornecidas abaixo:
# As cores vermelho, azul e amarelo são chamadas de cores primárias porque não podem ser obtidas a partir de outras cores e,
# quando misturadas, resultam numa cor secundária, de acordo com as seguintes regras:
# •	vermelho + azul = roxo;
# •	vermelho + amarelo = laranja;
# •	azul + amarelo = verde.

cor1 = input("""Qual a primeira cor que você deseja misturar? Vermelho, azul ou amarelo?""").upper

cor2 = input("""Qual a segunda cor que você deseja misturar? Vermelho, azul ou amarelo?""").upper

if ((cor1 == "VERMELHO" and cor2 == "AMARELO")) or ((cor1 == "AMARELO" and cor2 == "VERMELHO")):
    print("A mistura das cores forma laranja!")
elif ((cor1 == "AZUL" and cor2 == "AMARELO")) or ((cor1 == "AMARELO" and cor2 == "AZUL")):
    print("A mistura das cores forma verde!")
elif ((cor1 == "VERMELHO" and cor2 == "AZUL")) or ((cor1 == "AZUL" and cor2 == "VERMELHO")):
    print("A mistura das cores forma roxo!")

else:
    print("Escolha uma cor prímaria ou existente!")

