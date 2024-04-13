'''
### **Ejercicio 6**

Las plataformas de música online como ***YouTube*** y ***Spotify*** almacenan la 
información asociada a las canciones en estructuras de datos complejas para hacer las búsquedas de manera eficiente. 
Para esto se deben modelar las canciones. Implementar el TDA "Cancion" con los siguientes componentes:
- Nombre
- Artista
- Duración
- Género musical (6 posibles: Rock, Jazz, Blues, Funk, Reggae y Rap).
- Año de edición
- Número de likes

Implementar las siguientes operaciones:
- Constructor: Debe incluir las validaciones necesarias.
- __repr__: Al usar la función *print* con una variable del tipo canción debe mostrar: **'nombre' - 'artista' ('duracion')**.
- mayorDuracion: Operación que recibe dos canciones por parámetros y retorna la de mayor duración.
- agregaLikes: Operación que recibe un número e incrementa la cantidad de likes de la canción en ese número.
- masVotada: Operacion que recibe dos canciones y sin son del mismo artista y del mismo género musical, retorna la que 
tiene mayor cantidad de likes. En caso contrario debe lanzar una excepción.
'''
import Ejercicio_3, Validadores
listaGeneros = ["rock", "jazz", "blues", "funk", "reggae", "rap"]

def validarGenero(genero:str, varName:str ):
    if genero.lower() in listaGeneros:
        return genero
    else:
        raise Exception(f"El valor de {varName} no es un género válido.")



class Cancion:
    def __init__(self, nombre:str, artista:str, duracion:Ejercicio_3.Tiempo, generoMusical, anioEdicion:int, numLikes:int) -> None:
        self.__nombre = Validadores.validarStrVacia(nombre, "nombre")
        self.__artista = Validadores.validarStrVacia(artista, "artista")
        self.__duracion = Validadores.validarTipo(duracion, Ejercicio_3.Tiempo, "duracion") #Es un dato del clase Tiempo
        self.__generoMusical = validarGenero(generoMusical, "generoMusial")
        self.__anioEdicion = Validadores.validarNatural(anioEdicion, "anioEdicion")
        self.__numLikes = Validadores.validarNatural(numLikes, "numLikes")
    
    def __repr__(self) -> str:
        return f"{self.__nombre} - {self.__artista} ({self.__duracion})"
    
    def mayorDuracion(cancion1, cancion2):
        return cancion1 if cancion1.__duracion.tiempoASegundos() > cancion2.__duracion.tiempoASegundos() else cancion2

    def agregaLikes(self, likes:int):
        self.__numLikes += Validadores.validarNatural(likes, "likes")
    
    def masVotada(cancion1, cancion2):
        if(cancion1.__artista == cancion2.__artista and cancion1.__generoMusical == cancion2.__generoMusical ):
            return cancion1 if cancion1.__numLikes > cancion2.__numLikes else cancion2
        else:
            raise Exception(f"Las canciones no comparten genero y artista")

cancionPrueba1 = Cancion(
    "Medallo", "Blessd", Ejercicio_3.Tiempo(0,3,54),"rap", 2021, 5000
)
cancionPrueba2 = Cancion(
    "Chulo", "Young Miko", Ejercicio_3.Tiempo(0,3,39),"rap", 2024, 7000
)
cancionPrueba3 = Cancion(
    "Despechá", "Blessd", Ejercicio_3.Tiempo(0, 2, 37), "rap", 2022, 3000
)
print(cancionPrueba1)
print(Cancion.mayorDuracion(cancionPrueba3, cancionPrueba2))
print(Cancion.masVotada(cancionPrueba1, cancionPrueba3))
    


