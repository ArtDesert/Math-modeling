import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
from tkinter import *
import math


def get_arr(left, n, h):
    arr = [0] * n
    arr[0] = left
    for i in range(1, n):
        arr[i] = arr[i - 1] + h
    return arr


def draw():
    global n, K, T
    t_arr = get_arr(0, K + 1, T / K)
    N_ = get_solutions()
    plt.figure(label="Модель взаимодействия популяций")
    plt.xlabel('Время t, лет')
    plt.ylabel('Число особей N')
    sum_arr = [0] * (K + 1)
    for i in range(n):
        plt.plot(t_arr, N_[i], label=f"N_{i + 1}")
        for j in range(K + 1):
            sum_arr[j] += N_[i][j]
    diff = abs(max(sum_arr) - min(sum_arr))
    delta = abs(max(sum_arr) / min(sum_arr))
    print(f'diff = {diff}')
    print(f'delta = {delta}')
    plt.plot(t_arr, sum_arr, label="Общее число особей")
    plt.legend()
    plt.show()


def get_solutions():
    global n, N, A, C, B, K, T
    h_t = T / K
    solutions = [0] * n
    for i in range(n):
        solutions[i] = [0] * (K + 1)
    # Инициализация начальных условий
    for i in range(n):
        solutions[i][0] = float(N[i].get())

    for k in range(1, K + 1):
        for i in range(n):
            _sum = sum([float(B[i][j].get()) * solutions[i][k - 1] * solutions[j][k - 1] for j in range(n)]);
            solutions[i][k] = solutions[i][k - 1] + h_t * (float(A[i].get()) * (1 - float(C[i].get()) * math.exp(- i / T)) * solutions[i][k - 1] + _sum)
    return solutions


def init():
    tk.Label(text='Введите численность популяций, их прирост и коэффициенты бесплодия').grid(row=0, column=0, columnspan=3, sticky='we')
    tk.Label(text='Введите матрицу взаимодействия').grid(row=0, column=3, columnspan=3, sticky='we')
    for i in range(1, n + 1):
        for j in range(3):
            if j == 0:
                entry = tk.Entry(textvariable=tk.StringVar(value=f'{float(i * 100)}'))
                entry.grid(row=i, column=j, sticky='ew', pady=1)
                N[i - 1] = entry
            elif j == 1:
                if i == 1:
                    entry = tk.Entry(textvariable=tk.StringVar(value='0.01'))
                else:
                    entry = tk.Entry(textvariable=tk.StringVar(value='-0.01'))
                entry.grid(row=i, column=j, sticky='ew', pady=1)
                A[i - 1] = entry
            else:
                entry = tk.Entry(textvariable=tk.StringVar(value=f'0.05'))
                entry.grid(row=i, column=j, sticky='ew', padx=10, pady=1)
                C[i - 1] = entry


    for i in range(1, n + 1):
        for j in range(n):
            if i - 1 < j:
                entry = tk.Entry(textvariable=tk.StringVar(value='-0.0001'))
            elif i - 1 > j:
                entry = tk.Entry(textvariable=tk.StringVar(value='0.0001'))
            else:
                entry = tk.Entry(textvariable=tk.StringVar(value='0.0'))
            entry.grid(row=i, column=j + 4)
            B[i - 1][j] = entry

    #for j in range(n):

    btn = tk.Button(text='Построить график', command=draw)
    btn.grid(row=1, column=7, rowspan=3, sticky='ns')


win = Tk()
win.title('Модель взаимодействия популяций')
win.geometry('1000x600')

n = 2
T = 1000
K = 10 * T
N = [0.0] * n
A = [0.0] * n
C = [0.0] * n
B = [[0.0] * n for i in range(n)] * n
init()
while(True):
    win.mainloop()

'''
plt.figure(label="График зависимости амлпитуды от разности начальной численности популяций")
plt.xlabel('Разность численностей популяций')
plt.ylabel('Амплитуда')
x_arr = [-99,-90,-75,-50,-25,50,100,200,300,400,500,600,700,800,900,1000]
y_arr = [840.1937328637814,494.3179141109212,326.16076319548665,177.42988736161192,78.01470302281481,123.7290238489797,224.22238494420452,
         390.38520422439944,532.7960257797249,662.4457856092196,784.5044391074512,789.8703228466246,893.564466310061,995.9171805179215,1097.4154430253009,
         1198.3680528583252]
plt.plot(x_arr, y_arr)
plt.legend()
plt.show()
'''
