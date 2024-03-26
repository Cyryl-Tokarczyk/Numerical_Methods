def lagrange_interpolation(xs, ys, x):

    result = .0

    for i in range(len(xs)):
        
        term = ys[i]

        for j in range(len(xs)):
            if j != i:
                term *= (x - xs[j]) / (xs[i] - xs[j])

        result += term

    return result    
        