from archer import Archer
import random

def startgame(team_1, team_2):
    for Archer in team_1:
        shoot_til_tired(Archer)
    for Archer in team_1:
        shoot_til_tired(Archer)


def shoot_til_tired(Archer):
    print("############################################################")
    print("la resistencia inicial es "+ str(Archer.endurance))
    endurance = Archer.endurance
    individual_score = 0
    while endurance > 5:
        individual_score += making_shot(Archer)  #Realiza tiro, regresa el puntaje del tiro
        endurance -= 5
        print(endurance)
    if random.random() < 0.5:
        Archer.endurance = Archer.endurance -2
    else:
        Archer.endurance = Archer.endurance -1
    print("Score: ", individual_score)
    Archer.update_individual_score(individual_score) #Establece el score individual en el Archer
    print("Score Individual: ", Archer.individual_score)
    print("la resistencia bajo a "+ str(Archer.endurance))

# Recibe el arquero, valida el genero y establece las probabilidades
# de los tiros realizados, retorna el Puntaje segun el tiro realizado
def making_shot(Archer):
    shot = random.random()
    if Archer.gender == 0:
        print("Hommbre")
        if shot <= 0.2:
            print("Central", shot)
            return 10
        elif shot > 0.2 and shot <= 0.53:
            print("Intermedia", shot)
            return 9
        elif shot > 0.53 and shot <= 0.93:
            print("Exterior", shot)
            return 8
        else:
            print("Error", shot)
            return 0
    elif Archer.gender == 1:
        print("Mujer")
        if shot <= 0.3:
            print("Central", shot)
            return 10
        elif shot > 0.3 and shot <= 0.68:
            print("Intermedia", shot)
            return 9
        elif shot > 0.68 and shot <= 0.95:
            print("Exterior", shot)
            return 8
        else:
            print("Error", shot)
            return 0
        
team_1_score = 0

team_2_score = 0


# Crea un equipo con 5 arqueros

team_1 = [Archer(), Archer(), Archer(), Archer(), Archer()]

# Crea el equipo 2 con 5 Arqueros

team_2 = [Archer(), Archer(), Archer(), Archer(), Archer()]


print("Equipo 1")

for Archer in team_1:

    print("Resistencia: "+str(Archer.endurance) + " EXP: "+str(Archer.experiencia) +

          " Genero: " + str(Archer.gender)+" Suerte: "+str(Archer.suerte))


print("Equipo 2")

for Archer in team_2:

    print("Resistencia: "+str(Archer.endurance) + " EXP: "+str(Archer.experiencia) +

          " Genero: " + str(Archer.gender)+" Suerte: "+str(Archer.suerte))


startgame(team_1, team_2)
