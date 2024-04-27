
class Poblacion:
    def __init__(self, numero, peso, utilidad):
        self.peso = peso
        self.utilidad = utilidad
        self.numero = numero

    def __str__(self):
        res = "Binario: " + f'{str(self.numero):<10}' "Peso: " + f'{str(self.peso):<10}' "Utilidad: " + f'{str(self.utilidad):<10}'
        return res


def validar(inf, sup, tipo, mensaje="", msj_error=""):
    n = inf
    while n <= inf or n > sup:
        n = tipo(input(mensaje))
        if n <= inf or n > sup:
            print(msj_error)
    return n


def validar_inf(inf, tipo, mensaje="", msj_error=""):
    n = inf
    while n <= inf:
        n = tipo(input(mensaje))
        if n <= inf:
            print(msj_error)
    return n
