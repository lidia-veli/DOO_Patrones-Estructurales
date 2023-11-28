import csv

def get_id_ultimo_pedido():
    '''Funcion que da el ID del ultimo pedido'''
    try:
        with open("data/pedidos.csv", 'r') as file:
            reader = csv.reader(file)
            last_row = list(reader)[-1]
            last_id = int(last_row[0])
            return last_id
    except FileNotFoundError:
        return 0
    except ValueError:
        return 0
    
def comprobar_id_usado(num_id):
    '''Funcion que comprueba si el id ya ha sido usado en la base de datos'''
    try:
        with open("data/pedidos.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == num_id:
                    return True
            return False
    except FileNotFoundError:
        return False


def crear_id_pedido():
    '''Funcion que crea un id para el pedido'''
    num_id = get_id_ultimo_pedido() + 1
    while comprobar_id_usado(num_id): # si el id ya existe, se crea otro
        num_id += 1
    return id
