from gauss_seidel import *
from jacobi import *
from lu_factorization import *
import matrix_utils as mx
from timeit import default_timer as timer
import matplotlib.pyplot as plt


N = 924 # 924
E = 6
F = 8
a1 = 5 + E
a2 = a3 = -1
STOP_VALUE = 1e-9

# A

A = mx.create_band_matrix(N, a1, a2, a3)
b = mx.create_vector_b(N, F)

# B

jacobi_time = timer()
jacobi_r, jacobi_iters, jc_res_a = jacobi_iter(A, b, STOP_VALUE)
jacobi_time = timer() - jacobi_time
print('Jacobi:')
print(f'\tIterations needed: {jacobi_iters}')
print(f'\tTime needed: {jacobi_time}')

gauss_seidel_time = timer()
gauss_seidel_r, gauss_seidel_iters, gs_res_a = gauss_seidel_iter(A, b, STOP_VALUE)
gauss_seidel_time = timer() - gauss_seidel_time
print('Gauss-Seidel:')
print(f'\tIterations needed: {gauss_seidel_iters}')
print(f'\tTime needed: {gauss_seidel_time}')

plt.semilogy(jc_res_a)
plt.title('Wykres normy błędu rezydualnego dla macierzy z podpunktu A - metoda Jacobiego')
plt.xlabel('Liczba iteracji')
plt.ylabel('Norma błędu rezydualnego (skala logarytmiczna)')
plt.savefig(f'wykresy\\norm_res_jacobi_a', bbox_inches='tight')
plt.figure()
plt.semilogy(gs_res_a)
plt.title('Wykres normy błędu rezydualnego dla macierzy z podpunktu A - metoda Gaussa-Seidla')
plt.xlabel('Liczba iteracji')
plt.ylabel('Norma błędu rezydualnego (skala logarytmiczna)')
plt.savefig(f'wykresy\\norm_res_gs_a', bbox_inches='tight')
plt.show();

# C

A_2 = mx.create_band_matrix(N, 3, -1, -1)

jacobi_res = jacobi_check_for_convergence(A_2, b, STOP_VALUE)
gauss_seidel_res = gauss_seidel_check_for_convergence(A_2, b, STOP_VALUE)

plt.semilogy(jacobi_res)
plt.title('Wykres normy błędu rezydualnego dla macierzy z podpunktu C - metoda Jacobiego')
plt.xlabel('Liczba iteracji')
plt.ylabel('Norma błędu rezydualnego (skala logarytmiczna)')
plt.savefig(f'wykresy\\norm_res_jacobi', bbox_inches='tight')
plt.figure()
plt.semilogy(gauss_seidel_res)
plt.title('Wykres normy błędu rezydualnego dla macierzy z podpunktu C - metoda Gaussa-Seidla')
plt.xlabel('Liczba iteracji')
plt.ylabel('Norma błędu rezydualnego (skala logarytmiczna)')
plt.savefig(f'wykresy\\norm_res_gs', bbox_inches='tight')
plt.show();

# D

lu_fac_time = timer()
lu_r = lu_factorization(A_2, b)
lu_fac_time = timer() - lu_fac_time
print(f'LU factorization time needed: {lu_fac_time}')
print(f'LU factorization residuum norm: {mx.norm_res(A_2, lu_r, b)}')

# E

Ns = [100, 500, 1000, 2000, 3000, 4000, 5000]
jc_times = []
gs_times = []
lu_times = [1.5195677, 196.8323663, 1532.1153585]

for i in range(len(Ns)):
    A = mx.create_band_matrix(Ns[i], a1, a2, a3) # int(Ns[i]/10)
    b = mx.create_vector_b(Ns[i], F)

    t = timer()
    jacobi_iter(A, b, STOP_VALUE)
    jc_times.append(timer() - t)

    t = timer()
    gauss_seidel_iter(A, b, STOP_VALUE)
    gs_times.append(timer() - t)

    if Ns[i] < 2000:
        # continue
        t = timer()
        lu_factorization(A, b)
        lu_times.append(timer() - t)
    else:
        lu_times.append(lu_times[i-1]*(Ns[i]/Ns[i-1])**3)


jc_times = [0.4140812999999999, 8.4278512, 33.909779099999994, 176.41404770000003, 345.6452653, 696.5807665, 1123.5665381000003]
gs_times = [0.29992750000000035, 7.2284397999999985, 34.904126, 130.2929132, 289.3444824999999, 646.4793047999999, 989.9491484000005]

plt.plot(Ns, jc_times, 'o-', label='Jacobi')
plt.plot(Ns, gs_times, 'o-', label='Gauss-Seidel')
plt.plot(Ns, lu_times, 'o-', label='LU')
plt.xlabel('Liczba niewiadomych')
plt.ylabel('Czas trwania algorytmu [s]')
plt.title('Wykres czasu trwania funkcji dla różnych ilości niewiadomych')
plt.savefig(f'wykresy\\all_times', bbox_inches='tight')
plt.figure()
plt.plot(Ns, jc_times, 'o-', label='Jacobi')
plt.plot(Ns, gs_times, 'o-', label='Gauss-Seidel')
plt.xlabel('Liczba niewiadomych')
plt.ylabel('Czas trwania algorytmu [s]')
plt.title('Wykres czasu trwania funkcji dla różnych ilości niewiadomych, dla metod iteracyjnych')
plt.savefig(f'wykresy\\iter_times', bbox_inches='tight')
plt.show();

n = 3