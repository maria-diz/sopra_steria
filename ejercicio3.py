def calcula_salario():
    """
    Cálculo del salario de un trabajador. Calcular el sueldo recibido por el trabajador en base las horas trabajadas y la tarifa. 
    """

    # Leer horas trabajadas y tarifa
    horas_trabajadas = float(input("LEER HORASTRABAJADAS: "))
    tarifa = float(input("LEER TARIFA: "))

    limite_horas_trabajadas = 40

    salario = tarifa * horas_trabajadas # calculamos salario total
    horas_extra = 0
    if horas_trabajadas > limite_horas_trabajadas: 
        horas_extra = horas_trabajadas - limite_horas_trabajadas # conseguimos las horas extra
        salario = (limite_horas_trabajadas * tarifa) + (horas_extra * (tarifa * 1.5)) # calculamos el salario sumando las horas extras a un tarifa incrementada en 50%
    
    print(f"El salario recibido por el trabajador es {salario}€")


calcula_salario()
