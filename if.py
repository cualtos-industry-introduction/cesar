salida = "No"
while(salida in ["No"]):
    seleccion = input("Ingresa una opción")
    if seleccion == 'a':
        print("Elegiste la opción a")
    elif seleccion == 'b':
        print("Elegiste la ioción b")
    else:
        print("Elegiste otra opción")    
    salida = input("Desea salir?")