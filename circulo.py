class circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio * self.radio

    def perimetro(self):
        return 2 * 3.1416 * self.radio