# Importa as funções auxiliares
import funcoesAuxiliares as fa

# Abrindo arquivos para leitura e lendo suas palavras
arq1 = open("br-utf8.txt", 'r')
arq2 = open("palavras.txt", 'r')
palavras1 = arq1.read().split('\n')
arq1.close()
palavras2 = arq2.read().split('\n')
arq2.close()
lista_palavras = palavras1 + palavras2
nova_lista_palavras = []

# Limpando as palavras da lista e gravando os dados em um arquivo csv
with open("palavrasProcessadas.csv",'w') as arq:
    arq.write("palavra,canonicidade,tonicidade\n")
    for p in lista_palavras:
            if not fa.tem_maiuscula(p) and fa.min_threshold_letras(3, p):
                if fa.tem_hifen(p):
                    aux = p.split('-')
                    for p_aux in aux:
                        if fa.min_threshold_letras(3, p_aux):
                            nova_lista_palavras.append(p_aux)
                else:
                    nova_lista_palavras.append(p)