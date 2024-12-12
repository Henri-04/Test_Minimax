from AI import *

etats_systeme = [
    [0, 1], [1, 1], [2, 0], [3, 0],
    [4, 3], [5, 0], [6, 0], [7, 0],
    [8, 0]
]

compteur = 0

alpha = 1
beta = 1

#etats_systeme = generer_coups(1, etats_systeme)

#print (etats_systeme)
#print(len(etats_systeme))

#Appel de Minimax


score, best_move = minimax(etats_systeme, True, 1, 2, alpha, beta)



print("\nScore attribué à la situation finale :")
print(score)
print("\n")

print("Etat du plateau après avoir effectué le meilleur coup :\n ")
print(best_move)







"""
# L'ordinateur est le maximisateur, et il doit jouer le meilleur coup
is_maximizing = True
alpha = float('-inf')
beta = float('inf')

# Exemple de profondeur

# Appel de minimax pour déterminer le meilleur coup

print(f"Le meilleur coup à jouer est : {best_move}")

"""