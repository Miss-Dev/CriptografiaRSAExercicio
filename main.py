from GeradoraDeVariaveis import GeradoraDeVariaveis
from RSAMensagem import RSAMensagem
from utils import *

geradoraVariaveis = GeradoraDeVariaveis(487, 599)
dict_valores = geradoraVariaveis.retornar_valores_calculados()
mensagem = input('Digite o mensagem para encriptar: ')

lista = transforma_mensagem_ascii(mensagem)

rsa_msg = RSAMensagem(lista, dict_valores)
msg_encript = rsa_msg.retorna_mensagem_encriptada()
msg_decript = rsa_msg.retorna_mensagem_decriptada(msg_encript)

print("Mensagem encriptada: ", ''.join(msg_encript))
print("Mensagem decriptada: ", transforma_ascii_msg(msg_decript))