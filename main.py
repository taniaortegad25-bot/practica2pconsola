if __name__ == "__main__":
    from persona import Persona
    from holaMundo import Mensaje
    from operacionesMatematicas import OperacionesMatematicas

    print("este es el programa principal")
    print("elige la opcion que deseas ejecutar")
    print("1. Hola Mundo")
    print("2. Calcular edad de una persona")
    print("3. Operaciones Matematicas")
    print("4. Figuras geometricas")
    opcion = input("Ingresa el numero de la opcion: ")
    if opcion == "1":
        msg = Mensaje("Hola Mundo programacion con clases")
        msg.mostrar_mensaje()
    elif opcion == "2":
        nombre = input("Ingresa el nombre de la persona: ")
        anio_nacimiento = int(input("Ingresa el año de nacimiento de la persona: "))
        persona = Persona(nombre, anio_nacimiento, 0)
        anio_actual = int(input("Ingresa el año actual: "))
        edad = persona.calcular_edad(anio_actual)
        print(f"{persona.nombre} tiene {edad} años.")
    elif opcion == "3":
        operaciones = OperacionesMatematicas()
        a = float(input("Ingresa el primer número: "))
        b = float(input("Ingresa el segundo número: "))
        print("Suma:", operaciones.sumar(a, b))
        print("Resta:", operaciones.restar(a, b))
        print("Multiplicación:", operaciones.multiplicar(a, b))
        print("División:", operaciones.dividir(a, b))
    elif opcion == "4":
        from regtangulo import Rectangulo
        from circulo import circulo
        from triangulo import triangulo 
        from cuadrado import Cuadrado
        print("elige la figura geometrica que deseas calcular")
        print("1. Rectangulo")
        print("2. Circulo")
        print("3. Triangulo")
        print("4. Cuadrado")
        opcion_figura = input("Ingresa el numero de la figura: ")
        if opcion_figura == "1":
            ancho = float(input("Ingresa el ancho del rectangulo: "))
            alto = float(input("Ingresa el alto del rectangulo: "))
            rectangulo = Rectangulo(ancho, alto)
            print("Area del rectangulo:", rectangulo.area())
            print("Perimetro del rectangulo:", rectangulo.perimetro())
        elif opcion_figura == "2":
            radio = float(input("Ingresa el radio del circulo: "))
            circulo_obj = circulo(radio)
            print("Area del circulo:", circulo_obj.area())
            print("Perimetro del circulo:", circulo_obj.perimetro())
        elif opcion_figura == "3":
            base = float(input("Ingresa la base del triangulo: "))
            altura = float(input("Ingresa la altura del triangulo: "))
            triangulo_obj = triangulo(base, altura)
            print("Area del triangulo:", triangulo_obj.area())
            print("Perimetro del triangulo:", triangulo_obj.perimetro())
        elif opcion_figura == "4":
            lado = float(input("Ingresa el lado del cuadrado: "))
            cuadrado_obj = Cuadrado(lado)
            print("Area del cuadrado:", cuadrado_obj.area())
            print("Perimetro del cuadrado:", cuadrado_obj.perimetro())
        else:
            print("Opcion no valida")
    else:
        print("Opcion no valida")