horario = input("(M)anhã, (T)arde ou (S)em: ")

if horario.upper() == "M" or horario.upper() == "T" or horario.upper() == "S":
    nome = input("Nome do cliente: ")
    if horario.upper() == "M":
        cumprimentar = "\nBom dia, " + nome
    elif horario.upper() == "T":
        cumprimentar = "\nBoa tarde, " + nome
    elif horario.upper() == "S":
        cumprimentar = ""
else:
    exit()


print(cumprimentar + "\nTudo bem?\n")
print("Qualquer dúvida estamos à disposição.\nAtenciosamente,\nVictor.")



