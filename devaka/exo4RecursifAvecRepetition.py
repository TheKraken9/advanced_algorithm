def find_combinations(arr, target):
    # Trouve toutes les combinaisons possibles dans la liste `arr` qui ajoute à la somme `target`
    n = len(arr)
    combinations = []

    def find_combinations_helper(curr_combination, curr_sum, start_index):
        # si la somme courante est égale à la cible, on ajoute la combinaison courante à la liste des combinaisons
        if curr_sum == target:
            combinations.append(curr_combination[:])
            return

        # parcourir les éléments restants
        for i in range(start_index, n):

            # ignorer les éléments avec une valeur supérieure à la valeur cible
            if curr_sum + arr[i] > target:
                continue

            # ajouter l'élément actuel à la combinaison courante
            curr_combination.append(arr[i])

            # réduire la valeur cible de la somme par la valeur de l'élément actuel
            find_combinations_helper(curr_combination, curr_sum + arr[i], i)

            # retirer l'élément actuel de la combinaison courante pour tester les combinaisons suivantes
            curr_combination.pop()

    find_combinations_helper([], 0, 0)

    return combinations


arr = [2, 4, 6, 8, 10]
target = 10
if __name__ == '__main__':
    combinations = find_combinations(arr, target)
    print(combinations)
