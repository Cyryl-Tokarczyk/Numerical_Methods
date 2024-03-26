from extract_data import *
from lagrange import lagrange_interpolation
from cubic_spline import *
import matplotlib.pyplot as plt
import numpy as np
import os

points_nums = [8, 12, 18]
dir_path = 'data\\'
file_names = ['chelm.txt', 'MountEverest.csv', 'astale.txt', 'WielkiKanionKolorado.csv']

for file in file_names:

    for points_num in points_nums:
        dists, elev_vals = read_file(dir_path + file)

        current = 0
        xs, ys = [], []
        step = len(dists) // (points_num - 2)

        while current < len(dists):

            xs.append(dists[current])
            ys.append(elev_vals[current])

            current += step
        
        xs.append(dists[-1])
        ys.append(elev_vals[-1])

        # plt.plot(dists, elev_vals)
        # plt.plot(xs, ys)
        # plt.show()

        linspace = np.linspace(dists[0], dists[-1], 500)
        lagrange_results = []
        splines_results = []

        splines = calc_cubic_splines(xs, ys)

        for x in linspace:
            lagrange_results.append(lagrange_interpolation(xs, ys, x))
            splines_results.append(cubic_splines_interpolation(splines, xs, x))

        plt.title(f'Lagrange ilość punktów: {points_num - 1}')
        plt.xlabel('Dystans od startu [m]')
        plt.ylabel('Wysokość [m]')
        plt.plot(linspace, lagrange_results, label = 'Lagrange')
        plt.plot(dists, elev_vals, label = 'Trasa')
        plt.plot(xs, ys, 'o', label = 'Punkty węzłowe')
        plt.legend()
        plt.savefig(f'wykresy\\{os.path.splitext(file)[0]}_{points_num - 1}_lagrange.png', bbox_inches = 'tight')
        plt.show()

        plt.title(f'Splajny ilość punktów: {points_num - 1}')
        plt.xlabel('Dystans od startu [m]')
        plt.ylabel('Wysokość [m]')
        plt.plot(linspace, splines_results, label = 'Splajny')
        plt.plot(dists, elev_vals, label = 'Trasa')
        plt.plot(xs, ys, 'o', label = 'Punkty węzłowe')
        plt.legend()
        plt.savefig(f'wykresy\\{os.path.basename(file)}_{points_num - 1}_splajny.png', bbox_inches = 'tight')
        plt.show()

        plt.title(f'Zestawienie lagrange i splajny\n ilość punktów: {points_num - 1}')
        plt.xlabel('Dystans od startu [m]')
        plt.ylabel('Wysokość [m]')
        plt.plot(linspace, lagrange_results, label = 'Lagrange')
        plt.plot(linspace, splines_results, label = 'Splajny')
        plt.plot(dists, elev_vals, label = 'Trasa')
        plt.plot(xs, ys, 'o', label = 'Punkty węzłowe')
        plt.legend()
        plt.savefig(f'wykresy\\{os.path.basename(file)}_{points_num - 1}_oba.png', bbox_inches = 'tight')
        plt.show()