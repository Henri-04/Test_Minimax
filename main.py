from AI2 import *
import time


etats_systeme = [
    [0, 0], [1, 0], [2, 0], [3, 0],
    [4, 3], [5, 0], [6, 0], [7, 0],
    [8, 0]
]

compteur = 0

#Test
score = 42
best_move = []

compteur = [0]


start = time.perf_counter()
#Appel de Minimax

profondeur = 6
score, best_move = minimax(etats_systeme, True, 1, 2, profondeur, compteur)

end = time.perf_counter()


print("\nScore attribué à la situation finale :")
print(score)

print("Etat du plateau après avoir effectué le meilleur coup : ")
print(best_move)

print("Nb itérations :")
print(compteur[0])

print("Temps d'exécution:", end - start, "secondes")