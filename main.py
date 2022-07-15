from Classes.mainFrame import mainFrame

from Classes.inicio import inicio


if __name__ == "__main__":
    app = mainFrame()
    windows_start = inicio(app)
    app.show_frame(windows_start)
    #app.hide_frame()
    app.mainloop()