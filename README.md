#  Sistema de Gestión de Nómina - Aceros Industrializados S.A. de C.V.

![Python](https://img.shields.io/badge/Python-3.14-blue?style=flat&logo=python)


Este proyecto es una aplicación de consola desarrollada en **Python** para gestionar y calcular la nómina de los empleados de la empresa ficticia *Aceros Industrializados S.A. de C.V.* El sistema utiliza el manejo de **arreglos** (listas) para el almacenamiento temporal y la manipulación de la información de los trabajadores.

##  Características Principales

El programa cuenta con un menú interactivo que permite realizar las siguientes operaciones:

1. **Modificar información**: Permite buscar a un trabajador por su "No. de Trabajador" y actualizar de manera individual cualquiera de sus datos mediante un submenú.
2. **Calcula sueldos**: Procesa la información de todos los empleados en el arreglo y calcula su sueldo final utilizando la fórmula establecida.
3. **Despliega sueldos**: Muestra una tabla general con toda la información de los trabajadores, incluyendo el cálculo final de su salario.
4. **Sueldos por Departamentos**: Genera un reporte con el monto total a pagar en sueldos agrupado por los departamentos de la empresa (*Compras, Dirección, Producción, Recursos Humanos, Ventas*).
5. **Sueldos por tipo de Empleado**: Genera un reporte con el monto total a pagar agrupado por el tipo de contrato (*Obrero, Empleado, Directivo*).
6. **Sueldos, Horas Extra y Bonos (Alcance 2.A)**: Muestra el desglose financiero total de la empresa, separando los montos correspondientes a Sueldos Base, Horas Extra y Bonos de Producción.
7. **Salir**: Termina la ejecución del programa de manera segura.

##  Fórmula de Cálculo

El sistema calcula el salario de cada empleado utilizando la siguiente fórmula matemática:

Sueldo = (Días Trabajados * Pago Diario) + (Horas Extra * Pago por Hora Extra) + Bono Productividad
 Estructura de Datos
El programa gestiona los siguientes campos para cada trabajador:

No. de Trabajador (Identificador único)

Nombre

Departamento

Tipo de Empleado

Días Trabajados

Pago Diario

Horas Extra

Pago por Hora Extra

Bono Productividad

 Validaciones y Seguridad
El sistema incluye validaciones exhaustivas para manejar contingencias. Esto asegura que el programa no colapse ante entradas de datos incorrectas por parte del usuario (por ejemplo, ingresar letras cuando se esperan números, o seleccionar opciones de menú inexistentes).

 Instrucciones de Uso
Asegúrate de tener Python 3.14 instalado en tu sistema.

Clona este repositorio o descarga el archivo principal .py.

Abre una terminal o línea de comandos en el directorio del archivo.

Ejecuta el programa con el siguiente comando:

Bash
python main.py
(Sustituye main.py por el nombre real de tu archivo).

Autores
 - Leonardo Daniel Tenorio Martínez
 - Mayrin Ximena Oliva Reyes
 - Emmanuel Reyes Urbano
 - Ivan Dilan Picazo Flores
 - Valeria Salas Gutierrez




***

