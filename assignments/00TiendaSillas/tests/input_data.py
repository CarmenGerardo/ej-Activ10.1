# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["L", "F", "10"],
        ["Tipo silla: ", "Tipo cliente: ", "Cantidad de sillas: ",
        "Total sin dcto.  $15000.0", "Descuento        $ 3000.0", "Total a pagar    $12000.0"],
        '''Debe salir:T
        Total sin dcto.  $15000.0
        Descuento        $ 3000.0
        Total a pagar    $12000.0
        '''
    ),
    (
        ["L", "N", "10"],
        ["Tipo silla: ", "Tipo cliente: ", "Cantidad de sillas: ",
        "Total sin dcto.  $15000.0", "Descuento        $ 1500.0", "Total a pagar    $13500.0"],
        '''Debe salir:
        Total sin dcto.  $15000.0
        Descuento        $ 1500.0
        Total a pagar    $13500.0
        '''
    ),
    (
    ["E", "N", "10"],
    ["Tipo silla: ", "Tipo cliente: ", "Cantidad de sillas: ",
    "Total sin dcto.  $ 9000.0", "Descuento        $    0.0", "Total a pagar    $ 9000.0"],
    '''Debe salir:
    Total sin dcto.  $ 9000.0
    Descuento        $    0.0
    Total a pagar    $ 9000.0
    '''
    ),

    (
    ["B", "N", "30"],
    ["Tipo silla: ", "Tipo cliente: ", "Cantidad de sillas: ",
    "Total sin dcto.  $21000.0", "Descuento        $ 3150.0", "Total a pagar    $17850.0"],
    '''Debe salir:
        Total sin dcto.  $21000.0
        Descuento        $ 3150.0
        Total a pagar    $17850.0
    '''
    )
]
