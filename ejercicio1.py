def leer_numero():
    """
    Funcion que lee un numero entero y determina si el numero es par o impar.
    Si es par, escribe todos los pares de manera descendiente desde sí mismo y hasta el cero.
    Si es impar, escribe todos los impares de manera descendiente desde si sí mismo hasta el uno.
    """

    numero = int(input("LEER NUMERO: "))

    # Comprobamos si el numero es PAR o IMPAR
    if numero % 2 == 0: # si es par el resto es 0
        print(f"EL NUMERO {numero} ES PAR")
    else: # impar
        print(f"EL NUMERO {numero} ES IMPAR")

    print(f"***** LISTA DE NUMEROS DESCENDIENTE: *****")


    for i in range(numero,-1,-2):
        print(i)


leer_numero()
