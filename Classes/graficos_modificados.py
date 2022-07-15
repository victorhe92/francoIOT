import tkinter
import customtkinter
from mainFrame import mainFrame
import numpy as np
import matplotlib.pyplot as plt
import datetime
from tkinter import * 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

from tkinter import *
from tkinter import ttk
from scipy import interpolate

#engines2d

class inicio():
    
    t1 = 10
    t2 = 20
    t3 = 30
    t4 = 40
    tiempo = datetime.datetime.now()
    
    def __init__(self,master):
        #Create a general vision frame
        self.frame = customtkinter.CTkFrame(master=master)

        self.frame.grid(row=0, column=1,sticky="nsew",pady=10,padx=10)
        
        
        # ============ frame_sensors ============
        
        # configure grid layout (3x2)
        
        self.frame.columnconfigure(0,weight=1)
        self.frame.columnconfigure(1,weight=1)
        self.frame.rowconfigure(0,weight=1)
        self.frame.rowconfigure(1,weight=1)
      
        
        self.label_1 = customtkinter.CTkLabel(master=self.frame,
                                              text="Control de microtuneles",
                                              text_font=("Roboto Medium", -25))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10, columnspan=2)
        self.label_1 = customtkinter.CTkLabel(master=self.frame,
                                              text=self.tiempo,
                                              text_font=("Roboto Medium", -12))  # font name and size in px
        self.label_1.grid(row=0, column=0, pady=10, padx=10, columnspan=2,sticky="e")

        self.frame_station1 = customtkinter.CTkFrame(master=self.frame)
        #self.frame_station1.grid_propagate(0)
        self.frame_station1.grid(row=0, column=0,pady=5, padx=5, sticky="nsew")

        self.frame_station2 = customtkinter.CTkFrame(master=self.frame)
        self.frame_station2.grid(row=0, column=1, pady=5, padx=5, sticky="nsew")

        self.frame_station3 = customtkinter.CTkFrame(master=self.frame)
        self.frame_station3.grid(row=1, column=0, pady=5, padx=5, sticky="nsew")

        self.frame_station4 = customtkinter.CTkFrame(master=self.frame)
        self.frame_station4.grid(row=1, column=1, pady=5, padx=5, sticky="nsew")

        #==============INFORMATION OF EACH STATION======================

        #===STATION 1=====
        self.frame_station1.columnconfigure(1,weight=1)
        self.frame_station1.rowconfigure(1,weight=1)

        self.frame_station1_1 = customtkinter.CTkFrame(master=self.frame_station1)
        self.frame_station1_1.grid(row=1, column=1,pady=10, padx=10, sticky="nsew")

        self.fig = Figure(figsize=(1,2), dpi=80)
        self.fig.text(0.5, 0.92, "Station 1", ha='center', va='center', size=12)

        self.ax = self.fig.add_subplot(111)
        
        self.ax.analog_data = np.random.normal(0, 10, 100)
        self.ax.time_data = range(0,100,1)
        self.ax.set_xlabel('Time').set_fontsize(10)
        self.ax.set_ylabel('Temperature').set_fontsize(10)
        self.ax.plot(np.random.rand(10))
        self.ax.model=interpolate.interp1d(self.ax.time_data, self.ax.analog_data)
        self.ax.xs=np.linspace(0,50,1000)
        self.ax.ys= self.ax.model(self.ax.xs)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_station1_1)
       
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=BOTTOM, fill= BOTH, expand=TRUE)
 
        #===STATION 2=====
        self.frame_station2.columnconfigure(1,weight=4)
        self.frame_station2.rowconfigure(1,weight=4)

        
        self.frame_station1_2 = customtkinter.CTkFrame(master=self.frame_station2)
        self.frame_station1_2.grid(row=1, column=1,pady=5, padx=5, sticky="nsew")
     
        self.fig = Figure(figsize=(1,1.70), dpi=100)
        self.fig.text(0.5, 0.92, "Station 1", ha='center', va='center', size=12)
    
        self.ay = self.fig.add_subplot(111)
        
        self.ay.analog_data = np.random.normal(0, 10, 100)
        self.ay.time_data = range(0,100,1)
        self.ay.set_xlabel('Time').set_fontsize(10)
        self.ay.set_ylabel('Temperature').set_fontsize(10)
        self.ay.plot(np.random.rand(10))
        self.ay.model=interpolate.interp1d(self.ay.time_data, self.ay.analog_data)
        self.ay.xs=np.linspace(0,50,1000)
        self.ay.ys= self.ax.model(self.ay.xs)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_station1_2)
       
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=BOTTOM, fill= BOTH, expand=TRUE)
    
        #===STATION 3=====
        self.frame_station3.columnconfigure(1,weight=4)
        self.frame_station3.rowconfigure(1,weight=4)

        
        self.frame_station1_3 = customtkinter.CTkFrame(master=self.frame_station3)
        self.frame_station1_3.grid(row=1, column=1,pady=10, padx=10, sticky="nsew")
     
        self.fig = Figure(figsize=(1,2), dpi=100)
        self.fig.text(0.5, 0.92, "Station 1", ha='center', va='center', size=10)
    
        self.az = self.fig.add_subplot(111)
        
        self.az.analog_data = np.random.normal(0, 10, 100)
        self.az.time_data = range(0,100,1)
        self.az.set_xlabel('Time').set_fontsize(10)
        self.az.set_ylabel('Temperature').set_fontsize(10)
        self.az.plot(np.random.rand(10))
        self.az.model=interpolate.interp1d(self.az.time_data, self.az.analog_data)
        self.az.xs=np.linspace(0,50,1000)
        self.az.ys= self.ax.model(self.az.xs)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_station1_3)
       
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=BOTTOM, fill= BOTH, expand=TRUE)

        #===STATION 4=====
        self.frame_station4.columnconfigure(1,weight=4)
        self.frame_station4.rowconfigure(1,weight=4)

        
        self.frame_station1_4 = customtkinter.CTkFrame(master=self.frame_station4)
        self.frame_station1_4.grid(row=1, column=1,pady=10, padx=10, sticky="nsew")
     
        self.fig = Figure(figsize=(1,1.70), dpi=100)
        self.fig.text(0.5, 0.92, "Station 4", ha='center', va='center', size=12)
    
        self.aw = self.fig.add_subplot(111)
        
        self.aw.analog_data = np.random.normal(0, 10, 100)
        self.aw.time_data = range(0,100,1)
        self.aw.set_xlabel('Time').set_fontsize(10)
        self.aw.set_ylabel('Temperature').set_fontsize(10)
        self.aw.plot(np.random.rand(10))
        self.aw.model=interpolate.interp1d(self.aw.time_data, self.aw.analog_data)
        self.aw.xs=np.linspace(0,50,1000)
        self.aw.ys= self.ax.model(self.aw.xs)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_station1_4)
       
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=BOTTOM, fill= BOTH, expand=TRUE)

       

if __name__=="__main__":
    app = mainFrame()
    windows_start = inicio(app)
    app.show_frame(windows_start)
    #app.hide_frame()
    app.mainloop()