import tkinter as tk

app = tk.Tk()
app.geometry('1024x600')
app.resizable(width=0,height=0)
app.rowconfigure(0,weight=1)
app.columnconfigure(0,weight=1)


class window1:
    def __init__(self,parent):
        self.frame = tk.Frame(master=parent)
        self.frame.grid(row=0,column=0)
        self.frame.rowconfigure(0,weight=1)
        self.frame.columnconfigure(0,weight=1)

        self.btn_sensor1 = tk.Button(self.frame,text="Sensor1",width=60,height=15)
        self.btn_sensor1.grid(row=0,column=0,padx=10,pady=10)

        self.btn_sensor2 = tk.Button(self.frame,text="Sensor2",width=60,height=15)
        self.btn_sensor2.grid(row=0,column=1,padx=10,pady=10)

        self.btn_sensor3 = tk.Button(self.frame,text="Sensor3",width=60,height=15)
        self.btn_sensor3.grid(row=1,column=0,padx=10,pady=10)

        self.btn_sensor4 = tk.Button(self.frame,text="Sensor4",width=60,height=15)
        self.btn_sensor4.grid(row=1,column=1,padx=10,pady=10)
    def mostrar(self):
        self.frame.grid(row=0,column=0)
    def ocultar(self):
        self.frame.grid_forget()

class window2:
    def __init__(self,parent):
        self.frame_left = tk.Frame(master=parent)
        self.frame_left.grid(row=0,column=0)
        self.frame_left.rowconfigure(0,weight=1)
        self.frame_left.columnconfigure(0,weight=1)

        self.frame_right = tk.Frame(master=parent)
        self.frame_right.grid(row=0,column=1)
        self.frame_right.rowconfigure(0,weight=1)
        self.frame_right.columnconfigure(0,weight=1)

        self.btn_chart = tk.Button(self.frame_left,text="Graficos",width=20,height=5)
        self.btn_chart.grid(row=0,column=0,padx=10,pady=10)

        self.btn_config = tk.Button(self.frame_left,text="Configuración",width=20,height=5)
        self.btn_config.grid(row=1,column=0,padx=10,pady=10)

        self.lbl_chart = tk.Label(master=self.frame_right,text="Acá va un gráfico")
        self.lbl_chart.pack(padx=200,pady=20)
    def mostrar(self):
        self.frame_left.grid(row=0,column=0)
        self.frame_right.grid(row=0,column=0)
    def ocultar(self):
        self.frame_left.remove()
        self.frame_right.remove()
        

ventana1 = window1(app)
ventana1.ocultar()

ventana2 = window2(app)

app.mainloop()