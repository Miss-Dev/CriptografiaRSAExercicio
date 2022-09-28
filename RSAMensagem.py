class RSAMensagem:
    def __init__(self, mensagem: list, dict_valores: dict):
        self.mensagem = mensagem
        self.dict_valores = dict_valores

    def transforma_em_texto_criptografado(self):
        try:
            mensagem_criptografada = []
            for i in self.mensagem:
                mensagem_criptografada.append(str((i ** self.dict_valores['e']) % self.dict_valores['n']))
            return mensagem_criptografada
        except Exception:
            print("Erro ao tentar criptografar a mensagem")

    def decripta_mensagem(self, mensagem_encript):

        try:
            mensagem_decriptada = []
            for i in mensagem_encript:
                mensagem_decriptada.append((int(i) ** self.dict_valores['d']) % self.dict_valores['n'])

            return mensagem_decriptada
        except Exception:
            print("Erro ao tentar decriptar a mensagem")

    def retorna_mensagem_encriptada(self):
        return self.transforma_em_texto_criptografado()

    def retorna_mensagem_decriptada(self, mensagem_decript):
        return self.decripta_mensagem(mensagem_decript)
