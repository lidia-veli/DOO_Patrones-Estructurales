from __future__ import annotations
from abc import ABC, abstractmethod

class BuilderPizza(ABC):

    def __init__(self):
        self._pizza = None

    @property  # para que nos cree getters y setters
    @abstractmethod
    def pizza(self) -> None:
        pass

    @abstractmethod
    def nombre_pizza(self) -> None:
        pass

    @abstractmethod
    def tipo_masa(self) -> None:
        pass

    @abstractmethod
    def tipo_salsa_base(self) -> None:
        pass

    @abstractmethod
    def tipo_ingredientes(self) -> None:
        pass

    @abstractmethod
    def tipo_coccion(self) -> None:
        pass

    @abstractmethod
    def tipo_presentacion(self) -> None:
        pass

    @abstractmethod
    def tipo_bebida(self) -> None:
        pass

    @abstractmethod
    def tipo_extras(self) -> None:
        pass

    @abstractmethod
    def precio(self) -> None:
        pass


# -------------------------------------------
# CONCRETE BUILDER Pizza Personalizada
# -------------------------------------------


class ObjPizza():

    def __init__(self) -> None:
        self.parts = {} # es un diccionario

    def add(self, category: str, element: str) -> None:
        self.parts[category] = element

    def list_parts(self) -> None:
        print("Componentes pizza:")
        for category, element in self.parts.items():
            print(f"{category}: {element}")


class ConcreteBuilder_PizzaPersonalizada(BuilderPizza):
    """
    Builder de pizza personalizada
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._pizza = ObjPizza()

    @property
    def pizza(self) -> ObjPizza :
        pizza = self._pizza
        self.reset()
        return pizza
    
    def nombre_pizza(self) -> None:
        nombre = input("Escribe el nombre que quieres darle a tu pizza: ")
        self._pizza.add("Nombre", f"{nombre}")

    def tipo_masa(self) -> None:
        masa = input("Elige el tipo de masa (fina, normal, gruesa): ")
        self._pizza.add("Masa", f"{masa}")

    def tipo_salsa_base(self) -> None:
        salsa = input("Elige el tipo de salsa base (tomate, barbacoa, pesto): ")
        self._pizza.add("Salsa base", f"{salsa}")

    def tipo_ingredientes(self) -> None:
        lista_ing = []
        while True:
            ingrediente = input("Agrega ingredientes (escribe '0' para terminar): ")
            if ingrediente.lower() == '0':
                break
            lista_ing.append(ingrediente)
        self._pizza.add("Ingredientes", f"{', '.join(lista_ing)}")

    def tipo_coccion(self) -> None:
        coccion = input("Elige el tipo de cocción (horno, parrilla, leña): ")
        self._pizza.add("Cocción", f"{coccion}")

    def tipo_presentacion(self) -> None:
        presentacion = input("Elige el tipo de presentación (tradicional, cuadrada, personalizada): ")
        self._pizza.add("Presentación", f"{presentacion}")

    def tipo_bebida(self) -> None:
        maridaje = input("Elige el tipo de bebida (cerveza, vino, refresco): ")
        self._pizza.add("Bebida", f"{maridaje}")

    def tipo_extras(self) -> None:
        extra = input("Agrega un extra (o escribe '0' para omitir): ")
        self._pizza.add("Extra", f"{extra}")

    def precio(self) -> float:
        precio_base = 15
        # si hay más de 3 ingredientes, se añade 1.5€ por cada ingrediente extra
        lista_ing = self._pizza.parts["Ingredientes"].split(", ")
        if len(lista_ing) > 3:
            for _ in lista_ing[3:]:
                precio_base += 1.5
        # si la presentacion es personalizada, se añade 3€
        if self._pizza.parts["Presentación"] != "tradicional" and self._pizza.parts["Presentación"] != "cuadrada":
            precio_base += 3
        # si hay extra, se añade 2€
        if self._pizza.parts["Extra"] != "0":
            precio_base += 2
        
        self._pizza.add("Precio", f"{precio_base}")



# -------------------------------------------
# CONCRETE BUILDER Pizza Preestablecida
# -------------------------------------------

class ConstructorPizzaMargarita(BuilderPizza):
    
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._pizza = ObjPizza()

    @property
    def pizza(self) -> ObjPizza:
        pizza = self._pizza
        self.reset()
        return pizza
    
    def nombre_pizza(self) -> None:
        self._pizza.add("Nombre", "Pizza Margarita")

    def tipo_masa(self) -> None:
        self._pizza.add("Masa", "fina")

    def tipo_salsa_base(self) -> None:
        self._pizza.add("Salsa base", "tomate")

    def tipo_ingredientes(self) -> None:
        self._pizza.add("Ingredientes", "mozarella, albahaca")

    def tipo_coccion(self) -> None:
        self._pizza.add("Cocción", "horno")

    def tipo_presentacion(self) -> None:
        self._pizza.add("Presentación", "tradicional")

    def tipo_bebida(self) -> None:
        pass

    def tipo_extras(self) -> None:
        pass

    def precio(self) -> None:
        self._pizza.add("Precio", 8)


class ConstructorPizzaBarbacoa(BuilderPizza):
    
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._pizza = ObjPizza()

    @property
    def pizza(self) -> ObjPizza:
        pizza = self._pizza
        self.reset()
        return pizza
    
    def nombre_pizza(self) -> None:
        self._pizza.add("Nombre", "Pizza Barbacoa")

    def tipo_masa(self) -> None:
        self._pizza.add("Masa", "normal")

    def tipo_salsa_base(self) -> None:
        self._pizza.add("Salsa base", "barbacoa")

    def tipo_ingredientes(self) -> None:
        self._pizza.add("Ingredientes", "cheddar, bacon, cebolla, pollo")

    def tipo_coccion(self) -> None:
        self._pizza.add("Cocción", "horno")

    def tipo_presentacion(self) -> None:
        self._pizza.add("Presentación", "tradicional")

    def tipo_bebida(self) -> None:
        pass

    def tipo_extras(self) -> None:
        pass

    def precio(self) -> None:
        self._pizza.add("Precio", 10)


class ConstructorPizzaQuesos(BuilderPizza):
        
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._pizza = ObjPizza()

    @property
    def pizza(self) -> ObjPizza:
        pizza = self._pizza
        self.reset()
        return pizza
    
    def nombre_pizza(self) -> None:
        self._pizza.add("Nombre", "Pizza Cuatro Quesos")

    def tipo_masa(self) -> None:
        self._pizza.add("Masa", "fina")

    def tipo_salsa_base(self) -> None:
        self._pizza.add("Salsa base", "tomate")

    def tipo_ingredientes(self) -> None:
        self._pizza.add("Ingredientes", "mozzarella, parmesano, brie, cheddar")

    def tipo_coccion(self) -> None:
        self._pizza.add("Cocción", "horno")

    def tipo_presentacion(self) -> None:
        self._pizza.add("Presentación", "tradicional")

    def tipo_bebida(self) -> None:
        pass

    def tipo_extras(self) -> None:
        pass

    def precio(self) -> None:
        self._pizza.add("Precio", 10)



# -------------------------------------------
# DIRECTOR
# -------------------------------------------

class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> BuilderPizza:
        return self._builder

    @builder.setter
    def builder(self, builder: BuilderPizza) -> None:
        self._builder = builder

    def build_pizza_personalizada(self) -> None:
        self.builder.nombre_pizza()
        self.builder.tipo_masa()
        self.builder.tipo_salsa_base()
        self.builder.tipo_ingredientes()
        self.builder.tipo_coccion()
        self.builder.tipo_presentacion()
        self.builder.tipo_bebida()
        self.builder.tipo_extras()
        self.builder.precio()

    def build_pizza_menu(self) -> None:
        self.builder.nombre_pizza()
        self.builder.tipo_masa()
        self.builder.tipo_salsa_base()
        self.builder.tipo_ingredientes()
        self.builder.tipo_coccion()
        self.builder.tipo_presentacion()
        self.builder.precio()

    
def pedir_pizza_menu(tipo_pizza) -> dict:
    director = Director()
    if tipo_pizza == "Pizza Margarita":
        constructor = ConstructorPizzaMargarita()
    elif tipo_pizza == "Pizza Barbacoa":
        constructor = ConstructorPizzaBarbacoa()
    elif tipo_pizza == "Pizza Cuatro Quesos":
        constructor = ConstructorPizzaQuesos()
    else:
        print("No existe ese tipo de pizza")
        return None

    director.builder = constructor
    director.build_pizza_menu()
    return constructor.pizza.parts
