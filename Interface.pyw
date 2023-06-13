from tkinter import *
from mqtt import con, stop
import sys
import os

def rutas(self, ruta):
    try:
        rutabase = sys._MEIPASS
    except Exception:
        rutabase = os.path.abspath(".")
    return os.path.join(rutabase, ruta)

def main():
    root = Tk()

    root.title("Conexión a la base de datos - MQTT")
    root.resizable(False, False)
    root.geometry("350x150") 
    root.config(bg="white")

    #ico = self.rutas(r"mosquitto.ico")
    #root.iconbitmap(ico)

    frame = Frame(root, width="650", height="330")
    frame.pack()
    frame.config(bg="white")

    Label(frame, text="MQTT conexión a la DB", bg="white", font=("bold", 18), padx=20, pady=20).pack()

    Inicio = Button(frame, text="Iniciar", font=("bold", 12), fg="white", bg="green", bd=0, width=10, height=2, padx=4, pady=4, command=lambda:[con(), hide()] )
    #Stop = Button(frame, text="Detener", font=("bold", 12), fg="white", bg="red", bd=0, width=10, height=2, padx=4, pady=4, command=stop) #

    def hide():
        if Inicio.winfo_ismapped():
            Inicio.config(text="Detener", font=("bold", 12), fg="white", bg="red", bd=0, width=10, height=2, padx=4, pady=4, command=stop)

    Inicio.pack()    


    root.mainloop()

if __name__ == '__main__':
    main()