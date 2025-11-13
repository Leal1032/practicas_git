def areatri(): #Se encarga de devolver el area de un triangulo RECTANGULO, donde base es la BASE del triangulo y ALTURA es la altura del triangulo
    base = float(input("Digite la base de el triangulo: ")) #Aqui ingresamos el numero de la base 
    altura = float(input("Digite la altura de el triangulo :")) #Aqui ingresamos el numero de la alutra
    area = base*altura /2 #Aqui hacemos el proceso de los numeros
    print("Esta es el area de el triangulo", area) #Aqui se muestra el area del triangulo

def areacuadra(): 
    lado = float(input("Digite el primer lado del cuadrado: ")) #Aqui ingresamos el numero de el lado 
    area = lado*lado #Aqui hacemos el proceso de el numero
    print("El resultado del cuadrado es :", area) #Aqui se muestra el area del cuadrado

def area_circulo():
    radio = float(input("Digite el radio del circulo: "))
    radio = (3.1416*radio)**2
    print("Este es el area del circulo: ", radio)
   