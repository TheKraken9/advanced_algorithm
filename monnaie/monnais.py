def composant(k, values):
    if k == 1:
        return [1]
    for i in range(1, k):
        temp = all_composant(k, i)
        for j in range(len(temp)):
            if exist_in(temp[j], values):
                return temp[j]
    return None


def exist_in(this_value, in_that):
    for i in range(len(this_value)):
        if this_value[i] not in in_that:
            return False
    return True


def all_composant(n, combination_length):
    possibility = []
    if combination_length == 1:
        possibility.append([n])
        return possibility
    for i in range(1, n):
        temp = cross_join(i, all_composant(n - i, combination_length - 1))
        print(temp)
        for j in range(len(temp)):
            possibility.append(temp[j])
    return possibility


def cross_join(n, result):
    possibility = []
    for i in range(len(result)):
        temp = [n] + result[i]
        possibility.append(temp)
    return possibility


if __name__ == '__main__':
    print(composant(8, [1, 2, 3]))
