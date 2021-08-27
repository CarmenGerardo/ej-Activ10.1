![Tec de Monterrey](../../images/logotecmty.png)
# Tienda de Sillas

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

En una tienda de sillas para oficina se venden de 3 tipos: básica, estándar y de lujo.
Además existen los clientes normales y los clientes frecuentes.

El precio de las sillas es:
- Básica $700.00 c/u
- Estándar $900.00 c/u
- De Lujo $1,500.00 c/u

El dueño de la tienda ha decidido dar un descuento del 20% a los <b>clientes frecuentes</b>

Además ha decidido aplicar la siguiente política de descuentos por mayoreo a los
<b> clientes normales </b>:
- si su compra es >= $10,000 y < $20,000 un 10% de descuento
- si su compra es >= $20,000 un 15% de descuento

Escribe un programa que lea el tipo de silla (que es una letra mayúscula que puede ser B, E, L),
el tipo de cliente (que es una letra mayúscula que puede ser F o N) y
la cantidad a comprar (que es un número entero).  Supón que solo se va a comprar de un tipo de silla.

####  El programa debe tener las siguientes funciones:
- Función llamada  precio_antes_descuento que recibe como parámetros: tipo_silla y la cantidad:
La función retorna el total incial, antes del descuento.
- Función llamada calcula_descuento que recibe como parámetros: el total inicial y el tipo_cliente:
La función retorna el monto del descuento.

El programa debe calcular y mostrar los siguientes datos (todos los datos son flotantes y debes mostrar uno en cada renglón):
- El total inicial, antes de aplicar descuento
- La cantidad de dinero que se otorga por descuento y
- El total a pagar por el cliente.

La salida del programa debe de ser exactamente de la siguiente forma:

```
Tipo silla: L
Tipo cliente: F
Cantidad de sillas: 10
Total sin dcto.  $15000.0
Descuento        $ 3000.0
Total a pagar    $12000.0


Tipo silla: L
Tipo cliente: N
Cantidad de sillas: 10
Total sin dcto.  $15000.0
Descuento        $ 1500.0
Total a pagar    $13500.0


Tipo silla: E
Tipo cliente: N
Cantidad de sillas: 10
Total sin dcto.  $ 9000.0
Descuento        $    0.0
Total a pagar    $ 9000.0


Tipo silla: B
Tipo cliente: N
Cantidad de sillas: 30
Total sin dcto.  $21000.0
Descuento        $ 3150.0
Total a pagar    $17850.0

```

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
