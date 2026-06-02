"""
Módulo de Gestión de Inventario de Electrodomésticos.

Este programa permite administrar un inventario de aparatos domésticos
clasificándolos en categorías de gamas (Baja, Media, Alta) mediante el uso
de abstracciones, herencia, interfaces y manejo seguro de excepciones.
"""

from abc import ABC, abstractmethod
import os
import re
import time

# Constantes para límites de gamas 
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


# Funciones de validación y limpieza de pantalla
def limpiar_pantalla():
    """Limpia la consola de comandos de acuerdo al sistema operativo."""
    os.system("cls")


def leer_cadena(mensaje):
    """Solicita y valida una cadena de texto de manera limpia.

    Parámetros:
        mensaje (str): Texto explicativo para la solicitud de entrada.

    Retorna:
        str: Cadena de texto depurada y validada.
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
    """Valida que las dimensiones cumplan estrictamente con el formato NxNxN.

    Parámetros:
        mensaje (str): Texto explicativo para la solicitud de entrada.

    Retorna:
        str: Medida estandarizada en minúsculas.
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
    """Solicita y procesa un número decimal estrictamente mayor a cero.

    Parámetros:
        mensaje (str): Texto explicativo para la solicitud de entrada.

    Retorna:
        float: Número de precisión decimal validado.
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


def leer_entero(mensaje, permitir_cero=False):
    """Solicita y procesa un número entero positivo.

    Parámetros:
        mensaje (str): Texto explicativo para la solicitud de entrada.
        permitir_cero (bool): Indica si el valor cero es aceptado como válido.

    Retorna:
        int: Número entero validado.
    """
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
            print(
                "Error: Entrada inválida. Debe ingresar un número "
                "entero (ej. 10)."
            )


# Excepciones personalizadas para el control seguro de errores
class IDvacio(Exception):
    """Lanzada cuando el identificador está vacío o contiene solo espacios."""

    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class PrecioInvalido(Exception):
    """Lanzada cuando el precio asignado es menor o igual a cero."""

    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class InventarioVacio(Exception):
    """Lanzada al intentar mostrar un inventario sin elementos registrados."""

    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


# Interfaces y Modelado de Clases (POO)
class Gama(ABC):
    """Interfaz abstracta para definir la gama del producto."""

    @abstractmethod
    def tipo_gama(self):
        """Calcula y devuelve la gama correspondiente del artículo."""
        pass


class Electrodomestico:
    """Clase base con las propiedades comunes de un electrodoméstico."""

    def __init__(self, id, marca, modelo, precio):
        if not id or id.strip() == "":
            raise IDvacio("Error: El ID no puede estar vacio")
        if precio <= 0:
            raise PrecioInvalido(
                "Error: El precio es invalido, no puede ser negativo o cero"
            )

        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def __str__(self):
        return (
            f"ID: {self.id}, Marca: {self.marca}, "
            f"Modelo: {self.modelo}, Precio: ${self.precio:.2f}"
        )


class Lavadora(Electrodomestico, Gama):
    """Clase derivada para el manejo y clasificación de Lavadoras."""

    def __init__(
        self, id, marca, modelo, precio, capacidad, consumo_agua, ciclos
    ):
        super().__init__(id, marca, modelo, precio)
        self.capacidad = capacidad
        self.consumo_agua = consumo_agua
        self.ciclos_de_lavado = ciclos

    def __str__(self):
        return (
            super().__str__() + f", Capacidad de Carga: {self.capacidad} kg, "
            f"Consumo de Agua: {self.consumo_agua} L, "
            f"Ciclos de Lavado: {self.ciclos_de_lavado}\n"
            f"Tipo Gama: {self.tipo_gama()}"
        )

    def tipo_gama(self):
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
    """Clase derivada para el manejo y clasificación de Refrigeradores."""

    def __init__(self, id, marca, modelo, precio, puertas, metros, pies):
        super().__init__(id, marca, modelo, precio)
        self.no_puertas = puertas
        self.metros_cubicos = metros
        self.pies_capacidad = pies

    def __str__(self):
        return (
            super().__str__() + f", Número de Puertas: {self.no_puertas}, "
            f"Metros Cúbicos: {self.metros_cubicos}, "
            f"Pies de Capacidad: {self.pies_capacidad}, \n"
            f"Tipo Gama: {self.tipo_gama()}"
        )

    def tipo_gama(self):
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
    """Clase derivada para el manejo y clasificación de Microondas."""

    def __init__(self, id, marca, modelo, precio, potencia, consumo, medidas):
        super().__init__(id, marca, modelo, precio)
        self.potencia = potencia
        self.consumo_energia = consumo
        self.medidas = medidas

    def __str__(self):
        return (
            super().__str__() + f", Potencia: {self.potencia} W, "
            f"Consumo de Energía: {self.consumo_energia} kWh, "
            f"Medidas: {self.medidas}, \n"
            f"Tipo Gama: {self.tipo_gama()}"
        )

    def tipo_gama(self):
        if self.potencia < MICROONDAS_MAX_BAJA:
            return "Gama Baja"
        elif self.potencia <= MICROONDAS_MAX_MEDIA:
            return "Gama Media"
        else:
            return "Gama Alta"


# Funciones de control de operaciones del sistema
def mostrar_datos(lista):
    """Muestra el desglose de los elementos agregados en el almacén."""
    if not lista:
        raise InventarioVacio(
            "Error: El inventario está vacío. No hay datos para mostrar."
        )
    print("--- INVENTARIO ACTUAL ---")
    for obj in lista:
        print(obj)
        print("-" * 30)


def cargar_datos():
    """Despliega el menú para la captura secuencial de productos."""
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
                model = leer_cadena("Modelo de la lavadora: ")
                p = leer_float("Precio de la lavadora: ")
                capacidad_carga = leer_entero("Capacidad de carga (en kg): ")
                consumo_agua = leer_entero("Consumo de agua (en litros): ")
                ciclos_de_lavado = leer_entero("Número de ciclos de lavado: ")

                lav = Lavadora(
                    id_lav,
                    "Mabe",
                    model,
                    p,
                    capacidad_carga,
                    consumo_agua,
                    ciclos_de_lavado,
                )
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
                    id_refri,
                    "Mabe",
                    model,
                    p,
                    no_puertas,
                    metros_cubicos,
                    pies_capacidad,
                )
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
                consumo = leer_entero(
                    "Consumo de energía del microondas (en kWh): "
                )
                medidas = leer_medidas("Medidas del microondas (ej. 45x30x25): ")

                micro = Microondas(
                    id_micro, "Mabe", model, p, potencia, consumo, medidas
                )
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


# Inicialización del almacenamiento global
inventario_global = []

# Secuencia principal de ejecución (Orquestador de la aplicación)
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