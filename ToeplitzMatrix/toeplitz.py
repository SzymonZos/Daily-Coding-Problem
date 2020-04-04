def solve(matrix):
    last_row = matrix[0][:-1]
    for row in matrix[1:]:
        if row[1:] != last_row:
            return False
        last_row = row[:-1]
    return True


def main():
    matrix = [[1, 2, 3, 4, 8],
              [5, 1, 2, 3, 4],
              [4, 5, 1, 2, 3],
              [7, 4, 5, 1, 2]]
    print(solve(matrix))


if __name__ == "__main__":
    main()
