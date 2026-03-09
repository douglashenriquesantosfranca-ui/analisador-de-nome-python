nome = input("Digite seu nome:  ")
if nome:
    print(f"Seu nome é: {nome}")
    print(f"Seu nome maiusculo é: {nome.upper()}")
    print(f"Seu nome minúsculo é: {nome.lower()}")
    letras = len(nome.replace(" ", ""))
    print(f"Seu nome possui: {letras} ")
    if " " in nome:
        print("Seu nome tem espaço")
    else:
        print("Seu nome não contem espaço")  
    print(f"Seu nome invetido é: {nome[::-1 ]}")
    print(f"A primeira letra do seu nome é: {nome[0]}")
    print(f"a ultima letra do seu nome é: {nome[-1]}")

    
    if len(nome) <= 3 :
        print("Seu nome é muito Curto")      
else:
    print("Voce não digitou um nome")
