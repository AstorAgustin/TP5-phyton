empleados = [
    {"id": 1, "nombre": "Mariano", "salario": 490000},
    {"id": 2, "nombre": "Alejandro", "salario": 3900000},
    {"id": 3, "nombre": "Cristian", "salario": 550000},
    {"id": 4, "nombre": "Celeste", "salario": 470000},
    {"id": 5, "nombre": "Esther", "salario": 650000}
]

f = open('empleados.txt', 'w')
for empleado in empleados:
    f.write(f"{empleado['id']},{empleado['nombre']},{empleado['salario']}\n")
f.close()

def cargar_empleados():
    lista_empleados = []
    f = open('empleados.txt', 'r')
    for line in f:
        id, nombre, salario = line.strip().split(',')
        lista_empleados.append({
            "id": int(id),
            "nombre": nombre,
            "salario": float(salario)
        })
    f.close()
    return lista_empleados

def modificar_salario(empleados, empleado_id, nuevo_salario):
    for empleado in empleados:
        if empleado['id'] == empleado_id:
            empleado['salario'] = nuevo_salario
            return True
    return False

def mostrar_empleados(empleados):
    for empleado in empleados:
        print(empleado)

if __name__ == "__main__":
    empleados = cargar_empleados()
    
    empleado_id = int(input("Ingrese el ID del empleado cuyo salario desea modificar: "))
    nuevo_salario = float(input("Ingrese el nuevo salario: "))
    
    if modificar_salario(empleados, empleado_id, nuevo_salario):
        f = open('empleados.txt', 'w')
        for empleado in empleados:
            f.write(f"{empleado['id']},{empleado['nombre']},{empleado['salario']}\n")
        f.close()
        
        print("Salario modificado exitosamente.")
    else:
        print("Error: El ID del empleado no existe.")
    
    print("\nLista de empleados actualizada:")
    mostrar_empleados(empleados)