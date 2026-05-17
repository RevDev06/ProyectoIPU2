from abc import ABC, abstractmethod
import os
import time

def limpiar_pantalla():
    os.system("cls")

inventario_global = []

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

class Refrigerador(Electrodomestico, Gama):
    def __init__(self, id, marca, modelo, precio, no_puertas, metros_cubicos, pies_capacidad):
        super().__init__(id, marca, modelo, precio)
        self.no_puertas = no_puertas
        self.metros_cubicos = metros_cubicos
        self.pies_capacidad = pies_capacidad

    def __str__(self):
        return super().__str__() + f", Número de Puertas: {self.no_puertas}, Metros Cúbicos: {self.metros_cubicos}, Pies de Capacidad: {self.pies_capacidad}"
    
    def tipo_gama(self):
        if self.no_puertas == 1 and self.metros_cubicos <= 10:
            return "Gama Baja"
        elif self.no_puertas == 2 and self.metros_cubicos <= 13:
            return "Gama Media"
        else:
            return "Gama Alta"

class Microondas(Electrodomestico, Gama):
    def __init__(self, id, marca, modelo, precio, potencia, capacidad_interior, funciones):
        super().__init__(id, marca, modelo, precio)
        self.potencia = potencia
        self.capacidad_interior = capacidad_interior
        self.funciones = funciones

    def __str__(self):
        return super().__str__() + f", Potencia: {self.potencia} W, Capacidad Interior: {self.capacidad_interior} L, Funciones: {', '.join(self.funciones)}\nTipo Gama: {self.tipo_gama()}"

    def tipo_gama(self):
        if self.potencia < 1000:
            return "Gama Baja"
        elif self.potencia <= 1500:
            return "Gama Media"
        else:
            return "Gama Alta"


def mostrar_datos(lista):
    if not lista:
        raise InventarioVacio("Error: El inventario está vacío. Use la opción 1.")
    print(" INVENTARIO ACTUAL ")
    for obj in lista:
        print(obj)
        
def cargar_datos():
    print("Cargando datos...")
    while True:
        print("Eliga un electrodoméstico para cargar datos:")
        print("1. Lavadora")
        print("2. Refrigerador")
        print("3. Microondas")
        print("4. Volver al menú principal")
        tipo = input("Seleccione: ")
        limpiar_pantalla()
        
        if tipo == "1":
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
        
        elif tipo == "2":
            try:
                p = float(input("Precio del refrigerador: "))
                id_refri = input("ID del refrigerador: ")
                refri = Refrigerador(id_refri, "Mabe", "R-20", p, 2, 12, 15)
                inventario_global.append(refri)
                print(">> Objeto creado correctamente.")
                
            except ValueError:
                print("Error: El precio debe ser un número.")
            except IDvacio as e: 
                print(e.mensaje)
            except PrecioInvalido as e:
                print(e.mensaje)
            except TypeError as e:
                print(f"Error técnico en los argumentos: {e}")
        
        elif tipo == "3":
            try:
                p = float(input("Precio del microondas: "))
                id_micro = input("ID del microondas: ")
                micro = Microondas(id_micro, "Mabe", "M-20", p, 1200, 25, ["Descongelar", "Cocinar"])
                inventario_global.append(micro)
                print(">> Objeto creado correctamente.")
                
            except ValueError:
                print("Error: El precio debe ser un número.")
            except IDvacio as e: 
                print(e.mensaje)
            except PrecioInvalido as e:
                print(e.mensaje)
            except TypeError as e:
                print(f"Error técnico en los argumentos: {e}")
        
        elif tipo == "4":
            print("Volviendo al menú principal...")
            break
        else: 
            print("Opción no válida. Intente de nuevo.")

#Menu
while True:
    limpiar_pantalla()
    print("\n--- TODO PARA EL HOGAR S.A. ---")
    print("1. Instanciar (Cargar Datos)")
    print("2. Desplegar (Ver Inventario)")
    print("3. Salir")
    opc = input("Seleccione: ")
    limpiar_pantalla()
    
    if opc == "1":
        cargar_datos()
    
    elif opc == "2":
        try:
            mostrar_datos(inventario_global)
        except InventarioVacio as e:
            print(e.mensaje)

    elif opc == "3":
        limpiar_pantalla()
        print("Saliendo...")
        time.sleep(2)
        limpiar_pantalla()
        break
    
    else:
        print("Opción no válida. Intente de nuevo.")