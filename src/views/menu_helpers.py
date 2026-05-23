from rich.panel import Panel
from src.console import console
from rich.align import Align
from DB.estudiantes import estudiantes

def panel_opciones(
    *,

    #Propiedades del encabezado
    titulo : str, # None o String
    posicion_titulo : str = "center", #"left", "right" o "center",
    subtitulo : str = None, # None o Strings

    #propiedades del cuerpo
    opciones : list[str],
    centrar_opciones : bool = True,

    

    #Propiedades del panel
    color_borde : str = "cyan", #En minuscula, un color basico y que exista
    tamano : int = 70, #De 0 a 100 (representa puntos porcentuales)
    padding : tuple = (0, 0)
):
    
    """
    Generadora del panel de opciones; Renderiza una 'caja' con el menú de opciones
    """

    console.print(
        Align.center(
            Panel(
            title= f"{titulo}",
            title_align= posicion_titulo,

            renderable=  Align.center('\n'.join(opciones)) if centrar_opciones else '\n'.join(opciones),
            padding= padding,
            border_style= color_borde,
            width= tamano,
            )
        ),
    )



#Pedir campos al usuario


def pedir_nombre():

    """
    Pide el nombre al usuario, aplica validaciones, y retorna el nombre y el estado de la respuesta
    """

    nombre = None
    respuesta = "ok"

    
    
    while True:#Le pedira el campo nombre al usuario mientras el contenido sea menor a 5 caracteres
            
            nombre = console.input("[blue]      Nombre Completo: ")

            if nombre == "":#Si el usuario ingresa <<Enter>> retorna "volver"
                respuesta = "retroceder menu"
                break

            if len(nombre.strip()) < 5:
                console.print("[red]Error, el nombre debe tener un minimo de 5 caracteres[/]", justify="center")

            else:
                break
          


    return respuesta, nombre



def pedir_edad():
        
        """
        Pide la edad al usuario y aplica ciertas validaciones,
        retorna el estado de respuesta y la edad
        """

        respuesta = "ok"
        edad = None

        while type(edad) != int:#While para pedir constantemente el campo hasta que se cumplan las validaciones

            edad = console.input("[blue]      Edad: ", )#Pide edad al usuario

            if edad == "":#Si el usuario oprime <<Enter>> Volver al menu principal
                respuesta = "retroceder menu"
                break
            

            try:

                edad = int(edad)#Convierte edad a entero

            except ValueError:

                console.print("[red]Error, solo se permiten numeros enteros", justify="center")
                continue


        return respuesta, edad

            



def pedir_calificaciones():

    """
    Pide 4 calificaciones al usuario y aplica ciertas validaciones,
    retorna el estado de la respuesta y una lista de calificaciones
    """

    calificaciones = []#lista de calificaciones
    respuesta = "ok"

        #Pedimos las 4 calificaciones con un bucle for

    for i in range(1, 5):
        


        while True:#While para pedir constantemente el campo hasta que se cumplan las validaciones

            
            calificacion = console.input(f"[blue]      Calificacion {i}: ")#pedimos calificacion al usuario

            if calificacion == "":#salir del menu si se presiona enter
                respuesta = "retroceder menu"
                break
            

            try:

                calificacion = float(calificacion)#convertir calificacion a float


            except ValueError:

                console.print("[red]Error, solo se permiten valores numericos[/]", justify="center")
                continue


            if calificacion < 0 or calificacion > 100:#Valida si esta dentro del rango

                console.print("[red]Error, calificacion fuera del rango requerido [green](0-100)[/][/]", justify="center")
                continue


            #Agregamos la calificacion al final de la lista
            calificaciones.append(calificacion)
            break


        if respuesta == "retroceder menu":
            break

    
    return respuesta, calificaciones


            
        
    
    