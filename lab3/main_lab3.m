clc
clear all
close all

% odpowiednie fragmenty kodu mozna wykonac poprzez zaznaczenie i wcisniecie F9 w Matlabie
% komentowanie/odkomentowywanie: ctrl+r / ctrl+t

% Zadanie A
%------------------
N = 10;
density = 3; % parametr decydujacy o gestosci polaczen miedzy stronami
[Edges] = generate_network(N, density);
%-----------------

% Zadanie B
%------------------
% generacja macierzy I, A, B i wektora b
% macierze A, B i I musza byc przechowywane w formacie sparse (rzadkim)

d = 0.85;

B = sparse(Edges(2,:), Edges(1,:), ones(size(Edges(1,:))));
I = speye(N);
L = sum(B);
A = sparse(diag(1./L));

M = I - d*B*A;

% Zadanie C
%-----------------

b = ones(N,1)*((1-d)/N);
r = M \ b;

%-----------------

%% 


% Zadanie D
%------------------
clc
clear all
close all

N = [500, 1000, 3000, 6000, 12000];
density = 10;
d = 0.85;

for i = 1:5

    [Edges] = generate_network(N(i), density);

    B = sparse(Edges(2,:), Edges(1,:), ones(size(Edges(1,:))));
    I = speye(N(i));
    L = sum(B);
    A = sparse(diag(1./L));
   
    b = ones(N(i),1)*((1-d)/N(i));

    M = I - d*B*A;

    tic
    % obliczenia start
    r = M \ b;
    % obliczenia stop
    czas_Gauss(i) = toc;
end

plot(N, czas_Gauss)
title("Wykres zależności czasu od wielkości sieci dla metody bezpośredniej")
xlabel("Wielkość sieci")
ylabel("Czas [s]")
print -dpng zadanieD
%------------------

%% 


% Zadanie E
%------------------
clc
clear all
close all

% sprawdz przykladowe dzialanie funkcji tril, triu, diag:
% Z = rand(4,4)
% tril(Z,-1) 
% triu(Z,1) 
% diag(diag(Z))

N = [500, 1000, 3000, 6000, 12000];
density = 10;
d = 0.85;

for i = 1:5

    [Edges] = generate_network(N(i), density);

    B = sparse(Edges(2,:), Edges(1,:), ones(size(Edges(1,:))));
    I = speye(N(i));
    L = sum(B);
    A = sparse(diag(1./L));
   
    b = ones(N(i),1)*((1-d)/N(i));

    M = I - d*B*A;

    L = tril(M, -1);
    U = triu(M, 1);
    D = diag(diag(M));

    tic
    % obliczenia start

    r = (-D)\(L + U)*ones(N(i),1) + D\b;
    res = M*r - b;
    iter = 1;
    norm_res = norm(res);
    if N(i) == 1000
        norm_res_1000(iter) = norm_res;
    end
    while norm_res > 10^-14
        r = (-D)\(L + U)*r + D\b;
        res = M*r - b;
        iter = iter + 1;
        norm_res = norm(res);
        if N(i) == 1000
            norm_res_1000(iter) = norm_res;
        end
    end
    % obliczenia stop
    czas_Jacobi(i) = toc;
    iters(i) = iter;
end

plot(N, czas_Jacobi)
title("Wykres zależności czasu od wielkości sieci dla metody Jacobiego")
xlabel("Wielkość sieci")
ylabel("Czas [s]")
print -dpng zadanieE_czas
figure

plot(N, iters)
title("Wykres zależności iteracji od wielkości sieci dla metody Jacobiego")
xlabel("Wielkość sieci")
ylabel("Ilość iteracji")
print -dpng zadanieE_iteracje
figure

semilogy(norm_res_1000)
title(["Wykres zmiany normy błędu rezydualnego w kolejnych iteracjach ",
    "dla wielkości sieci równej 1000, dla metody Jacobiego"])
xlabel("Ilość iteracji")
ylabel("Błąd rezydualny")
print -dpng zadanieE_norma
%------------------

%% 

% Zadanie F
%------------------

clc
clear all
close all

% sprawdz przykladowe dzialanie funkcji tril, triu, diag:
% Z = rand(4,4)
% tril(Z,-1) 
% triu(Z,1) 
% diag(diag(Z))

N = [500, 1000, 3000, 6000, 12000];
density = 10;
d = 0.85;

for i = 1:5

    [Edges] = generate_network(N(i), density);

    B = sparse(Edges(2,:), Edges(1,:), ones(size(Edges(1,:))));
    I = speye(N(i));
    L = sum(B);
    A = sparse(diag(1./L));
   
    b = ones(N(i),1)*((1-d)/N(i));

    M = I - d*B*A;

    L = tril(M, -1);
    U = triu(M, 1);
    D = diag(diag(M));

    tic
    % obliczenia start

    r = (-(D+L))\(U*ones(N(i),1)) + (D+L)\b;
    res = M*r - b;
    iter = 1;
    norm_res = norm(res);
    if N(i) == 1000
        norm_res_1000(iter) = norm_res;
    end
    while norm_res > 10^-14
        r = (-(D+L))\(U*r) + (D+L)\b;
        res = M*r - b;
        iter = iter + 1;
        norm_res = norm(res);
        if N(i) == 1000
            norm_res_1000(iter) = norm_res;
        end
    end
    % obliczenia stop
    czas_Gaussa_Seidla(i) = toc;
    iters(i) = iter;
end

plot(N, czas_Gaussa_Seidla)
title("Wykres zależności czasu od wielkości sieci dla metody Gaussa-Seidla")
xlabel("Wielkość sieci")
ylabel("Czas [s]")
print -dpng zadanieF_czas
figure

plot(N, iters)
title("Wykres zależności iteracji od wielkości sieci dla metody Gaussa-Seidla")
xlabel("Wielkość sieci")
ylabel("Ilość iteracji")
print -dpng zadanieF_iteracje
figure

semilogy(norm_res_1000)
title(["Wykres zmiany normy błędu rezydualnego w kolejnych iteracjach ",
    "dla wielkości sieci równej 1000, dla metody Gaussa-Seidla"])
xlabel("Ilość iteracji")
ylabel("Błąd rezydualny")
print -dpng zadanieF_norma

%% 

% Zadanie G
%------------------

clc
clear all
close all

load("Dane_Filtr_Dielektryczny_lab3_MN.mat")

% Metoda bezpośrednia

r = M\b;
res = M*r - b;
norm_res_bez = norm(res);

% Metoda Jacobiego

L = tril(M, -1);
U = triu(M, 1);
D = diag(diag(M));

r = (-D)\(L + U)*ones(length(M),1) + D\b;
res = M*r - b;
norm_res = norm(res);
while norm_res > 10^-14
    r = (-D)\(L + U)*r + D\b;
    res = M*r - b;
    norm_res = norm(res);
end

norm_res_Jacobi = norm_res;

% Metoda Gaussa-Seidla

L = tril(M, -1);
U = triu(M, 1);
D = diag(diag(M));

r = (-(D+L))\(U*ones(length(M),1)) + (D+L)\b;
res = M*r - b;
norm_res = norm(res);
while norm_res > 10^-14
    r = (-(D+L))\(U*r) + (D+L)\b;
    res = M*r - b;
    norm_res = norm(res);
end

norm_res_Gaussa = norm_res;
