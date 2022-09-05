#booleans
boolean = #true o false

#numerales
num =10
fl = 10.99
#parseInt() el texto lo convierte en enter.. Round para redondear
nuevo_float = float(num)
numero_entero = int(fl)

print(nuevo_float)
nuevo_entero = int(fl)

print(nuevo_float)
print(nuevo_entero)
print(round(fl)) #round(numero) redondeamos

import random #Importamos una librería llamada random
num_aleatorio = random.randint(2, 5) #Número aleatorio entre 2 y 5

#Cadenas o TEXTOS O STRING
string = "ABCDEFG"
print("Este es el alfabeto", string) #La coma en automatico me va a agregar un espacio 
print("Este es el lfabeto"+string) #El + concatena las cadenas tal cual
print("Este es un numero", 10)
print("Este es un numero", 10)
#print(" Este es un numero"+10)
print("Este es un numero "+str(10)) #str(10)-> "10"
print(f"Este es el alfabato{string}")
print("les presento a{nombre}, le pueden llamar '{apodo}'")

#metodos que nos pueden servir
string2 = "hola mundo! soy Priscila Espinoza y hoy es 5 de Septiembre"
print(string2.title()) #primera letra de cada letra sera mayuscula
print(string2.upper()) #todas las letras seran en mayuscula
print(string2.lower()) #todas minúsculas
print(string2.count('oy')) #regresa cuántos 'oy' hay en la cadena
string3 = "Elena!Juana!Pablo!Pedro"
print(string3.split('!')) #Enlistas y dividir mi cadena por cada '!' que haya
print(string2.find('elena')) #Devuelve dónde comienza 'Elena'. Regresa -1 es que NO LO ENCONTRÓ. Case-sensitive

#LISTAS / ARRAY / ARREGLO
lista_vacia = []
lista_llena = ["Hugo", "Paco", "Luis"] #0-> Hugo; 1-> Paco; 2-> Luis
print(lista_llena[2])
lista_llena[2] = "Donald"
print(lista_llena)
lista_llena.pop() #Elimina el último dato de mi lista
print(lista_llena)
lista_llena.pop(0) #Elimina el dato en la posición indicada
print(lista_llena)
lista_llena.append("Mickey") #Me agrega un dato al final de mi lista
print(lista_llena)

lista_mix = ["Texto1", "Texto2", 1, False, ["Lista1", "Lista2"] ] #Podemos guardar distintos tipos de valores
lista_nombres = ["Elena", "Juana", "Pedro"]
nuevo_lista = lista_llena + lista_nombres
print(nuevo_lista)


#DICCIONARIOS -> Objetos en Javascript
diccionario_vacio = {}
diccionario = {"nombre": "Elena", "edad":30, "soltera": False, "hobbies": ["leer", "comer", "ver tele"]}
diccionario['estatura'] = 1.67
print(diccionario)
diccionario.pop('estatura') #Eliminamos por completo la propiedad
print(diccionario)
edad = diccionario.pop('edad') #Eliminamos de diccionario esa propiedad Y el valor lo asignamos a la variable
print(diccionario)
print(edad)

lista_alumnas = [
    {"nombre": "Elena", "apellido": "De Troya", "id": 123, "cursos": ["Fundamentos de la Web", "Python"]},
    {"nombre": "Juana", "apellido": "De Arco", "id": 234, "cursos": ["Fundamentos de la Web", "Python", "MERN"]},
    {"nombre": "Pedro", "apellido": "Páramo", "id": 345, "cursos": ["Fundamentos de la Web", "Python", "MERN", "Java"]}
]

#¿Cómo eliminamos de la lista de cursos de Pedro MERN?
lista_alumnas[2]["cursos"].pop(2)
from pprint import pprint #Bonitas nuestras impresiones
print(lista_alumnas)
