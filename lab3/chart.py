import matplotlib as mpl
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
import tkinter.filedialog as fd
from calculations import *
mpl.use('TkAgg')


def chart(window, lines, time, alpha, betta, capacity, check, max_count):
    lines, count_calls, missed, queue, busy_count = calculate_calls(lines, time, alpha, betta, capacity, check, max_count)
    fig = plt.Figure(figsize=(10, 6), dpi=100)
    print(count_calls, missed, queue, busy_count)
    colors = ["red", "blue", "green", "orange", "peru", "aqua", "pink", "olive", "lime"]
    plt1 = fig.add_subplot(1, 1, 1)
    t = (0, time)
    for i in range(len(lines)):
        plt1.plot(t, (i + 1, i + 1), color="black", linewidth=1)
    for i, line in enumerate(lines):
        val = (i + 1, i + 1)
        for j, call in enumerate(line):
            plt1.scatter(call[0], val[0], color=colors[j % len(colors)], s=10)
            plt1.scatter(call[1], val[1], color=colors[j % len(colors)], s=10)
            plt1.plot(call, val, color=colors[j % len(colors)], linewidth=2)
    #plt1.legend(fontsize="small")
    #plt1.grid(visible=True, which='major', axis='y')
    plt1.set_title(f'Число вызовов = {int(count_calls)}                Отклоненные вызовы = {missed} \n'
                   f'Загруженные линии = {busy_count}        Загруженность накопителя = {queue} \n'
                   f'Эффективность = {(count_calls - missed) / count_calls}', loc='left')
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()

    canvas.get_tk_widget().pack()
