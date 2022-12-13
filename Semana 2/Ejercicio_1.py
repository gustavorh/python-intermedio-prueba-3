# Clase Cuadrado
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return self.lado * 4

    def imprimir(self):
        print("--------------------")
        print("Cuadrado")
        print("Lado: ", self.lado)
        print("Area: ", self.area())
        print("Perimetro: ", self.perimetro())
        print("--------------------")

# Clase Rectangulo
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return (self.base + self.altura) * 2

    def imprimir(self):
        print("--------------------")
        print("Rectangulo")
        print("Base: ", self.base)
        print("Altura: ", self.altura)
        print("Area: ", self.area())
        print("Perimetro: ", self.perimetro())
        print("--------------------")

# Clase Triangulo
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        return (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def tipo(self):
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            return "Equilatero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "Isoceles"
        else:
            return "Escaleno"

    def imprimir(self):
        print("--------------------")
        print("Triangulo")
        print("Lado 1: ", self.lado1)
        print("Lado 2: ", self.lado2)
        print("Lado 3: ", self.lado3)
        print("Area: ", self.area())
        print("Perimetro: ", self.perimetro())
        print("Tipo: ", self.tipo())
        print("--------------------")

# Clase Circulo
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio * self.radio

    def perimetro(self):
        return 2 * 3.1416 * self.radio

    def imprimir(self):
        print("--------------------")
        print("Circulo")
        print("Radio: ", self.radio)
        print("Area: ", self.area())
        print("Perimetro: ", self.perimetro())
        print("--------------------")

# Instanciar las clases
cuadrado = Cuadrado(5)
rectangulo = Rectangulo(5, 10)
triangulo = Triangulo(5, 5, 5)
circulo = Circulo(5)

# Imprimir la información de cada figura
cuadrado.imprimir()
rectangulo.imprimir()
triangulo.imprimir()
circulo.imprimir()
