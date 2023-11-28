import csv
from .pizzas import Director, ConstructorPizzaMargarita, ConstructorPizzaBarbacoa, ConstructorPizzaQuesos
from abc import ABC, abstractmethod


class Component(ABC):
    '''interfaz común para todos los componentes (hojas y compuestos)'''

    @abstractmethod
    def get_precio(self) -> float:
        pass


# -------------------------------------------
# HOJAS
# -------------------------------------------

class Entrante_Component(Component):
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
    
    def get_precio(self) -> float:
        return self.precio


class Pizza_Component(Component):
    def __init__(self, pedido_pizza: str) -> None:
        self.pedido_pizza = pedido_pizza
        director = Director()  # director
        constructor = self.tipo_pizza(self.pedido_pizza)
        director.builder = constructor
        #construimos la pizza de menú
        director.build_pizza_menu()
        # ahora ya tenemos el objeto pizza
        self.pizza = constructor.pizza
        self.nombre = self.pizza.parts["Nombre"]

    def tipo_pizza(self, nombre_pizza) -> str:
        if nombre_pizza == "Pizza Margarita":
            return ConstructorPizzaMargarita()
        elif nombre_pizza == "Pizza Barbacoa":
            return ConstructorPizzaBarbacoa()
        elif nombre_pizza == "Pizza Cuatro Quesos":
            return ConstructorPizzaQuesos()
        else:
            print("Nombre de pizza no reconocido")
            return None
    
    def list_parts(self) -> None:
        self.pizza.list_parts()

    def get_precio(self) -> float:
        return self.pizza.parts["Precio"]


class Bebida_Component(Component):
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
    
    def get_precio(self) -> float:
        return self.precio


class Postre_Component(Component):
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
   
    def get_precio(self) -> float:
        return self.precio


# -------------------------------------------
# COMPOSITE
# -------------------------------------------

class CompositeMenu(Component):
    def __init__(self, codigo: int) -> None:
        self.codigo = codigo
        self.nombre = 'Menú Pizza'  # nombre del menu
        self.componentes = []

    def add_component(self, component: Component) -> None:
        self.componentes.append(component)

    def remove_component(self, component: Component) -> None:
        self.componentes.remove(component)

    def get_precio(self) -> float:
        total_price = sum(comp.get_precio() for comp in self.componentes)
        return total_price

    def to_csv(self):
        with open("data/pedidos.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            lista_comp = []
            for comp in self.componentes:
                lista_comp.append(comp.nombre)
            writer.writerow([self.codigo, self.nombre, lista_comp[0], lista_comp[1], lista_comp[2], lista_comp[3]])
                                                    #     entrante       pizza           bebida          postre



def client_code(component: Component) -> None:
    '''proporciona una forma de interactuar con cualquier componente 
    (ya sea una hoja o un compuesto) sin preocuparse por su tipo concreto.'''

    print(f"Precio: {component.get_precio()}")
