def find_combinations(arr, target):
    # Trouve toutes les combinaisons possibles dans la liste `arr` qui ajoutent à la somme `target`
    n = len(arr)
    combinations = []

    def find_combinations_helper(curr_combination, curr_sum, start_index): # fonction récursive
        # si la somme courante est égale à la cible, on ajoute la combinaison courante à la liste des combinaisons
        if curr_sum == target: # condition d'arrêt
            combinations.append(curr_combination[:]) # copie de la combinaison courante
            return # retourner à l'appelant

        # parcourir les éléments restants
        for i in range(start_index, n): # boucle principale

            # ignorer les éléments avec une valeur supérieure à la valeur cible
            if curr_sum + arr[i] > target: # condition d'arrêt
                continue # passer à l'élément suivant

            # ignorer les éléments déjà utilisés dans la combinaison courante
            if i > start_index and arr[i] == arr[i-1]: # condition d'arrêt
                continue # passer à l'élément suivant

            # ajouter l'élément actuel à la combinaison courante
            curr_combination.append(arr[i]) # ajouter l'élément actuel à la combinaison courante

            # réduire la valeur cible de la somme par la valeur de l'élément actuel
            find_combinations_helper(curr_combination, curr_sum + arr[i], i + 1) # appel récursif

            # retirer l'élément actuel de la combinaison courante pour tester les combinaisons suivantes
            curr_combination.pop() # retirer l'élément actuel de la combinaison courante

    # trier la liste pour gérer les doublons
    arr.sort() # trier la liste

    find_combinations_helper([], 0, 0) # appel initial

    return combinations # retourner la liste des combinaisons


arr = [1, 2, 3, 4, 5, 7] # liste des nombres
target = 21 # valeur cible
if __name__ == '__main__':
    combinations = find_combinations(arr, target) # trouver les combinaisons
    print(combinations) # afficher les combinaisons
