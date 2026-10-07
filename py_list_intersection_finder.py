def list_intersection_finder(lists: list[list[int]]) -> list[int]:
    if len(lists) == 0:
        return []
    result = []
    for n in lists[0]:
        found = True
        for lst in lists[1:]:
            if n not in lst:
                found = False
        if found:
            if n not in result:
                result.append(n)
    return result


if __name__ == "__main__":
    print(list_intersection_finder([[1, 2, 3], [2, 3, 4], [2, 3, 5]]))
    print(list_intersection_finder([[1, 2, 3, 4], [2, 4, 6, 8], [4, 8, 12]]))
    print(list_intersection_finder([[1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3]]))
    print(list_intersection_finder([[1, 2, 3], [4, 5, 6]]))
    print(list_intersection_finder([]))
    print(list_intersection_finder([[1, 2, 3], []]))
    print(list_intersection_finder([[5]]))
