from typing import Dict
from pizzas import BuilderPizza, Director, ConcreteBuilder_PizzaPersonalizada
from menu import Component, Entrante_Component, Pizza_Component, Bebida_Component, Postre_Component, CompositeMenu
import csv

class Pedido:
    def __init__(self, num_id: int, nombre: str) -> None:
        self.num_id = num_id
        self.nombre = nombre
        self.componentes = []  # Lista para almacenar los componentes del pedido

    def hacer_pedido(self) -> Dict:
        director = Director()
        builder_personalizada = ConcreteBuilder_PizzaPersonalizada()

        # Solicitar al cliente el tipo de menú que desea
        print("1. Menú Personalizado")
        print("2. Menú Completo")
        opcion = input("Seleccione el tipo de menú que desea (1-2): ")

        if opcion == "1":
            director.builder = builder_personalizada
            director.build_pizza_personalizada()
            pizza_personalizada = builder_personalizada.pizza
            # Agregar la pizza personalizada al pedido
            self.componentes.extend([pizza_personalizada])

        elif opcion == "2":
            # Solicitar al cliente el tipo de pizza para el menú completo
            print("1. Pizza Margarita")
            print("2. Pizza Barbacoa")
            print("3. Pizza Cuatro Quesos")
            tipo_pizza = input("Seleccione el tipo de pizza para el Menú Completo (1-3): ")

            if tipo_pizza == "1":
                pizza_menu = Pizza_Component("Pizza Margarita")
            elif tipo_pizza == "2":
                pizza_menu = Pizza_Component("Pizza Barbacoa")
            elif tipo_pizza == "3":
                pizza_menu = Pizza_Component("Pizza Cuatro Quesos")
            else:
                print("Opción no válida. Seleccionando Pizza Margarita por defecto.")
                pizza_menu = Pizza_Component("Pizza Margarita")

            # Agregar componentes al pedido
            entrante = Entrante_Component("Entrante", 4)
            bebida = Bebida_Component("Refresco", 2)
            postre = Postre_Component("Brownie", 5)
            self.componentes.extend([entrante, pizza_menu, bebida, postre])

        else:
            print("Opción no válida")
            return None

        return {"Nombre Cliente": self.nombre, "Componentes Pedido": [comp.nombre for comp in self.componentes]}


    def generar_factura(self) -> None:
        # Crear un menú compuesto con los componentes del pedido
        menu_pedido = CompositeMenu(self.num_id)
        for comp in self.componentes:
            menu_pedido.add_component(comp)

        # Calcular y mostrar el precio total del pedido
        precio_total = menu_pedido.get_precio()
        print(f"\nPrecio total del pedido ({self.num_id}): ${precio_total}")

        # Escribir el pedido en un archivo CSV
        menu_pedido.to_csv()
