def merge_sorted_list(lists: list[list[int]]) -> list[int]:
    merged = sum(lists, [])
    return sorted(merged)


if __name__ == "__main__":
    merge0 = merge_sorted_list([[1, 4, 5], [1, 3, 4], [2, 6]])
    print(merge0)
    merge1 = merge_sorted_list([[1, 2, 3], [], [0, 4]])
    print(merge1)
    merge2 = merge_sorted_list([])
    print(merge2)
    merge3 = merge_sorted_list([[], []])
    print(merge3)
