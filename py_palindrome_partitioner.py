def palindrome(s: str) -> bool:
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return 0
    return 1


def palindrome_partitioner(s: str) -> int:
    if palindrome(s) == 1:
        return 0
    best = len(s) - 1
    for i in range(1, len(s)):
        if palindrome(s[:i]) == 1:
            cuts = 1 + palindrome_partitioner(s[i:])
            if cuts < best:
                best = cuts
    return best


if __name__ == "__main__":
    print(palindrome_partitioner("aab"))
    # 1
    print(palindrome_partitioner("aba"))
    # 0
    print(palindrome_partitioner("abc"))
    # 2
    print(palindrome_partitioner("aabbc"))