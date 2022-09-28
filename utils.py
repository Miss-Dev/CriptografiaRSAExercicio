def transforma_mensagem_ascii(mensagem: str):
    lista_ascii = []
    for i in mensagem:
        lista_ascii.append(ord(i))
    return lista_ascii


def transforma_ascii_msg(lista_ascii: list):
    texto = ''
    for i in lista_ascii:
        texto += chr(i)
    return texto
