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
        valor = input(mensaje).strip()
        if valor.isdigit():
            return int(valor)
        else: 
            print("\n[!] Error: Entrada inválida. Por favor, ingresa un número entero.")

def leer_flotante(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor.replace('.', '', 1).isdigit() and valor != ".":
            return float(valor)
        else:
            print("\n[!] Error: Entrada inválida. Ingresa un número válido (ej: 250 o 250.50).")

def leer_cadena(mensaje):
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("\n[!] Error: No puedes dejar este campo en blanco.")
            continue  
            
        if valor.replace(" ", "").isalpha():
            return valor.title()  
        else:
            print("\n[!] Error: Entrada inválida. Ingresa solo letras (sin números ni símbolos especiales).")


def imprimir_tabla(empleados):
    print("\n" + "=" * 105)
    print(f"{'ID':<4} | {'NOMBRE':<26} | {'DEPTO':<17} | {'DIAS':<4} | {'PAGO D.':<7} | {'HE':<3} | {'P.HE':<5} | {'BONO':<5}")
    print("-" * 105)
    for emp in empleados:
        print(f"{emp[0]:<4} | {emp[1]:<26} | {emp[2]:<17} | {emp[4]:<4} | {emp[5]:<7} | {emp[6]:<3} | {emp[7]:<5} | {emp[8]:<5}")
    print("=" * 105 + "\n")


def menu_principal():
    limpiar_pantalla()

    print("\n" + "=" * 50 + "\n" +
    f"{'SISTEMA DE NÓMINA - ACEROS INDUSTRIALIZADOS':^50}" +
    f"\n" + "=" * 50 + "\n" * 2 +
    f"{'OPERACIONES':-^50}" + "\n" +
    f"1. Modificar información" + "\n" +
    f"2. Calcular sueldos" + "\n" +
    f"3. Desplegar sueldos" + "\n" + "\n" +

    f"{'REPORTES ESTADÍSTICOS':-^50}" + "\n" +
    f"4. Sueldos por Departamentos" + "\n" +
    f"5. Sueldos por tipo de Empleado" + "\n" +
    f"6. Sueldos, Horas Extra y Bonos" + "\n"*2 +
    f"{'SISTEMA':-^50}" + "\n" +
    f"7. Salir" + "\n" +
    f"=" * 50 + "\n")


def desplegar_tabla(empleados):
    print("\n" + "=" * 110)
    print(f"{'ID':<4} | {'NOMBRE':<26} | {'DEPTO':<17} | {'DIAS':<4} | {'PAGO D.':<7} | {'HE':<3} | {'P.HE':<5} | {'BONO':<5} | {'SUELDO TOTAL'}")
    print("-" * 110)
    for emp in empleados:
        print(f"{emp[0]:<4} | {emp[1]:<26} | {emp[2]:<17} | {emp[4]:<4} | {emp[5]:<7} | {emp[6]:<3} | {emp[7]:<5} | {emp[8]:<5} | ${emp[9]:.2f}")
    print("=" * 110 + "\n")


def desplegar_datos_empleado(num):
    for emp in empleados:
        if emp[0] == num:
            print("\n" + "=" * 105)
            print(f"{'ID':<4} | {'NOMBRE':<26} | {'DEPTO':<17} | {'DIAS':<4} | {'PAGO D.':<7} | {'HE':<3} | {'P.HE':<5} | {'BONO':<5}")
            print("-" * 105)
            print(f"{emp[0]:<4} | {emp[1]:<26} | {emp[2]:<17} | {emp[4]:<4} | {emp[5]:<7} | {emp[6]:<3} | {emp[7]:<5} | {emp[8]:<5}")
            print("=" * 105 + "\n")


def calcular_sueldos(empleados):
    for emp in empleados:
        sueldo_total = (emp[4]*emp[5])+(emp[6]*emp[7])+emp[8]
        emp[9] = sueldo_total
    print("Se ha realizado el cálculo de los sueldos")
        


def buscar_empleado(empleados, numero):
    i=0
    while i<len(empleados):
        if empleados[i][0]==numero:
            return i
        i=i+1
    return -1


def modificar(empleados):
    desplegar_tabla(empleados)
    num=leer_entero("Ingrese el número del trabajador a modificar (Presione 0 para regresar): ")
    if num==0:
        limpiar_pantalla()
        print("Regresando al menú principal...")
        return
    pos=buscar_empleado(empleados, num)
    if pos==-1:
        print("No se encontró el empleado")
        input("Presiona cualquier tecla para reintentarlo...")
        limpiar_pantalla()
        modificar(empleados)
        return
    while True:
        limpiar_pantalla()
        desplegar_datos_empleado(num)
        print(f"\n" + "=" * 50 +
        f"\n" + f"{'MODIFICAR INFORMACIÓN':^50}" +
        f"\n" + "=" * 50 +
        f"\n" + "1. Número del trabajador" + 
        f"\n" + "2. Nombre del trabajador" +  
        f"\n" + "3. Departamento del trabajador" +
        f"\n" + "4. Tipo de empleado" +
        f"\n" + "5. Días trabajados" +
        f"\n" + "6. Pago por día" +
        f"\n" + "7. Horas extras" +
        f"\n" + "8. Pago por hora extra" +
        f"\n" + "9. Bono"+
        f"\n" + "10. Regresar al menú principal" +
        f"\n" + "=" * 50)
        opcion=leer_entero("Ingrese la opción a modificar: ")
        if opcion==10:
            break
        if opcion==1:
            var=leer_entero("Ingrese el nuevo número del trabajador: ")
            if var != num and buscar_empleado(empleados, var) != -1:
                print("Error: El número ingresado ya existe para otro trabajador.")
                input("Presiona cualquier tecla para intentar de nuevo...")
                continue
            if var == 0:
                print("Error: El número del trabajador no puede ser 0.")
                input("Presiona cualquier tecla para intentar de nuevo...")
                continue
            else:
                empleados[pos][0] = var
                num = var
        elif opcion==2:
            empleados[pos][1]=leer_cadena("Ingrese el nuevo nombre del trabajador: ")
        elif opcion==3:
            empleados[pos][2]=leer_cadena("Ingrese el nuevo departamento del trabajador: ")
        elif opcion==4:
            empleados[pos][3]=leer_cadena("Ingrese el nuevo tipo de empleado: ")
        elif opcion==5:
            empleados[pos][4]=leer_entero("Ingrese los nuevos días trabajados: ")
        elif opcion==6:
            empleados[pos][5]=leer_flotante("Ingrese el nuevo pago por día: ")
        elif opcion==7:
            empleados[pos][6]=leer_entero("Ingrese las nuevas horas extras: ")
        elif opcion==8:
            empleados[pos][7]=leer_flotante("Ingrese el nuevo pago por hora extra: ")
        elif opcion==9:
            empleados[pos][8]=leer_flotante("Ingrese el nuevo bono: ")
        else:
            print("Opción no válida, intente de nuevo.")


def reporte_departamentos(empleados):
    if empleados[0][9]>0:
        p_total=0
        v_total=0
        c_total=0
        r_total=0
        d_total=0
        for emp in empleados:
            sueldo_emp=emp[9]
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
        print(f"\n" + "=" * 50 +
        f"\n" + f"{'SUELDOS POR DEPARTAMENTO':^50}" +
        f"\n" + "=" * 50 + 
        f"\n {'Departamento':<25} {'Total':<15}" +
        f"\n" + "-" * 50 +
        f"\n {'Produccion':<25} ${p_total:>14.2f}" +
        f"\n {'Ventas':<25} ${v_total:>14.2f}" +
        f"\n {'Compras':<25} ${c_total:>14.2f}" +
        f"\n {'Recursos humanos':<25} ${r_total:>14.2f}" +
        f"\n {'Direccion':<25} ${d_total:>14.2f}" +
        f"\n" + "=" * 50 + "\n")

    else:
        print("Error, todavia no se han calculado los sueldos")

    

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

    print(f"\n" + "=" * 50 +
    f"\n" + f"{'SUELDOS POR TIPO DE EMPLEADO':^50}" +
    f"\n" + "=" * 50 +
    f"\n {'Tipo de Empleado':<35} {'Total':<15}" +
    f"\n" + "-" * 50 +
    f"\n {'Obrero':<30} ${o_total:>14.3f}" +
    f"\n {'Empleado':<30} ${e_total:>14.3f}" +
    f"\n {'Directivo':<30} ${d_total:>14.3f}" +
    f"\n" + "=" * 50 + "\n")
    return


def reporte_nomina(empleados):
    total_nomina = sum((emp[4]*emp[5]) + (emp[6]*emp[7]) + emp[8] for emp in empleados)
    th_extras = sum(emp[6]*emp[7] for emp in empleados)
    bonos = sum(emp[8] for emp in empleados)

    print(f"\n" + "=" * 50 + "\n" +
    f"{'REPORTE DE NÓMINA TOTAL':^50}" + "\n" +
    f"=" * 50 + "\n" +
    f"{'Tipo':<35} {'Total':<15}" + "\n" +
    f"-" * 50 + "\n" +
    f"{'Total de Nómina:':<30} ${total_nomina:>14.3f}" + "\n" +
    f"{'Total de Horas Extra:':<30} ${th_extras:>14.3f}" + "\n" +
    f"{'Total de Bonos:':<30} ${bonos:>14.3f}" + "\n" +
    f"=" * 50 + "\n")
    return


while True:
    menu_principal()
    opcion = leer_entero("\nSelecciona una opción (1-7): ")
    if opcion == 1:
        limpiar_pantalla()
        modificar(empleados)
        input("Presiona enter para continuar...")
    elif opcion == 2:
        limpiar_pantalla()
        calcular_sueldos(empleados)
        input("Presiona enter para continuar...")
    elif opcion == 3:
        limpiar_pantalla()
        desplegar_tabla(empleados)
        input("Presiona enter para continuar...")
    elif opcion == 4:
        limpiar_pantalla()
        reporte_departamentos(empleados)
        input("Presiona enter para continuar...")
    elif opcion == 5:
        limpiar_pantalla()
        reporte_tipo_empleado(empleados)
        input("Presiona enter para continuar...")
    elif opcion == 6:
        limpiar_pantalla()
        reporte_nomina(empleados)
        input("Presiona enter para continuar...")
    elif opcion == 7:
        limpiar_pantalla()
        print("\nCerrando el sistema. ¡Hasta luego!")
        time.sleep(2)
        limpiar_pantalla()
        break
    else:
        print("\n[!] Opción no válida. Por favor, selecciona una opción del 1 al 7.")
        input("Presiona enter para continuar...")
        