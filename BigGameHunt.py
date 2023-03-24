from archery import Archer

def startgame(team_1,team_2): 
    for Archer in team_1:
         shoot_til_tired(Archer)
    for Archer in team_1:
         shoot_til_tired(Archer)

def shoot_til_tired(Archer):
    endurance = Archer.endurance
    while endurance > 5:
        print(endurance)
        endurance -= 5


    
    
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

