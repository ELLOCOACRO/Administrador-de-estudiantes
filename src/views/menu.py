
from src.console import console
from rich.table import Table
from rich.align import Align
from src.models.estudiante import Estudiante
from DB.estudiantes import estudiantes
from .menu_helpers import panel_opciones, pedir_nombre, pedir_edad, pedir_calificaciones



"""
Menu's y procesado de las entradas
"""



def main_menu():


    """
    Muestra el panel principal, pide y procesa la entrada del usuario y redirecciona al menu seleccionado
    
    """
    opcion_invalida_flag = False#Bandera para saber si el usuario ingreso una opcion invalida

    while True:
        console.clear()

        
    
        #Mostrar el panel de opciones
        panel_opciones(titulo= "[cyan bold]Administrador De Estudiantes[/cyan bold]", opciones=[
            "1- [blue]Ver estudiantes[/] ","2- [green]Agregar estudiante[/]",
            "3- [red]Borrar estudiante[/]","4- [yellow]Modificar estudiante[/]",
            "5- [white]Salir del programa[/]"
        ])

     
        if opcion_invalida_flag:#Si la bandera esta activa poner el sigte mensaje justo despues del panel de opciones

            console.print("[yellow]Opcion invalida o fuera del rango definido [green](1-5)[/][/]", justify="center")

        opcion_invalida_flag = False#Resetear bandera



        #Pedir entrada al usuario
        
        opcion = input("      >>")#Disculpen la forma tan fea de alinear este input XD
        #Procesar entrada del usuario
        match opcion:
            case '1':
                mostrar_estudiantes()
            case '2':
                agregar_estudiante()
            case '3':
                borrar_estudiante()
            case '4':
                modificar_estudiante()
                
            case '5':
                console.print("[yellow]Programa finalizado[/]", justify="center" )
                break

            case _:#En caso de que no se elija una opcion valida, activar la bandera de opcion invalida
                opcion_invalida_flag = True
                continue

        


def mostrar_estudiantes():
    """
    Muestra la tabla de los estudiantes
    """


    tabla = Table(title="[blue]Estudiantes[/]", width=80)
    tabla.add_column("ID")
    tabla.add_column("Nombre")
    tabla.add_column("Edad")
    tabla.add_column("Calificaciones")
    tabla.add_column("Promedio")
    for estudiante in estudiantes:
        # Calcular promedio dinamicamente
        calificaciones = estudiante['calificaciones']
        promedio = sum(calificaciones) / len(calificaciones) if calificaciones else 0
        tabla.add_row(str(estudiante['id']),
        str(estudiante['nombre']),
        str(estudiante['edad']),
        str(estudiante['calificaciones']),
        f"{promedio:.2f}",
        )
    console.clear()

    #Mostrar el panel de opciones(unica opcion la de volver de menu)
    panel_opciones(titulo= "[cyan bold]<<Estudiantes>>[/cyan bold]", opciones=[
        "[yellow]<<ENTER>>[/]- [red]Volver[/]",
    ])
    console.print(Align.center(tabla))
    #Congelar menu hasta que el usuario haga alguna accion
    opcion = input("      >>")
    


def agregar_estudiante():


    """
    Renderiza el formulario de creacion de un estudiante,
    aplica validaciones a cada campo y por ultimo crea un nuevo estudiante
    con los datos dados y lo guarda
    
    """

    while True:
        console.clear()#Centramos el menu

        #Mostrar el panel de opciones
        panel_opciones(titulo= "[green bold]<<Agregar estudiante>>[/green bold]", opciones=[
                "[yellow]<<ENTER>>[/]- [red]Cancelar[/]",
            ])


        """
        Pedir campos al usuario
        """

        #pedir nombre
        respuesta,nombre = pedir_nombre()

        if respuesta == "retroceder menu":
            return


        #Edad
        respuesta, edad = pedir_edad()

        if respuesta == "retroceder menu":
            return
        


        #calificaciones
        respuesta, calificaciones = pedir_calificaciones()

        if respuesta == "retroceder menu":
            return
        


        estudiante = Estudiante(nombre=nombre, edad=edad, calificaciones=calificaciones)#Instanciamos un estudiante

        estudiante.save()#lo guardamos en la lista de estudiantes

        console.print("[green]Estudiante agregado con exito[/]", justify="center")
        console.input("[yellow]                         <<ENTER>>[/]- Para volver al menu principal")
        break





def borrar_estudiante():

    """
    Renderiza el menu de borrar estudiante,
    recibe un id del usuario y realiza la filtracion,
    pedira una confirmacion para borrar el estudiante
    """
    while True:
        console.clear()

        panel_opciones(titulo= "[red bold]<<Borrar estudiante>>[/red bold]", opciones=[
                "[yellow]<<ENTER>>[/]- [red]Volver al menu[/]",
            ])


        while True: #Bucle para pedir el id de nuevo cada que falle una validacion

            estudiante_id = console.input("[blue]      ID del estudiante a borrar: ") #Pide al usuario el id del estudiante a borrar


            if estudiante_id == "":#Filtro por si ingresa <<enter>>, para que lo lleve al menu principal
                break



            try:#Convierte lo ingresado a int, si falla la conversion saca "IdInvalidoError"

                estudiante_id = int(estudiante_id)
                estudiante_a_borrar = None #Contendra el diccionario del estudiante a borrar 

            except ValueError:
                console.print("[red]Error, el ID solo contiene valores enteros[/]", justify="center")
                continue


            #Iteramos la lista de estudiantes
            for estudiante in estudiantes:

                if estudiante["id"] == estudiante_id:#Si el id coincide guardarlo en la variable "estudianteAborrar" y seguir salir del bucle
                    estudiante_a_borrar = estudiante
                    break


            else:#Si ningun id coincide dar mensaje al usuario y pedir otro ID
                console.print("[yellow]Estudiante no encontrado[/]", justify="center")
                continue


        #pedir al usuario una verificacion para borrar al estudiante


            while True:
                opcion = console.input(f"[gray]      ¿Deseas borrar al estudiante [italic cyan]{estudiante_a_borrar['nombre']}[/]?[/] [yellow](s/n)[/]:")


                match opcion.lower():

                    case 's':#Si el usuario ingresa "s", borra el estudiante,
                        estudiantes.remove(estudiante_a_borrar)
                        console.print("[green]Estudiante borrado con exito", justify="center")
                        console.print("(Presiona [yellow]<<ENTER>>[/] para continuar)", justify="center")
                        input()
                        break

                    case 'n':#si ingresa "n", finaliza el menu sin hacer nada,
                        break

                    case _:#Si ingresa algo distinto a las opciones anteriores, lanzara "opcionInvalidaError"
                        continue

        break







def modificar_estudiante():

   
    """
    Renderiza el menu de borrar estudiante,
    recibe un id del usuario y preguntara por los campos a
    modificar
    """
    
    while True:
        console.clear()

        panel_opciones(titulo= "[yellow bold]<<Modificar estudiante>>[/yellow bold]", opciones=[
                "[yellow]<<ENTER>>[/]- [red]Retroceder[/]",
            ])
        


        while True:#El bucle para pedir de nuevo el ID cada que no se cumpla una validacion

            estudiante_id = console.input("[blue]      ID del estudiante a Modificar: ") #Pide al usuario el id del estudiante a borrar


            if estudiante_id == "":#Filtro por si ingresa <<enter>>, para que lo lleve al menu principal
                return


            #Convierte lo ingresado a int, si falla la conversion da un mensaje de error y vuelve a pedir el campo, si todo sale bien, continua con la busqueda
            try:

                estudiante_id = int(estudiante_id)
                estudiante_a_modificar = None #Contendra el diccionario del estudiante a borrar 

            except ValueError:
                console.print("[red]Error, [italic]ID solo puede ser un numero entero[/]", justify="center")
                continue

              

            #Iteramos la lista de estudiantes para buscar el estudiante
            for estudiante in estudiantes:

                if estudiante["id"] == estudiante_id:#Si el id coincide guardarlo en la variable "estudianteAborrar" y continuar con el menu de modificacion
                    estudiante_a_modificar = estudiante
                    break


            else:#Si ningun id coincide dar mensaje al usuario y finalizar ejecucion del menu
                console.print("[yellow]Estudiante no encontrado[/]", justify="center")
                continue

        
            break





        #Menu de modificación de campo de estudiante

        while True:
            console.clear()
            panel_opciones(titulo= f"[yellow bold]<<Modificar datos de [cyan italic]{estudiante['nombre']} [/]>>[/yellow bold]", opciones=[
                    f"1- Nombre: {estudiante['nombre']}",
                    f"2- Edad: {estudiante['edad']}",
                    f"3- Calificaciones: {estudiante['calificaciones']}",
                    f"[yellow]<<ENTER>>[/]- [red]Retroceder[/]",
                ])
            opcion = console.input("      >>")



            match opcion:

                #Nombre
                case "1":
                       
                    respuesta, nombre = pedir_nombre()

                    if respuesta == "retroceder menu":
                        continue 
                    
                    while True: 
                        #Pedir confirmacion al usuario de si desea modificar el campo
                        opcion = console.input(f"[gray]      modificar  nombre? [yellow](s/n)[/][/]:")

                        match opcion:

                            case "s":
                                estudiante_a_modificar['nombre'] = nombre
                                break

                            case "n":
                                break

                            case _:
                                continue
                        


                           
        


                #edad
                case '2':
                    respuesta, edad = pedir_edad()

                    if respuesta == "retroceder menu":
                        continue
                     
                    
                    #Pedir confirmacion al usuario de si desea modificar el camp
                    while True:

                        opcion = console.input(f"[gray]      modificar  edad? [yellow](s/n)[/][/]")
                        match opcion:
                            case "s":
                                estudiante_a_modificar["edad"] = edad
                                break
                            case "n":
                                break
                            case _:
                                continue
                    
                        break

                            
                            
                    

                #Calificaciones
                case '3':
                    
                    respuesta, calificaciones = pedir_calificaciones()

                    if respuesta == "retroceder menu":
                        continue

                    #Pedir confirmacion de modificacion al usuario
                    while True:

                        opcion = console.input(f"[gray]      modificar  calificaciones? [yellow](s/n)[/][/]")

                        match opcion:

                            case "s":
                                

                                estudiante_a_modificar['calificaciones'] = calificaciones

                                break


                            case "n":
                                break
                                

                            case _:
                                continue

                   
                            
                               
                                
                    
                case "":
                    break

                case _:
                    continue