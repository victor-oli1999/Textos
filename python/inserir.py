import json

inserir = input("Você gostaria de inserir um texto no seu macro? (S/N) ")

if inserir.upper() == "N":
    exit()
elif inserir.upper() == "S":
    titulo = str(input("Qual será o título? ") + ".json")
    qnt_parag = int(input("Serão quantos paragrafos? (Em número) "))
    print(qnt_parag)
    if qnt_parag == 1:
        parag_1 = str("\n" +input("Insira o texto aqui: "))
        parag_total = parag_1
    elif qnt_parag == 2:
        parag_1 = str("\n" + input("Insira o primeiro texto aqui: "))
        parag_2 = str("\n" + input("Insira o segundo texto aqui: "))
        parag_total = parag_1 + parag_2
    elif qnt_parag == 3:
        parag_1 = str("\n" + input("Insira o primeiro texto aqui: "))
        parag_2 = str("\n" + input("Insira o segundo texto aqui: "))
        parag_3 = str("\n" + input("Insira o terceiro texto aqui: "))
        parag_total = parag_1 + parag_2 + parag_3
print(parag_total)

#Json file

#with open(titulo, "w" ) as f:
#    json.dump(parag_total, f)


