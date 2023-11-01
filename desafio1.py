def palindromo(palavra):
    palavra_reversa = palavra[::-1]

    if palavra == palavra_reversa:
        return True
    else:
        return False


palavra = input("Digite uma palavra: ")

resultado = palindromo(palavra)

print("Palavra reversa:", palavra[::-1])
print("Palíndromo:", resultado)
