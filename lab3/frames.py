from tkinter import *


def validate_entry(symbol):
    return True


class FrameLE:

    def __init__(self, name_label, fr, val):
        self.label_frame = LabelFrame(fr, pady=5)
        self.label = Label(self.label_frame, text=name_label, width=25, font=('Times 14'))
        self.entry = Entry(self.label_frame, validate="key", validatecommand=(fr.register(validate_entry), "%S"))
        self.label.pack(side=LEFT, ipadx=5, padx=5)
        self.entry.pack(side=LEFT, ipadx=5, padx=5)
        self.label_frame.pack(side=TOP, fill='both', padx=10, pady=10)
        self.entry.insert(END, val)

    def get(self):
        return self.entry.get()


class FrameCheck:

    def __init__(self, name_label, fr, val):
        self.label_frame = LabelFrame(fr, pady=5)
        self.label = Label(self.label_frame, text=name_label, width=25, font=('Times 14'))
        self.entry = Entry(self.label_frame, validate="key", validatecommand=(fr.register(validate_entry), "%S"))
        self.label.pack(side=LEFT, ipadx=5, padx=5)
        self.entry.pack(side=LEFT, ipadx=5, padx=5)
        self.label_frame.pack(side=TOP, fill='both', padx=10, pady=10)
        self.entry.insert(END, val)
        self.var = DoubleVar()
        self.var.set(False)
        self.check = Checkbutton(self.label_frame, variable=self.var, onvalue=1., offvalue=.0)
        self.check.pack(side=LEFT, ipadx=70, padx=5)

    def get(self):
        return self.entry.get()

