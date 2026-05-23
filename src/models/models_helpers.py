from DB.estudiantes import estudiantes

def generar_id():

    """
    Genera un id 
    no existente
    """
    id = max(e['id'] for e in estudiantes) + 1 if estudiantes else 0

    return id

