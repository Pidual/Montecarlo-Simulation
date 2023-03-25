import random

class Archer:
    gender = None  # 0 para hombre y 1 para mujer
    max_endurance = None #la resistencia que es definitiva
    endurance = None  # 35 ± 10
    experiencia = None  # Entero 10
    suerte = None  # 1 a 3

    def __init__(self):  # aca para que se creen pseudo aletoriamente
        #Escoje el genero con el metodo montecarlo 0.5 de chance cada genero
        ri = random.random()
        if ri < 0.5:
            self.gender = 0
        else:
            self.gender = 1
        #Resistencia 35 ± 10 
        if ri < 0.5:
            self.endurance = 35 - random.randint(1,10)
        else:
            self.endurance = 35 + random.randint(1,10)
            
        if ri <= 0.3:  # este metodo matematicamente tiene como un 0.002 de probabilidad extra la suerte 3 o 2
            self.suerte = 1
        elif ri > 0.3 and ri <= 0.66:
            self.suerte = 2
        else:
            self.suerte = 3
        self.experiencia = 10
        self.individual_score = 0
        self.max_endurance = self.endurance
