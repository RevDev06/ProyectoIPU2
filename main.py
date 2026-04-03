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
    print(f"{"Produccion":<25} | ${p_total:>14f}")
    print(f"{"Ventas":<25} | ${v_total:>14f}")
    print(f"{"Compras":<25} | ${c_total:>14f}")
    print(f"{"Recursos humanos":<25} | ${r_total:>14f}")
    print(f"{"Direccion":<25} | ${d_total:>14f}")
    print("-" * 45 + "\n")

imprimir_tabla(empleados)
reporte_departamentos(empleados)