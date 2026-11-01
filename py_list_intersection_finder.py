def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if lists == []:
        return []

    result = []
    first_list = lists[0]

    for element in first_list:
        found = True

        for i in lists:
            if element not in i:
                found = False
                break

        if found and element not in result:
            result.append(element)

    return result