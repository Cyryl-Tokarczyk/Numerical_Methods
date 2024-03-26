import matrix_utils as mx

def jacobi_iter(M, b, stop_value):
    L = mx.get_l_matrix(M)
    D = mx.get_d_matrix(M)
    U = mx.get_u_matrix(M)

    # r_k1 = -D^(-1)(L + U)r_k + D^(-1)b
    # Lx = b
    # D x = mx.mul_by_vec(mx.sum(L, U), r)
    # x = D^(-1) * mx.mul_by_vec(mx.sum(L, U), r)

    iters = 0
    r = [1]*len(M)
    ress = []
    res = mx.norm_res(M, r, b)
    ress.append(res)

    while res > stop_value:
        left_side = [i * -1 for i in mx.forward_sub(D, mx.mul_by_vec(mx.sum(L, U), r))]
        right_side = mx.forward_sub(D, b)
        r = [left_side[i] + right_side[i] for i in range(len(left_side))]
        iters += 1
        res = mx.norm_res(M, r, b)
        ress.append(res)

    return r, iters, ress

def jacobi_check_for_convergence(M, b, stop_value):
    L = mx.get_l_matrix(M)
    D = mx.get_d_matrix(M)
    U = mx.get_u_matrix(M)

    # r_k1 = -D^(-1)(L + U)r_k + D^(-1)b
    # Lx = b
    # D x = mx.mul_by_vec(mx.sum(L, U), r)
    # x = D^(-1) * mx.mul_by_vec(mx.sum(L, U), r)

    iters = 0
    r = [1]*len(M)
    norm_ress = []

    while mx.norm_res(M, r, b) > stop_value:
        norm_ress.append(mx.norm_res(M, r, b))
        left_side = [i * -1 for i in mx.forward_sub(D, mx.mul_by_vec(mx.sum(L, U), r))]
        right_side = mx.forward_sub(D, b)
        r = [left_side[i] + right_side[i] for i in range(len(left_side))]
        iters += 1
        if iters > 50:
            break

    return norm_ress