def check_sum_exists2(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return True
    return False
arr = [3, 5, 8, 2, 9, 10]
target = 13
if __name__ == '__main__':
    print(check_sum_exists2(arr, target))  # True


def check_sum_exists3(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] == target:
                    return True
    return False
arr = [3, 5, 8, 2, 9, 10]
target = 13
if __name__ == '__main__':
    print(check_sum_exists3(arr, target))  # True