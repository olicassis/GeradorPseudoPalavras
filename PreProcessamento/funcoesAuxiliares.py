# Imports
import re

# Contém as funções auxiliares para a leitura das palavras desejadas
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

def cz_ps(palavra):
    padroes = ['cz','ps']
    for p in padroes:
        if re.search(p,palavra) is not None:
            return True
    return False

def tres_consoantes(palavra):
    v_letras = representacao_palavra(palavra)
    if re.search("CCC",v_letras)is not None:
        return True
    else:
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

def consoante_consoante_m(palavra,m):
    v_letras = representacao_palavra(palavra)
    aux = len(re.findall("CC",palavra))
    if aux > m:
        return True
    else:
        return False

def silaba_tem_vogal(silaba):
    vogais = "aeiouáéíóúâêôã"
    for v in vogais:
        if v in silaba:
            return True
    return False

# --------------------------------------------------------------------------------------------
# Funções que definem os formatos das palavras que serão lidas
def tem_tritongo_formato(palavra):
    tritongos = ['uai','uei','uou','uiu','uão','uem','uõe']
    formatos_tritongo = [
                            'VCVCVVVC','VCVCVVVV','VCVCVVV','CVCVCVVVV','CVCVCVVVC','CVCVCVVV',
                            'CVCVVV','CVCVVVV','CVCVVVC','VCVVVC','VCVVVC','VCVVV'
                        ]
    return verificar_formato(tritongos,formatos_tritongo,palavra)

def tem_ditongo_formato(palavra):
    ditongos_decrescentes = [
                                'ai','êi','ãi','ei','éi','oi','ói','ui','au','áu','eu',
                                'éu','iu','ou','ãe','ão','õe'
                            ]
    formatos_ditongo = ['CVCVVCV','VCVVCV','CVCVV','VCVV','CVVCV','CVV','VVCV','CVCCVVV']
    return verificar_formato(ditongos_decrescentes,formatos_ditongo,palavra)

def tem_hiato_vogais_duplas_formato(palavra):
    hiatos_vogais_duplas = [
                                'ea','eo','ia','ie','io','oa','oe','ua','ue','ui','uo', # hiatos
                                'aa','ee','ii','oo','uu' # vogais duplas
                           ]
    formatos_hiatos_vogais_duplas = ['CVVCV','VVCV','CVCVVCV','CVV','CVCCVVVCV','CVCVVVCV']
    return verificar_formato(hiatos_vogais_duplas,formatos_hiatos_vogais_duplas,palavra)

def tem_gu_qu(palavra):
    padroes = ['gu','qu']
    formatos_gu_qu = [
                        'CVCVVCV','CVCCVV','CVVCVCCV','VCVV','CVCVCCVV',
                        'CVCCVVCV','CCVCCVVCV','VCVVCCCV'
                    ]
    return verificar_formato(padroes,formatos_gu_qu,palavra)

def tem_bcdfgptv_lh_formato(palavra):
    padroes = [
                'br','bl','cr','cl','dr','fr','fl','gr','gl','pr','pl','tr','vr',
                'lh','nh','ch'
              ]
    formatos_bcdfgptv_lh = [
                            'CCVCV','CVCCV','CVCVCCV','CCVCCV','VCCVCV',
                            'CCVVCCV','CVCCV','CVCCVCV'
                           ]
    return verificar_formato(padroes,formatos_bcdfgptv_lh,palavra)

def tem_outros_formatos(palavra):
    formatos = [
                'CVCVC','VCV','VCCVCV','VCCVCVCVC','CVCCV','CVCCVCV','CVCCVCCV',
                'CVVCCV','CVCCVC','CVCVCCV','CVCCVCVV','CVCCCVCVV'
               ]
    for formato in formatos:
        if representacao_palavra(palavra) == formato:
            return True
    return False

def verificar_formato(padroes,formatos, palavra):
    for padrao in padroes:
        if padrao in palavra:
            for formato in formatos:
                if representacao_palavra(palavra) == formato:
                    return True
    return False

# Definindo novo formato para as palavras não-canônicas
def validar_formato(palavra):
    if canonicidade(palavra):
        return True
    else:
        if tem_ditongo_formato(palavra):
            return True
        if tem_gu_qu(palavra):
            return True
        if tem_tritongo_formato(palavra):
            return True
        if tem_hiato_vogais_duplas_formato(palavra):
            return True
        if tem_bcdfgptv_lh_formato(palavra):
            return True
        if tem_outros_formatos(palavra):
            return True
    return False