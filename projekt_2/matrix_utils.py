from math import sin, sqrt
from copy import deepcopy

from exceptions import DifferentSizesException

def create_band_matrix(N, a1, a2, a3):
    matrix = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):

        # Diagonal of a3
        if i > 1:
            matrix[i][i-2] = a3

        # Diagonal of a2
        if i > 0:
            matrix[i][i-1] = a2

        # Diagonal of a1
        matrix[i][i] = a1

        # Diagonal of a2
        if i < N-1:
            matrix[i][i+1] = a2

        # Diagonal of a3
        if i < N-2:
            matrix[i][i + 2] = a3

    return matrix

def create_vector_b(N, F):
    vector = []
    for i in range(N):
        vector.append(sin((i+1)*(F + 1)))
    return vector

def get_l_matrix(M):
    L = deepcopy(M)

    for i in range(len(M)):
        for j in range(i, len(M)):
            L[i][j] = 0

    return L

def get_d_matrix(M):
    D = [[0 for _ in range(len(M))] for _ in range(len(M))]

    for i in range(len(M)):
        D[i][i] = M[i][i]

    return D

def get_u_matrix(M):
    U = deepcopy(M)

    for i in range(len(M)):
        for j in range(0, i + 1):
            U[i][j] = 0

    return U

def sum(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise DifferentSizesException

    sum = [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]

    return sum

def mul_by_vec(M, vec):
    if len(M[0]) != len(vec):
        raise DifferentSizesException

    result = [0]*len(vec)

    for i in range(len(vec)):
        sum = 0
        for j in range(len(vec)):
            sum += M[i][j] * vec[j]

        result[i] = sum

    return result

def forward_sub(L, b):
    """ Solves Lx = b for x """

    x = []
    for i in range(len(b)):
        x.append(b[i])
        for j in range(i):
            x[i] = x[i]-(L[i][j]*x[j])
        x[i] = x[i]/L[i][i]
    return x

    # x = [0]*len(L)
    # for i in range(len(L)):
    #     sum = b[i]
    #     for j in range(i-1):
    #         sum -= L[i][j] * x[j]
    #     x[i] = sum / L[i][i]
    # return x

    # b = deepcopy(b)
    # x = [0]*len(b)

    # for i in range(len(b)):
    #     x[i] = b[i]
    #     for j in range(len(b)):
    #         b[j] = b[j] - L[j][i] * x[i]
    # return x

def back_sub(U, b):
    """ x = back_sub(U, b) is the solution to U x = b """

    x = [0]*len(U)

    for i in range(len(U) - 1, -1, -1):
        tmp = b[i]
        for j in range(i+1, len(U)):
            tmp -= U[i][j] * x[j]
        x[i] = tmp / U[i][i]
    return x

def norm_res(A, x, b):
    result = res(A, x, b)
    result = norm(result)
    return result

def res(A, x, b):
    res = mul_by_vec(A, x)
    res = [res[i] - b[i] for i in range(len(b))]
    return res

def norm(vec):
    sum = 0
    for v in vec:
        sum += v**2
    return sqrt(sum)