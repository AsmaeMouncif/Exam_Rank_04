def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    if k <= 0:
        return []
    result = []
    for i in range(len(nums) - k + 1):
        new_l = nums[i:]
        max_n = max(new_l[:k])
        result.append(max_n)
    return result


if __name__ == "__main__":
    print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(sliding_window_maximum([1, 2, 3, 4, 5], 2))
    print(sliding_window_maximum([5, 4, 3, 2, 1], 1))
    print(sliding_window_maximum([1, 2, 3], 3))
    print(sliding_window_maximum([1, 2, 3], 4))
    print(sliding_window_maximum([], 2))
    print(sliding_window_maximum([1, 2, 3], 0))
