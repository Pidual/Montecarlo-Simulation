import random

class Archer:
    gender = None #0 para hombre y 1 para mujer
    resisntecia = None #35 ± 10
    experiencia = None #Entero 10
    suerte = None #1 a 3
    puntucion_individual = 666
    
    def __init__(self): #aca para que se creen pseudo aletoriamente
        ri = random.random()
        if ri < 0.5:
            gender = 0
        else:
            gender = 1

        if ri <= 0.3: #este metodo matematicamente tiene como un 0.002 de probabilidad extra la suerte 3 o 2
            suerte = 1
        else if ri > 0.3 and ri <= 0.66
            suerte = 2
        else:
            suerte = 3

