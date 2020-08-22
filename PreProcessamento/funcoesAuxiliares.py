## Imports
import re

## Variáveis globais utilizadas na separação de sílabas e identificação de formatos
# Tritongos
tritongos = ['uai','uei','uou','uiu','uão','uem','uõe']
formatos_tritongo = [
                        'VCVCVVVC','VCVCVVVV','VCVCVVV','CVCVCVVVV','CVCVCVVVC','CVCVCVVV',
                        'CVCVVV','CVCVVVV','CVCVVVC','VCVVVC','VCVVVC','VCVVV'
                    ]
formatos_tritongo_hifenizados = [
                                    'V-CV-CVVV-C','V-CV-CVVV-V','V-CV-CVVV','CV-CV-CVVV-V',
                                    'CV-CV-CVVV-C','CV-CV-CVVV','CV-CVVV','CV-CVVV-V',
                                    'CV-CVVV-C','V-CVVV-V','V-CVVV-C','V-CVVV'
                                ]
# Ditongos
ditongos_decrescentes = [
                                'ai','êi','ãi','ei','éi','oi','ói','ui','au','áu','eu',
                                'éu','iu','ou','ãe','ão','õe'
                            ]
formatos_ditongo = ['CVCVVCV','VCVVCV','CVCVV','VCVV','CVVCV','CVVV','VVCV','CVCCVVV']
formatos_ditongo_hifenizados = [
                                'CV-CVV-CV','V-CVV-CV','CV-CVV','V-CVV','CVV-CV',
                                'CVV-V','VV-CV','CVC-CVV-V'
                               ]
# Hiatos ou vogais duplas
hiatos_vogais_duplas = [
                        'ea','eo','ia','ie','io','oa','oe','ua','ue','ui','uo', # hiatos
                        'aa','ee','ii','oo','uu' # vogais duplas
                       ]
formatos_hiatos_vogais_duplas = [
                                    'CVVCV','VVCV','CVCVVCV','CVV','CVCCVVVCV',
                                    'CVCVVVCV','CVVC','VCCVCVV'
                                ]
formatos_hiatos_vogais_duplas_hifenizados = [
                                                'CV-V-CV','V-V-CV','CV-CV-V-CV','CV-V',
                                                'CVC-CV-VV-CV','CV-CVV-V-CV','CV-VC',
                                                'VC-CV-CV-V'    
                                            ]
# Qu ou Gu
padroes_gu_qu = ['gu','qu']
formatos_gu_qu = [
                    'CVCVVCV','CVCCVV','CVVCVCCV','VCVV','CVCVCCVV',
                    'CVCCVVCV','CCVCCVVCV','VCVVCCCV'
                 ]
formatos_gu_qu_hifenizados = [
                                'CV-CVV-CV','CVC-CVV','CVV-CVC-CV','V-CVV','CV-CVC-CVV',
                                'CVC-CVV-CV','CCVC-CVV-CV','V-CVV-CCV'
                             ]
# Consoantes indivisíveis
padroes_consoante_indivisivel = [
                'br','bl','cr','cl','dr','fr','fl','gr','gl','pr','pl','tr','vr',
                'lh','nh','ch'
              ]
formatos_consoante_indivisivel = [
                                    'CCVCV','CVCCV','CVCVCCV','CCVCCV','VCCVCV',
                                    'CCVVCCV','CVCCVCV','CVCCVC','CCVCVCV'
                                 ]
formatos_consoante_indivisivel_hifenizados = [
                                                'CCV-CV','CV-CCV','CV-CV-CCV','CCV-CCV',
                                                'V-CCV-CV','CCV-VC-CV','CV-CCV-CV','CV-CCVC',
                                                'CCV-CV-CV'
                                             ]
# Cz ou ps
padroes_cz_ps = ['cz','ps']
formatos_cz_ps = ['CCVCVCV','CCVCCV','CCVCCV','CCVCVCCV','CCVCVCVCV','CCVCVCVCVV']
formatos_cz_ps_hifenizados = [
                                'CCV-CV-CV','CCVC-CV','CCV-CCV',
                                'CCV-CVC-CV','CCV-CV-CV-CV	','CCV-CV-CV-CV-V'
                             ]
# Outros formatos
outros_formatos = [
                'CVCVC','VCV','VCCVCV','VCCVCVCVC','CVCCV','CVCCVCV','CVCCVCCV',
                'CVVCCV','CVCCVC','CVCVCCV','CVCCVCVV','CVCCCVCVV','VCVCVCV',
                'CVCCVCCCV','CVVC'
               ]
outros_formatos_hifenizados = [
                'CV-CVC','V-CV','VC-CV-CV','VC-CV-CV-CVC','CVC-CV','CVC-CV-CV','CVC-CVC-CV',
                'CVVC-CV','CVC-CVC','CV-CVC-CV','CVC-CV-CV-V','CVC-CCV-CV-V','V-CV-CV-CV',
                'CVC-CVC-CCV','CV-VC'
               ]

## Contém as funções auxiliares para a leitura das palavras desejadas
def representacao_palavra(palavra):
    v_letras = ""
    for l in palavra:
        if vogal(l):
            v_letras += 'V'
        else:
            v_letras += 'C'
    return v_letras

def hifen(palavra):
    if '-' in palavra:
        return True
    else:
        return False

def maiuscula(palavra):
    for l in palavra:
        codigo_ascii = ord(l)
        if (codigo_ascii >= 65 and codigo_ascii <= 90) or (l in "ÁÉÍÓÚ"):
            return True
    return False

def min_threshold_letras(min, palavra):
    if len(palavra) >= min:
        return True
    else:
        return False
        
def canonicidade(palavra):
    t = len(palavra)
    if t % 2 != 0 or vogal(palavra[0]):
        return False
    else:
        for i in range(t):
            if vogal(palavra[i]) != (i%2 != 0):
                return False
        return True

def vogal(letra):
    if letra in "aeiouáéíóúâêôã":
        return True
    else:
        return False

def hiato_final_palavra(palavra):
    hiatos = ['ea','eo','ia','ie','io','oa','oe','ua','ue','ui','uo']
    for h in hiatos:
        re_match_object = re.search(h,palavra)
        if re_match_object is not None:
            if re_match_object.end() == len(palavra):
                return True
    return False

def prefixos(palavra):
    padroes = ["sub","ab","ad"]
    for p in padroes:
        re_match_object = re.search(p,palavra)
        if re_match_object is not None:
            if re_match_object.start() == 0:
                return True
            else:
                return False
        else:
            return False

def silaba_tem_vogal(silaba):
    vogais = "aeiouáéíóúâêôã"
    for v in vogais:
        if v in silaba:
            return True
    return False

def verifica_silabas(silabas):
    for silaba in silabas:
        if not silaba_tem_vogal(silaba):
            return False
    return True

#--------------------------------------------------------------------------------------------------#
## Funções que definem os formatos das palavras que serão lidas
def tem_tritongo(palavra):
    return verificar_formato(tritongos,formatos_tritongo,palavra)

def tem_ditongo(palavra):
    return verificar_formato(ditongos_decrescentes,formatos_ditongo,palavra)

def tem_hiato_vogais_duplas(palavra):
    return verificar_formato(hiatos_vogais_duplas,formatos_hiatos_vogais_duplas,palavra)

def tem_gu_qu(palavra):
    return verificar_formato(padroes_gu_qu,formatos_gu_qu,palavra)

def tem_consoante_indivisivel(palavra):
    return verificar_formato(padroes_consoante_indivisivel,formatos_consoante_indivisivel,palavra)

def tem_cz_ps(palavra):
    return verificar_formato(padroes_cz_ps,formatos_cz_ps,palavra)

def tem_outros_formatos(palavra):
    count = 0
    for formato in outros_formatos:
        if representacao_palavra(palavra) == formato:
            return (True,count)
        count += 1
    return (False,None)

def verificar_formato(padroes,formatos, palavra):
    count = 0
    for padrao in padroes:
        if padrao in palavra:
            for formato in formatos:
                if representacao_palavra(palavra) == formato:
                    return (True,count)
                count += 1
    return (False,None)

def validar_formato(palavra):
    if canonicidade(palavra):
        return True
    else:
        if tem_ditongo(palavra)[0]:
            return True
        if tem_gu_qu(palavra)[0]:
            return True
        if tem_tritongo(palavra)[0]:
            return True
        if tem_hiato_vogais_duplas(palavra)[0]:
            return True
        if tem_consoante_indivisivel(palavra)[0]:
            return True
        if tem_outros_formatos(palavra)[0]:
            return True
 
    return False

## Função que retorna uma determinada palavra dividida em sílabas
def separa_formato(palavra,formato,silabas,aux):
    count = 0
    for i in formato:
        if i != '-':
            aux += palavra[count]
            count += 1
        else:
            silabas.append(aux)
            aux = ""
    silabas.append(aux)

def separa_em_silabas(palavra):
    silabas = []
    aux = ""
    t = len(palavra)
    if canonicidade(palavra):
        for i in range(t):
            if i % 2 != 0:
                aux += palavra[i]
                silabas.append(aux)
            else:
                aux = palavra[i]
    else:
        # Separa palavras com tritongo
        finder = tem_tritongo(palavra)
        if finder[0]:
            separa_formato(palavra,formatos_tritongo_hifenizados[finder[1]],silabas,aux)
            return silabas
        # Separa palavras com ditongo
        finder = tem_ditongo(palavra)
        if finder[0]:
            separa_formato(palavra,formatos_ditongo_hifenizados[finder[1]],silabas,aux)
            return silabas
        # Separa palavras com hiatos ou vogais duplas
        finder = tem_hiato_vogais_duplas(palavra)
        if finder[0]:
            separa_formato(palavra,formatos_hiatos_vogais_duplas_hifenizados[finder[1]],silabas,aux)
            return silabas
        # Separa palavras com qu ou gu
        finder = tem_gu_qu(palavra)
        if finder[0]:
            separa_formato(palavra,formatos_gu_qu_hifenizados[finder[1]],silabas,aux)
            return silabas
        # Separa palavras com consoantes indivisíveis
        finder = tem_consoante_indivisivel(palavra)
        if finder[0]:
            separa_formato(palavra,formatos_consoante_indivisivel_hifenizados[finder[1]],silabas,aux)
            return silabas
        # Separa palavras com cz ou ps
        finder = tem_cz_ps(palavra)
        if finder[0]:
            separa_formato(palavra,formatos_cz_ps_hifenizados[finder[1]],silabas,aux)
            return silabas
        # Separa outros formatos
        finder = tem_outros_formatos(palavra)
        if finder[0]:
            separa_formato(palavra,outros_formatos_hifenizados[finder[1]],silabas,aux)
            return silabas 
    return silabas if verifica_silabas(silabas) else []

## Funções para classificar a palavra quanto sua tonicidade
def tem_acento(palavra):
    acentos = 'áéíóúâêô'
    for acento in acentos:
        re_match_object = re.search(acento,palavra)
        if re_match_object is not None:
            return True,re_match_object.start()
    return False,None

def oxitona(silaba):
    terminacoes = ['r','l','z','x','i','u','im','um','om']
    for terminacao in terminacoes:
        if verificar_terminacao(silaba,terminacao):
            return True
    return False

def paroxitona(silaba):
    terminacoes = ['o','os','a','as','e','es']
    for terminacao in terminacoes:
        if verificar_terminacao(silaba,terminacao):
            return True
    return False

def verificar_terminacao(silaba,terminacao):
    t_terminacao = len(terminacao)
    t_silaba = len(silaba)
    if t_terminacao > t_silaba:
        return False
    if t_terminacao == t_silaba:
        return terminacao in silaba
    if t_terminacao < t_silaba:
        return terminacao == silaba[-t_terminacao:]

def tonicidade(palavra):
    classificacao = ["oxítona","paroxítona","proparoxítona","NA"]
    silabas = separa_em_silabas(palavra)
    if silabas != []:
        t = len(silabas) 
        if tem_acento(palavra)[0]:
            for i in range(t):
                if (t-1-i) >= 0:
                    if tem_acento(silabas[t-1-i])[0]:
                        return classificacao[i]
        else:
            if oxitona(silabas[t-1]):
                return classificacao[0]
            else:
                if paroxitona(silabas[t-1]):
                    return classificacao[1]
                else:
                    return classificacao[3]  
    else:
        return classificacao[3]  
