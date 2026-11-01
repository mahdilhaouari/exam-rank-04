def array_rotation_detector(arr1: list, arr2: list) -> bool:
    if arr1 == [] and arr2 == []:
        return True
    if arr1 == [] or arr2 == []:
        return False

    len1 = len(arr1)
    len2 = len(arr2)

    if len1 != len2:
        return False

    if arr1 == arr2:
        return True

    new_arr = [0] * len1

    for _ in arr1:
        i = 0
        while i < len1:
            new_arr[i] = arr1[i - 1]
            i += 1

        if new_arr == arr2:
            return True

        arr1 = new_arr.copy()

    return False


def main():
    print(array_rotation_detector([1, 2, 3], [3, 1, 2]))
    print(array_rotation_detector([1, 2, 3], [2, 3, 1]))
    print(array_rotation_detector([1, 2, 3], [1, 2, 3]))
    print(array_rotation_detector([1, 2, 3], [3, 2, 1]))
    print(array_rotation_detector([], []))


main()