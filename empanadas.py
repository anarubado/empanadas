def pedir_nombre_cliente():
    return input("Ingrese su nombre: ")

def pedir_gusto_empanada():
    return input("Ingrese su gusto: ")

def pedir_empanadas(pedidos,gustos):
    key_nombre = pedir_nombre_cliente()
    while key_nombre != "":
        preferencias = {}
        key_gusto = pedir_gusto_empanada()
        while key_gusto != "":
            if key_gusto not in gustos:
                print("El gusto no esta disponible")
                key_gusto = pedir_gusto_empanada()
            else:
                cantidad = input("Ingrese cantidad de empanadas del gusto " + key_gusto + ": ")
                cantidad = int(cantidad)
                preferencias[key_gusto] = cantidad
                key_gusto = pedir_gusto_empanada()

        pedidos[key_nombre] = preferencias
        key_nombre = pedir_nombre_cliente()
    print(pedidos)

def pedir_opcion():
    return int(input("Ingrese opcion: "))

def main():
    pedidos = {}
    gustos = ["carne", "pollo", "atun", "verdura", "roquefort"]

    opcion = pedir_opcion()

    while opcion != 5:
        if opcion == 1:
            print("Pedido de empanaditis")
            pedir_empanadas(pedidos,gustos)
        elif opcion == 2:
            print("Agregado de gustos de empanadas")
            agregar_gusto(gustos)
            print(gustos)
        elif opcion == 3:
            print("Suma de empanadas")
            print(sumar_cantidad_cada_gusto(pedidos))
        elif opcion == 4:
            print("Precio de las empanadas")

            print(valorar_empanadas(pedidos))
        else:
            print("No existe tal opcion")
        opcion = pedir_opcion()

    print("Gracias por usar este softie!")

def agregar_gusto(gustos):
    gustos.append(pedir_gusto_empanada())

def sumar_cantidad_cada_gusto(pedidos):
    suma = {}
    preferencias = pedidos.values()
    for pedido in preferencias:
        for clave in pedido:
            if clave not in suma:
                suma[clave] = pedido[clave]
            else:
                suma[clave] += pedido[clave]
    return suma



def valorar_empanadas(pedidos):
    empas = sumar_cantidad_cada_gusto(pedidos)
    total = 0
    precio = 10
    for gusto in empas:
        total += empas[gusto]
    return "$" + str(total*precio)


main()



#promo



