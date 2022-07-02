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



customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
class App(customtkinter.CTk):

    WIDTH = 1024
    HEIGHT = 600
    def __init__(self):
        

        super().__init__()

        self.title("Microtunel control")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create left and windows frames  ============
        # The menu is on the left
        # Windows are on the right


        
        self.create_general() #Default window
        self.hide_general()
        self.show_general()


    #=====GENERAL WINDOWS METHODS=====
    def create_general(self):
        # configure grid layout (1x1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        #Create a general vision frame
        self.frame_general = customtkinter.CTkFrame(master=self)
        self.frame_general.grid(row=0, column=0,sticky="")

        # ============ frame_sensors ============
        
        # configure grid layout (3x2)
        #self.frame_general.rowconfigure((0, 1,), weight=1)
        #self.frame_general.rowconfigure(2, weight=1)
        #self.frame_general.columnconfigure((0, 1), weight=1)
        #self.frame_general.columnconfigure(1, weight=1)

        
        self.frame_general.columnconfigure(1,weight=1)
        self.frame_general.rowconfigure(2,weight=1)
        
        self.label_1 = customtkinter.CTkLabel(master=self.frame_general,
                                              text="Control de microtuneles",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

        self.frame_station1 = customtkinter.CTkFrame(master=self.frame_general)
        self.frame_station1.grid(row=1, column=0,pady=20, padx=20, sticky="nsew")

        self.frame_station2 = customtkinter.CTkFrame(master=self.frame_general)
        self.frame_station2.grid(row=1, column=1, pady=20, padx=20, sticky="nsew")

        self.frame_station3 = customtkinter.CTkFrame(master=self.frame_general)
        self.frame_station3.grid(row=2, column=0, pady=20, padx=20, sticky="nsew")

        self.frame_station4 = customtkinter.CTkFrame(master=self.frame_general)
        self.frame_station4.grid(row=2, column=1, pady=20, padx=20, sticky="nsew")

        #==============INFORMATION OF EACH STATION======================

        #===STATION 1=====
        self.frame_station1.columnconfigure(1,weight=1)
        self.frame_station1.rowconfigure(3,weight=1)

        self.lbl_station1_title = customtkinter.CTkLabel(master=self.frame_station1,
                                              text="Estación 1",
                                              text_font=("Roboto Medium", -20))  # font name and size in px
        self.lbl_station1_title.grid(row=0,column=0,columnspan=2,pady=10)

        self.lbl_station1_temperature_txt = customtkinter.CTkLabel(master=self.frame_station1,
                                              text="Temperatura:",
                                              text_font=("Roboto Medium", -15))  # font name and size in px
        self.lbl_station1_temperature_txt.grid(row=1,column=0,padx=10,sticky="n")

        self.lbl_station1_humidity_txt = customtkinter.CTkLabel(master=self.frame_station1,
                                              text="Humedad:",
                                              text_font=("Roboto Medium", -15))  # font name and size in px
        self.lbl_station1_humidity_txt.grid(row=1,column=1,padx=10,sticky="n")

        self.lbl_station1_temperature = customtkinter.CTkLabel(master=self.frame_station1,
                                              text="20ºC",
                                              text_font=("Roboto Medium", -56))  # font name and size in px
        self.lbl_station1_temperature.grid(row=2,column=0,padx=10,sticky="n")

        self.lbl_station1_humidity = customtkinter.CTkLabel(master=self.frame_station1,
                                              text="55%",
                                              text_font=("Roboto Medium", -56))  # font name and size in px
        self.lbl_station1_humidity.grid(row=2,column=1,padx=10,sticky="n")

        self.button_station1 = customtkinter.CTkButton(master=self.frame_station1,
                                                text="Detalles",
                                                command=self.button_event)
        self.button_station1.grid(row=3, column=0, pady=10, padx=20, columnspan=2)



        #===STATION 2=====
        self.frame_station2.columnconfigure(1,weight=1)
        self.frame_station2.rowconfigure(3,weight=1)

        self.lbl_station2_title = customtkinter.CTkLabel(master=self.frame_station2,
                                              text="Estación 2",
                                              text_font=("Roboto Medium", -20))  # font name and size in px
        self.lbl_station2_title.grid(row=0,column=0,columnspan=2,pady=10)

        self.lbl_station2_temperature_txt = customtkinter.CTkLabel(master=self.frame_station2,
                                              text="Temperatura:",
                                              text_font=("Roboto Medium", -15))  # font name and size in px
        self.lbl_station2_temperature_txt.grid(row=1,column=0,padx=10,sticky="n")

        self.lbl_station2_humidity_txt = customtkinter.CTkLabel(master=self.frame_station2,
                                              text="Humedad:",
                                              text_font=("Roboto Medium", -15))  # font name and size in px
        self.lbl_station2_humidity_txt.grid(row=1,column=1,padx=10,sticky="n")

        self.lbl_station2_temperature = customtkinter.CTkLabel(master=self.frame_station2,
                                              text="34ºC",
                                              text_font=("Roboto Medium", -56))  # font name and size in px
        self.lbl_station2_temperature.grid(row=2,column=0,padx=10,sticky="n")

        self.lbl_station2_humidity = customtkinter.CTkLabel(master=self.frame_station2,
                                              text="35%",
                                              text_font=("Roboto Medium", -56))  # font name and size in px
        self.lbl_station2_humidity.grid(row=2,column=1,padx=10,sticky="n")

        self.button_station2 = customtkinter.CTkButton(master=self.frame_station2,
                                                text="Detalles",
                                                command=self.button_event)
        self.button_station2.grid(row=3, column=0, pady=10, padx=20, columnspan=2)

        #===STATION 3=====
        self.frame_station3.columnconfigure(1,weight=1)
        self.frame_station3.rowconfigure(3,weight=1)

        self.lbl_station3_title = customtkinter.CTkLabel(master=self.frame_station3,
                                              text="Estación 3",
                                              text_font=("Roboto Medium", -20))  # font name and size in px
        self.lbl_station3_title.grid(row=0,column=0,columnspan=2,pady=10)

        self.lbl_station3_temperature_txt = customtkinter.CTkLabel(master=self.frame_station3,
                                              text="Temperatura:",
                                              text_font=("Roboto Medium", -15))  # font name and size in px
        self.lbl_station3_temperature_txt.grid(row=1,column=0,padx=10,sticky="n")

        self.lbl_station3_humidity_txt = customtkinter.CTkLabel(master=self.frame_station3,
                                              text="Humedad:",
                                              text_font=("Roboto Medium", -15))  # font name and size in px
        self.lbl_station3_humidity_txt.grid(row=1,column=1,padx=10,sticky="n")

        self.lbl_station3_temperature = customtkinter.CTkLabel(master=self.frame_station3,
                                              text="34ºC",
                                              text_font=("Roboto Medium", -56))  # font name and size in px
        self.lbl_station3_temperature.grid(row=2,column=0,padx=10,sticky="n")

        self.lbl_station3_humidity = customtkinter.CTkLabel(master=self.frame_station3,
                                              text="35%",
                                              text_font=("Roboto Medium", -56))  # font name and size in px
        self.lbl_station3_humidity.grid(row=2,column=1,padx=10,sticky="n")

        self.button_station3 = customtkinter.CTkButton(master=self.frame_station3,
                                                text="Detalles",
                                                command=self.button_event)
        self.button_station3.grid(row=3, column=0, pady=10, padx=20, columnspan=2)

        #===STATION 4=====
        self.frame_station4.columnconfigure(1,weight=1)
        self.frame_station4.rowconfigure(3,weight=1)

        self.lbl_station4_title = customtkinter.CTkLabel(master=self.frame_station4,
                                              text="Estación 4",
                                              text_font=("Roboto Medium", -20))  # font name and size in px
        self.lbl_station4_title.grid(row=0,column=0,columnspan=2,pady=10)

        self.lbl_station4_temperature_txt = customtkinter.CTkLabel(master=self.frame_station4,
                                              text="Temperatura:",
                                              text_font=("Roboto Medium", -15))  # font name and size in px
        self.lbl_station4_temperature_txt.grid(row=1,column=0,padx=10,sticky="n")

        self.lbl_station4_humidity_txt = customtkinter.CTkLabel(master=self.frame_station4,
                                              text="Humedad:",
                                              text_font=("Roboto Medium", -15))  # font name and size in px
        self.lbl_station4_humidity_txt.grid(row=1,column=1,padx=10,sticky="n")

        self.lbl_station4_temperature = customtkinter.CTkLabel(master=self.frame_station4,
                                              text="34ºC",
                                              text_font=("Roboto Medium", -56))  # font name and size in px
        self.lbl_station4_temperature.grid(row=2,column=0,padx=10,sticky="n")

        self.lbl_station4_humidity = customtkinter.CTkLabel(master=self.frame_station4,
                                              text="35%",
                                              text_font=("Roboto Medium", -56))  # font name and size in px
        self.lbl_station4_humidity.grid(row=2,column=1,padx=10,sticky="n")

        self.button_station4 = customtkinter.CTkButton(master=self.frame_station4,
                                                text="Detalles",
                                                command=self.button_event)
        self.button_station4.grid(row=3, column=0, pady=10, padx=20, columnspan=2)
    
       
    def show_general(self):
        self.frame_general.grid()

    def hide_general(self):
        self.frame_general.grid_remove()
        
    #=====PLOTS METHODS=====
    def create_plots(self):
        self.frame_plots = customtkinter.CTkFrame(master=self)
        self.frame_plots.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_plots.columnconfigure(0,weight=1)
        self.frame_plots.rowconfigure(2,weight=1)

        self.label_1 = customtkinter.CTkLabel(master=self.frame_plots,
                                              text="Gráfico",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=0, column=0, pady=10, padx=10, columnspan=2)

    def show_plots(self):
        self.frame_plots.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    def hide_plots(self):
        self.frame_plots.grid_remove()

    #========CONTROL METHODS==========

    def create_control(self):
        self.frame_control = customtkinter.CTkFrame(master=self)
        self.frame_control.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.label_1 = customtkinter.CTkLabel(master=self.frame_control,
                                              text="Control",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=0, column=0, pady=10, padx=10, columnspan=2)
    
    def show_control(self):
        self.frame_control.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    def hide_control(self):
        self.frame_control.grid_remove()

#==========button events===============

    def button_general(self):
        print("General")
        self.show_general()
        self.hide_plots()
        self.hide_control()
    
    def button_plots(self):
        print("Graficos")
        self.show_plots()
        self.grafico()
        self.hide_general()
        self.hide_control()

    def button_control(self):
        print("Control automático")
        self.show_control()
        self.hide_general()
        self.hide_plots()

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

    def button_event(self):
        print("Button pressed")

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
    app.mainloop()