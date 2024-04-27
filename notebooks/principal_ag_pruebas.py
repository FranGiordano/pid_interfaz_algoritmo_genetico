from modulo_ag import *
import random


"""def iteracion(prob_padre, prob_ac1, prob_ac2, prob_ac3, prob_ac4, vect1, vect2, vect3, vect4):
    if prob_padre <= prob_ac1:
        vector = vect1
        num = 1
        prob = round(prob_ac1, 4)
    else:
        if prob_padre <= prob_ac2:
            vector = vect2
            num = 2
            prob = round(prob_ac2, 4)
        else:
            if prob_padre <= prob_ac3:
                vector = vect3
                num = 3
                prob = round(prob_ac3, 4)
            else:
                vector = vect4
                num = 4
                prob = round(prob_ac4, 4)
    return num, vector, prob"""

"""def util_peso1_man(registro, num):
    for i in range(num):
        numer = validar(-1, 1, int, "Ingrese numeros binarios", "Error, numero incorrecto.")
        peso = 0
        utili = 0
        if numer == 0:
            peso = 0
            utili = 0
        else:
            if i == 0:
                peso = 7
                utili = 4
            if i == 1:
                peso = 6
                utili = 5
            if i == 2:
                peso = 8
                utili = 6
            if i == 3:
                peso = 2
                utili = 3
        pobla = Poblacion(numer, peso, utili)
        registro.append(pobla)


def peso_utilidades_man(reg1, reg2, reg3, reg4, num):
    print("Cromosoma1")
    util_peso1_man(reg1, num)
    print("Cromosoma2")
    util_peso1_man(reg2, num)
    print("Cromosoma3")
    util_peso1_man(reg3, num)
    print("Cromosoma4")
    util_peso1_man(reg4, num)        
        """

def menu():

    print("\n*****************")
    print("MENU DE OPCIONES")
    print("1. Carga de datos de población")
    print("2. Mostrar Poblacion inicial ")
    print("3. Mostrar pesos y utilidades")
    print("4. Funcion Aptitud y Funcion Objetivo")
    print("5. Primera iteración")
    print("10. Salir")


def menu_vec():
    print("*****************\n")
    print("1. Cargar poblacion automaticamente")
    print("2. Cargar poblacion manualmente")


def menu_probabilidad():
    print("\n Probabilidad de cruce y mutacion::")
    print("1. Cargar automaticamente")
    print("2. Cargar manualmente")


def generar_probabilidades(op_prob):
    prob_cruce = 0
    prob_mutacion = 0
    if op_prob == 1:
        prob_cruce = 0.98
        prob_mutacion = 0.1
        #prob_cruce = random.uniform(0.95, 0.99)
        #prob_mutacion = random.uniform(0.001, 0.008)
    if op_prob == 2:
        print("Probalidad de cruce entre 0.95 y 0.99")
        print("Probalidad de mutacion entre 0.002 y 0.008")
        prob_cruce = validar(0.94, 0.99, float, "Ingrese la probabilidad de cruce(3 decimales):", "Fuera de rango")
        prob_mutacion = validar(0.001, 0.009, float, "Ingrese la probabilidad de mutacion(3 decimales):", "Fuera de rango")
    return round(prob_cruce, 3), round(prob_mutacion, 3)


def mostrar(vector1, vector2, vector3, vector4):
    print("Cromosomas1", vector1)
    print("Cromosomas2", vector2)
    print("Cromosomas3", vector3)
    print("Cromosomas4", vector4)


#CARGAR Y MOSTRAR MANUALMENTE CROMOSOMAS
def util_peso1_manualmente(vector_peso, vector_utilid, registro, num):
    for i in range(num):
        numer = validar(-1, 1, int, "Ingrese numeros binarios", "Error, numero incorrecto.")
        if numer == 0:
            peso = 0
            utili = 0
        else:
            if i == 0:
                peso = vector_peso[i]
                utili = vector_utilid[i]
            if i == 1:
                peso = vector_peso[i]
                utili = vector_utilid[i]
            if i == 2:
                peso = vector_peso[i]
                utili = vector_utilid[i]
            if i == 3:
                peso = vector_peso[i]
                utili = vector_utilid[i]
        pobla = Poblacion(numer, peso, utili)
        registro.append(pobla)


def peso_utilidades_manualmenteee(vector_peso, vector_util, reg1, reg2, reg3, reg4, num):
    for i in range(4):
        vector_peso.append(validar_inf(0, int, "Ingrese un valor peso: ", "Error, ingrese un valor entero y mayor a cero"))
    for i in range(4):
        vector_util.append(validar_inf(0, int, "Ingrese un valor utilidad: ", "Error, ingrese un valor entero y mayor a cero"))
    print("Cromosoma1")
    util_peso1_manualmente(vector_peso, vector_util, reg1, num)
    print("Cromosoma2")
    util_peso1_manualmente(vector_peso, vector_util, reg2, num)
    print("Cromosoma3")
    util_peso1_manualmente(vector_peso, vector_util, reg3, num)
    print("Cromosoma4")
    util_peso1_manualmente(vector_peso, vector_util, reg4, num)


#CARGAR Y MOSTRAR MANUALMENTE CROMOSOMAS
def util_peso1_autom(registro, num):
    for i in range(num):
        numer = random.randint(0, 1)
        peso = 0
        utili = 0
        if numer == 0:
            peso = 0
            utili = 0
        else:
            if i == 0:
                peso = 7
                utili = 4
            if i == 1:
                peso = 6
                utili = 5
            if i == 2:
                peso = 8
                utili = 6
            if i == 3:
                peso = 2
                utili = 3
        pobla = Poblacion(numer, peso, utili)
        registro.append(pobla)


def pesos_utilidades_auto(reg1, reg2, reg3, reg4, num):
    util_peso1_autom(reg1, num)
    util_peso1_autom(reg2, num)
    util_peso1_autom(reg3, num)
    util_peso1_autom(reg4, num)


def crear_vector(registro, n):
    vector = []
    for i in range(n):
        vector.append(registro[i].numero)
    return vector


def crear_vectores(reg1, reg2, reg3, reg4, n):
    vec1 = crear_vector(reg1, n)
    vec2 = crear_vector(reg2, n)
    vec3 = crear_vector(reg3, n)
    vec4 = crear_vector(reg4, n)
    return vec1, vec2, vec3, vec4


def mostrar_todo(vec):
    n = len(vec)
    for i in range(n):
        print(vec[i])


#FUNCION OBJETIVO/ APTITUD
def fun_apt(reg):
    suma = 0
    suma += reg.peso * reg.numero
    return suma

def funcion_objetivo(reg1, reg2, reg3, reg4):
    suma_1 = suma_2 = suma_3 = suma_4 = suma_tot = 0
    for i in range(len(reg1)):
        suma_1 += reg1[i].utilidad * reg1[i].numero
        suma_2 += reg2[i].utilidad * reg2[i].numero
        suma_3 += reg3[i].utilidad * reg3[i].numero
        suma_4 += reg4[i].utilidad * reg4[i].numero
    suma_tot += suma_1 + suma_2 + suma_3 + suma_4
    return suma_tot, suma_1, suma_2, suma_3, suma_4

def funcion_aptitud(reg1, reg2, reg3, reg4):
    suma_1 = suma_2 = suma_3 = suma_4 = 0
    for i in range(len(reg1)):
        suma_1 += reg1[i].peso * reg1[i].numero
        suma_2 += reg2[i].peso * reg2[i].numero
        suma_3 += reg3[i].peso * reg3[i].numero
        suma_4 += reg4[i].peso * reg4[i].numero
    return suma_1, suma_2, suma_3, suma_4


def probabilidad(total_par, total_final):
    probabilidad = round((total_par / total_final), 5)
    return probabilidad


def prob_acumulada(*args):
    suma = 0
    for i in range(len(args)):
        suma += args[i]
    return round(suma, 5)

"""
def info(vec1, vec2, vec3, vec4, total, total1, total2, total3, total4, apt1, apt2, apt3, apt4, cm):
    print("Cromosoma 1:", vec1, ":")
    print("Total utilidades: ", total1)
    print("Total peso: ", apt1)
    if apt1 > cm:
        print("Cromosoma No apto")
        apto1 = False
    else:
        apto1 = True
        print("Cromosoma apto")
    prob1 = probabilidad(total1, total)
    print("Probab Z: ", prob1)
    prob_acum1 = prob_acumulada(prob1)
    print("Probab acum: ", prob_acum1, "\n")

    print("Cromosoma 2:", vec2, ":")
    print("Total utilidades: ", total2)
    print("Total peso: ", apt2)
    if apt2 > cm:
        print("Cromosoma No apto")
        apto2 = False
    else:
        apto2 = True
        print("Cromosoma apto")
    prob2 = probabilidad(total2, total)
    print("Probab Z: ", prob2)
    prob_acum2 = prob_acumulada(prob1, prob2)
    print("Probab acum: ", prob_acum2, "\n")

    print("Cromosoma 3:", vec3, ":")
    print("Total utilidades: ", total3)
    print("Total peso: ", apt3)
    if apt3 > cm:
        print("Cromosoma No apto")
        apto3 = False
    else:
        apto3 = True
        print("Cromosoma apto")
    prob3 = probabilidad(total3, total)
    print("Probab Z: ", prob3)
    prob_acum3 = prob_acumulada(prob1, prob2, prob3)
    print("Probab acum: ", prob_acum3, "\n")

    print("Cromosoma 4:", vec4, ":")
    print("Total utilidades: ", total4)
    print("Total peso: ", apt4)
    if apt4 > cm:
        print("Cromosoma No apto")
        apto4 = False
    else:
        apto4 = True
        print("Cromosoma apto")
    prob4 = probabilidad(total4, total)
    print("Probab Z: ", prob4)
    prob_acum4 = prob_acumulada(prob1, prob2, prob3, prob4)
    print("Probab acum: ", prob_acum4, "\n")


    print("Sumatoria total de utilidades: ", total)
    return prob_acum1, prob_acum2, prob_acum3, prob_acum4, apto1, apto2, apto3, apto4
"""


def info(vec1, vec2, vec3, vec4, total, total_ut1, total_ut2, total_ut3, total_ut4, total_apt1, total_apt2, total_apt3, total_apt4, cm):
    vector_apt = []
    vector_apt.append(total_apt1)
    vector_apt.append(total_apt2)
    vector_apt.append(total_apt3)
    vector_apt.append(total_apt4)
    vector_util = []
    vector_util.append(total_ut1)
    vector_util.append(total_ut2)
    vector_util.append(total_ut3)
    vector_util.append(total_ut4)

    for i in range(4):
        if vector_apt[i] > cm:
            total -= vector_util[i]

    print("Cromosoma 1:", vec1, ":")
    print("Total utilidades: ", total_ut1)
    print("Total peso: ", total_apt1)
    if total_apt1 > cm:
        print("Cromosoma No apto")
        bandera_apto1 = False
        total_ut1 = 0
    else:
        print("Cromosoma apto")
        bandera_apto1 = True
    prob1 = probabilidad(total_ut1, total)
    print("Probab Z: ", prob1)
    prob_acum1 = prob_acumulada(prob1)
    print("Probab acum: ", prob_acum1, "\n")

    print("Cromosoma 1:", vec2, ":")
    print("Total utilidades: ", total_ut2)
    print("Total peso: ", total_apt2)
    if total_apt2 > cm:
        print("Cromosoma No apto")
        bandera_apto2 = False
        total_ut2 = 0
    else:
        print("Cromosoma apto")
        bandera_apto2 = True
    prob2 = probabilidad(total_ut2, total)
    print("Probab Z: ", prob2)
    prob_acum2 = prob_acumulada(prob1, prob2)
    print("Probab acum: ", prob_acum2, "\n")

    print("Cromosoma 3:", vec3, ":")
    print("Total utilidades: ", total_ut3)
    print("Total peso: ", total_apt3)
    if total_apt3 > cm:
        print("Cromosoma No apto")
        bandera_apto3 = False
        total_ut3 = 0
    else:
        print("Cromosoma apto")
        bandera_apto3 = True
    prob3 = probabilidad(total_ut3, total)
    print("Probab Z: ", prob3)
    prob_acum3 = prob_acumulada(prob1, prob2, prob3)
    print("Probab acum: ", prob_acum3, "\n")

    print("Cromosoma 4:", vec4, ":")
    print("Total utilidades: ", total_ut4)
    print("Total peso: ", total_apt4)
    if total_apt4 > cm:
        print("Cromosoma No apto")
        bandera_apto4 = False
        total_ut4 = 0
    else:
        print("Cromosoma apto")
        bandera_apto4 = True
    prob4 = probabilidad(total_ut4, total)
    print("Probab Z: ", prob4)
    prob_acum4 = prob_acumulada(prob1, prob2, prob3, prob4)
    print("Probab acum: ", prob_acum4, "\n")

    print("Sumatoria total de utilidades: ", total)
    return prob_acum1, prob_acum2, prob_acum3, prob_acum4, bandera_apto1, bandera_apto2, bandera_apto3, bandera_apto4


def reemplazos_no_aptos(bandera, vec):
    if not bandera:
        vec = []
        util_peso1_autom(vec, 4)
        vec = crear_vector(vec, 4)
        print(vec)



def generar_aleat_padre():
    op = -1
    while op != 1 or 2:
        print()
        print("1. Carga automatica de aleatorio Padre1 y Padre2")
        print("2. Carga manual de Padre1 y Padre2")
        op = validar(0, 2, float, "Ingrese una opcion: ", "Error.. opcion incorrecta ")
        if op == 1:
            prob_padre1 = round(random.uniform(0, 0.9999), 4)
            prob_padre2 = round(random.uniform(0, 0.9999), 4)
        if op == 2:
            print("Ingrese probabilidades padre entre 0 y 1")
            prob_padre1 = round(validar(0, 1, float, "Ingrese un valor para la probabilidad Padre1(4 decim): ", "Error.. fuera de rango"), 4)
            prob_padre2 = round(validar(0, 1, float, "Ingrese un valor para la probabilidad Padre2(4 decim): ", "Error.. fuera de rango"), 4)
        return prob_padre1, prob_padre2


def iteracion(prob_padre, prob_ac1, prob_ac2, prob_ac3, prob_ac4, vect1, vect2, vect3, vect4, bander1, bander2, bander3, bander4):
    if prob_padre <= prob_ac1:
        vector = vect1
        num = 1
        prob = round(prob_ac1, 4)
        bandera = bander1
    else:
        if prob_padre <= prob_ac2:
            vector = vect2
            num = 2
            prob = round(prob_ac2, 4)
            bandera = bander2
        else:
            if prob_padre <= prob_ac3:
                vector = vect3
                num = 3
                prob = round(prob_ac3, 4)
                bandera = bander3
            else:
                vector = vect4
                num = 4
                prob = round(prob_ac4, 4)
                bandera = bander4
    return num, vector, prob, bandera


def genes(num, indiv1, indiv2):
    indiv1_cop1 = indiv1
    indiv2_cop2 = indiv2

    indiv1 = indiv1[0:num] + indiv2[num:4]
    indiv2 = indiv2_cop2[0:num] + indiv1_cop1[num:4]
    return indiv1, indiv2


def cruzamiento(prob_cruce, indiv1, indiv2, bandera):
    aleatorio_cruce = round(random.uniform(0, 0.99), 4)
    aleatorio_corte = None
    print("Aleatorio de cruzamiento: ", aleatorio_cruce)
    if aleatorio_cruce < prob_cruce:
        print("Hay Cruzamiento")
        aleatorio_corte = round(random.uniform(0, 0.99), 4)
        print("Se ha generado un PUNTO DE CORTE aleatorio: ", aleatorio_corte)
        if aleatorio_corte <= 0.33:
            gen = 1
            indiv1, indiv2 = genes(gen, indiv1, indiv2)
        if aleatorio_corte <= 0.66:
            gen = 2
            indiv1, indiv2 = genes(gen, indiv1, indiv2)
        else:
            gen = 3
            indiv1, indiv2 = genes(gen, indiv1, indiv2)
        bandera = True
        return indiv1, indiv2, bandera, aleatorio_corte
    else:
        print("Aleatorio de cruzamiento es mayor a la probabilidad de cruce ingresada: ", prob_cruce)
        return indiv1, indiv2, bandera, aleatorio_corte


def aleatorior_por_gen(prob_mutacion, indiv1, indiv2):
    aleat_indiv1 = []
    aleat_indiv2 = []
    for i in range(len(indiv1)):
        aleat_indiv1.append(round(random.uniform(0, 1), 4))
        aleat_indiv2.append(round(random.uniform(0, 1), 4))
    for i in range(len(aleat_indiv1)):
        if aleat_indiv1[i] < prob_mutacion:
            if indiv1[i] == 1:
                indiv1[i] = 0
            else:
                indiv1[i] = 1
        if aleat_indiv2[i] < prob_mutacion:
            if indiv2[i] == 1:
                indiv2[i] = 0
            else:
                indiv2[i] = 0
    return aleat_indiv1, aleat_indiv2, indiv1, indiv2


def apto(bandera, indiv):
    if bandera is True:
        print("Individuo", indiv, "apto")
    else:
        print("Individuo", indiv, "no apto")



def principal():
    global prob_cruc, prob_mut
    vec1, vec2, vec3, vec4, vect1, vect2 = [], [], [], [], [], []
    reg1, reg2, reg3, reg4 = [], [], [], []
    op, op_vec, op_prob = -1, -1, -1
    prob_cruc, prob_mut = 0, 0
    bander = False
    n = 4
    cm = 15
    while op != 10:
        menu()
        op = validar(0, 10, int, "Por favor, ingrese una opcion: ", "Error, no existe opcion ingresada..")
        if op == 1:
            #Carga de individuos de la poblacion "#
            while op_vec != 2 and vec1 == []:
                menu_vec()
                op_vec = validar(0, 2, int, "Ingrese una opcion: ", "Error, no existe opcion ingresada..")
                if op_vec == 1:
                    pesos_utilidades_auto(reg1, reg2, reg3, reg4, n)
                    vec1, vec2, vec3, vec4 = crear_vectores(reg1, reg2, reg3, reg4, n)
                    mostrar(vec1, vec2, vec3, vec4)
                    print("Carga de datos de la poblacion")
                    menu_probabilidad()
                    op_prob = validar(0, 2, int, "Ingrese una opcion: ", "Error, no existe opcion ingresada..")
                    if op_prob == 1:
                        prob_cruc, prob_mut = generar_probabilidades(op_prob)
                        print("Probabilidad de cruce: ", prob_cruc)
                        print("Probabilidad de mutacion: ", prob_mut)
                        print("cruc:", prob_cruc, "prob mut", prob_mut)
                    if op_prob == 2:
                        prob_cruc, prob_mut = generar_probabilidades(op_prob)
                        print("cruc:", prob_cruc, "prob mut", prob_mut)

                if op_vec == 2:
                    print("Carga de datos de la poblacion")
                    menu_probabilidad()
                    op_prob = validar(0, 2, int, "Ingrese una opcion: ", "Error, no existe opcion ingresada..")
                    if op_prob == 1:
                        prob_cruc, prob_mut = generar_probabilidades(op_prob)
                        print("Probabilidad de cruce: ", prob_cruc)
                        print("Probabilidad de mutacion: ", prob_mut)
                    if op_prob == 2:
                        prob_cruc, prob_mut = generar_probabilidades(op_prob)
                        print("cruc:", prob_cruc, "prob mut", prob_mut)

                    cm = validar_inf(0, int, "Capacidad maxima: ", "Error, ingrese un valor mayor a 0")
                    vector_peso, vector_util = [], []
                    peso_utilidades_manualmenteee(vector_peso, vector_util, reg1, reg2, reg3, reg4, n)
                    vec1, vec2, vec3, vec4 = crear_vectores(reg1, reg2, reg3, reg4, n)
                    mostrar(vec1, vec2, vec3, vec4)

            else:
                print("\nCromosomas registrados")
        else:
            if vec1 == [] and op != 10:
                print("Es necesario cargar .. por favor ingrese en la opcion 1..")
            else:
                if op == 2:
                    print("Población principal")
                    mostrar(vec1, vec2, vec3, vec4)
                if op == 3:
                    print("Cromosomas1", vec1)
                    mostrar_todo(reg1)
                    print("Cromosomas2", vec2)
                    mostrar_todo(reg2)
                    print("Cromosomas3", vec3)
                    mostrar_todo(reg3)
                    print("Cromosomas4", vec4)
                    mostrar_todo(reg4)

                if op == 4:
                
                    print()
                    total, total1, total2, total3, total4 = funcion_objetivo(reg1, reg2, reg3, reg4)
                    apt1, apt2, apt3, apt4 = funcion_aptitud(reg1, reg2, reg3, reg4)


                    prob_acum1, prob_acum2, prob_acum3, prob_acum4, crom_apto1, crom_apto2, crom_apto3, crom_apto4 =\
                        info(vec1, vec2, vec3, vec4, total, total1, total2, total3, total4, apt1, apt2, apt3, apt4, cm)


                if op == 5:
                    prob_padre1, prob_padre2 = generar_aleat_padre()

                    indiv, vect1, prob1, es_apto = iteracion(prob_padre1, prob_acum1, prob_acum2, prob_acum3, prob_acum4,
                                                             vec1, vec2, vec3, vec4, crom_apto1, crom_apto2, crom_apto3,
                                                             crom_apto4)

                    print("\n Individuo con probabilidad acumulada por encima del aleatorio padre1 ")
                    print("Aleatorio Padre1: ", prob_padre1)
                    print("Probabilidad acumulada: ", prob1)
                    print("Infividuo", indiv, ": ", vect1)
                    apto(es_apto, indiv)

                    indiv2, vect2, prob2, es_apto2 = iteracion(prob_padre2, prob_acum1, prob_acum2, prob_acum3, prob_acum4, vec1,
                                                     vec2, vec3, vec4, crom_apto1, crom_apto2, crom_apto3, crom_apto4)

                    print("\n Individuo con probabilidad acumulada por encima del aleatorio padre2 ")
                    print("Aleatorio Padre2: ", prob_padre2)
                    print("Probabilidad acumulada: ", prob2)
                    print("Infividuo", indiv2, ": ", vect2)
                    apto(es_apto2, indiv2)
                    print()
                    print()

                    vect1_1, vect2_2, bander, aleat_corte = cruzamiento(prob_cruc, vect1, vect2, bander)
                    if aleat_corte is None:
                        print("NO HAY CRUZAMIENTO")
                    else:
                        print("\n Individios cruzados: ")
                        if aleat_corte <= 0.33:
                            print("   |           Punto de corte")
                        elif aleat_corte <= 0.66:
                            print("      |        Punto de corte")
                        elif aleat_corte > 0.66:
                            print("         |     Punto de corte")

                        print(vect1)
                        print(vect2)

                        prob_ind1, prob_ind2, vect1_1, vect2_2 = aleatorior_por_gen(prob_mut, vect1_1, vect2_2)
                        print("\nProbabilidades de individuo1: ", prob_ind1)
                        print("Probabilidades de individuo2: ", prob_ind2, "\n")
                        print("Los genes que sean menores a la probabilidad de mutacion (", prob_mut, ") cambiaran sus valores")
                        print(vect1_1)
                        print(vect2_2)



    print("Gracias por usar el servicio")


if __name__ == '__main__':
    principal()


"""
Ficha 12 Arreglos.

Resolver: 
cuando se aprieta enter u otra opcion que no sea la indicada 
el aleatorio de cruzamiento ( no el punto de corte ) se genera aleatoriamente o tambien se solicita manualmente ?

prob_cruce = random.uniform(0.95, 0.99) cambien la probabilidad de cruce ... antes estaba entre 0.096 y 0.099



prob_cruce = random.uniform(0.95, 0.99) cambien la probabilidad de cruce ... antes estaba entre 0.096 y 0.099
-SI en una eleccion de dos individuos aptos se elige al mismo individuo? al cual se tomaria en cuanta.. al que tiene 
probabilidad de mutacion ???


°°°°°°°antes de itereacion ELIMINAR LOS NO APTOS!°°°°°°



"""




