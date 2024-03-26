import matrix_utils as mx

def gauss_seidel_iter(M, b, stop_value):
    L = mx.get_l_matrix(M)
    D = mx.get_d_matrix(M)
    U = mx.get_u_matrix(M)

    iters = 0
    r = [1]*len(M)
    ress = []
    res = mx.norm_res(M, r, b)
    ress.append(res)

    while res > stop_value:
        left_side = [i * -1 for i in mx.forward_sub(mx.sum(D, L), mx.mul_by_vec(U, r))]
        right_side = mx.forward_sub(mx.sum(D, L), b)
        r = [left_side[i] + right_side[i] for i in range(len(left_side))]
        iters += 1
        res = mx.norm_res(M, r, b)
        ress.append(res)

    return r, iters, ress

def gauss_seidel_check_for_convergence(M, b, stop_value):
    L = mx.get_l_matrix(M)
    D = mx.get_d_matrix(M)
    U = mx.get_u_matrix(M)

    iters = 0
    r = [1]*len(M)
    norm_ress = []

    while mx.norm_res(M, r, b) > stop_value:
        norm_ress.append(mx.norm_res(M, r, b))
        left_side = [i * -1 for i in mx.forward_sub(mx.sum(D, L), mx.mul_by_vec(U, r))]
        right_side = mx.forward_sub(mx.sum(D, L), b)
        r = [left_side[i] + right_side[i] for i in range(len(left_side))]
        iters += 1
        if iters > 50:
            break

    return norm_ress