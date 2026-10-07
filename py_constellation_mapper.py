def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
    result = []
    for r in range(dim):
        row = ""
        for c in range(dim):
            if (r, c) in stars:
                row = row + "*"
            else:
                row = row + "."
        result.append(row)
    return result


if __name__ == "__main__":
    print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3))
    print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3))
    print(constellation_mapper([], 2))
    print(constellation_mapper([(0, 0), (0, 0), (1, 1)], 2))
    print(constellation_mapper([(0, 0), (5, 5)], 3))
    print(constellation_mapper([(1, 0), (1, 1), (1, 2)], 3))
