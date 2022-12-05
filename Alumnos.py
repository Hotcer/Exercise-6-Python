class Alumnos:
    nombre = 'David Gonzalez'
    notas = 12

    def resultado(self):
        if self.notas >= 10:
            print('Aprobado el Alumno', self.nombre, 'con una calificacion de ', self.notas, 'puntos')


A = Alumnos()
A.resultado()
