import os
import time 
# [ID, Nombre, Depto, Tipo, Dias, PagoD, He, PagoHe, Bono, SueldoTotal]
empleados=[
    [100, "Jose Perez Ramos", "Produccion", "Obrero", 7, 825, 9, 200, 0, 0],
    [110, "Pablo Ramirez Ruiz", "Produccion", "Obrero", 7, 825, 10, 200, 0, 0],
    [130, "Ma. Luz Aguilar Hernandez", "Produccion", "Obrero", 7, 825, 12, 200, 0, 0],
    [135, "Roberto Haro Torres", "Ventas", "Empleado", 15, 955, 10, 250, 0, 0],
    [143, "Rosa Lopez Juarez", "Ventas", "Empleado", 15, 955, 4, 250, 0, 0],
    [150, "Ramon Martinez Suarez", "Ventas", "Empleado", 15, 955, 9, 250, 0, 0],
    [163, "Santiago Alonso Contreras", "Compras", "Empleado", 15, 955, 11, 250, 0, 0],
    [174, "Jesus Campos Sanchez", "Compras", "Empleado", 15, 955, 11, 250, 0, 0],
    [183, "Moises Castro Montante", "Compras", "Empleado", 15, 955, 0, 250, 0, 0],
    [192, "Pablo Cervantes Salinas", "Recursos Humanos", "Empleado", 15, 955, 6, 250, 0, 0],
    [203, "Anahi Torres Carreon", "Recursos Humanos", "Empleado", 15, 955, 3, 250, 0, 0],
    [213, "Nuria Lira Gonzalez", "Recursos Humanos", "Empleado", 15, 955, 0, 250, 0, 0],
    [226, "Miguel Mendoza Sanchez", "Produccion", "Obrero", 7, 825, 1, 200, 0, 0],
    [234, "Sofia Gonzalez Esparza", "Direccion", "Directivo", 15, 2000, 0, 0, 800, 0],
    [241, "Cristian Gonzalez Gonzalez", "Produccion", "Obrero", 7, 825, 6, 200, 0, 0],
    [255, "Juan Gamez Aguilar", "Ventas", "Empleado", 15, 955, 8, 250, 0, 0],
    [261, "Fernando Lopez Nuño", "Direccion", "Directivo", 15, 1200, 1, 250, 0, 0],
    [274, "Abraham Lozano De Lira", "Compras", "Empleado", 15, 955, 8, 250, 0, 0],
    [283, "Angel Negrete Demetrio", "Ventas", "Empleado", 15, 955, 1, 250, 0, 0],
    [294, "Damian Nieves Quezada", "Recursos Humanos", "Empleado", 15, 955, 10, 250, 0, 0],
    [307, "Armando Reyes Martinez", "Compras", "Empleado", 15, 955, 8, 250, 0, 0],
    [318, "Manuel Ruiz Mendoza", "Ventas", "Empleado", 15, 955, 3, 250, 0, 0],
    [326, "Esteban Salado Muñoz", "Direccion", "Directivo", 15, 1500, 0, 0, 1000, 0],
    [331, "Alejandro Soto Ocampo", "Direccion", "Directivo", 15, 1200, 0, 0, 1200, 0],
    [337, "Alondra Valdes Mora", "Direccion", "Directivo", 15, 1200, 0, 0, 2000, 0]
]

def limpiar_pantalla():
    os.system('cls')

def leer_entero(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor)
        else: 
            print("\n[!] Error: Entrada inválida. Por favor, ingresa un número entero.")

def leer_flotante(mensaje):
    while True:
        valor = input(mensaje)
        if valor.replace('.', '', 1).isdigit():
            return float(valor)
        else:
            print("\n[!] Error: Entrada inválida. Por favor, ingresa un número válido.")

def leer_cadena(mensaje):
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("\n[!] Error: No puedes dejar este campo en blanco.")
            continue  
        if valor.replace(" ", "").isalpha():
            return valor  
        else:
            print("\n[!] Error: Entrada inválida. Ingresa solo letras (sin números ni símbolos especiales).")


def imprimir_tabla(matriz):
    print("\n" + "="*110)
    print(f"{"ID":<5} | {"NOMBRE":<28} | {"DEPTO":<18} | {"DIAS":<5} | {"PAGO D.":<8} | {"HE":<3} | {"P.HE":<6} | {"BONO":<6}")
    print("-" * 110)
    for emp in matriz:
        print(f"{emp[0]:<5} | {emp[1]:<28} | {emp[2]:<18} | {emp[4]:<5} | {emp[5]:<8} | {emp[6]:<3} | {emp[7]:<6} | {emp[8]:<6}")

    print("="*110 + "\n")

def reporte_departamentos(matriz):
    p_total=0
    v_total=0
    c_total=0
    r_total=0
    d_total=0
    for emp in matriz:
        sueldo_emp=(emp[4]*emp[5])+(emp[6]*emp[7])+emp[8]
        depto=emp[2]
        if depto=="Produccion":
            p_total+=sueldo_emp
        elif depto=="Ventas":
            v_total+=sueldo_emp
        elif depto=="Compras":
            c_total+=sueldo_emp
        elif depto=="Recursos Humanos":
            r_total+=sueldo_emp
        elif depto=="Direccion": 
            d_total+=sueldo_emp

    print("--- Sueldos por departamento ---")
    print(f"{"Departamento":<25} | {"Total":>15}")
    print("-" * 45)
    print(f"{"Produccion":<25} | ${p_total:>14.2f}")
    print(f"{"Ventas":<25} | ${v_total:>14.2f}")
    print(f"{"Compras":<25} | ${c_total:>14.2f}")
    print(f"{"Recursos humanos":<25} | ${r_total:>14.2f}")
    print(f"{"Direccion":<25} | ${d_total:>14.2f}")
    print("-" * 45 + "\n")

def modificar_info(empleados):
    # Aquí irá la lógica para modificar la información de un empleado
    return

def calcular_sueldos(empleados):
    for emp in empleados:
        sueldo_total = (emp[4]*emp[5])+(emp[6]*emp[7])+emp[8]
        emp[9] = sueldo_total
        
def desplegar_sueldos(empleados):
    print("\n" + "="*110)
    print(f"{"ID":<5} | {"NOMBRE":<28} | {"DEPTO":<18} | {"DIAS":<5} | {"PAGO D.":<8} | {"HE":<3} | {"P.HE":<6} | {"BONO":<6} | {"SUELDO TOTAL":<12}")
    print("-" * 110)
    for emp in empleados:
        print(f"{emp[0]:<5} | {emp[1]:<28} | {emp[2]:<18} | {emp[4]:<5} | {emp[5]:<8} | {emp[6]:<3} | {emp[7]:<6} | {emp[8]:<6} | ${emp[9]:<11.2f}")

    print("="*110 + "\n")
    
def reporte_tipo_empleado(empleados):
    o_total=0
    e_total=0
    d_total=0
    for emp in empleados:
        tipo_emp=emp[3]
        if tipo_emp=="Obrero":
            o_total+=((emp[4]*emp[5])+(emp[6]*emp[7])+emp[8])
        elif tipo_emp=="Empleado":
            e_total+=((emp[4]*emp[5])+(emp[6]*emp[7])+emp[8])
        elif tipo_emp=="Directivo":
            d_total+=((emp[4]*emp[5])+(emp[6]*emp[7])+emp[8])
    print("--- Sueldos por tipo de empleado ---")
    print("-" * 45)
    print(f"{"Tipo de Empleado":<25} | {"Total":>15}")
    print("-" * 45)    
    print(f"{"Obrero":<25} | ${o_total:>14.3f}")
    print(f"{"Empleado":<25} | ${e_total:>14.3f}")
    print(f"{"Directivo":<25} | ${d_total:>14.3f}")
    print("-" * 45 + "\n")
    return

def reporte_nomina(empleados):
    total_nomina = sum((emp[4]*emp[5]) + (emp[6]*emp[7]) + emp[8] for emp in empleados)
    th_extras = sum(emp[6]*emp[7] for emp in empleados)
    bonos = sum(emp[8] for emp in empleados)
    print("---  Reporte de Nómina Total ---")
    print("-" * 45)
    print(f"{"Tipo":<25} | {"Total":>15}")
    print("-" * 45)
    print(f"{"Total de Nómina:":<25} | ${total_nomina:>14.3f}")
    print(f"{"Total de Horas Extra:":<25} | ${th_extras:>14.3f}")
    print(f"{"Total de Bonos:":<25} | ${bonos:>14.3f}")
    print("-" * 45 + "\n")
    return


def menu_principal():
    limpiar_pantalla()

    print("\n" + "="*50)
    print("  SISTEMA DE NÓMINA - ACEROS INDUSTRIALIZADOS")
    print("="*50)
    print("  --- OPERACIONES ---")
    print("  1. Modificar información")
    print("  2. Calcular sueldos")
    print("  3. Desplegar sueldos\n")

    print("  --- REPORTES ESTADÍSTICOS ---")
    print("  4. Sueldos por Departamentos")
    print("  5. Sueldos por tipo de Empleado")
    print("  6. Sueldos, Horas Extra y Bonos\n")

    print("  --- SISTEMA ---")
    print("  7. Salir")
    print("="*50)



while True:
    menu_principal()
    opcion = leer_entero("Selecciona una opción (1-7): ")
    if opcion == 1:
        limpiar_pantalla()
        modificar_info(empleados)
        input("Presiona culaquier tecla para continuar...")
    elif opcion == 2:
        limpiar_pantalla()
        calcular_sueldos(empleados)
        input("Presiona culaquier tecla para continuar...")
    elif opcion == 3:
        limpiar_pantalla()
        desplegar_sueldos(empleados)
        input("Presiona culaquier tecla para continuar...")
    elif opcion == 4:
        limpiar_pantalla()
        reporte_departamentos(empleados)
        input("Presiona culaquier tecla para continuar...")
    elif opcion == 5:
        limpiar_pantalla()
        reporte_tipo_empleado(empleados)
        input("Presiona culaquier tecla para continuar...")
    elif opcion == 6:
        limpiar_pantalla()
        reporte_nomina(empleados)
        input("Presiona culaquier tecla para continuar...")
    elif opcion == 7:
        limpiar_pantalla()
        print("\nCerrando el sistema. ¡Hasta luego!")
        time.sleep(2)
        limpiar_pantalla()
        break


