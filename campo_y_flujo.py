import numpy
def scientific_notation(num) :
   return numpy.format_float_scientific(num, 2)

def flujo_electrico():
    cantidad_cargas = int(input("Ingrese la cantidad de cargas: "))
    cargas =  []
    carga_neta = 0
    for i in range(cantidad_cargas) :
        carga = float(input(f"Ingrese su carga número {i + 1}: "))
        cargas.append(carga)
    for i in cargas :
        carga_neta += i
    
    print("Flujo electrico: ",scientific_notation(carga_neta / 8.85e-12))


def campo_electrico(q, d) :
    print("E = ",scientific_notation((9e9*q)/d**2))

print()
print()
print("Que desea hacer?")
print()
print("Calcular flujo electrico -> 1")
print()
print("Calcular Campo electriico -> 2")
print()
option = int(input("INGRESE SU OPCION: "))
if option == 1 :
    flujo_electrico()
elif option == 2:
    q = float(input("Ingrese su carga (q): "))
    d = float(input("Ingrese la distancia (r): "))
    campo_electrico(q, d)