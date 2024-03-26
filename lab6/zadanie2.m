clc
clear all
close all

warning('off','all')

load trajektoria1

plot3(x, y, z, 'o')
grid on
axis equal

%% 4

N = 60;
xa = aproksymacjaWielomianowa(n, x, N);  % aproksymacja wspolrzednej x
ya = aproksymacjaWielomianowa(n, y, N);  % aproksymacja wspolrzednej y
za = aproksymacjaWielomianowa(n, z, N);  % aproksymacja wspolrzednej z

plot3(x,y,z,'o')
hold on
plot3(xa, ya, za, 'g', 'LineWidth', 4)
title("Aproksymacja wielomianowa trajektorii drona")
xlabel("Współrzędna x [m]")
ylabel("Współrzędna y [m]")
zlabel("Współrzędna z [m]")

print -dpng zadanie4.png

%% 5

load trajektoria2

N = 60;
xa = aproksymacjaWielomianowa(n, x, N);  % aproksymacja wspolrzednej x
ya = aproksymacjaWielomianowa(n, y, N);  % aproksymacja wspolrzednej y
za = aproksymacjaWielomianowa(n, z, N);  % aproksymacja wspolrzednej z

plot3(x,y,z,'o')
hold on
plot3(xa, ya, za, 'g', 'LineWidth', 4)
title("Aproksymacja wielomianowa drugiej trajektorii drona")
xlabel("Współrzędna x [m]")
ylabel("Współrzędna y [m]")
zlabel("Współrzędna z [m]")

print -dpng zadanie5a.png

%% 5b

for i = 1:71
    xa = aproksymacjaWielomianowa(n, x, i);  % aproksymacja wspolrzednej x
    ya = aproksymacjaWielomianowa(n, y, i);  % aproksymacja wspolrzednej y
    za = aproksymacjaWielomianowa(n, z, i);  % aproksymacja wspolrzednej z

    sum_x = 0;
    sum_y = 0;
    sum_z = 0;

    for j = 1:length(n)
        sum_x = sum_x + (x(j) - xa(j))^2;
        sum_y = sum_y + (y(j) - ya(j))^2;
        sum_z = sum_z + (z(j) - za(j))^2;
    end

    err(i) = sqrt(sum_x)/length(n) + sqrt(sum_y)/length(n) + sqrt(sum_z)/length(n);
end

plot(err)
title("Wykres błędu w zależności od rzędu aproksymacji")
xlabel("Rząd aproksymacji")
ylabel("Wartość błędu")

print -dpng zadanie5b

%% 6

load trajektoria2

N = 60;
xa = aproksymacjaTrygonometryczna(n, x, N);  % aproksymacja wspolrzednej x
ya = aproksymacjaTrygonometryczna(n, y, N);  % aproksymacja wspolrzednej y
za = aproksymacjaTrygonometryczna(n, z, N);  % aproksymacja wspolrzednej z

plot3(x,y,z,'o')
hold on
plot3(xa, ya, za, 'g', 'LineWidth', 4)
title("Aproksymacja trygonometryczna drugiej trajektorii drona")
xlabel("Współrzędna x [m]")
ylabel("Współrzędna y [m]")
zlabel("Współrzędna z [m]")

print -dpng zadanie6a.png

%% 6b

for i = 1:71
    xa = aproksymacjaTrygonometryczna(n, x, i);  % aproksymacja wspolrzednej x
    ya = aproksymacjaTrygonometryczna(n, y, i);  % aproksymacja wspolrzednej y
    za = aproksymacjaTrygonometryczna(n, z, i);  % aproksymacja wspolrzednej z

    sum_x = 0;
    sum_y = 0;
    sum_z = 0;

    for j = 1:length(n)
        sum_x = sum_x + (x(j) - xa(j))^2;
        sum_y = sum_y + (y(j) - ya(j))^2;
        sum_z = sum_z + (z(j) - za(j))^2;
    end

    err(i) = sqrt(sum_x)/length(n) + sqrt(sum_y)/length(n) + sqrt(sum_z)/length(n);
end

plot(err)
title("Wykres błędu w zależności od rzędu aproksymacji trygonometrycznej")
xlabel("Rząd aproksymacji")
ylabel("Wartość błędu")

print -dpng zadanie6b

%% 6c

N = 150;
xa = aproksymacjaTrygonometryczna(n, x, N);  % aproksymacja wspolrzednej x
ya = aproksymacjaTrygonometryczna(n, y, N);  % aproksymacja wspolrzednej y
za = aproksymacjaTrygonometryczna(n, z, N);  % aproksymacja wspolrzednej z

plot3(x,y,z,'o')
hold on
plot3(xa, ya, za, 'g', 'LineWidth', 4)
title("Aproksymacja trygonometryczna drugiej trajektorii drona N = 150")
xlabel("Współrzędna x [m]")
ylabel("Współrzędna y [m]")
zlabel("Współrzędna z [m]")

print -dpng zadanie6c.png
