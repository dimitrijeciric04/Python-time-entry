import tkinter as tk

class time_entry:
    def __init__(self, window):
        self.h=tk.Entry(window, textvariable=tk.StringVar(window, 'hh'), width=2)
        self.separate=tk.Label(window, text=":")
        self.m=tk.Entry(window, textvariable=tk.StringVar(window, 'mm'), width=3)
    def pack(self):
        self.h.pack(side=tk.LEFT)
        self.separate.pack(side=tk.LEFT)
        self.m.pack(side=tk.LEFT)
    def grid(self, row, column):
        self.h.grid(row=row, column=column)
        self.separate.grid(row=row, column=column+1)
        self.m.grid(row=row, column=column+2)
    def get(self):
        ans=[]
        tmp=self.h.get()
        if len(tmp) != 2 or tmp == 'hh': return (-1, -1)
        hh=int(tmp[0])*10+int(tmp[1])
        if hh>=24: return(-1, -1)
        ans.append(hh)
        tmp1=self.m.get()
        if len(tmp1) != 2 or tmp1 == 'mm': return (-1, -1)
        mm=int(tmp1[0])*10+int(tmp1[1])
        if mm>=60: return(-1, -1)
        ans.append(mm)
        return ans
