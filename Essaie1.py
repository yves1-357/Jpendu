import tkinter as tk
from random import randrange

# Fonction pour afficher une frame
def show_frame(frame):
    frame.tkraise()

# Création de la fenêtre principale et personnalisation
fenetre = tk.Tk()
fenetre.title('Jeu_Pendu')
fenetre.geometry('890x600')
fenetre.resizable(False, False)

# Création des frames
frame1 = tk.Frame(fenetre, bg='#E6E6E6')
frame2 = tk.Frame(fenetre, bg='#E6E6E6')

for frame in (frame1, frame2):
    frame.place(x=0, y=0, width=880, height=600)

# ================================ Frame 1 ================================

# Ajouter des fenêtres "présentation du jeu"
label = tk.Label(frame1, text="Le Jeu du Pendu", bg="Green", width=20)
label.place(x=360, y=10, height=40)
label = tk.Label(frame1, text="Présentation", bg="Green", width=20)
label.place(x=5, y=60)
label = tk.Label(frame1, text="Règles", bg="Green", width=20)
label.place(x=5, y=170)
label = tk.Label(frame1, text="Choix des Joueurs", bg="Green", width=20)
label.place(x=5, y=380)

# la Description du jeu
TEXTE = ("Dans ce jeu, au lieu de pendre un personnage, vous allez aider un jardinier "
         "à prendre soin d'une fleur délicate. Chaque fois que vous faites un essai "
         "infructueux pour deviner le mot, vous retirez un élément essentiel à la santé "
         "de la fleur, comme une goutte d'eau, un rayon de soleil, etc. Une fois que tous "
         "les éléments ont été retirés et que la fleur est privée de ses ressources, elle se "
         "flétrira et le jeu sera perdu.")
label = tk.Label(frame1, text=TEXTE, wraplength=860)
label.place(x=5, y=100)

# Création d'une liste pour ajouter des textes dans les règles
text = [
    "Chaque mot trouvé vaut 1 point.",
    "Chaque joueur a 70 secondes pour trouver le mot.",
    "Cliquez sur GO pour commencer le jeu et démarrer le chrono.",
    "Cliquez sur Nouveau pour refaire la partie pendant le jeu.",
    "Dès que le chrono arrive à ZERO, ça passe directement au joueur suivant.",
    "Le jeu s'arrête dès qu'un joueur atteint 2 points."
]

y_pos = 210
for text in text:
    label = tk.Label(frame1, text=text, justify="left")
    label.place(x=10, y=y_pos)
    y_pos += 25  # On incrémente de 25 pixels vers le bas

# Ajout des noms des joueurs
tk.Label(frame1, text="Joueur 1").place(x=10, y=420)
tk.Label(frame1, text="Joueur 2").place(x=10, y=460)
tk.Label(frame1, text="Joueur 3").place(x=10, y=500)
tk.Label(frame1, text="Joueur 4").place(x=10, y=540)

#cadre pour les inputs de leurs 'Noms'
e1 = tk.Entry(frame1, width=70)
e1.place(x=80, y=420)
e2 = tk.Entry(frame1, width=70)
e2.place(x=80, y=460)
e3 = tk.Entry(frame1, width=70)
e3.place(x=80, y=500)
e4 = tk.Entry(frame1, width=70)
e4.place(x=80, y=540)

#Fonctions pour debut du jeu:
def start_game():
    global joueur, current_joueur, joueur_score_scores
    joueur = [e1.get(), e2.get(), e3.get(), e4.get()]
    joueur_score_scores = [0, 0, 0, 0]
    current_joueur = 0
    update_player_display()
    show_frame(frame2)

# Ajout du bouton 'Next' pour aller au frame 2
button = tk.Button(frame1, text='Next', font=("Courrier", 15), bg='Green', fg='White', command=start_game)
button.place(x=790, y=520)

# ================================ Frame 2 ================================

label = tk.Label(frame2, text="Game", bg="yellow", width=20)
label.place(x=360, y=10, height=30)

# Jeu du Pendu intégré dans frame2
def maj_mot_en_progres(mot_en_progres, lettre, secret):
    for i, char in enumerate(secret):
        if char == lettre:
            mot_en_progres[2 * i] = lettre

def score(lettre):
    global mo, end, img, mot_en_progres, joueur_score_scores, timer_id
    if lettre not in secret:
        cnv.delete(images[mo])
        mo -= 1
        cnv.create_image((small_width_img / 2, small_height_img / 2), image=images[mo])
        if mo == 0:
            cnv.create_image((small_width_img / 2, small_height_img / 2), image=fail)
            lbl["text"] = " ".join(secret)
            end = True
            next_player()
    elif ''.join(mot_en_progres) == " ".join(secret):
        cnv.create_image((small_width_img / 2, small_height_img / 2), image=win)
        joueur_score_scores[current_joueur] += 1
        end = True
        if joueur_score_scores[current_joueur] == 2:
            cnv.create_text(small_width_img / 2, small_height_img / 2, text=f"{joueur[current_joueur]} Wins!", font=('Deja Vu Sans Mono', 30, 'bold'), fill="green")
            display_winner(joueur[current_joueur])
            frame2.after_cancel(timer_id) #arret du miniteur
        else:
            next_player()

def next_player():
    global current_joueur, end
    current_joueur = (current_joueur + 1) % 4  # Correction: change 5 to 4 for valid player index
    end = False
    update_player_display()
    init()

def update_player_display():
    for i, player in enumerate(joueur):
        if i == current_joueur:
            player_labels[i].config(text=f"{player}: {joueur_score_scores[i]} points", fg="green")
        else:
            player_labels[i].config(text=f"{player}: {joueur_score_scores[i]} points", fg="black")

def choisir_lettre(event):
    global mot_en_progres
    if end:
        return
    mon_btn = event.widget
    lettre = mon_btn["text"]
    mon_btn["state"] = tk.DISABLED
    maj_mot_en_progres(mot_en_progres, lettre, secret)
    lbl["text"] = "".join(mot_en_progres)
    score(lettre)

def init():
    global end, mot_en_progres, secret, mo, img
    secret = arbres[randrange(len(arbres))]
    mot_en_progres = list(' '.join("●" * len(secret)))
    lbl["text"] = ''.join(mot_en_progres)
    cnv.delete(tk.ALL)
    cnv.create_image((small_width_img / 2, small_height_img / 2), image=images[-1])

    for btn in btns:
        btn["state"] = tk.NORMAL

    mo = limite
    end = False
    start_timer()

def start_timer():
    global time_left
    time_left = 70
    countdown()

timer_id = None

def countdown():
    global time_left, timer_id
    if time_left > 0:
        timer_label.config(text=f"{time_left}")
        time_left -= 1
        timer_id = frame2.after(1000, countdown)
    else:
        next_player()

def display_winner(winner_name):
    winner_button = tk.Button(frame2, text=f"{winner_name} a gagné", font=("Helvetica", 15), bg="green", fg="white", command=lambda: show_frame(frame1))
    winner_button.place(x=400, y=385)

limite = 7

# Les images
images = []
for j in range(limite + 1):
    try:
        img = tk.PhotoImage(file=f"{j}.png").subsample(4, 4)  # Resizing images
        images.append(img)
    except Exception as e:
        print(f"Error loading image {j}.png: {e}")
        images.append(None)
try:
    fail = tk.PhotoImage(file="fail crying.png").subsample(4, 4)
except Exception as e:
    print(f"Error loading fail crying.png: {e}")
    fail = None

try:
    win = tk.PhotoImage(file="win.png").subsample(4, 4)
except Exception as e:
    print(f"Error loading win.png: {e}")
    win = None

# Vérifiez si toutes les images ont été chargées correctement
if None in images:
    print("Some images failed to load.")
if fail is None:
    print("Fail image failed to load.")
if win is None:
    print("Win image failed to load.")

small_width_img = win.width() if win else 200  # Default width if win.png not loaded
small_height_img = win.height() if win else 150  # Default height if win.png not loaded

cnv = tk.Canvas(frame2, width=small_width_img, height=small_height_img, highlightthickness=4, bg="#E6E6E6")
cnv.place(x=20, y=120)  # Image à gauche de l'interface


# Boutons pour les lettres
Alphabet = "ABDEFGILMNOPRSTV"
btns = []

lettres = tk.Frame(frame2, bg="#E6E6E6")
lettres.place(x=490, y=200)  # Les lettres au-dessous du mot à deviner

for i in range(2):
    for j in range(8):
        if 8 * i + j < len(Alphabet):
            btn = tk.Button(lettres, text=Alphabet[8 * i + j], relief=tk.FLAT, font='times 15')
            btn.grid(row=i, column=j)
            btn.bind("<Button-1>", choisir_lettre)
            btns.append(btn)

for j in range(4):
    btn = tk.Button(lettres, text=Alphabet[8 + j], relief=tk.FLAT, font='times 15')
    btn.grid(row=2, column=j + 2)
    btn.bind("<Button-1>", choisir_lettre)
    btns.append(btn)

# Ajout du label pour afficher le mot en cours
lbl = tk.Label(frame2, font=("Helvetica", 20), bg="#E6E6E6")
lbl.place(x=520, y=120)  # Position du mot en cours

# Bouton pour refaire la partie
reset = tk.Button(frame2, text="Nouveau", font="Times 15 bold", command=init)
reset.place(x=10, y=460)

# Bouton pour commencer le jeu
go_button = tk.Button(frame2, text="GO", font="Times 15 bold", bg="green", fg="white", command=init)
go_button.place(x=420, y=450)

# Ajout du minuteur
timer_label = tk.Label(frame2, font="Times 15 bold", fg="Green", bg="#E6E6E6")
timer_label.place(x=430, y=400)

# Affichage des joueurs et des points
player_labels = []
x_pos = 90
for i in range(4):
    lbl_player = tk.Label(frame2, text="", font=("Helvetica", 15), bg="#E6E6E6")
    lbl_player.place(x=x_pos, y=550)
    player_labels.append(lbl_player)
    x_pos += 175

# Bouton pour retourner à la frame 1
back_button = tk.Button(frame2, text="Back", font="Times 15 bold", command=lambda: show_frame(frame1))
back_button.place(x=810, y=460)

with open("arbres.txt") as f:
    arbres = f.read().split("\n")

show_frame(frame1)
fenetre.mainloop()
