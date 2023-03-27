import tkinter as tk
from Teams import Team
from PIL import ImageTk, Image
import BigGameHunt as bg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.geometry("1400x600")

def change_window_content():
    # remove existing widgets
    for widget in root.winfo_children():
        widget.destroy()

    # poner aca las graficas
    # imprimir el jugador con mas suerte
    luckiest_label = tk.Label(root, text="Arquero mas suertudo: " + str(bg.get_luckiest_archer()))
    luckiest_label.grid(row=0, column=0)
    # Jugador que haya ganando mas experiencia en todos los 20.000 juegos
    equipos = bg.get_teams()
    puntajes = [equipos[0].round_wins, equipos[1].round_wins]
    puntajes_genero = bg.get_gender_rounds_won()
    puntajes_arqueros = [equipos[0].team[0].get_staked_score(),equipos[0].team[1].get_staked_score(),equipos[0].team[2].get_staked_score(),equipos[0].team[3].get_staked_score(),equipos[0].team[4].get_staked_score(),equipos[1].team[0].get_staked_score(),equipos[1].team[1].get_staked_score(),equipos[1].team[2].get_staked_score(),equipos[1].team[3].get_staked_score(),equipos[1].team[4].get_staked_score()]
    fig, axs = plt.subplots(1, 3, dpi=80, figsize=(19, 5))
    nombre_arqueros = ['Arq 1','Arq 2','Arq 3','Arq 4','Arq 5','Arq 6','Arq 7','Arq 8','Arq 9','Arq 10']
    # Equipos y su puntaje
    axs[0].bar(["equipo1", "equipo2"], puntajes)
    # Genero con mas victorias en los 20.000 juegos y vic total
    axs[1].bar(["Hombre","Mujer"],puntajes_genero)
    #Todos los arqueros y sus puntuaciones
    axs[2].bar(nombre_arqueros, puntajes_arqueros)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=1, rowspan=3)
    # root.mainloop()

    # Grafica de Jugadores vs Juego


def start_big_game_hunt():
    bg.start_game(20000)
    change_window_content()


label = tk.Label(root, text="Simulacion de arqueria", bg="green", pady=10, padx=50)
img = ImageTk.PhotoImage(Image.open("imagenes/targets.jpg"))
button1 = tk.Button(root, text="Empezar", padx=30, pady=40, command=start_big_game_hunt)

panel_img = tk.Label(root, image=img)
label.config(font=("Courier", 24))

label.grid(row=0, column=0)
panel_img.grid(row=1, column=0)
button1.grid(row=1, column=1)

root.mainloop()
