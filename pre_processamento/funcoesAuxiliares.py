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
    """Representação da palavra em vogais e consoantes.
        Sintaxe:
            rep_palavra = representacao_palavra(palavra)
        Descrição:
            Representa uma dada palavra classificando cada uma de suas letras em vogal (V) ou consoante (C).
        Args:
            palavra (string): Palavra a ser representada em vogais e consoantes.
        Retornos:
            string: Representação da palavra em vogais e consoantes.
    """
    v_letras = ""
    for l in palavra:
        if vogal(l):
            v_letras += 'V'
        else:
            v_letras += 'C'
    return v_letras

def hifen(palavra):
    """Verificador da presença de hífen na palavra.
        Sintaxe:
            verificacao = hifen(palavra)
        Descrição:
            Verifica se a palavra tem ou não pelo menos um hífen.
        Args:
            palavra (string): Palavra a ser verificada.
        Retornos:
            verificacao (bool): True (se a palavra tem hífen), False (se a palavra não tem hífen).
    """
    if '-' in palavra:
        return True
    else:
        return False

def maiuscula(palavra):
    """Verificador da presença de letra maiúscula na palavra.
        Sintaxe:
            verificacao = maiuscula(palavra)
        Descrição:
            Verifica se a palavra tem ou não pelo menos uma letra maiúscula.
        Args:
            palavra (string): Palavra a ser verificada.
        Retornos:
            verificacao (bool): True (se a palavra tem letra maiúscula), False (se a palavra não tem letra maiúscula).
    """
    for l in palavra:
        codigo_ascii = ord(l)
        if (codigo_ascii >= 65 and codigo_ascii <= 90) or (l in "ÁÉÍÓÚ"):
            return True
    return False

def min_threshold_letras(min, palavra):
    """Verificador do número mínimo de letras de uma palavra.
        Sintaxe:
            verificacao = min_threshold(palavra)
        Descrição:
            Verifica se a palavra possui o mínimo de letras desejado.
        Args:
            min (int): número mínimo de letras que a palavra deve ter.
            palavra (string): Palavra a ser verificada.
        Retornos:
            verificacao (bool): True (se a palavra atende ao threshold), False (se a palavra não atende ao threshold).
    """
    if len(palavra) >= min:
        return True
    else:
        return False
        
def canonicidade(palavra):
    """Verificador da canonicidade de uma palavra.
        Sintaxe:
            verificacao = canonicidade(palavra)
        Descrição:
            Verifica se a palavra possui ou não formato CV (consoante-vogal) em suas sílabas.
        Args:
            palavra (string): Palavra a ser verificada.
        Retornos:
            verificacao (bool): True (se a palavra é canônica), False (se a palavra não é canônica).
    """
    t = len(palavra)
    if t % 2 != 0 or vogal(palavra[0]):
        return False
    else:
        for i in range(t):
            if vogal(palavra[i]) != (i%2 != 0):
                return False
        return True

def vogal(letra):
    """Verificador da natureza da letra.
        Sintaxe:
            verificacao = vogal(letra)
        Descrição:
            Verifica se uma letra é uma vogal.
        Args:
            letra (string): Letra a ser verificada.
        Retornos:
            verificacao (bool): True (se a letra é uma vogal), False (se a letra não é uma vogal).
    """
    if letra in "aeiouáéíóúâêôã":
        return True
    else:
        return False

def hiato_final_palavra(palavra):
    """Verificador da presença de hiato no final de uma palavra.
        Sintaxe:
            verificacao = hiato_final_palavra(palavra)
        Descrição:
            Verifica se a palavra possui hiato em sua terminação.
        Args:
            palavra (string): Palavra a ser verificada.
        Retornos:
            verificacao (bool): True (se a palavra tem hiato no final), False (se a palavra não hiato no final).
    """
    hiatos = ['ea','eo','ia','ie','io','oa','oe','ua','ue','ui','uo']
    for h in hiatos:
        re_match_object = re.search(h,palavra)
        if re_match_object is not None:
            if re_match_object.end() == len(palavra):
                return True
    return False

def prefixos(palavra):
    """Verificador da presença de prefixos conhecidos na palavra.
        Sintaxe:
            verificacao = prefixos(palavra)
        Descrição:
            Verifica se a palavra tem ou não algum prefixo conhecido.
        Args:
            palavra (string): Palavra a ser verificada.
        Retornos:
            verificacao (bool): True (se a palavra tem hífen), False (se a palavra não tem hífen).
    """
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
    """Verificador da presença de vogal na sílaba.
        Sintaxe:
            verificacao = silaba_tem_vogal(palavra)
        Descrição:
            Verifica se a sílaba tem ou não pelo menos uma vogal.
        Args:
            silaba (string): Sílaba a ser verificadas.
        Retornos:
            verificacao (bool): True (se a sílaba tem vogal), False (se a sílaba não tem vogal).
    """
    vogais = "aeiouáéíóúâêôã"
    for v in vogais:
        if v in silaba:
            return True
    return False

def verifica_silabas(silabas):
    """Verificador da presença de vogal nas sílabas da palavra.
        Sintaxe:
            verificacao = verifica_silabas(palavra)
        Descrição:
            Verifica se as sílabas da palavra tem ou não pelo menos uma vogais.
        Args:
            silabas (string): Sílabasa a serem verificadas.
        Retornos:
            verificacao (bool): True (se as sílabas tem vogal), False (se as sílabas não tem vogal).
    """
    for silaba in silabas:
        if not silaba_tem_vogal(silaba):
            return False
    return True

#--------------------------------------------------------------------------------------------------#
## Funções que definem os formatos das palavras que serão lidas
def tem_tritongo(palavra):
    """Verificador da presença de tritongo na palavra.
        Sintaxe:
            verificacao = tem_tritongo(palavra)
        Descrição:
            Verifica se a palavra tem ou não um tritongo.
        Args:
            palavra (string): Palavra a ser verificada.
        Retornos:
            verificacao (bool): True (se a palavra tem tritongo), False (se a palavra não tem tritongo).
    """
    return verificar_formato(tritongos,formatos_tritongo,palavra)

def tem_ditongo(palavra):
    """Verificador da presença de ditongo na palavra.
        Sintaxe:
            verificacao = tem_ditongo(palavra)
        Descrição:
            Verifica se a palavra tem ou não um ditongo.
        Args:
            palavra (string): Palavra a ser verificada.
        Retornos:
            verificacao (bool): True (se a palavra tem ditongo), False (se a palavra não tem ditongo).
    """
    return verificar_formato(ditongos_decrescentes,formatos_ditongo,palavra)

def tem_hiato_vogais_duplas(palavra):
    """Verificador da presença de hiatos ou vogais duplas na palavra.
        Sintaxe:
            verificacao = tem_hiato_vogais_duplas(palavra)
        Descrição:
            Verifica se a palavra tem ou não um hiato ou vogais duplas.
        Args:
            palavra (string): Palavra a ser verificada.
        Retornos:
            verificacao (bool): True (se a palavra tem hiato ou vogais duplas), False (se a palavra não tem hiato ou vogais duplas).
    """
    return verificar_formato(hiatos_vogais_duplas,formatos_hiatos_vogais_duplas,palavra)

def tem_gu_qu(palavra):
    """Verificador da presença de gu ou qu na palavra.
        Sintaxe:
            verificacao = tem_gu_qu(palavra)
        Descrição:
            Verifica se a palavra tem ou não um gu ou qu.
        Args:
            palavra (string): Palavra a ser verificada.
        Retornos:
            verificacao (bool): True (se a palavra tem gu ou qu), False (se a palavra não tem gu ou qu).
    """
    return verificar_formato(padroes_gu_qu,formatos_gu_qu,palavra)

def tem_consoante_indivisivel(palavra):
    """Verificador da presença de um padrão indivisível de encontros consonantais na palavra.
        Sintaxe:
            verificacao = tem_consoante_indivisivel(palavra)
        Descrição:
            Verifica se a palavra tem ou não um padrão indivisível de consoantes.
        Args:
            palavra (string): Palavra a ser verificada.
        Retornos:
            verificacao (bool): True (se a palavra tem padrão indivisível de consoantes), False (se a palavra não tem padrão indivisível de consoantes).
    """
    return verificar_formato(padroes_consoante_indivisivel,formatos_consoante_indivisivel,palavra)

def tem_cz_ps(palavra):
    """Verificador da presença de cz ou ps na palavra.
        Sintaxe:
            verificacao = tem_cz_ps(palavra)
        Descrição:
            Verifica se a palavra tem ou não um cz ou ps.
        Args:
            palavra (string): Palavra a ser verificada.
        Retornos:
            verificacao (bool): True (se a palavra tem cz ou ps), False (se a palavra não tem cz ou ps).
    """
    return verificar_formato(padroes_cz_ps,formatos_cz_ps,palavra)

def tem_outros_formatos(palavra):
    """Verificador da presença de outros formatos na palavra.
        Sintaxe:
            verificacao = tem_outros_formatos(palavra)
        Descrição:
            Verifica se a palavra tem ou não outros formatos.
        Args:
            palavra (string): Palavra a ser verificada.
        Retornos:
            verificacao (bool): True (se a palavra tem outros formatos), False (se a palavra não tem outros formatos).
    """
    count = 0
    for formato in outros_formatos:
        if representacao_palavra(palavra) == formato:
            return (True,count)
        count += 1
    return (False,None)

def verificar_formato(padroes,formatos, palavra):
    """Verificador da validade do formato de uma palavra.
        Sintaxe:
            (verificador,indice_formato) = verificar_formato(padroes,formatos,palavra)
        Descrição:
            Verifica se a palavra tem ou não um gu ou qu.
        Args:
            padroes (list): Padrões pré-definidos que a palavra pode conter
            formatos (list): Formatos pré-definidos que a palavra deve ter
            palavra (string): Palavra a ser verificada.
        Retornos:
            verificacao (bool): True (se a palavra tem formato válido), False (se a palavra não tem formato válido).
            indice_formato (int): Índice do formato na lista onde foi encontrado. 
    """
    count = 0
    for padrao in padroes:
        if padrao in palavra:
            for formato in formatos:
                if representacao_palavra(palavra) == formato:
                    return (True,count)
                count += 1
    return (False,None)

def validar_formato(palavra):
    """Verificador do formato de uma palavra.
        Sintaxe:
            verificacao = validar_formato(palavra)
        Descrição:
            Verifica se a palavra tem ou não um formato válido.
        Args:
            palavra (string): Palavra a ser verificada.
        Retornos:
            verificacao (bool): True (se a palavra tem formato válido), False (se a palavra não tem formato válido).
    """
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
    """Aplica o processo de hifenização na sílaba com formato = formato (função auxiliar).
        Sintaxe:
            separa_formato(palavra)
        Descrição:
            Aplica o processo de hifenização em uma palavra com dado formato.
        Args:
            palavra (string): Palavra a ser hifenizada.
        Retornos:
            None: None.
    """
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
    """Separador de palavra em sílabas.
        Sintaxe:
            silabas = separa_em_silabas(palavra)
        Descrição:
            Aplica o processo de hifenização em uma palavra.
        Args:
            palavra (string): Palavra a ser verificada.
        Retornos:
            silabas (list): Sílabas da palavra. 
    """
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
    """Verificador da presença de acento na palavra.
        Sintaxe:
            verificacao = tem_acento(palavra)
        Descrição:
            Verifica se a palavra tem ou não um acento.
        Args:
            palavra (string): Palavra a ser verificada.
        Retornos:
            verificacao (bool): True (se a palavra tem acento), False (se a palavra não tem acento).
    """
    acentos = 'áéíóúâêô'
    for acento in acentos:
        re_match_object = re.search(acento,palavra)
        if re_match_object is not None:
            return True,re_match_object.start()
    return False,None

def oxitona(silaba):
    """Verifica se a sílaba é oxítona.
        Sintaxe:
            verificacao = oxitona(palavra)
        Descrição:
            Verifica se a sílaba indica ou não uma oxítona.
        Args:
            palavra (string): Sílaba a ser verificada.
        Retornos:
            verificacao (bool): True (se a sílaba tem um indicador), False (se a sílaba não tem um indicador).
    """
    terminacoes = ['r','l','z','x','i','u','im','um','om']
    for terminacao in terminacoes:
        if verificar_terminacao(silaba,terminacao):
            return True
    return False

def paroxitona(silaba):
    """Verifica se a sílaba é paroxítona.
        Sintaxe:
            verificacao = paroxitona(palavra)
        Descrição:
            Verifica se a sílaba indica ou não uma paroxítona.
        Args:
            palavra (string): Sílaba a ser verificada.
        Retornos:
            verificacao (bool): True (se a sílaba tem um indicador), False (se a sílaba não tem um indicador).
    """
    terminacoes = ['o','os','a','as','e','es']
    for terminacao in terminacoes:
        if verificar_terminacao(silaba,terminacao):
            return True
    return False

def verificar_terminacao(silaba,terminacao):
    """Verifica se a sílaba tem uma determinada terminação.
        Sintaxe:
            verificacao = verificar_terminacao(palavra)
        Descrição:
            Verifica se a sílaba tem ou não uma determinada terminação.
        Args:
            palavra (string): Sílaba a ser verificada.
        Retornos:
            verificacao (bool): True (se a sílaba tem a terminação), False (se a sílaba não tem a terminação).
    """
    t_terminacao = len(terminacao)
    t_silaba = len(silaba)
    if t_terminacao > t_silaba:
        return False
    if t_terminacao == t_silaba:
        return terminacao in silaba
    if t_terminacao < t_silaba:
        return terminacao == silaba[-t_terminacao:]

def tonicidade(palavra):
    """Verifica a tonicidade da palavra.
        Sintaxe:
            classificacao = tonicidade(palavra)
        Descrição:
            Classifica a palavra quanto a sua tonicidade (proparoxítona, paroxítona ou oxítona).
        Args:
            palavra (string): Palavra a ser verificada.
        Retornos:
            classificacao (string): Classificação da tonicidade da palavra.
    """
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