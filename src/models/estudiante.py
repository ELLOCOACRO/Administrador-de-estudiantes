from .models_helpers import generar_id
from DB.estudiantes import estudiantes
"""
Modelos y objetos aqui
"""



class Estudiante:

    def __init__(self,*,  nombre: str, edad: int,  calificaciones : list[int | float]):
        self.id = generar_id()
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones
        self.promedio = sum(calificaciones) / len(calificaciones)


    def save(self):
        """
        Método para guardar
        el estudiante en la "Base de datos" (lista en memoria)
        
        """

        estudiantes.append(
        {
        'id': self.id,
        "nombre": self.nombre,
        'edad': self.edad,
        "calificaciones": self.calificaciones,
        "promedio": self.promedio,
        }
        )


    


#Codigo de prueba
if __name__ == "__main__":

    #Crear estudiante
    estudiante = Estudiante(nombre="erick", calificaciones=[56, 44.6, 77], edad=48)

    print("Ultimo estudiante: " + str(estudiantes[-1]))#Imprimir el ultimo estudiante almacenado
    estudiante.save()#Guardamos el estudiante creado

    print("Ultimo estudiante: " + str(estudiantes[-1]))#volvemos a imprimir el ultimo estudiante almacenado

    estudiante.delete()#borramos el estudiante creado

    print("ultimo: " + str(estudiantes[-1]))#Imprimimos de nuevo el ultimo estudiante almacenado