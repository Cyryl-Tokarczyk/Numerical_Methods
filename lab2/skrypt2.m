clear all
close all

Edges = [ 1 1 2 2 2 3 3 3 4 4 5 5 6 6 7;
          4 6 3 4 5 5 6 7 5 6 4 6 4 7 6 ];
N = 7;
d = 0.85;

B = sparse(Edges(2,:), Edges(1,:), ones(size(Edges(1,:))));
I = speye(N);
L = sum(B);
A = sparse(diag(1./L));

full(B)
full(I)
full(L)
full(A)

M = I - d*B*A;
full(M)

b = ones(N,1)*((1-d)/N);
full(b)

diary("sparse_test.txt")
whos A B I M b
diary off

spy(B)
title("Macierz sąsiedztwa połączeń stron")
print -dpng spy_b

r = M\b;
full(r)

figure
bar(r)
title("Wartość PageRank dla poszczególnych stron")
xlabel("Strona")
ylabel("Wartość PageRank")
print -dpng bar

