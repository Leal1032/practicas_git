from calculos import areatri,areacuadra
from funtions import sumar
print("Hola Mundo")

menu_interactivo = True
while menu_interactivo:
    print("------Menu------")
    print("1. Sumar")
    print("2. Area triangulo")
    print("3. Area cuadrado")
    print("4. Salir")
    opcion=input("Seleccione una opcion: ")

    if (opcion == "1"):
        sumar()
    elif  (opcion == "2"):
        areatri()
    elif (opcion == "3"):
        areacuadra ()
    elif (opcion == "4"):
        print("Saliendo del programa")
        break
    else: 
        print("Opcion no valida")