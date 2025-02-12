import random

def leer_personas(numero_personas):
    """
    Genera una lista del numero de personas recibido como parametro, que será 50.
    Cada elemento de la lista será un diccionario con datos aleatorios de cada persona.
    Cada persona tiene un 'sexo' ('F' o 'M') y una 'edad' (entre 0 y 100 años).
    """
    personas = []
    for i in range(numero_personas):
        persona = {
            "sexo": random.choice(["F", "M"]),
            "edad": random.randint(0, 100)
        }
        personas.append(persona)
    
    return personas


def clasificacion_personas():
    """
    Algoritmo que visualice una clasificación de 50 personas según edad y sexo. Deberá mostrar los siguientes resultados: 
    
    mayores_edad:           Cantidad de personas mayores de edad (18 años o más).
    menores_edad:           Cantidad de personas menores de edad.
    masculinos_mayores:     Cantidad de personas masculinas mayores de edad.
    femeninas_menores:      Cantidad de personas femeninas menores de edad.
    p_mayores_edad:         Porcentaje que representan las personas mayores de edad respecto al total de personas.
    p_femeninas_total:      Porcentaje que representan las mujeres respecto al total de personas.
    """

    personas = leer_personas(50)  # Generamos los datos aleatoriamente para 50 personas
    print("***** PERSONAS *****")
    print(personas)

    # Contadores
    mayores_edad = 0
    menores_edad = 0
    masculinos_mayores = 0
    femeninas_menores = 0
    total_femeninas = 0

    for persona in personas: # chequeamos las condiciones

        # Contar total de mujeres
        if persona["sexo"] == 'F':
            total_femeninas += 1
    
        # Contar mayores y menores de edad
        if persona["edad"] >= 18: 
            mayores_edad += 1
            if persona["sexo"] == 'M':
                masculinos_mayores +=1
        else:
            menores_edad +=1
            if persona["sexo"] == 'F':
                femeninas_menores +=1

    total_personas = len(personas)

    # calculamos los porcentajes
    p_mayores_edad = (mayores_edad / total_personas) * 100
    p_femeninas_total = (total_femeninas / total_personas) * 100

    # Mostrar resultados
    print("***** RESULTADOS: *****")
    print(f"a. Cantidad de personas mayores de edad (18 años o más): {mayores_edad}")
    print(f"b. Cantidad de personas menores de edad: {menores_edad}")
    print(f"c. Cantidad de personas masculinas mayores de edad: {masculinos_mayores}")
    print(f"d. Cantidad de personas femeninas menores de edad: {femeninas_menores}")
    print(f"e. Porcentaje que representan las personas mayores de edad respecto al total de personas: {p_mayores_edad}%")
    print(f"f. Porcentaje que representan las mujeres respecto al total de personas: {p_femeninas_total}%")
  

clasificacion_personas()