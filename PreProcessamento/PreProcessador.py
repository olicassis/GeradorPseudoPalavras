# Imports
import funcoesAuxiliares as fa

# Abrindo arquivo para leitura e lendo suas palavras
arq = open("brazilian", 'r')
palavras = arq.read().split('\n')
arq.close()
nova_lista_palavras = []

# Filtra as palavras desejadas
for p in palavras:
    if not fa.maiuscula(p):
        if fa.min_threshold_letras(3, p):
            if not fa.hifen(p): 
                if not fa.prefixos(p):
                    if not fa.hiato_final_palavra(p):
                        if fa.validar_formato(p):
                            nova_lista_palavras.append(p)
del palavras
palavras = nova_lista_palavras
nova_lista_palavras = []
# Retira as palavras que a sílaba foi dividida incorretamente (possui sílaba sem vogal)
# ou que não foi classificado quanto a tonicidade
for p in palavras:
    if fa.tonicidade(p) != "NA":
        nova_lista_palavras.append(p)
del palavras
# Gravando os dados em um arquivo csv
with open("palavrasProcessadas.csv",'w') as arq:
    arq.write("palavra,canonicidade,tonicidade\n")
    for p in nova_lista_palavras:
        string = p + ',' + str(fa.canonicidade(p)) + ',' + fa.tonicidade(p) + '\n'
        arq.write(string)