import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from .funciones import cargar_imagenes

class VisorImagenes:
    def __init__(self, root):
        self.root = root
        self.root.title("Visor de Imágenes")
        self.imagenes = []
        self.index = 0

        self.canvas = tk.Label(root)
        self.canvas.pack(expand=True)

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Abrir carpeta", command=self.abrir_carpeta).pack(side="left")
        tk.Button(btn_frame, text="Anterior", command=self.imagen_anterior).pack(side="left")
        tk.Button(btn_frame, text="Siguiente", command=self.imagen_siguiente).pack(side="left")

    def abrir_carpeta(self):
        carpeta = filedialog.askdirectory()
        self.imagenes = cargar_imagenes(carpeta)
        self.index = 0
        self.mostrar_imagen()

    def mostrar_imagen(self):
        if self.imagenes:
            imagen = Image.open(self.imagenes[self.index])
            imagen = imagen.resize((400, 300))
            self.tk_image = ImageTk.PhotoImage(imagen)
            self.canvas.config(image=self.tk_image)

    def imagen_anterior(self):
        if self.index > 0:
            self.index -= 1
            self.mostrar_imagen()

    def imagen_siguiente(self):
        if self.index < len(self.imagenes) - 1:
            self.index += 1
            self.mostrar_imagen()

def iniciar_app():
    root = tk.Tk()
    app = VisorImagenes(root)
    root.mainloop()
