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
        
        
