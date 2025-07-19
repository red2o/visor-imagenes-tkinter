import os

def cargar_imagenes(ruta):
    extensiones = [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
    return [
        os.path.join(ruta, archivo)
        for archivo in os.listdir(ruta)
        if os.path.splitext(archivo)[1].lower() in extensiones
    ]
