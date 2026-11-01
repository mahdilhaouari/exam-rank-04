################## my version with bad timecomplixcety ############## 

def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    result = []
    for list in lists:
        for element in list:
            result.append(element)
    limit = len(result)
    i = 0
    while i < limit:
        j = i + 1
        while j < limit :
            if result[i] > result[j]:
                tmp = result[i]
                result[i] = result[j]
                result[j] = tmp
            j += 1
        i += 1 
    return result
print(merge_sorted_lists([[1,2,3],[1,2,3]]))

################ more efficient one ###################
def merge_two(a, b):
    result = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    result.extend(a[i:])
    result.extend(b[j:])

    return result


def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    result = []

    for current_list in lists:
        result = merge_two(result, current_list)

    return result


print(merge_sorted_lists([[1, 3, 5], [2, 4, 6]]))
