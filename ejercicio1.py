###Ejercicio 1

class Humano:
    def __init__(self,nombre,edad,estatura,ocupacion,ojo,pelo,nacimiento,):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.ocupacion = ocupacion
        self.ojo = ojo
        self.pelo = pelo
        self.nacimiento = nacimiento
        
        
        
        
       
### Método 1

    def presentar(self):
        presentacion = ("Hola soy {}, tengo {} años , mido {} ,mi ocupacion es {}, el color de mis ojos es {},el color de mi cabello es {}, nací en el año de {}")
        print(presentacion.format(self.nombre ,self.edad,self.estatura,self.ocupacion,self.ojo,self.pelo,self.nacimiento))
        
      
        
Marcos = Humano("Marcos",25,1.75,"vigilante","azul","castaño","1996")
Elisa = Humano("Elisa",37,1.50,"chancera","verdes","negro", "1984")

Marcos.presentar()
Elisa.presentar()
