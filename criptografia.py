from caracteres import lista_caracteres as chars



def pesquisar_letra(str, dict=chars):
    """Realiza a busca da letra e retorna o valor correspondente.

    Args:
        str (string): Letra a ser pesquisada.
        dict (dictionary, opcional): Lista de caracteres padrão.
    
    Returns:
        int: Número referente a letra.
    """
    # Realiza a busca por chave específica.
    return dict.get(str)


def pesquisar_numero(int, dict=chars):
    """
        Realiza uma busca no dicionário pelo número atribuído à letra. Retorna a letra correspondente.

        Args:
            int (int): Número a ser pesquisado.
            dict (dictionary, opcional): Lista de caracteres padrão.
        
        Returns:
            str: Letra.
    """
    for k, v in dict.items():
        if v == int:
            return k


def separar_letras(str):
    """Separa as letras de uma frase.

    Args:
        str (str): Frase que será separada em letras.

    Returns:
        list: Lista com letras separadas em índices.
    """
    letras = []

    for i in str:
        letras.append(i)
    
    return letras


def montar_frase(str):
    """Monta uma frase a partir de letras separadas (ou avulsas) por índices de uma lista.

    Args:
        str (str): Letras avulsas ou lista com letras separadas.

    Returns:
        str: Frase completa.
    """
    frase = ''
    
    for letras in str:
        frase += letras
    
    return frase



def cifra_cesar(rot, str):
    """Realiza a criptografia baseada na Cifra de César.

    Args:
        key (int): Chave na qual será baseada a criptografia.
        str (str): String que será criptografada.

    Returns:
        str: String criptografada
    """
    # Separando as letras em uma frase para atribuir a chave pra cada letra.
    frase = separar_letras(str)

    nova_frase = ''
    for l in frase:

        # Pesquisando o número correspondente de cada letra no dicionário.
        letra = pesquisar_letra(l)
        # Atribuindo a chave para realizar a criptografia, retornando um novo valor que será uma nova letra.
        k = rot + letra
        # Realizando a busca de acordo com a soma da chave e do valor da letra, retornando a letra que corresponde a esse novo valor.
        nova_letra = pesquisar_numero(k)

        # Montando uma nova frase com as letras sendo trocadas.
        nova_frase += montar_frase(nova_letra)

    return(nova_frase)