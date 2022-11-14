# alfabeto = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
#         'w', 'x', 'y', 'z'}

def contarLetrasRepetidas(string):
    letrasRepetidas = []
    for letra in string:
        if letra in letrasRepetidas:
            letrasRepetidas.append(letra)

    return len(str(letrasRepetidas))


print(contarLetrasRepetidas("Amandaa"))

# Não consegui :(