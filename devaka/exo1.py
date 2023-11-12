# exo3.py
def trouver_somme(tab, param):
    for i in range(len(tab) - 2):
        for j in range(i + 1, len(tab) - 1):
            for k in range(j + 1, len(tab)):
                if tab[i] + tab[j] + tab[k] == param:
                    return (tab[i], tab[j], tab[k])
    return None


tableau = [1, 2, 3, 4, 5]
but = 9

if __name__ == '__main__':
    resultat = trouver_somme(tableau, but)

    if resultat is None:
        print("Aucune combinaison de 3 éléments dans S ne donne une somme de", but)
    else:
        print("La somme de", resultat, "est égale à", but)
