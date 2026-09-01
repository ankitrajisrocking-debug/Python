def determinant(A):
    n = len(A)
    A = [row[:] for row in A]
    det = 1

    for i in range(n):
        for j in range(i, n):
            if A[j][i] != 0:
                break

        if A[j][i] == 0:
            return 0

        if i != j:
            A[i], A[j] = A[j], A[i]
            det = -det

        det *= A[i][i]

        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]

    return det


def rank(A):
    A = [row[:] for row in A]
    rows = len(A)
    cols = len(A[0])
    r = 0

    for col in range(cols):
        pivot = None

        for i in range(r, rows):
            if A[i][col] != 0:
                pivot = i
                break

        if pivot is not None:
            A[r], A[pivot] = A[pivot], A[r]

            for i in range(r + 1, rows):
                factor = A[i][col] / A[r][col]
                for j in range(col, cols):
                    A[i][j] -= factor * A[r][j]

            r += 1

    return r


def inverse(A):
    n = len(A)
    aug = [A[i][:] + [1 if i == j else 0 for j in range(n)]
           for i in range(n)]

    for i in range(n):
        pivot = i

        for j in range(i, n):
            if aug[j][i] != 0:
                pivot = j
                break

        if aug[pivot][i] == 0:
            return None

        aug[i], aug[pivot] = aug[pivot], aug[i]

        x = aug[i][i]
        aug[i] = [v / x for v in aug[i]]

        for j in range(n):
            if j != i:
                x = aug[j][i]
                aug[j] = [aug[j][k] - x * aug[i][k]
                          for k in range(2 * n)]

    return [row[n:] for row in aug]


# Matrix
A = [[1, 2, 3],
     [0, 1, 4],
     [5, 6, 0]]

print("Determinant =", determinant(A))
print("Rank =", rank(A))

inv = inverse(A)

if inv:
    print("Inverse:")
    for row in inv:
        print(row)
else:
    print("Inverse does not exist.")
