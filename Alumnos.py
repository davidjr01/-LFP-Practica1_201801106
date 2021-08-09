class Alumno:
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
        

    def getNombre(self):
        return self.nombre
    def getNota(self):
        return self.nota

    def setNombre(self,nombre):
        self.nombre=nombre
    
    def setNota(self,nota):
        self.nota=nota