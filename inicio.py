import tkinter
import customtkinter
from mainFrame import mainFrame


class inicio():
    def __init__(self,master):
        self.frame = customtkinter.CTkFrame(master=master,
                                                 width=180,
                                                 corner_radius=10)
        self.frame.grid()

        self.label_1 = customtkinter.CTkLabel(master=self.frame,
                                              text="Menú",
                                              text_font=("Roboto Medium", -16)) 

        self.label_1.grid()


if __name__=="__main__":
    app = mainFrame()
    windows_start = inicio(app)
    app.show_frame(windows_start)
    #app.hide_frame()
    app.mainloop()