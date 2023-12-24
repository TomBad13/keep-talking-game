from random import randint
from paint import *
import tkinter as tk
from time import sleep as sl
import sys

try:
    nbdefils = int(sys.argv[1])
except ValueError:
    print("ValueError: Le nombre de fils doit être un entier.")
    sys.exit(1)
if nbdefils < 3:
      nbdefils = 3
elif nbdefils > 6:
      nbdefils = 6

#-----------------------------------

couleur_dico = {
    0: NOI,
    1: ROU,
    2: VER,
    3: JAU,
    4: BLE,
    5: MAG,
    6: BLA
}
couleur_dico_nom = {
    0: "NOI",
    1: "ROU",
    2: "VER",
    3: "JAU",
    4: "BLE",
    5: "MAG",
    6: "BLA"
}
couleur_dico_color = {
    "NOI":"black",
    "ROU":"red",
    "VER":"green",
    "JAU":"yellow",
    "BLE":"blue",
    "MAG":"purple",
    "BLA":"white"
}

couleur_dico_nomcomplet = {
    "NOI":"Noir",
    "ROU":"Rouge",
    "VER":"Vert",
    "JAU":"Jaune",
    "BLE":"Bleu",
    "MAG":"Magenta",
    "BLA":"Blanc"
}

impair = "13579"
def creer_numero_serie():
      numero_serie = ""
      for _ in range(8):
            numero_serie  = numero_serie+str(randint(0,9))
      return numero_serie


def creer_combinaison(combinaison:int):
    couleur_liste = []
    couleur_liste_nom = []
    for _ in range(combinaison):
        rdm = randint(0,6)
        couleur_liste.append(couleur_dico.get(rdm))
        couleur_liste_nom.append(couleur_dico_nom.get(rdm))
    return combinaison,couleur_liste,couleur_liste_nom


def creer_bombe(combinaison,couleur_liste,couleur_liste_nom):
      afficher = ""
      for i in range(combinaison):
            if i == combinaison:
                  afficher = str(afficher + "["+couleur_liste_nom[i]+"]" + "*20")
            else:
                  afficher = str(afficher + "["+couleur_liste_nom[i]+"]" + "*20,")
      #exec(f"dessiner([{afficher}])")
      return combinaison,couleur_liste,couleur_liste_nom

def check_reponse(y,nb,serie,numero_serie):
      global fil_coupe
      fil_coupe = couleur_dico_nomcomplet.get(serie[y])
      y +=1
      if nb == 3:
            if "ROU" not in serie:
                  if y == 2:
                        return True
                  else:
                        return False
            elif serie[2] == "BLA":
                  if y == 3:
                        return True
                  else:
                        return False
            elif serie.count("BLE") > 1:
                  if serie[2] == "BLE":
                        if y == 3:
                              return True
                        else:
                              return False
            elif serie[1] == "BLE":
                  if y == 2:
                        return True
                  else:
                        return False
            else:
                  if y == 3:
                        return True
                  else:
                        return False
      elif nb == 4:
            if serie.count("ROU") > 1 and str(numero_serie[-1]) in impair:
                  if y == 3:
                        return True
                  else:
                        return False
            elif serie[3] == "JAU" and "ROU" not in serie:
                  if y == 1:
                        return True
                  else:
                        return False
            elif serie.count("BLE") == 1:
                  if y == 1:
                        return True
                  else:
                        return False
            elif serie.count("JAU") > 1:
                  if y == 4:
                        return True
                  else:
                        return False
            else:
                  if y == 2:
                        return True
                  else:
                        return False
      elif nb == 5:
            if serie[4] == "VER":
                  if y == 5:
                        return True
                  else:
                        return False
            elif serie.count("ROU") == 1 and serie.count("JAU") > 1:
                  if y == 1:
                        return True
                  else:
                        return False
            elif "VER" not in serie:
                  if y == 2:
                        return True
                  else:
                        return False
            else:
                  if y == 1:
                        return True
                  else:
                        return False
      elif nb == 6:
            if "JAU" not in serie and str(numero_serie[-1]) in impair:
                  if y == 3:
                        return True
                  else:
                        return False
            elif serie.count("JAU") == 1 and serie.count("BLA") > 1:
                  if y == 4:
                        return True
                  else:
                        return False
            elif "ROU" not in serie:
                  if y == 6:
                        return True
                  else:
                        return False
            else:
                  if y == 4:
                        return True
                  else:
                        return False


def nbdefilsf():
      fils = []
      numero_serie = creer_numero_serie()
      combn = creer_combinaison(nbdefils)
      comb = creer_bombe(combn[0],combn[1],combn[2])
      bouton1.destroy()
      texte3 = tk.Label(fenetre, text=f"Veuillez choisir un fil à couper! \nPour savoir quel fil couper, vous pouvez regarder les conditions de désamorçage pour {nbdefils} fils!", font=("Arial", 15), bg='light blue')
      texte3.pack()
      texte4 = tk.Label(fenetre, text=f"Numéro de série: {numero_serie}", font=("Arial", 15), bg='light blue')
      texte4.pack()
      for i in range(nbdefils):
            fil = tk.Button(fenetre, text="                                  ",command=lambda y=i: affichage_correct(check_reponse(y,nbdefils,comb[2],numero_serie)),font=("Courier",30,"bold"),fg=couleur_dico_color.get(combn[2][i]),bg=couleur_dico_color.get(combn[2][i]))
            fil.pack()
            fils.append(fil)
      def affichage_correct(reponse):
            def suite_affichage_correct():
                  CouperFiltxt.destroy()
                  CouperFiltxt2.destroy()
                  if reponse == True:
                        texteblanc = tk.Label(fenetre, text=" ", font=("Arial", 15), bg="#d1ffb8")
                        texteblanc.pack()
                        texte5 = tk.Label(fenetre, text=f"Bravo! Vous avez trouvé la bonne réponse.", font=("Arial", 15), bg="#d1ffb8")
                        texte5.pack()
                        BombeTremble = tk.Label(fenetre, image=BombeImg,bg="#d1ffb8")
                        BombeTremble.pack()
                        fenetre.configure(bg='#d1ffb8')
                  else:
                        texteblanc = tk.Label(fenetre, text=" ", font=("Arial", 15), bg="#ff7a7a")
                        texteblanc.pack()
                        texte5 = tk.Label(fenetre, text=f"Malheureusement ceci n'est pas la bonne réponse.", font=("Arial", 15), bg="#ff7a7a")
                        texte5.pack()
                        fenetre.configure(bg='#ff7a7a')
                        ExplosionImgTxt = tk.Label(fenetre, image=ExplosionImg,bg="#ff7a7a")
                        ExplosionImgTxt.pack()
            for fil in fils:
                  fil.destroy()
            texte3.destroy()
            texte4.destroy()
            global CouperFiltxt,CouperFiltxt2
            CouperFiltxt2 = tk.Label(fenetre, text=f"Vous choisissez de couper le fil {fil_coupe}...", font=("Arial", 15), bg='light blue')
            CouperFiltxt2.pack()
            CouperFiltxt = tk.Label(fenetre, image=CouperFil,bg='light blue')
            CouperFiltxt.pack()            
            fenetre.after(1500, suite_affichage_correct)

#-----------------------------------
    
fenetre = tk.Tk()
PlayAgainImg = tk.PhotoImage(file="PlayAgain.png")
ExplosionImg = tk.PhotoImage(file="Explosion.png")
BombeImg = tk.PhotoImage(file="ImgBombe.png")
CouperFil = tk.PhotoImage(file="CouperFil.png")
fenetre.title("Keep talking and Nobody Explodes")
fenetre.iconbitmap("Logo.ico")
fenetre.geometry("920x620")

fenetre.resizable(False, False)
fenetre.configure(bg='light blue') 
texte1 = tk.Label(fenetre,text="Keep talking and Nobody Explodes",font=("Courier",20,"bold"),bg="#c5fce1")
texte1.pack()
bouton1 = tk.Button(fenetre, text="Démarrer!", command=nbdefilsf,font=("Courier",20,"bold"))
bouton1.pack()
fenetre.mainloop()
