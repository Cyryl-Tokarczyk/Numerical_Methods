clc
clear all
close all

% A:

a = 1;
b = 60000;
eps = 1e-3;

[xvect, xdif, fx, it_cnt] = bisection(@algo,a,b,eps);

plot(xvect);
xlabel("Liczba iteracji")
ylabel("Kolejne wartości rozwiązania")
title(["Wartości przybliżonego rozwiązania dla metody bisekcji",
    "zastosowanej do algorytmu"])
print -dpng zadBAlgoBis_1

semilogy(xdif)
xlabel("Liczba iteracji")
ylabel("Różnica między kolejnymi rozwiązaniami")
title(["Różnice kolejnych rozwiązań dla metody bisekcji",
    "zastosowanej do algorytmu"])
print -dpng zadBAlgoBis_2

[xvect, xdif, fx, it_cnt] = secant(@algo,a,b,eps);

plot(xvect);
xlabel("Liczba iteracji")
ylabel("Kolejne wartości rozwiązania")
title(["Wartości przybliżonego rozwiązania dla metody siecznych",
    "zastosowanej do algorytmu"])
print -dpng zadBAlgoSec_1

semilogy(xdif)
xlabel("Liczba iteracji")
ylabel("Różnica między kolejnymi rozwiązaniami")
title(["Różnice kolejnych rozwiązań dla metody siecznych",
    "zastosowanej do algorytmu"])
print -dpng zadBAlgoSec_2

%%

clc
clear all
close all

% B:

a = 0;
b = 50;
eps = 1e-12;

[xvect, xdif, fx, it_cnt] = bisection(@compute_impedance, a, b, eps);

plot(xvect);
xlabel("Liczba iteracji")
ylabel("Kolejne wartości rozwiązania")
title(["Wartości przybliżonego rozwiązania dla metody bisekcji",
    "zastosowanej do impedancji"])
print -dpng zadBImpedBis_1

semilogy(xdif)
xlabel("Liczba iteracji")
ylabel("Różnica między kolejnymi rozwiązaniami")
title(["Różnice kolejnych rozwiązań dla metody bisekcji",
    "zastosowanej do impedancji"])
print -dpng zadBImpedBis_2

[xvect, xdif, fx, it_cnt] = secant(@compute_impedance,a,b,eps);

plot(xvect);
xlabel("Liczba iteracji")
ylabel("Kolejne wartości rozwiązania")
title(["Wartości przybliżonego rozwiązania dla metody siecznych",
    "zastosowanej do impedancji"])
print -dpng zadBImpedSec_1

semilogy(xdif)
xlabel("Liczba iteracji")
ylabel("Różnica między kolejnymi rozwiązaniami")
title(["Różnice kolejnych rozwiązań dla metody siecznych",
    "zastosowanej do impedancji"])
print -dpng zadBImpedSec_2

%%

clc
clear all
close all

% C:

a = 0;
b = 50;
eps = 1e-12;

[xvect, xdif, fx, it_cnt] = bisection(@rocket, a,b,eps);

plot(xvect);
xlabel("Liczba iteracji")
ylabel("Kolejne wartości rozwiązania")
title(["Wartości przybliżonego rozwiązania dla metody bisekcji",
    "zastosowanej do czasu lotu rakiety"])
print -dpng zadBRocketBis_1

semilogy(xdif)
xlabel("Liczba iteracji")
ylabel("Różnica między kolejnymi rozwiązaniami")
title(["Różnice kolejnych rozwiązań dla metody bisekcji",
    "zastosowanej do czasu lotu rakiety"])
print -dpng zadBRocketBis_2

[xvect, xdif, fx, it_cnt] = secant(@rocket,a,b,eps);

plot(xvect);
xlabel("Liczba iteracji")
ylabel("Kolejne wartości rozwiązania")
title(["Wartości przybliżonego rozwiązania dla metody siecznych",
    "zastosowanej do rakiety"])
print -dpng zadBRocketSec_1

semilogy(xdif)
xlabel("Liczba iteracji")
ylabel("Różnica między kolejnymi rozwiązaniami")
title(["Różnice kolejnych rozwiązań dla metody siecznych",
    "zastosowanej do rakiety"])
print -dpng zadBRocketSec_2

function T = algo(N)

T = (N^(1.43) + N^(1.14)) / 1000;
T = T - 5000;

end

function v = rocket(t)

g = 9.81;
m_0 = 150000;
q = 2700;
u = 2000;

v = (u * log(m_0/(m_0 - (q * t)))) - (g * t);
v = v - 750;

end