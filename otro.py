# Clase para representar los productos (ingredientes, pizza, bebida, postre)
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

# Clase para representar las opciones de menú (personalizado, completo)
class Menu:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def obtener_precio_total(self):
        return sum(producto.precio for producto in self.productos)

# Clase Builder para construir una pizza personalizada
class PizzaBuilder:
    def __init__(self):
        self.pizza = Producto("Pizza Personalizada", 0)

    def agregar_ingrediente(self, ingrediente):
        self.pizza.precio += ingrediente.precio

    def obtener_pizza(self):
        return self.pizza

# Clase Composite para representar las opciones preestablecidas (entrante, pizza, bebida, postre)
class Combo(Menu):
    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre

# Clase Director que utiliza el Builder para construir una pizza personalizada
class Director:
    def construir_pizza_personalizada(self, builder, ingredientes):
        for ingrediente in ingredientes:
            builder.agregar_ingrediente(ingrediente)
        return builder.obtener_pizza()
