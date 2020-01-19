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
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        else:
            print("No existe tal opcion")
        opcion = pedir_opcion()

    print("Gracias por usar este softie!")

#suma de empanadas de cada gusto por pedido


#calcular precio de empanadas

#promo



main()