from tkinter import *
from tkinter import ttk
from frames import *
import numpy as np
from chart import chart


def build_chart():
    newWindow = Toplevel(win)
    newWindow.grab_set()
    chart(newWindow, int(label_count.get()), float(label_time.get()), float(label_p_time.get()),
          float(label_p_duration.get()), int(label_capacity.get()), int(label_check_max.var.get()), int(label_check_max.get()))


win = Tk()
win.geometry('660x460')
win.title('MM3')
win.resizable(False, False)
wrapper1 = LabelFrame(win)
#wrapper2 = LabelFrame(win)
canvas = Canvas(wrapper1, bg="white", width=1200, height=800)
canvas.pack(side=LEFT)
frame = Frame(canvas, pady=10)
sb = ttk.Scrollbar(win, orient='vertical', command=canvas.yview)
sb.pack(side=RIGHT, fill='y')
sbv = ttk.Scrollbar(win, orient='horizontal', command=canvas.xview)
sbv.pack(side=BOTTOM, fill='x')
canvas.configure(yscrollcommand=sb.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
canvas.configure(xscrollcommand=sbv.set)
#frame = Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor='nw')
wrapper1.pack(side=BOTTOM, fill='both', expand=True, padx=10, pady=10)

font = ('Times 14')
label_count = FrameLE("Число линий", frame, 3)
label_time = FrameLE("Время", frame, 1000)
label_p_time = FrameLE("Показатель для времени", frame, 0.1)
label_p_duration = FrameLE("Показатель для длительности", frame, 0.1)
label_capacity = FrameLE("Емкость накопителя", frame, 1)
label_check_max = FrameCheck("Максимум линий", frame, 5)
button = Button(frame, text='Построить', font=('Times 14'), command=lambda: build_chart())
button.pack(side=BOTTOM)


win.mainloop()
