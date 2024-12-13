
#Vérificatoin de la victoire pour l'évaluation de la situation
def check_victory(etats_systeme, joueur):
    """
    Vérifie si le joueur a gagné.
    Un joueur gagne si trois de ses pions sont alignés horizontalement, verticalement ou diagonalement.

    :param etats_systeme: Liste représentant l'état du système.
    :param joueur: Identifiant du joueur à vérifier (1 ou 2).
    :return: True si le joueur a gagné, False sinon.
    """
    plateau = [[etats_systeme[i * 3 + j][1] for j in range(3)] for i in range(3)]

    # Vérification des lignes
    for row in plateau:
        if all(cell == joueur for cell in row):
            return True

    # Vérification des colonnes
    for col in range(3):
        if all(plateau[row][col] == joueur for row in range(3)):
            return True

    # Vérification des diagonales
    if all(plateau[i][i] == joueur for i in range(3)):  # Diagonale principale
        return True
    if all(plateau[i][2 - i] == joueur for i in range(3)):  # Diagonale secondaire
        return True

    return False


#Génération de tous les états possibles du plateau en partant d'un état donné
def generer_coups(joueur_actuel, etats_systeme):
    """
    Génère tous les états possibles après un coup du joueur_actuel.

    Chaque état généré est un nouvel état du plateau après un coup (poser pion, déplacer pion, déplacer case).
    Vous avez fourni une implémentation qui génère une liste d'états possibles, on la réutilise telle quelle.
    """

    coups_possibles = []

    #Calcul du nombre total de pions
    nb_pions_total = sum(1 for case in etats_systeme if case[1] in (1, 2))

    #Calcul du nombre de pions du joueur actuel
    nb_pions_joueur_actuel = sum(1 for case in etats_systeme if case[1] == joueur_actuel)

    #Generation des coups de type "poser un pion"
    if nb_pions_joueur_actuel < 3 :
        for case in etats_systeme:
            if case[1] == 0:  # La case est vide
                nouvel_etat = [list(c) for c in etats_systeme]  # Copie profonde
                nouvel_etat[case[0]][1] = joueur_actuel
                coups_possibles.append(nouvel_etat)

    #Génération des coups de type "bouger un pion"
    if nb_pions_total >= 1 :
        # Créer la liste des cases occupées par les pions (1 ou 2)
        cases_avec_pions = [case for case in etats_systeme if case[1] in (1, 2)]
        # Créer la liste des cases vides
        cases_vides = [case for case in etats_systeme if case[1] == 0]

        for case_pion in cases_avec_pions:
            for case_vide in cases_vides:
                nouvel_etat = [list(c) for c in etats_systeme]
                # Déplacement du pion
                nouvel_etat[case_vide[0]][1] = case_pion[1]
                nouvel_etat[case_pion[0]][1] = 0
                coups_possibles.append(nouvel_etat)

    #Génération des coups de type "bouger une case"
    # On suppose que la case void (3) est unique
    void_case_index = next((i for i, case in enumerate(etats_systeme) if case[1] == 3), None)
    if void_case_index is not None:
        taille_plateau = 3
        voisins_void_case = []

        # Voisin de gauche
        if void_case_index % taille_plateau > 0:
            voisins_void_case.append(void_case_index - 1)

        # Voisin de droite
        if void_case_index % taille_plateau < taille_plateau - 1:
            voisins_void_case.append(void_case_index + 1)

        # Voisin du haut
        if void_case_index >= taille_plateau:
            voisins_void_case.append(void_case_index - taille_plateau)

        # Voisin du bas
        if void_case_index < taille_plateau * (taille_plateau - 1):
            voisins_void_case.append(void_case_index + taille_plateau)

        # Générer les nouveaux états en swappant la case vide avec ses voisins
        for voisin_index in voisins_void_case:
            nouvel_etat = [list(c) for c in etats_systeme]
            nouvel_etat[void_case_index][1], nouvel_etat[voisin_index][1] = (
                nouvel_etat[voisin_index][1],
                nouvel_etat[void_case_index][1],
            )
            coups_possibles.append(nouvel_etat)

    return coups_possibles

#Evaluation de la situation ( victoire ou égalité)
def evaluate_state(etats_systeme, joueur, joueur_adverse):
    """
    Évalue l'état du plateau du point de vue du joueur maximisant.
    Retourne un score :
    1 si le joueur a gagné,
    -1 si le joueur adverse a gagné,
    0 sinon (pour cet exemple).
    """
    if check_victory(etats_systeme, joueur):
        return 1
    if check_victory(etats_systeme, joueur_adverse):
        return -1
    # Si pas de victoire, match nul ou état intermédiaire, score 0
    if all(case[1] != 0 for case in etats_systeme):
        # Plateau plein sans victoire = match nul
        return 0
    # État non terminal
    return 0


def minimax(etats_systeme, is_maximizing, joueur, joueur_adverse, profondeur, compteur = [0]):
    """
    Implémentation de Minimax sans alpha-bêta sur l'état du système.

    :param etats_systeme: État actuel du plateau (liste de [ID_case, état_case])
    :param is_maximizing: True si c'est au joueur 'joueur' de jouer, False sinon
    :param joueur: Le joueur maximisant
    :param joueur_adverse: L'autre joueur (minimisant)
    :param profondeur: Profondeur maximale de recherche
    :return: (score, best_move) où best_move est l'état choisi
    """
    #Incrémenter le compteur
    compteur[0] += 1

    # Évaluer l'état actuel
    score = evaluate_state(etats_systeme, joueur, joueur_adverse)

    # Conditions de fin
    if profondeur == 0 or score != 0 or all(case[1] != 0 for case in etats_systeme):
        # On est dans un état terminal ou profondeur max atteinte
        return score, None

    if is_maximizing:
        best_score = float('-inf')
        best_move = None
        possible_moves = generer_coups(joueur, etats_systeme)
        if not possible_moves:
            # Pas de coups possibles, match nul
            return 0, None

        for move in possible_moves:
            new_score, _ = minimax(move, False, joueur, joueur_adverse, profondeur - 1, compteur)
            if new_score > best_score:
                best_score = new_score
                best_move = move
        return best_score, best_move
    else:
        best_score = float('inf')
        best_move = None
        possible_moves = generer_coups(joueur_adverse, etats_systeme)
        if not possible_moves:
            # Pas de coups possibles, match nul
            return 0, None

        for move in possible_moves:
            new_score, _ = minimax(move, True, joueur, joueur_adverse, profondeur - 1, compteur)
            if new_score < best_score:
                best_score = new_score
                best_move = move
        return best_score, best_move
