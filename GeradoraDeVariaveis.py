class GeradoraDeVariaveis:
    z = 0
    n = 0
    e = 0
    d = 0

    def __init__(self, p: int, q: int):
        self.p = p
        self.q = q

    def gerarN(self):
        self.n = self.p * self.q

    def gerarZ(self):
        self.z = (self.p - 1) * (self.q - 1)

    def gerarD(self):
        try:
            for i in range(10):
                x = 1 + (i * self.z)
                if x % self.e == 0:
                    self.d = int(x / self.e)
                    break
        except Exception:
            print("Erro ao gerar o D")

    def gerarE(self):
        z = self.z
        e = 0
        for e in range(2, z):
            if recursivaE(e, z) == 1:
                break
        # print("Valor de e encontrado: ", e)
        self.e = e

    def calcular_valores(self):
        self.gerarN()
        self.gerarZ()
        self.gerarE()
        self.gerarD()

    def retornar_valores_calculados(self) -> dict:
        self.calcular_valores()
        dict_chaves = {'e': self.e, 'd': self.d, 'n': self.n}
        return dict_chaves


def recursivaE(e: int, z: int) -> int:
    if e == 0:
        return z
    else:
        return recursivaE(z % e, e)
