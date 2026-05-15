from abc import ABC, abstractmethod
#Excepciones
class IDvacio(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class PrecioInvalido(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class InventarioVacio(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
  

# Interface
class Gama(ABC):
    @abstractmethod
    def tipo_gama(self):
        pass
class Electrodomestico:
    def __init__(self,id, marca, modelo, precio):
        if not id or id.strip()=="":
            raise IDvacio("Error: El ID no puede estar vacio")
        if precio <=0:
            raise PrecioInvalido("Error:El precio es invalido, no puede ser negativo o cero")

        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Marca: {self.marca}, Modelo: {self.modelo}, Precio: ${self.precio}"

class Lavadora(Electrodomestico, Gama):
    def __init__(self, id, marca, modelo, precio, capacidad_carga,consumo_agua,ciclos_de_lavado):
        super().__init__(id, marca, modelo, precio)
        self.capacidad = capacidad_carga
        self.consumo_agua = consumo_agua
        self.ciclos_de_lavado = ciclos_de_lavado
    def __str__(self):
        return super().__str__() + f", Capacidad de Carga: {self.capacidad} kg, Consumo de Agua: {self.consumo_agua} L,"
        f"Ciclos de Lavado: {self.ciclos_de_lavado}\nTipo Gama: {self.tipo_gama()}"

    def tipo_gama(self):
        if self.capacidad <= 10 and self.ciclos_de_lavado <= 3:
            return "Gama Baja"
        elif self.capacidad <= 15 and self.ciclos_de_lavado <= 5:
            return "Gama Media"
        else:
            return "Gama Alta"

def mostrar_datos(lista):
    if not lista:
        raise InventarioVacio("Error: El inventario está vacío. Use la opción 1.")
    print(" INVENTARIO ACTUAL ")
    for obj in lista:
        print(obj)

inventario_global = []
#Menu
while True:
    print("\n--- TODO PARA EL HOGAR S.A. ---")
    print("1. Instanciar (Cargar Datos)")
    print("2. Desplegar (Ver Inventario)")
    print("3. Salir")
    opc = input("Seleccione: ")
    if opc == "1":
        try:
            p = float(input("Precio de la lavadora: "))
            id_lav = input("ID de la lavadora: ")
            lav = Lavadora(id_lav, "Mabe", "L-20", p, 12, 10, 5)
            inventario_global.append(lav)
            print(">> Objeto creado correctamente.")
        except ValueError:
            print("Error: El precio debe ser un número.")
        except IDvacio as e: 
            print(e.mensaje)
        except PrecioInvalido as e:
            print(e.mensaje)
        except TypeError as e:
            print(f"Error técnico en los argumentos: {e}")

    elif opc == "2":
        try:
            mostrar_datos(inventario_global)
        except InventarioVacio as e:
            print(e.mensaje)

    elif opc == "3":
        print("Saliendo...")
        break