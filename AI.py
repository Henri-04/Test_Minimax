

def generer_coups(joueur_actuel, etats_systeme):
    """
    Génère tous les coups possibles pour un joueur donné à partir de l'état du système.

    :param joueur_actuel: Identifiant du joueur (1 pour bleu, 2 pour rouge).

    :param etats_systeme: Liste représentant les cases du plateau.
                          Chaque élément est de la forme [ID_case, état_case].
                          état_case : 0=vide, 1=bleu, 2=rouge, 3=void.

    :return: Liste des coups possibles. Chaque coup est un dictionnaire décrivant l'action.
    """
    coups_possibles = []

    #Calcul du nombre total de pions
    nb_pions_total = 0
    for case in etats_systeme:
        if case[1] in (1, 2):  # Vérifie si case[1] est dans la liste [1, 2]
            nb_pions_total += 1
    #TEST
    print(nb_pions_total)

    #Calcul du nombre de pions du joueur actuel
    nb_pions_joueur_actuel = 0

    for case in etats_systeme :
        if case[1] == joueur_actuel:
            nb_pions_joueur_actuel += 1
    #TEST
    print(nb_pions_joueur_actuel)


    #Generation des coups de type "poser un pion"
    if nb_pions_joueur_actuel < 3 :

        for case in etats_systeme:

            if case[1] == 0:  # La case est vide

                # Créer une copie de l'état actuel
                nouvel_etat = [list(c) for c in etats_systeme]

                # Mettre à jour l'état de la case avec le pion du joueur
                nouvel_etat[case[0]][1] = joueur_actuel

                # Ajouter le nouvel état à la liste des états possibles
                coups_possibles.append(nouvel_etat)


    #Génération des coups de type "bouger un pion"
    if nb_pions_total >= 1 :

        # Créer la liste des cases occupées par les pions du joueur
        cases_avec_pions = [case for case in etats_systeme if case[1] == 1 or case[1] == 2]

        # Créer la liste des cases vides
        cases_vides = [case for case in etats_systeme if case[1] == 0]


        # Boucles imbriquées pour générer tous les déplacements possibles
        for case_pion in cases_avec_pions:

            for case_vide in cases_vides:
                # Créer une copie de l'état actuel
                nouvel_etat = [list(c) for c in etats_systeme]

                # Swapper l'état des cases
                nouvel_etat[case_vide[0]][1] = case_pion[1]  # La case vide prend le statut de la case d'origine
                nouvel_etat[case_pion[0]][1] = 0  # L'ancienne case devient vide

                # Ajouter le nouvel état à la liste des coups possibles
                coups_possibles.append(nouvel_etat)



    #Génération des coups de type "bouger une case"

    # Trouver l'indice de la case vide (void case, état 3)
    void_case_index = next((i for i, case in enumerate(etats_systeme) if case[1] == 3), None)

    if void_case_index is not None:
        taille_plateau = 3  # Le plateau est de taille fixe 3x3

        # Calculer les voisins latéraux et horizontaux de la case vide
        voisins_void_case = []

         # Voisin de gauche (sur la même ligne)
        if void_case_index % taille_plateau > 0:
            voisins_void_case.append(void_case_index - 1)

        # Voisin de droite (sur la même ligne)
        if void_case_index % taille_plateau < taille_plateau - 1:
            voisins_void_case.append(void_case_index + 1)

        #Voisin du haut
        if void_case_index >= taille_plateau:
                voisins_void_case.append(void_case_index - taille_plateau)

        # Voisin du bas
        if void_case_index < taille_plateau * (taille_plateau - 1):
                voisins_void_case.append(void_case_index + taille_plateau)


        # Générer les nouveaux états en swappant la case vide avec ses voisins
        for voisin_index in voisins_void_case:

            # Créer une copie de l'état actuel
            nouvel_etat = [list(c) for c in etats_systeme]
            # Swapper l'état des deux cases
            nouvel_etat[void_case_index][1], nouvel_etat[voisin_index][1] = (
                nouvel_etat[voisin_index][1],
                nouvel_etat[void_case_index][1],
            )
            # Ajouter le nouvel état à la liste des coups possibles
            coups_possibles.append(nouvel_etat)

    return coups_possibles


"""
    #Génération des coups de type "bouger DEUX cases"

     # Indices des cases de bord et des coins
    coins = {0, 2, 6, 8}

    bords = {1,3,5,7}


    #generer la liste des paires de voisins de la case


    #Si la void case est dans un coin
    if void_case_index in coins :

        voisins_two = []

        # Calcul des paires de voisins pour chaque coin
        if void_case_index == 0:  # Coin supérieur gauche
            voisins_two.append([1, 2])  # Voisins horizontaux
            voisins_two.append([3, 6])  # Voisins verticaux

        elif void_case_index == 2:  # Coin supérieur droit
            voisins_two.append([1, 0])  # Voisins horizontaux
            voisins_two.append([5, 8])  # Voisins verticaux

        elif void_case_index == 6:  # Coin inférieur gauche
            voisins_two.append([7, 8])  # Voisins horizontaux
            voisins_two.append([3, 0])  # Voisins verticaux

        elif void_case_index == 8:  # Coin inférieur droit
            voisins_two.append([7, 6])  # Voisins horizontaux
            voisins_two.append([5, 2])  # Voisins verticaux



        etats_systeme[8][1] = etats_systeme[7][1]
        etats_systeme[7][1] = etats_systeme[6][1]
        etats_systeme[6][1] = 3




        #faire les swaps

    if void_case_index in bords:

        voisins_one = []

        # Calcul des voisins en face en fonction du bord
        if void_case_index == 1:  # Bord supérieur (milieu)
            voisins = [4, 7]  # Voisins en dessous
        elif void_case_index == 3:  # Bord gauche (milieu)
            voisins = [4, 5]  # Voisins à droite
        elif void_case_index == 5:  # Bord droit (milieu)
            voisins = [3, 4]  # Voisins à gauche
        elif void_case_index == 7:  # Bord inférieur (milieu)
            voisins = [1, 4]  # Voisins au-dessus

        #Trouver la paire de voisins
        #Faire le swap



        for toutes les paires de cases :
        simuler le déplacement des deux cases en même temps :

            la void case prend le statut de la case du milieu
            la case du milieu prend le statut de celle du fond
            la case du fond (initiallement la voisine de celle collée à la void case) prend le statut de void case (3)


            coups_possibles.append(nouvel_etat)

"""










"""
    # Étape 1 : Identifier les pions
    pions = [case for case in etats_systeme if case[1] == 1 or case[1] == 2]

    # Étape 2 : Identifier les cases vides
    cases_jouables = [case for case in etats_systeme if case[1] == 0]
"""





##################################################

def check_victory(etats_systeme, joueur):
    """
    Vérifie si le joueur a gagné.
    Un joueur gagne si trois de ses pions sont alignés horizontalement, verticalement ou diagonalement.

    :param etats_systeme: Liste représentant l'état du système.
    :param joueur: Identifiant du joueur à vérifier (1 ou 2).
    :return: True si le joueur a gagné, False sinon.
    """
    # Supposons que le plateau soit 3x3 ou autre format, chaque ligne étant dans l'état du système
    # Transformation en tableau 2D basé sur l'état du système
    plateau = [etats_systeme[i:i + 3] for i in range(0, len(etats_systeme), 3)]

    # Vérification des lignes
    for row in plateau:
        if all(cell[1] == joueur for cell in row):
            return True

    # Vérification des colonnes
    for col in range(3):
        if all(plateau[row][col][1] == joueur for row in range(3)):
            return True

    # Vérification des diagonales
    if all(plateau[i][i][1] == joueur for i in range(3)):  # Diagonale principale
        return True
    if all(plateau[i][2 - i][1] == joueur for i in range(3)):  # Diagonale secondaire
        return True

    return False

def minimax(etats_systeme, is_maximizing, joueur, joueur_adverse, alpha, beta):
    """
    Implémente l'algorithme Minimax avec élagage alpha-bêta.

    :param etats_systeme: Liste représentant l'état du système.
                          Chaque élément est de la forme [ID_case, état_case].
    :param is_maximizing: Booléen indiquant si c'est le tour du joueur maximisant.
    :param joueur: Identifiant du joueur (1 ou 2).
    :param joueur_adverse: Identifiant du joueur adverse (1 ou 2).
    :param alpha: Meilleure valeur trouvée pour le joueur maximisant.
    :param beta: Meilleure valeur trouvée pour le joueur minimisant.
    :return: Une paire (score, coup) où :
             - score est le score évalué pour le meilleur coup.
             - coup est un dictionnaire représentant le coup à jouer.
    """
    # Étape 1 : Vérifier les conditions de fin
    if check_victory(etats_systeme, joueur):  # Victoire du joueur
        return 1, None
    if check_victory(etats_systeme, joueur_adverse):  # Victoire de l'adversaire
        return -1, None
    if all(case[1] != 0 for case in etats_systeme):  # Pas de coup possible (match nul)
        return 0, None

    # Étape 2 : Initialisation des variables
    best_move = None
    if is_maximizing:
        best_score = float('-inf')
    else:
        best_score = float('inf')

    # Étape 3 : Générer tous les coups possibles
    possible_moves = generer_coups(joueur if is_maximizing else joueur_adverse, etats_systeme)

    # Étape 4 : Parcourir les coups possibles
    for move in possible_moves:
        # Simuler le coup
        etats_systeme = apply_move(etats_systeme, move)

        # Appel récursif avec l'état modifié
        score, _ = minimax(
            etats_systeme,
            not is_maximizing,
            joueur,
            joueur_adverse,
            alpha,
            beta
        )

        # Annuler le coup (backtracking)
        etats_systeme = undo_move(etats_systeme, move)

        # Mettre à jour le meilleur score et coup selon le type de joueur
        if is_maximizing:
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, best_score)
        else:
            if score < best_score:
                best_score = score
                best_move = move
            beta = min(beta, best_score)

        # Élagage alpha-bêta
        if beta <= alpha:
            break

    # Étape 5 : Retourner le meilleur score et coup
    return best_score, best_move



# Exemple des fonctions utilitaires utilisées ci-dessus


#######################################

# Modification de la fonction apply_move
def apply_move(etats_systeme, move):
    """
    Applique un coup à l'état du système et enregistre les informations nécessaires pour annuler ce coup.

    :param etats_systeme: Liste représentant l'état du système.
    :param move: Coup à appliquer.
    :return: État du système modifié.
    """
    # Enregistrer l'état de la case avant le coup
    case = next((case for case in etats_systeme if case[0] == move['id_case']), None)
    if case:
        move['previous_state'] = case[1]  # Enregistre l'état précédent de la case
        move['previous_coords'] = case[0]  # Enregistre les coordonnées de la case avant le déplacement

    # Appliquer le coup, par exemple poser un pion ou déplacer une case
    if move['type'] == 'poser_pion':
        case[1] = move['new_state']  # Le nouvel état de la case (pion posé)

    elif move['type'] == 'deplacer_pion':
        source_case = next((case for case in etats_systeme if case[0] == move['source_case_id']), None)
        target_case = next((case for case in etats_systeme if case[0] == move['id_case']), None)

        if source_case and target_case:
            # Appliquer le déplacement du pion
            source_case[1] = 0  # La case source devient vide
            target_case[1] = move['new_state']  # Le pion est déplacé vers la case cible

    elif move['type'] == 'deplacer_case':
        case = next((case for case in etats_systeme if case[0] == move['id_case']), None)
        if case:
            # Appliquer le déplacement de la case
            case[0] = move['new_coords']  # Met à jour les coordonnées de la case

    # Retourner l'état modifié
    return etats_systeme


#############################################

# Modification de la fonction undo_move
def undo_move(etats_systeme, move):
    """
    Annule un coup sur l'état du système en utilisant les informations stockées.

    :param etats_systeme: Liste représentant l'état du système.
    :param move: Coup à annuler.
    :return: État du système restauré.
    """
    case = next((case for case in etats_systeme if case[0] == move['id_case']), None)
    if case:
        # Restaurer l'état de la case à son état précédent
        case[1] = move['previous_state']  # Restaure l'état original de la case

        # Si le coup était un "déplacement de pion", annuler le mouvement
        if move['type'] == 'deplacer_pion':
            source_case = next((case for case in etats_systeme if case[0] == move['source_case_id']), None)
            target_case = next((case for case in etats_systeme if case[0] == move['id_case']), None)

            if source_case and target_case:
                # Restaure la case source et la case cible
                source_case[1] = move['new_state']  # Restaure l'état du pion sur la case source
                target_case[1] = 0  # La case cible devient vide

        # Si le coup était un "déplacement de case", annuler le déplacement
        elif move['type'] == 'deplacer_case':
            case[0] = move['previous_coords']  # Restaure les coordonnées d'origine de la case déplacée

    # Retourner l'état restauré
    return etats_systeme
