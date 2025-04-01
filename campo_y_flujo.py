def flujo_electrico():
    cantidad_cargas = int(input("Ingrese la cantidad de cargas: "))
    cargas =  []
    carga_neta = 0
    for i in cantidad_cargas :
        carga = float(input("Ingrese su carga numero", i+1))
        cargas.append(carga)
    for i in cargas :
        carga_neta += i
    
    print("Flujo electrico: ",carga_neta / 8.85e-12)


def campo_electrico(q, d) :
    print("E = ",(9e9*q)/d**2)


print("Que desea hacer?")
print()
print()
print("Calcular flujo electrico -> 1")
print()
print("Calcular Campo electriico -> 2")
print()
option = int(input())
if option == 1 :
    flujo_electrico()
else:
    q = int(input("Ingrese su carga (q): "))
    d = int(input("Ingrese la distancia (r): "))
    campo_electrico(q, d)