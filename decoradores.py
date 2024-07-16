import os
os.system("cls")
#  Lunes 20 de julio
# Definición de un decorador
def f_decorador(F_parametro):
    # definición de la función interiro esta llama la función original
    def f_interior():
        # Acción
        print("Vamos a realizar una operación")
    # Llamo la función original
    F_parametro()
    # acción
    print("El calculo ya esta hecho")