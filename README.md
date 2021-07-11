# Python-time-entry
I was making some project and I needed time entry in python with tkinter. So I made one and wanted to share with you.
Method __init__(self, window) takes window argument which is tkinter.Tk(), and makes h=tk.Entry()-entry for hours, and m=tk.Entry()-entry for minutes
hours will be entered in hh format(07, 11, ...)
minutes will be entered in mm format(15, 01, 09, 59, ...)
Method pack() will pack time entry to window(self.window)
Method grid(row, column) will grid time entry to window(self.window) to certain row, and column
Method get() returns tuple which represents entered time(hh, mm) when there is some error(wrong format) it returns (-1, -1)
