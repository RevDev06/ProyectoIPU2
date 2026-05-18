from abc import ABC, abstractmethod
import os
import time

def limpiar_pantalla():
    os.system("cls")



def leer_cadena(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: El campo no puede estar vacío. Intente de nuevo.")

def leer_float(mensaje):
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("Error: El campo no puede estar vacío.")
            continue
        try:
            numero = float(valor)
            if numero <= 0:
                print("Error: El valor debe ser estrictamente mayor a 0.")
                continue
            return numero
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un número decimal (ej. 1500.50).")

def leer_entero(mensaje, permitir_cero=False):
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("Error: El campo no puede estar vacío.")
            continue
        try:
            numero = int(valor)
            if numero < 0:
                print("Error: El valor no puede ser negativo.")
                continue
            if not permitir_cero and numero == 0:
                print("Error: El valor debe ser mayor a 0.")
                continue
            return numero
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un número entero (ej. 10).")


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


class Gama(ABC):
    @abstractmethod
    def tipo_gama(self):
        pass


class Electrodomestico:
    def __init__(self, id, marca, modelo, precio):
        if not id or id.strip() == "":
            raise IDvacio("Error: El ID no puede estar vacio")
        if precio <= 0:
            raise PrecioInvalido(
                "Error: El precio es invalido, no puede ser negativo o cero")

        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Marca: {self.marca}, Modelo: {self.modelo}, Precio: ${self.precio:.2f}"


class Lavadora(Electrodomestico, Gama):
    def __init__(self, id, marca, modelo, precio, capacidad_carga, consumo_agua, ciclos_de_lavado):
        super().__init__(id, marca, modelo, precio)
        self.capacidad = capacidad_carga
        self.consumo_agua = consumo_agua
        self.ciclos_de_lavado = ciclos_de_lavado

    def __str__(self):
        return super().__str__() + f", Capacidad de Carga: {self.capacidad} kg, Consumo de Agua: {self.consumo_agua} L, Ciclos de Lavado: {self.ciclos_de_lavado}\nTipo Gama: {self.tipo_gama()}"

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
        return super().__str__() + f", Número de Puertas: {self.no_puertas}, Metros Cúbicos: {self.metros_cubicos}, Pies de Capacidad: {self.pies_capacidad}, \n Tipo Gama: {self.tipo_gama()}"

    def tipo_gama(self):
        if self.no_puertas == 1 and self.metros_cubicos <= 10:
            return "Gama Baja"
        elif self.no_puertas == 2 and self.metros_cubicos <= 13:
            return "Gama Media"
        else:
            return "Gama Alta"


class Microondas(Electrodomestico, Gama):
    def __init__(self, id, marca, modelo, precio, potencia, consumo_energia, medidas):
        super().__init__(id, marca, modelo, precio)
        self.potencia = potencia
        self.consumo_energia = consumo_energia
        self.medidas = medidas

    def __str__(self):
        return super().__str__() + f", Potencia: {self.potencia} W, Consumo de Energía: {self.consumo_energia} kWh, Medidas: {self.medidas}, \n Tipo Gama: {self.tipo_gama()}"

    def tipo_gama(self):
        if self.potencia < 1000:
            return "Gama Baja"
        elif self.potencia <= 1500:
            return "Gama Media"
        else:
            return "Gama Alta"


def mostrar_datos(lista):
    if not lista:
        raise InventarioVacio(
            "Error: El inventario está vacío. No hay datos para mostrar.")
    print("--- INVENTARIO ACTUAL ---")
    for obj in lista:
        print(obj)
        print("-" * 30)


def cargar_datos():
    while True:
        limpiar_pantalla()
        print("Elija un electrodoméstico para cargar datos:")
        print("1. Lavadora")
        print("2. Refrigerador")
        print("3. Microondas")
        print("4. Volver al menú principal")
        tipo = input("Seleccione: ")
        limpiar_pantalla()

        if tipo == "1":
            try:
                id_lav = leer_cadena("ID de la lavadora: ")
                p = leer_float("Precio de la lavadora: ")
                capacidad_carga = leer_entero("Capacidad de carga (en kg): ")
                consumo_agua = leer_entero("Consumo de agua (en litros): ")
                ciclos_de_lavado = leer_entero("Número de ciclos de lavado: ")
                
                lav = Lavadora(id_lav, "Mabe", "L-20", p,
                               capacidad_carga, consumo_agua, ciclos_de_lavado)
                inventario_global.append(lav)
                print(">> Objeto creado correctamente.")
            except (IDvacio, PrecioInvalido, TypeError) as e:
                print(f"Error técnico al instanciar: {e}")
            input("Presione Enter para continuar...")

        elif tipo == "2":
            try:
                id_refri = leer_cadena("ID del refrigerador: ")
                model = leer_cadena("Modelo del refrigerador: ")
                p = leer_float("Precio del refrigerador: ")
                no_puertas = leer_entero("Número de puertas: ")
                metros_cubicos = leer_entero("Metros cúbicos: ")
                pies_capacidad = leer_entero("Pies de capacidad: ")
                
                refri = Refrigerador(
                    id_refri, "Mabe", model, p, no_puertas, metros_cubicos, pies_capacidad)
                inventario_global.append(refri)
                print(">> Objeto creado correctamente.")
            except (IDvacio, PrecioInvalido, TypeError) as e:
                print(f"Error técnico al instanciar: {e}")
            input("Presione Enter para continuar...")

        elif tipo == "3":
            try:
                id_micro = leer_cadena("ID del microondas: ")
                model = leer_cadena("Modelo del microondas: ")
                p = leer_float("Precio del microondas: ")
                potencia = leer_entero("Potencia del microondas (en W): ")
                consumo = leer_entero("Consumo de energía del microondas (en kWh): ")
                medidas = leer_cadena("Medidas del microondas (ej. 45x30x25 cm): ")
                
                micro = Microondas(id_micro, "Mabe", model,
                                   p, potencia, consumo, medidas)
                inventario_global.append(micro)
                print(">> Objeto creado correctamente.")
            except (IDvacio, PrecioInvalido, TypeError) as e:
                print(f"Error técnico al instanciar: {e}")
            input("Presione Enter para continuar...")

        elif tipo == "4":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")


inventario_global = []

while True:
    try:
        limpiar_pantalla()
        print("\n--- TODO PARA EL HOGAR S.A. ---")
        print("1. Instanciar (Cargar Datos)")
        print("2. Desplegar (Ver Inventario)")
        print("3. Salir")
        opc = input("Seleccione: ")

        if opc == "1":
            cargar_datos()

        elif opc == "2":
            limpiar_pantalla()
            try:
                mostrar_datos(inventario_global)
            except InventarioVacio as e:
                print(e.mensaje)
            input("Presione Enter para continuar...")

        elif opc == "3":
            limpiar_pantalla()
            print("Saliendo...")
            time.sleep(2)
            limpiar_pantalla()
            break

        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")
            
    except KeyboardInterrupt:
        print("\nInterrupción por el usuario.")
        input("Presione Enter para continuar...")
    except EOFError:
        print("\nError de fin de archivo o interrupción de teclado.")
        input("Presione Enter para continuar...")