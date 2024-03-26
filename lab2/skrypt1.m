clear all
close all

a = 20
r_max = a/2
n_max = 200

war = true;
liczba_losowan(1) = 0;

while war
    liczba_losowan(1) = liczba_losowan(1) + 1;

    x_t = rand(1) * a;
    y_t = rand(1) * a;
    r_t = rand(1) * r_max;       

    if x_t - r_t > 0 && x_t + r_t < 20 && y_t - r_t > 0 && y_t + r_t < 20
        war = false;
        x(1) = x_t;
        y(1) = y_t;
        r(1) = r_t;
        pole(1) = r_t^2 * pi;
    end
end

sred_licz_los(1) = sum(liczba_losowan) / length(liczba_losowan);

plot_circle(x(1), y(1), r(1))

axis equal
axis([0 a 0 a])

hold on

n = 2

while n <= n_max

    war = true;
    liczba_losowan(n) = 0;

    while war
        liczba_losowan(n) = liczba_losowan(n) + 1;

        x_t = rand(1) * a;
        y_t = rand(1) * a;
        r_t = rand(1) * r_max;

        war_od = true;
        i = 1;

        while war_od && i < n
            if pdist([x(i) y(i); x_t y_t]) < r(i) + r_t
                war_od = false;
            end
            i = i + 1;
        end        

        if x_t - r_t > 0 && x_t + r_t < 20 && y_t - r_t > 0 && y_t + r_t < 20 && war_od
            war = false;
            x(n) = x_t;
            y(n) = y_t;
            r(n) = r_t;
            pole(n) = r_t^2 * pi;
        end
    end

    sred_licz_los(n) = sum(liczba_losowan) / length(liczba_losowan);

    plot_circle(x(n), y(n), r(n))

    n = n + 1;

    pause(0.01)
end

figure

plot(cumsum(pole))
xlabel("Liczba okręgów")
ylabel("Suma powierzchni")
title("Powierzchnia całkowita kół")
print -dpng zadanie1a

figure

plot(sred_licz_los)
xlabel("Liczba okręgów")
ylabel("Liczba losowań")
title("Średnia liczba potrzebnych losowań")
print -dpng zadanie1b

function plot_circle(X, Y, R)
    theta = linspace(0,2*pi);
    x = R*cos(theta) + X;
    y = R*sin(theta) + Y;
    plot(x,y)
end
