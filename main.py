"""
Módulo de Gestión de Inventario de Electrodomésticos.

Este programa sirve para llevar el control de un inventario de aparatos domésticos.
Los clasifica de forma automática en tres grupos: Gama Baja, Media o Alta.
Para lograrlo, usa herramientas de programación como clases, herencia y control de errores.
"""

from abc import ABC, abstractmethod
import os
import re
import time

# Valores límite para decidir la gama de cada aparato
LAVADORA_MAX_BAJA = 10
LAVADORA_CICLOS_BAJA = 3
LAVADORA_MAX_MEDIA = 15
LAVADORA_CICLOS_MEDIA = 5

REFRIGERADOR_PUERTAS_BAJA = 1
REFRIGERADOR_METROS_BAJA = 10
REFRIGERADOR_PUERTAS_MEDIA = 2
REFRIGERADOR_METROS_MEDIA = 13

MICROONDAS_MAX_BAJA = 1000
MICROONDAS_MAX_MEDIA = 1500


# Funciones para validar los datos que escribe el usuario y limpiar la pantalla
def limpiar_pantalla():
    """Borra todo el texto de la pantalla de la consola para que se vea limpia."""
    os.system("cls" if os.name == "nt" else "clear")


def leer_cadena(mensaje):
    """Pide un texto al usuario y revisa que no esté vacío ni tenga símbolos raros.

    Parámetros:
        mensaje (str): El texto que se le muestra al usuario para pedirle el dato.

    Retorna:
        str: El texto que escribió el usuario ya revisado y sin espacios de más.
    """
    patron = r"^[a-zA-Z0-9\s\-_áéíóúÁÉÍÓÚñÑ]+$"
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("Error: El campo no puede estar vacío. Intente de nuevo.")
            continue
        if not re.match(patron, valor):
            print(
                "Error: Caracteres inválidos. Solo se permiten letras, "
                "números, espacios, guiones (-) y guiones bajos (_)."
            )
            continue
        return valor


def leer_medidas(mensaje):
    """Pide las medidas del aparato y revisa que tengan la forma correcta (Número x Número x Número).

    Parámetros:
        mensaje (str): El texto que se le muestra al usuario para pedirle las medidas.

    Retorna:
        str: Las medidas escritas en letras minúsculas (por ejemplo: 80x90x80).
    """
    patron = r"^\d+(\.\d+)?[xX]\d+(\.\d+)?[xX]\d+(\.\d+)?$"
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("Error: El campo no puede estar vacío.")
            continue
        if not re.match(patron, valor):
            print(
                "Error: Formato inválido. Debe ser estrictamente "
                "en formato NxNxN (ej. 80x90x80)."
            )
            continue
        return valor.lower()


def leer_float(mensaje):
    """Pide un número con punto decimal y revisa que sea mayor a cero.

    Parámetros:
        mensaje (str): El texto que se le muestra al usuario para pedirle el número.

    Retorna:
        float: El número decimal que escribió el usuario.
    """
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
            print(
                "Error: Entrada inválida. Debe ingresar un número "
                "decimal (ej. 1500.50)."
            )


def leer_entero(mensaje):
    """Pide un número entero y revisa que no sea negativo.

    Parámetros:
        mensaje (str): El texto que se le muestra al usuario para pedirle el número.

    Retorna:
        int: El número entero que escribió el usuario.
    """
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("Error: El campo no puede estar vacío.")
            continue
        try:
            numero = int(valor)
            if numero <= 0:
                print("Error: El valor no puede ser menor o igual a 0.")
                continue
            return numero
        except ValueError:
            print(
                "Error: Entrada inválida. Debe ingresar un número "
                "entero (ej. 10)."
            )


# Alertas o avisos de error personalizados
class InventarioVacio(Exception):
    """Este error se activa si el usuario intenta ver la lista de aparatos pero todavía no ha guardado ninguno."""

    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


# Clases y moldes para crear los aparatos (Programación Orientada a Objetos)
class Gama(ABC):
    """Esta es una plantilla obligatoria para asegurar que todos los aparatos calculen su tipo de gama."""

    @abstractmethod
    def tipo_gama(self):
        """Calcula y dice si el aparato es de Gama Baja, Media o Alta."""
        pass


class Electrodomestico:
    """Esta es la clase padre. Contiene los datos básicos que tienen todos los aparatos del inventario."""

    def __init__(self, id, marca, modelo, precio):
        """Guarda los datos generales como el código, la marca, el modelo y el precio."""
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        """Devuelve un texto con los datos básicos del aparato listos para leerse en pantalla."""
        return (
            f"ID: {self.id}, Marca: {self.marca}, "
            f"Modelo: {self.modelo}, Precio: ${self.precio:.2f}"
        )


class Lavadora(Electrodomestico, Gama):
    """Esta clase sirve para crear y controlar los datos específicos de las lavadoras."""

    def __init__(
        self, id, marca, modelo, precio, capacidad, consumo_agua, ciclos
    ):
        """Guarda los datos generales de la lavadora y le añade su capacidad, consumo de agua y ciclos."""
        super().__init__(id, marca, modelo, precio)
        self.capacidad = capacidad
        self.consumo_agua = consumo_agua
        self.ciclos_de_lavado = ciclos

    def __str__(self):
        """Devuelve un texto completo con todos los datos generales y específicos de la lavadora."""
        return (
            super().__str__() + f", Capacidad de Carga: {self.capacidad} kg, "
            f"Consumo de Agua: {self.consumo_agua} L, "
            f"Ciclos de Lavado: {self.ciclos_de_lavado}\n"
            f"Tipo Gama: {self.tipo_gama()}"
        )

    def tipo_gama(self):
        """Revisa la capacidad y los ciclos para decidir si la lavadora es de Gama Baja, Media o Alta."""
        if (
            self.capacidad <= LAVADORA_MAX_BAJA
            and self.ciclos_de_lavado <= LAVADORA_CICLOS_BAJA
        ):
            return "Gama Baja"
        elif (
            self.capacidad <= LAVADORA_MAX_MEDIA
            and self.ciclos_de_lavado <= LAVADORA_CICLOS_MEDIA
        ):
            return "Gama Media"
        else:
            return "Gama Alta"


class Refrigerador(Electrodomestico, Gama):
    """Esta clase sirve para crear y controlar los datos específicos de los refrigeradores."""

    def __init__(self, id, marca, modelo, precio, puertas, metros, pies):
        """Guarda los datos generales del refrigerador y le añade sus puertas, metros cúbicos y pies de capacidad."""
        super().__init__(id, marca, modelo, precio)
        self.no_puertas = puertas
        self.metros_cubicos = metros
        self.pies_capacidad = pies

    def __str__(self):
        """Devuelve un texto completo con todos los datos generales y específicos del refrigerador."""
        return (
            super().__str__() + f", Número de Puertas: {self.no_puertas}, "
            f"Metros Cúbicos: {self.metros_cubicos}, "
            f"Pies de Capacidad: {self.pies_capacidad}, \n"
            f"Tipo Gama: {self.tipo_gama()}"
        )

    def tipo_gama(self):
        """Revisa el número de puertas y el tamaño para decidir si el refrigerador es de Gama Baja, Media o Alta."""
        if (
            self.no_puertas == REFRIGERADOR_PUERTAS_BAJA
            and self.metros_cubicos <= REFRIGERADOR_METROS_BAJA
        ):
            return "Gama Baja"
        elif (
            self.no_puertas == REFRIGERADOR_PUERTAS_MEDIA
            and self.metros_cubicos <= REFRIGERADOR_METROS_MEDIA
        ):
            return "Gama Media"
        else:
            return "Gama Alta"


class Microondas(Electrodomestico, Gama):
    """Esta clase sirve para crear y controlar los datos específicos de los microondas."""

    def __init__(self, id, marca, modelo, precio, potencia, consumo, medidas):
        """Guarda los datos generales del microondas y le añade su potencia, consumo de energía y medidas."""
        super().__init__(id, marca, modelo, precio)
        self.potencia = potencia
        self.consumo_energia = consumo
        self.medidas = medidas

    def __str__(self):
        """Devuelve un texto completo con todos los datos generales y específicos del microondas."""
        return (
            super().__str__() + f", Potencia: {self.potencia} W, "
            f"Consumo de Energía: {self.consumo_energia} kWh, "
            f"Medidas: {self.medidas}, \n"
            f"Tipo Gama: {self.tipo_gama()}"
        )

    def tipo_gama(self):
        """Revisa los Watts de potencia para decidir si el microondas es de Gama Baja, Media o Alta."""
        if self.potencia < MICROONDAS_MAX_BAJA:
            return "Gama Baja"
        elif self.potencia <= MICROONDAS_MAX_MEDIA:
            return "Gama Media"
        else:
            return "Gama Alta"


# Funciones para controlar lo que hace el programa
def mostrar_datos(lista):
    """Muestra en la pantalla la lista de todos los aparatos guardados hasta el momento.

    Parámetros:
        lista (list): La lista donde están guardados los aparatos.
    """
    if not lista:
        raise InventarioVacio(
            "Error: El inventario está vacío. No hay datos para mostrar."
        )
    print("--- INVENTARIO ACTUAL ---")
    for obj in lista:
        print(obj)
        print("-" * 30)


def cargar_datos():
    """Muestra un menú para que el usuario elija qué aparato quiere registrar y le pide sus datos."""
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
            id_lav = leer_cadena("ID de la lavadora: ")
            marca = leer_cadena("Marca de la lavadora: ")
            model = leer_cadena("Modelo de la lavadora: ")
            p = leer_float("Precio de la lavadora: ")
            capacidad_carga = leer_entero("Capacidad de carga (en kg): ")
            consumo_agua = leer_entero("Consumo de agua (en litros): ")
            ciclos_de_lavado = leer_entero("Número de ciclos de lavado: ")
            lav = Lavadora(id_lav, marca, model, p, capacidad_carga, consumo_agua, ciclos_de_lavado,)
            inventario_global.append(lav)
            print("\n>> Objeto creado correctamente.")
            input("Presione Enter para continuar...")

        elif tipo == "2":
            id_refri = leer_cadena("ID del refrigerador: ")
            marca = leer_cadena("Marca del refrigerador: ")
            model = leer_cadena("Modelo del refrigerador: ")
            p = leer_float("Precio del refrigerador: ")
            no_puertas = leer_entero("Número de puertas: ")
            metros_cubicos = leer_entero("Metros cúbicos: ")
            pies_capacidad = leer_entero("Pies de capacidad: ")
            refri = Refrigerador(id_refri, marca ,model, p, no_puertas, metros_cubicos, pies_capacidad)
            inventario_global.append(refri)
            print("\n>> Objeto creado correctamente.")
            input("Presione Enter para continuar...")

        elif tipo == "3":
            id_micro = leer_cadena("ID del microondas: ")
            marca = leer_cadena("Marca del microondas: ")
            model = leer_cadena("Modelo del microondas: ")
            p = leer_float("Precio del microondas: ")
            potencia = leer_entero("Potencia del microondas (en W): ")
            consumo = leer_entero("Consumo de energía del microondas (en kWh): ")
            medidas = leer_medidas("Medidas del microondas (ej. 45x30x25): ")
            micro = Microondas(id_micro, marca, model, p, potencia, consumo, medidas)
            inventario_global.append(micro)
            print("\n>> Objeto creado correctamente.")
            input("Presione Enter para continuar...")

        elif tipo == "4":
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione Enter para continuar...")


# Lista principal donde se guardarán todos los aparatos creados
inventario_global = []

# Menú principal que se repite todo el tiempo mientras el programa esté abierto
if __name__ == "__main__":

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
        except Exception:
            print("\nOcurrió un error inesperado. Intente de nuevo.")
            input("Presione Enter para continuar...")