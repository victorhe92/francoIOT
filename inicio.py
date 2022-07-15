import tkinter
import customtkinter
from mainFrame import mainFrame
import matplotlib.pyplot as plt
import datetime




class inicio():
    
    t1 = 10
    t2 = 20
    t3 = 30
    t4 = 40
    tiempo = datetime.datetime.now()
    
    def __init__(self,master):
        #Create a general vision frame
        self.frame.grid(row=0, column=1,sticky="nsew",pady=10,padx=10)
        self.frame = customtkinter.CTkFrame(master=self.frame)

        
   


        #==============INFORMATION OF EACH STATION======================

        #===STATION 1=====
        self.frame_station1.columnconfigure(1,weight=1)
        self.frame_station1.rowconfigure(3,weight=1)

        self.lbl_station1_title = customtkinter.CTkLabel(master=self.frame_station1,
                                              text="Microtunel 1",
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
                                              text=str(self.t1)+"ºC",
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
                                              text="Microtunel 2",
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
                                              text=str(self.t2)+"ºC",
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
                                              text="Microtunel 3",
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
                                              text=str(self.t3)+"ºC",
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
                                              text="Microtunel 4",
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
                                              text=str(self.t4)+"ºC",
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
    def button_event(self):
        print("detalles")

if __name__=="__main__":
    app = mainFrame()
    windows_start = inicio(app)
    #app.show_frame(windows_start)
    #app.hide_frame()
    app.mainloop()