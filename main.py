from fractions import Fraction


def parse_matrix():
    print("Enter the size n of an n x n matrix:")
    n = int(input("> ").strip())

    matrix = []
    print(f"Enter {n} rows. Separate numbers with spaces.")

    for i in range(n):
        while True:
            row = input(f"Row {i + 1}: ").strip().split()

            if len(row) != n:
                print(f"Please enter exactly {n} numbers.")
                continue

            try:
                matrix.append([Fraction(x) for x in row])
                break
            except ValueError:
                print("Please enter valid integers or fractions.")

    return matrix


def print_augmented(augmented, n):
    width = 10

    for row in augmented:
        left = row[:n]
        right = row[n:]

        left_text = " ".join(f"{str(x):>{width}}" for x in left)
        right_text = " ".join(f"{str(x):>{width}}" for x in right)

        print(f"{left_text}   |   {right_text}")

    print()


def inverse_gauss_jordan(matrix, show_steps=True):
    n = len(matrix)

    # Build [A | I]
    augmented = [
        row[:] + [Fraction(int(i == j)) for j in range(n)]
        for i, row in enumerate(matrix)
    ]

    if show_steps:
        print("\nInitial augmented matrix [A | I]")
        print_augmented(augmented, n)

    for col in range(n):
        # Find a non-zero pivot.
        pivot_row = None
        for r in range(col, n):
            if augmented[r][col] != 0:
                pivot_row = r
                break

        if pivot_row is None:
            return None

        # Swap rows if necessary.
        if pivot_row != col:
            augmented[col], augmented[pivot_row] = augmented[pivot_row], augmented[col]

            if show_steps:
                print(f"R{col + 1} <-> R{pivot_row + 1}")
                print_augmented(augmented, n)

        # Make pivot equal to 1.
        pivot = augmented[col][col]

        if pivot != 1:
            augmented[col] = [x / pivot for x in augmented[col]]

            if show_steps:
                print(f"R{col + 1} <- R{col + 1} / ({pivot})")
                print_augmented(augmented, n)

        # Eliminate this column from all other rows.
        for r in range(n):
            if r == col:
                continue

            factor = augmented[r][col]

            if factor != 0:
                augmented[r] = [
                    augmented[r][c] - factor * augmented[col][c]
                    for c in range(2 * n)
                ]

                if show_steps:
                    print(
                        f"R{r + 1} <- R{r + 1} - ({factor})R{col + 1}"
                    )
                    print_augmented(augmented, n)

    return [row[n:] for row in augmented]


def print_matrix(matrix):
    if matrix is None:
        print("No inverse exists.")
        return

    for row in matrix:
        print("[ " + "  ".join(f"{str(x):>8}" for x in row) + " ]")


def main():
    print("=" * 46)
    print("        MATRIX INVERSE CLICKER")
    print("     Gauss-Jordan, from scratch")
    print("=" * 46)

    try:
        matrix = parse_matrix()
    except (ValueError, EOFError):
        print("Invalid input.")
        return

    print("\nFinding the inverse...\n")
    inverse = inverse_gauss_jordan(matrix, show_steps=True)

    print("=" * 46)

    if inverse is None:
        print("This matrix is singular.")
        print("Its inverse does not exist.")
    else:
        print("Inverse matrix:")
        print_matrix(inverse)

    print("=" * 46)


if __name__ == "__main__":
    main()
