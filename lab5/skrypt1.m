clc
close all
clear all

K = [5, 15, 25, 35];

for i = 1:length(K)
    [x, y, f, xp, yp] = lazik(K(i));

    [XX, YY] = meshgrid(linspace(0, 1, 101), linspace(0, 1, 101));

    [p] = polyfit2d(x, y, f);
    [FP] = polyval2d(XX, YY, p);

    [t] = trygfit2d(x, y, f);
    [FT] = trygval2d(XX, YY, t);

    figure
    subplot(2, 2, 1)
    plot(xp, yp, '-o', 'LineWidth', 2);
    title('Tor ruchu łazika')
    xlabel('x')
    ylabel('y')

    subplot(2, 2, 2)
    surf(reshape(x, K(i), K(i)), reshape(y, K(i), K(i)), reshape(f, K(i), K(i)));
    shading flat
    title('Wartości próbek')
    xlabel('x')
    ylabel('y')
    zlabel('f(x, y)')

    subplot(2, 2, 3)
    surf(XX, YY, FP)
    shading flat
    title('Interpolacja wielomianowa')
    xlabel('x')
    ylabel('y')
    zlabel('f(x, y)')

    subplot(2, 2, 4)
    surf(XX, YY, FT)
    shading flat
    title('Interpolacja trygonometryczna')
    xlabel('x')
    ylabel('y')
    zlabel('f(x, y)')

    sgtitle(strcat('K=', string(K(i))))
    name = strcat('wykresy_dla_K_', string(K(i)));
    print(name, '-dpng')
end

%% Zad 2a

clc
close all
clear all

div_k = [];

[x, y, f, xp, yp] = lazik(5);

[XX, YY] = meshgrid(linspace(0, 1, 101), linspace(0, 1, 101));

[p] = polyfit2d(x, y, f);
[FP1] = polyval2d(XX, YY, p);

for K = 6:45
    [x, y, f, xp, yp] = lazik(K);
    
    [p] = polyfit2d(x, y, f);
    [FP] = polyval2d(XX, YY, p);

    div_k(K) = max(max(abs(FP-FP1)));

    FP1 = FP;
end

plot(div_k)
title('Wykres zbieżności punktów pomiarowych dla interpolacji wielomianowej')
xlim([6, 45])
xlabel('K')
ylabel('Div(K)')

print -dpng zbieznosc_wielomianowa

%% Zad2b

clc
close all
clear all

div_k = [];

[x, y, f, xp, yp] = lazik(5);

[XX, YY] = meshgrid(linspace(0, 1, 101), linspace(0, 1, 101));

[t] = trygfit2d(x, y, f);
[FT1] = trygval2d(XX, YY, t);

for K = 6:45
    [x, y, f, xp, yp] = lazik(K);    
    
    [t] = trygfit2d(x, y, f);
    [FT] = trygval2d(XX, YY, t);

    div_k(K) = max(max(abs(FT-FT1)));

    FT1 = FT;
end

plot(div_k)
title('Wykres zbieżności punktów pomiarowych dla interpolacji trygonometrycznej')
xlim([6, 45])
xlabel('K')
ylabel('Div(K)')

print -dpng zbieznosc_trygonometryczna

