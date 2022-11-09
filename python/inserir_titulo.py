import json

inserir = input("Você gostaria de inserir um texto no seu macro? (S/N) ")

if inserir.upper() == "N":
    exit()
elif inserir.upper() == "S":
    novo_titulo = str(input("Qual será o título? "))

with open("textos.json", "w" ) as f:
    json.dumps(novo_titulo, f)

with open("textos.json", "r") as f:
    ler_titulo = json.load(f)
print(ler_titulo)
