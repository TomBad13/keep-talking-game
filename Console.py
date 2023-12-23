from random import randint
import sys
from paint import *
fils = int(sys.argv[1])

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
def creer_numero_serie():
      numero_serie = ""
      for _ in range(8):
            numero_serie  = numero_serie+str(randint(0,9))
      return numero_serie


impair = "13579"


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
      exec(f"dessiner([{afficher}])")
      return combinaison,couleur_liste,couleur_liste_nom


numero_serie = creer_numero_serie()
combn = creer_combinaison(fils)
comb = creer_bombe(combn[0],combn[1],combn[2])
print(f"n°{numero_serie}")
try:
      y = int(input("Quel fil veux-tu couper?  "))
except ValueError:
      print("Veuillez entrez un nombre entier.")
if comb[0] == 3:
      if "ROU" not in comb[2]:
            if y == 2:
                  print("Gagné!")
            else:
                  print(f"Vous avez perdu...")
      elif comb[2][2] == "NOI":
            if y == 3:
                  print("Gagné!")
            else:
                  print(f"Vous avez perdu...")
      elif comb[2].count("BLE") > 1:
            if comb[2][2] == "BLE":
                  if y == 3:
                        print("Gagné!")
            else:
                  print(f"Vous avez perdu...")
      elif comb[2][1] == "BLE":
            if y == 2:
                  print("Gagné!")
            else:
                  print(f"Vous avez perdu...")
      else:
            if y == 3:
                  print("Gagné!")
            else:
                  print(f"Vous avez perdu...")
elif comb[0] == 4:
      if comb[2].count("ROU") > 1 and str(numero_serie[-1]) in impair:
            if y == 3:
                  print("Gagné!")
            else:
                  print(f"Vous avez perdu...")
      elif comb[2][3] == "JAU" and "ROU" not in comb[2]:
            if y == 1:
                  print("Gagné!")
            else:
                  print(f"Vous avez perdu...")
      elif comb[2].count("BLE") == 1:
            if y == 1:
                  print("Gagné!")
            else:
                  print(f"Vous avez perdu...")
      elif comb[2].count("JAU") > 1:
            if y == 4:
                  print("Gagné!")
            else:
                  print(f"Vous avez perdu...")
      else:
            if y == 2:
                  print("Gagné!")
            else:
                  print(f"Vous avez perdu...")
elif comb[0] == 5:
      if comb[2][4] == "VER":
            if y == 5:
                  print("Gagné!")
            else:
                  print(f"Vous avez perdu...")
      elif comb[2].count("ROU") == 1 and comb[2].count("JAU") > 1:
            if y == 1:
                  print("Gagné!")
            else:
                  print(f"Vous avez perdu...")
      elif "VER" not in comb[2]:
            if y == 2:
                  print("Gagné!")
            else:
                  print(f"Vous avez perdu...")
      else:
            if y == 1:
                  print("Gagné!")
            else:
                  print(f"Vous avez perdu...")
elif comb[0] == 6:
      if "JAU" not in comb[2] and str(numero_serie[-1]) in impair:
            if y == 3:
                  print("Gagné!")
            else:
                  print(f"Vous avez perdu...")
      elif comb[2].count("JAU") == 1 and comb[2].count("NOI") > 1:
            if y == 4:
                  print("Gagné!")
            else:
                  print(f"Vous avez perdu...")
      elif "ROU" not in comb[2]:
            if y == 6:
                  print("Gagné!")
            else:
                  print(f"Vous avez perdu...")
      else:
            if y == 4:
                  print("Gagné!")    
            else:
                  print(f"Vous avez perdu...")




#ERREURS:
#- couleur_choisi n'est pas l'indice du bon fil à couper
#- les "else:" des conditions ne sont pas activés aux bons moments"""