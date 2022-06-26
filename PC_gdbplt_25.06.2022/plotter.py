import tkinter
import matplotlib.pyplot as plt
import numpy as np
import time
from tkinter import *
from tkinter import ttk
from scipy import interpolate

root = tkinter.Tk() 
root.title("Graph")
root.geometry("800x600")
root.resizable(False, False)

class graphic:
    def Graph_Generator():
        analog_data = np.random.normal(0, 10, 100)
        time_data = range(0,100,1)
        model=interpolate.interp1d(time_data, analog_data)
        xs=np.linspace(0,10,1000)
        ys=model(xs)
        plt.plot(xs,ys)
        plt.xlabel('Time')
        plt.ylabel('Analog Data') 
        plt.title("Analog Data")
        plt.show()

graph_button = Button(root, text="Graph", command=graphic.Graph_Generator)
graph_button.pack(pady=30)
root.mainloop()