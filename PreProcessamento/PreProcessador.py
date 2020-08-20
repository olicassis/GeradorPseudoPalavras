# Importa as funções auxiliares
import funcoesAuxiliares as fa

# Abrindo arquivo para leitura e lendo suas palavras
arq = open("brazilian", 'r')
palavras = arq.read().split('\n')
arq.close()
nova_lista_palavras = []

# Limpando as palavras da lista e gravando os dados em um arquivo csv
with open("palavrasProcessadas.csv",'w') as arq:
    arq.write("palavra,canonicidade,tonicidade\n")
    # Filtra as palavras desejadas (sem letras maiúsculas, sem hífen e com o mínimo de 3 letras)
    for p in palavras:
        if not fa.tem_maiuscula(p) and fa.min_threshold_letras(3, p):
            if not fa.tem_hifen(p):
                nova_lista_palavras.append(p)
                s = p + ',' + str(fa.canonicidade(p)) + '\n'
                arq.write(s)

    print(nova_lista_palavras)
    print(len(nova_lista_palavras))