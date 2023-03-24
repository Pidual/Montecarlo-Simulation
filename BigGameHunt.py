from archery import Archer

team_1_score = 0
team_2_score = 0


#Crea un equipo con 5 arqueros
Team_1 = [Archer(),Archer(),Archer(),Archer(),Archer()]
#Crea el equipo 2 con 5 Arqueros
Team_2 = [Archer(),Archer(),Archer(),Archer(),Archer()] 

for Archer in Team_1:
    print("Resistencia: "+str(Archer.endurance) +" EXP: "+str(Archer.experiencia) +" Genero: "+ str(Archer.gender))