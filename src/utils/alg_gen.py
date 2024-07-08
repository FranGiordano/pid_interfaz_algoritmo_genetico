import copy
import random as rd
from enum import Enum


class ErrorPoblacionConIndividuosRechazados(Exception):
    pass


class Individuo:
    class Estado(Enum):
        ACEPTADO = 1
        RECHAZADO = 2

    # Constructor
    def __init__(self, bits, utilidades, pesos, peso_maximo):
        self.__bit_1 = bits[0]
        self.__bit_2 = bits[1]
        self.__bit_3 = bits[2]
        self.__bit_4 = bits[3]
        self.__utilidad = self.__calcular_utilidad(utilidades)
        self.__peso = self.__calcular_peso(pesos)
        self.__estado = self.__calcular_estado(peso_maximo)

    # Getters
    def get_utilidad(self):
        return self.__utilidad

    def get_peso(self):
        return self.__peso

    def get_estado(self):
        return self.__estado

    def get_bits(self):
        return [self.__bit_1, self.__bit_2, self.__bit_3, self.__bit_4]

    # Metodos privados
    def __calcular_estado(self, peso_maximo):
        if self.__peso > peso_maximo:
            return self.Estado.RECHAZADO
        else:
            return self.Estado.ACEPTADO

    def __calcular_utilidad(self, utilidades):
        return (self.__bit_1 * utilidades[0] +
                self.__bit_2 * utilidades[1] +
                self.__bit_3 * utilidades[2] +
                self.__bit_4 * utilidades[3])

    def __calcular_peso(self, pesos):
        return (self.__bit_1 * pesos[0] +
                self.__bit_2 * pesos[1] +
                self.__bit_3 * pesos[2] +
                self.__bit_4 * pesos[3])

    # Metodos publicos
    def mutar_individuo(self, probabilidad_mutacion, utilidades, pesos, peso_maximo):

        prob_mutaciones = [rd.random() for _ in range(4)]

        if prob_mutaciones[0] < probabilidad_mutacion:
            self.__bit_1 = 1 - self.__bit_1
        if prob_mutaciones[1] < probabilidad_mutacion:
            self.__bit_2 = 1 - self.__bit_2
        if prob_mutaciones[2] < probabilidad_mutacion:
            self.__bit_3 = 1 - self.__bit_3
        if prob_mutaciones[3] < probabilidad_mutacion:
            self.__bit_4 = 1 - self.__bit_4

        self.__utilidad = self.__calcular_utilidad(utilidades)
        self.__peso = self.__calcular_peso(pesos)
        self.__estado = self.__calcular_estado(peso_maximo)

        return prob_mutaciones


class Cruzador:

    # Constructor
    def __init__(self, probabilidad_cruce, probabilidad_mutacion, utilidades, pesos, peso_maximo, nro_poblacion_padres,
                 nro_cruce):
        self.__probabilidad_cruce = probabilidad_cruce
        self.__probabilidad_mutacion = probabilidad_mutacion
        self.__utilidades = utilidades
        self.__pesos = pesos
        self.__peso_maximo = peso_maximo
        self.__nro_poblacion_padres = nro_poblacion_padres
        self.__nro_cruce = nro_cruce
        self.__prob_cruce = rd.random()
        self.__prob_ind_1 = rd.random()
        self.__prob_ind_2 = rd.random()
        self.__bits_individuo_padre1 = None
        self.__bits_individuo_padre2 = None
        self.__cruzo = None
        self.__nro_ind_padre1 = None
        self.__nro_ind_padre2 = None
        self.__punto_corte = None
        self.__bits_padre_1_izq = None
        self.__bits_padre_1_der = None
        self.__bits_padre_2_izq = None
        self.__bits_padre_2_der = None
        self.__probabilidad_mutaciones_1 = None
        self.__probabilidad_mutaciones_2 = None
        self.__bits_individuo_hijo1 = None
        self.__bits_individuo_hijo2 = None
        self.__peso_hijo1 = None
        self.__peso_hijo2 = None
        self.__hijo1_aceptado = None
        self.__hijo2_aceptado = None
        self.__nro_hijo1 = None
        self.__nro_hijo2 = None

    # Getters
    def get_data_cruce(self):
        data = {
            "nro_poblacion_padres": self.__nro_poblacion_padres,
            "nro_cruce": self.__nro_cruce,
            "probabilidad_cruce": self.__probabilidad_cruce,
            "probabilidad_mutacion": self.__probabilidad_mutacion,
            "prob_cruce": self.__prob_cruce,
            "cruzo": self.__cruzo,
            "prob_ind_1": self.__prob_ind_1,
            "prob_ind_2": self.__prob_ind_2,
            "bits_individuo_padre1": self.__bits_individuo_padre1,
            "bits_individuo_padre2": self.__bits_individuo_padre2,
            "nro_ind_padre1": self.__nro_ind_padre1,
            "nro_ind_padre2": self.__nro_ind_padre2,
            "punto_corte": self.__punto_corte,
            "bits_padre_1_izq": self.__bits_padre_1_izq,
            "bits_padre_1_der": self.__bits_padre_1_der,
            "bits_padre_2_izq": self.__bits_padre_2_izq,
            "bits_padre_2_der": self.__bits_padre_2_der,
            "probabilidad_mutaciones_1": self.__probabilidad_mutaciones_1,
            "probabilidad_mutaciones_2": self.__probabilidad_mutaciones_2,
            "bits_individuo_hijo1": self.__bits_individuo_hijo1,
            "bits_individuo_hijo2": self.__bits_individuo_hijo2,
            "peso_hijo1": self.__peso_hijo1,
            "peso_hijo2": self.__peso_hijo2,
            "hijo1_aceptado": self.__hijo1_aceptado,
            "hijo2_aceptado": self.__hijo2_aceptado
        }
        return data

    # Metodos privados
    @staticmethod
    def __seleccionar_padres(self, individuos, prob_acum, prob):

        for i in range(1, 4):
            if prob_acum[i - 1] < prob < prob_acum[i]:
                bits_individuo_padre = individuos[i].get_bits()
                nro_ind_padre = i + 1
                break
        else:
            bits_individuo_padre = individuos[0].get_bits()
            nro_ind_padre = 1

        return bits_individuo_padre, nro_ind_padre

    @staticmethod
    def __cortar_individuo(bits, punto_corte):
        if punto_corte < 0.33:
            return bits[:1], bits[1:]
        elif punto_corte < 0.66:
            return bits[:2], bits[2:]
        else:
            return bits[:3], bits[3:]

    # Metodos publicos
    def cruzar(self, individuos, prob_acum):

        self.__bits_individuo_padre1, self.__nro_ind_padre1 = self.__seleccionar_padres(self, individuos, prob_acum,
                                                                                        self.__prob_ind_1)
        self.__bits_individuo_padre2, self.__nro_ind_padre2 = self.__seleccionar_padres(self, individuos, prob_acum,
                                                                                        self.__prob_ind_2)

        if self.__prob_cruce >= self.__probabilidad_cruce:
            individuo_hijo1 = Individuo(self.__bits_individuo_padre1, self.__utilidades, self.__pesos,
                                        self.__peso_maximo)
            individuo_hijo2 = Individuo(self.__bits_individuo_padre2, self.__utilidades, self.__pesos,
                                        self.__peso_maximo)
            self.__cruzo = False
        else:
            self.__punto_corte = rd.random()
            self.__bits_padre_1_izq, self.__bits_padre_1_der = self.__cortar_individuo(self.__bits_individuo_padre1,
                                                                                       self.__punto_corte)
            self.__bits_padre_2_izq, self.__bits_padre_2_der = self.__cortar_individuo(self.__bits_individuo_padre2,
                                                                                       self.__punto_corte)
            individuo_hijo1 = Individuo([*self.__bits_padre_1_izq, *self.__bits_padre_2_der], self.__utilidades,
                                        self.__pesos, self.__peso_maximo)
            individuo_hijo2 = Individuo([*self.__bits_padre_2_izq, *self.__bits_padre_1_der], self.__utilidades,
                                        self.__pesos, self.__peso_maximo)
            self.__cruzo = True

        self.__probabilidad_mutaciones_1 = individuo_hijo1.mutar_individuo(self.__probabilidad_mutacion,
                                                                           self.__utilidades, self.__pesos,
                                                                           self.__peso_maximo)
        self.__probabilidad_mutaciones_2 = individuo_hijo2.mutar_individuo(self.__probabilidad_mutacion,
                                                                           self.__utilidades, self.__pesos,
                                                                           self.__peso_maximo)
        self.__bits_individuo_hijo1 = individuo_hijo1.get_bits()
        self.__bits_individuo_hijo2 = individuo_hijo2.get_bits()
        self.__peso_hijo1 = individuo_hijo1.get_peso()
        self.__peso_hijo2 = individuo_hijo2.get_peso()
        self.__hijo1_aceptado = individuo_hijo1.get_estado() == Individuo.Estado.ACEPTADO
        self.__hijo2_aceptado = individuo_hijo2.get_estado() == Individuo.Estado.ACEPTADO

        return individuo_hijo1, individuo_hijo2


class Poblacion:

    # Constructor
    def __init__(self, individuo1, individuo2, individuo3, individuo4, nro_poblacion):

        for individuo in [individuo1, individuo2, individuo3, individuo4]:
            if individuo.get_estado() == Individuo.Estado.RECHAZADO:
                raise ErrorPoblacionConIndividuosRechazados("No se puede crear una población con individuos rechazados")

        self.__individuos = [individuo1, individuo2, individuo3, individuo4]
        self.__nro_poblacion = nro_poblacion
        self.__probabilidades = self.__calcular_probabilidades()
        self.__probabilidades_acumuladas = self.__calcular_probabilidades_acumuladas()

    # Getters
    def get_nr_poblacion(self):
        return self.__nro_poblacion

    def get_probabilidades(self):
        return self.__probabilidades

    def get_probabilidades_acumuladas(self):
        return self.__probabilidades_acumuladas

    def get_copy_individuos(self):
        return copy.deepcopy(self.__individuos)

    def get_data_poblacion(self):
        data = {'nro_poblacion': self.__nro_poblacion,
                'individuos': []}
        for i in range(4):
            bits = self.__individuos[i].get_bits()
            data['individuos'].append({
                'Individuo': f'Individuo {i + 1}',
                '1': bits[0],
                '2': bits[1],
                '3': bits[2],
                '4': bits[3],
                'Z': self.__individuos[i].get_utilidad(),
                'Peso': self.__individuos[i].get_peso(),
                'Prob': self.__probabilidades[i],
                'Prob Acum': self.__probabilidades_acumuladas[i]
            })
        return data

    def get_data_mayor_utilidad(self):

        mayor_utilidad = 0
        individuo_mayor_utilidad = self.__individuos[0]

        for individuo in self.__individuos:
            if individuo.get_utilidad() > mayor_utilidad:
                mayor_utilidad = individuo.get_utilidad()
                individuo_mayor_utilidad = individuo

        return {
            'Individuo': f'Individuo {self.__individuos.index(individuo_mayor_utilidad) + 1}',
            'Bits': individuo_mayor_utilidad.get_bits(),
            'Utilidad': individuo_mayor_utilidad.get_utilidad(),
            'Peso': individuo_mayor_utilidad.get_peso(),
            'NroPoblacion': self.__nro_poblacion
        }

    # Metodos privados
    def __calcular_probabilidades(self):
        utilidades = [individuo.get_utilidad() for individuo in self.__individuos]
        suma_utilidades = sum(utilidades)
        if suma_utilidades == 0:
            return [0, 0, 0, 0]
        return [utilidad / suma_utilidades for utilidad in utilidades]

    def __calcular_probabilidades_acumuladas(self):
        probabilidades_acumuladas = [self.__probabilidades[0]]
        for i in range(1, 4):
            probabilidades_acumuladas.append(probabilidades_acumuladas[i - 1] + self.__probabilidades[i])
        return probabilidades_acumuladas


class AlgGenMochila:

    # Constructor
    def __init__(self,
                 utilidades,
                 pesos,
                 capacidad_mochila,
                 probabilidad_cruce,
                 probabilidad_mutacion,
                 matriz_individuos,
                 semilla=None):

        if semilla is not None:
            rd.seed(semilla)
        self.__utilidades = utilidades
        self.__pesos = pesos
        self.__capacidad_mochila = capacidad_mochila
        self.__probabilidad_cruce = probabilidad_cruce
        self.__probabilidad_mutacion = probabilidad_mutacion
        self.__matriz_individuos = matriz_individuos
        self.__poblacion = None
        self.__data = {
            'Poblaciones': [],
            'Cruces': [],
            'Solucion': None
        }
        self.__crear_poblacion(self.__matriz_individuos, 0)

    # Getters
    def get_data(self):
        return self.__data

    # Metodos privados
    def __crear_poblacion(self, individuos, nro_poblacion):
        individuo1 = Individuo(individuos[0], self.__utilidades, self.__pesos, self.__capacidad_mochila)
        individuo2 = Individuo(individuos[1], self.__utilidades, self.__pesos, self.__capacidad_mochila)
        individuo3 = Individuo(individuos[2], self.__utilidades, self.__pesos, self.__capacidad_mochila)
        individuo4 = Individuo(individuos[3], self.__utilidades, self.__pesos, self.__capacidad_mochila)
        self.__poblacion = Poblacion(individuo1, individuo2, individuo3, individuo4, nro_poblacion)
        self.__data['Poblaciones'].append(self.__poblacion.get_data_poblacion())

    def __iterate(self):

        cantidad_hijos_aceptados = 0
        nro_cruce = 0
        individuos_aceptados = []
        nro_poblacion_padres = self.__poblacion.get_nr_poblacion()
        individuos = self.__poblacion.get_copy_individuos()
        prob_acum = self.__poblacion.get_probabilidades_acumuladas()

        while cantidad_hijos_aceptados < 4:

            nro_hijo1, nro_hijo2 = None, None
            nro_cruce += 1
            cruzador = Cruzador(self.__probabilidad_cruce,
                                self.__probabilidad_mutacion,
                                self.__utilidades,
                                self.__pesos,
                                self.__capacidad_mochila,
                                nro_poblacion_padres,
                                nro_cruce)
            hijo1, hijo2 = cruzador.cruzar(individuos, prob_acum)
            if hijo1.get_estado() == Individuo.Estado.ACEPTADO:
                cantidad_hijos_aceptados += 1
                nro_hijo1 = cantidad_hijos_aceptados
                individuos_aceptados.append(hijo1)
            if hijo2.get_estado() == Individuo.Estado.ACEPTADO:
                individuos_aceptados.append(hijo2)
                cantidad_hijos_aceptados += 1
                nro_hijo2 = cantidad_hijos_aceptados
            data_cruce = cruzador.get_data_cruce()
            data_cruce['nro_hijo1'] = nro_hijo1
            data_cruce['nro_hijo2'] = nro_hijo2
            self.__data['Cruces'].append(data_cruce)

        self.__crear_poblacion([ind.get_bits() for ind in individuos_aceptados], nro_poblacion_padres + 1)

    # Metodos publicos
    def run(self, cantidad_iteraciones):

        mejor_individuo_alg = self.__poblacion.get_data_mayor_utilidad()

        for i in range(cantidad_iteraciones):
            self.__iterate()

            mejor_individuo_poblacion = self.__poblacion.get_data_mayor_utilidad()
            if mejor_individuo_poblacion['Utilidad'] > mejor_individuo_alg['Utilidad']:
                mejor_individuo_alg = mejor_individuo_poblacion

        self.__data['Solucion'] = mejor_individuo_alg


if __name__ == '__main__':
    utilidades = [1, 2, 3, 4]
    pesos = [1, 2, 3, 4]
    capacidad_mochila = 7
    probabilidad_cruce = 0.98
    probabilidad_mutacion = 0.1
    matriz_individuos = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 1], [1, 0, 1, 0]]
    semilla = 0
    cantidad_iteraciones = 2

    alg_gen = AlgGenMochila(utilidades, pesos, capacidad_mochila, probabilidad_cruce, probabilidad_mutacion,
                            matriz_individuos, semilla)
    alg_gen.run(cantidad_iteraciones)

    import json

    with open('result.json', 'w') as fp:
        json.dump(alg_gen.get_data(), fp)
