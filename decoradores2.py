import os
os.system("cls")
#  Lunes 20 de julio
# Definición de un decorador
def f_decorador(F_parametro):
    # definición de la función interiro esta llama la función original
    def f_interior():
        # Acción
        print("Vamos a realizar una operación")
#********************************************************************
#23 de Julio
    
    # Llamo la función original
    F_parametro()
    # acción
    print("El calculo ya esta hecho")
    return f_interior
# ************************************************************
#28 de Julio
@f_decorador
def suma():
    print(20 + 5)
@f_decorador   
def resta():
    print(20 - 5)

suma()  # invocamos la función
resta()  # invocamos la función