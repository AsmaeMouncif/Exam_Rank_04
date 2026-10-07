def merge_sorted_lists(lists: list[list[int]]) -> list[int]:
    merge = sum(lists, [])
    while True:
        swapped = False
        for n in range(len(merge) - 1):
            if merge[n] > merge[n + 1]:
                merge[n], merge[n + 1] = merge[n + 1], merge[n]
                swapped = True
        if swapped == False:
            break
    return merge


if __name__ == "__main__":
    print(merge_sorted_lists([[1, 3, 5], [2, 4, 6]]))
    print(merge_sorted_lists([[1, 5, 9], [2, 3, 8], [4, 6, 7]]))
    print(merge_sorted_lists([[5], [1, 3], [2, 4]]))
    print(merge_sorted_lists([[1, 1, 2], [2, 3, 3]]))
    print(merge_sorted_lists([[], [1, 2, 3]]))
    print(merge_sorted_lists([[]]))
    print(merge_sorted_lists([[-5, -1, 0], [-3, 2, 4]]))
    print(merge_sorted_lists([[10], [10], [10]]))
