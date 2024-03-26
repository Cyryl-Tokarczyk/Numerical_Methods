%% A
clc
clear all

for i = 1:20
    density(i) = dens(i);
end

plot(density)
title("Gęstość prawdopodobieństwa")
xlabel("x")
ylabel("p(x)")
print -dpng gestosc

%% B

N = 10;
max_val = max(density);
n = 20;

rect(0, n, N)
trap(0, n, N)
simpson(0, n, N)
monte_carlo(0, n, max_val, N)

%% C

clear all

for i = 1:20
    density(i) = dens(i);
end

load P_ref.mat

n = 5;
max_val = max(density);
i = 1;

for N = 5:50:10^4
    rect_err(i) = abs(P_ref - rect(0, n, N));
    trap_err(i) = abs(P_ref - trap(0, n, N));
    simp_err(i) = abs(P_ref - simpson(0, n, N));
    monte_err(i) = abs(P_ref - monte_carlo(0, n, max_val, N));
    i = i + 1;
end

loglog(5:50:10^4, rect_err)
title("Bład dla metody prostokątów")
xlabel("N")
ylabel("Błąd")
print -dpng blad_1

loglog(5:50:10^4, trap_err)
title("Bład dla metody trapezów")
xlabel("N")
ylabel("Błąd")
print -dpng blad_2

loglog(5:50:10^4, simp_err)
title("Bład dla metody Simpsona")
xlabel("N")
ylabel("Błąd")
print -dpng blad_3

loglog(5:50:10^4, monte_err)
title("Bład dla metody Monte Carlo")
xlabel("N")
ylabel("Błąd")
print -dpng blad_4

%% D
N = 10^7;

tic
rect(0, n, N);
rect_time = toc;

tic
trap(0, n, N);
trap_time = toc;

tic
simpson(0, n, N);
simp_time = toc;

tic
monte_carlo(0, n, max_val, N);
monte_time = toc;

bar([rect_time, trap_time, simp_time, monte_time])
set(gca, 'xticklabel', ["Rect", "Trap", "Simp", "Monte"])
title("Porównanie czasów wykonania metod")
ylabel("Czas [s]")
xlabel("Metoda")
print -dpng czasy

%%

function monte = monte_carlo(a, b, c, N)
    S = (b - a) * (c);
    N_1 = 0;
    for i = 1:N
        x = a + rand() * (b - a);
        y = rand() * c;
        if dens(x) > y
            N_1 = N_1 + 1;
        end
    end
    monte = (N_1/N)*S;
end

function simp = simpson(a, b, N)
    dx = (b - a)/N;
    simp = 0;
    for i = 1:N
        x = x_i(a, i-1, dx);
        x_1 = x_i(a, i, dx);
        simp = simp + dens(x) + 4 * dens((x_1 + x)/2) + dens(x_1);
    end
    simp = simp * (dx/6);
end

function tr = trap(a, b, N)
    dx = (b - a)/N;
    tr = 0;
    for i = 1:N
        tr = tr + ((dens(x_i(a, i-1, dx)) + dens(x_i(a, i, dx)))/2) * dx;
    end
end

function rec = rect(a, b, N)
    dx = (b - a)/N;
    rec = 0;
    for i = 1:N
        rec = rec + dens((x_i(a, i, dx) + x_i(a, i-1, dx))/2) * dx;
    end
end

function x_i = x_i(a, i_1, dx)
    x_i = a + (i_1)*dx;
end

function dens = dens(t)
    sig = 3;
    mu = 10;
    dens = ((1/(sig*sqrt(2*pi))) * exp(-(t-mu)^2/(2*sig^2)));
end


