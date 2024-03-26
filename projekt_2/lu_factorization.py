import matrix_utils as mx

def lu_factorization(M, b):
    L, U = doolitle_decomposition(M)

    y = mx.forward_sub(L, b)
    x = mx.back_sub(U, y)

    return x

def doolitle_decomposition(A):
    L = [[0 for _ in range(len(A))] for _ in range(len(A))]
    U = [[0 for _ in range(len(A))] for _ in range(len(A))]

    for i in range(len(L)):
        L[i][i] = 1

    for j in range(len(L)):
        for i in range(j+1):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))

        for i in range(j + 1, len(L)):
            L[i][j] = (1 / U[j][j]) * (A[i][j] - sum(L[i][k] * U[k][j] for k in range(j)))

    return L, U

M = [
    [5, 3, 7, 4, 2],
    [9, 2, 2, 1, 1],
    [3, 6, 2, 8, 9],
    [9, 4, -2, -1, -3],
    [0, 5, 3, -6, -11]
]

M1 = [
    [2, 7, 1],
    [3, -2, 0],
    [1, 5, 3]
]

doolitle_decomposition(M1)