import tkinter
import tkinter.messagebox
from tkinter.ttk import Style
import customtkinter
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from scipy import interpolate

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class  App(customtkinter.CTk):

    WIDTH = 1024
    HEIGHT = 600
    def __init__(self):
        

        super().__init__()

        self.title("Microtunel control")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        
        

    def create_plots(self):
        self.frame_plots = customtkinter.CTkFrame(master=self)
        self.frame_plots.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_plots.columnconfigure(0,weight=1)
        self.frame_plots.rowconfigure(2,weight=1)

        self.label_1 = customtkinter.CTkLabel(master=self.frame_plots,
                                              text="Gráfico",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

    def grafico(self):
        analog_data = np.random.normal(0, 10, 100)
        time_data = range(0,100,1)
        model=interpolate.interp1d(time_data, analog_data)
        xs=np.linspace(0,10,1000)
        ys=model(xs)
        plt.style.use('dark_background')
        
        # create a figure
        self.figure = plt.Figure()

        self.figure.add_subplot(111).plot(xs,ys)
        
        # create FigureCanvasTkAgg object
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self.frame_plots)
        

        self.figure_canvas.get_tk_widget().grid(row=2,column=0,sticky="n")


if __name__ == "__main__":
    app = App()
    app.create_plots()
    app.grafico()
    app.mainloop()