def precio_antes_descuento(tipo_silla, cantidad) :
    # Agrega aquí el código de la funcion
    pass

def calcula_descuento(precio, tipo_cl) :
    # Agrega aquí el código de la funcion
    pass

def main() :
    # pido el tipo de silla (B E L)
    tipo_silla = input("Tipo silla: ")
    # pido el tipo de cliente (N F)
    tipo_cl = input("Tipo cliente: ")
    cantidad = int(input("Cantidad de sillas: "))

    subtotal = # Calcula el precio antes del descuento
    desc = # Calcula del descuento
    total = # Calcula el total a pagar

    print(f"Total sin dcto.  ${subtotal:>7}")
    print(f"Descuento        ${desc:>7}")
    print(f"Total a pagar    ${total:>7}")

if __name__=='__main__':
    main()
