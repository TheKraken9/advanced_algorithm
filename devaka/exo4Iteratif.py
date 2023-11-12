def find_sum(arr, target):
    n = len(arr)
    # crée une matrice de dimensions (n+1)x(target+1) remplie de valeurs False
    table = [[False] * (target+1) for _ in range(n+1)]
    # initialiser la première colonne à True
    for i in range(n+1):
        table[i][0] = True
    # remplir le tableau avec des valeurs booléennes
    for i in range(1, n+1):
        for j in range(1, target+1):
            if j < arr[i-1]:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = table[i-1][j] or table[i-1][j-arr[i-1]]
    return table[n][target]

arr1 = [2, 3, 5, 8, 15, 20, 25, 30, 7]
target1 = 9
arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target2 = 12
if __name__ == '__main__':
    if find_sum(arr2, target2):
        print("Il existe des éléments dont la somme est égale à la cible.")
    else:
        print("Il n'existe pas d'éléments dont la somme est égale à la cible.")