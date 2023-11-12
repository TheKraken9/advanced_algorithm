# Exo4.py - Récursif
def find_sum_recursive(arr, target, index):
    if target == 0:
        return True
    elif target < 0 or index >= len(arr):
        return False
    else:
        return find_sum_recursive(arr, target-arr[index], index+1) or find_sum_recursive(arr, target, index+1)
arr = [2, 3, 5, 8, 15, 20, 25, 30, 1]
target = 9
if __name__ == '__main__':
    if find_sum_recursive(arr, target, 0):
        print("Il existe des éléments dont la somme est égale à la cible.")
    else:
        print("Il n'existe pas d'éléments dont la somme est égale à la cible.")
