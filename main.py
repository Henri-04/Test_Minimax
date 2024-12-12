from AI import *

etats_systeme = [
    [0, 0], [1, 0], [2, 0], [3, 0],
    [4, 3], [5, 0], [6, 0], [7, 0],
    [8, 0]
]



#coups_possibles = generer_coups(1, etats_systeme)
#print(coups_possibles)






print(pions)
print(cases_vides_et_jouables)


"""
# L'ordinateur est le maximisateur, et il doit jouer le meilleur coup
is_maximizing = True
alpha = float('-inf')
beta = float('inf')
profondeur = 3
# Exemple de profondeur


# Appel de minimax pour déterminer le meilleur coup
score, best_move = minimax(etats_systeme, True, 2, 1, alpha, beta)

print(f"Le meilleur coup à jouer est : {best_move}")

"""