# Contém as funções auxiliares para a leitura das palavras desejadas.
def tem_hifen(palavra):
    if '-' in palavra:
        return True
    else:
        return False

def tem_maiuscula(palavra):
    for l in palavra:
        codigo_ascii = ord(l)
        if codigo_ascii >= 65 and codigo_ascii <= 90:
            return True
    return False

def min_threshold_letras(min, palavra):
    if len(palavra) >= min:
        return True
    else:
        return False

def presente_lista(lista, palavra):
    if palavra in lista:
        return True
    else:
        return False

def canonicidade(palavra):
    t = len(palavra)
    if t % 2 != 0 and vogal(palavra[0]):
        return False
    else:
        for i in range(t):
            if vogal(palavra[i]) != (i%2 != 0):
                return False
        return True

def vogal(letra):
    if letra in ['a','e','i','o','u']:
        return True
    else:
        return False