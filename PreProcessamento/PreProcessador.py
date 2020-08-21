# Importa as funções auxiliares
import funcoesAuxiliares as fa

# Abrindo arquivo para leitura e lendo suas palavras
arq = open("brazilian", 'r')
palavras = arq.read().split('\n')
arq.close()
nova_lista_palavras = []

# Limpando as palavras da lista e gravando os dados em um arquivo csv
#with open("palavrasProcessadas.csv",'w') as arq:
    #arq.write("palavra,canonicidade,tonicidade\n")
# Filtra as palavras desejadas
for p in palavras:
    if not fa.maiuscula(p):
        if fa.min_threshold_letras(3, p):
            if not fa.hifen(p): 
                if not fa.prefixos(p):
                    if not fa.hiato_final_palavra(p):
                        if fa.validar_formato(p):
                            nova_lista_palavras.append(p)
palavras = nova_lista_palavras
print(len(nova_lista_palavras))
nova_lista_palavras = []
# Retira as palavras que a sílaba foi dividida incorretamente (possui sílaba sem vogal)
for p in palavras:
    if fa.verifica_silabas(fa.separa_em_silabas(p)):
        nova_lista_palavras.append(palavras)
palavras = nova_lista_palavras
print(len(nova_lista_palavras))
nova_lista_palavras = []
# Retira as palavras que não conseguiram ser classificadas quanto à tonicidade
