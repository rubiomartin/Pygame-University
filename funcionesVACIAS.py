from principal import *
from configuracion import *
from funcionesSeparador import *
from extras import *
import random
import math

def lectura(archivo, salida):
    with archivo as txt:  #Abre el archivo que contiene el lemario.txt.
        for lineas in txt:    #Recorre cada palabra del lemario.
            salida.extend(lineas.split()) #Agrega cada palabra a una lista y le borra el espacio.

def nuevaPalabra(lista):
    azar = random.choice(lista) #Elije una palabra al azar de la lista.
    while "ñ" in azar or len(azar)<=1:
        azar = random.choice(lista)
    return azar #Retorna la palabra al azar.

def silabasTOpalabra(silaba):
    palabraSinGuiones = ""  #Nueva variable para la palabra transformada.
    for caracter in silaba:  #Recorro cada caracter de la palabra.
        if caracter == "-":  #Si el caracter es un - lo reemplaza por un espacio
            palabraSinGuiones += " "
        else:
            palabraSinGuiones += caracter #Si no entra es por que es una letra.
    return palabraSinGuiones #Retorna la nueva palabra.

def palabraTOsilaba(palabra):
    palabraSeparadaEnSilabas = separador(palabra) #Llamo a la funcion separador, para separar la palabra en silabas.
    return palabraSeparadaEnSilabas #Retorno la palabra separada en silabras.

def esCorrecta(palabraEnSilabasEnPantalla, palabra):
    palabraSinAgregados = silabasTOpalabra(palabraEnSilabasEnPantalla).lower()
    palabraOriginalSinAgregrados = silabasTOpalabra(palabra).lower()
    if palabraSinAgregados == palabraOriginalSinAgregrados: #Compara si la palabra escrita por el usuario es igual a la palabra original separada en silabas.
        return True #Entra y retorna que si es correcta.
    return False #No entra y retorna que no es correcta.

def puntaje(palabra):
    if len(palabra)>6: #Si el largo de la palabra es mayor a 6.
        return True #Devuelve True.
    return False #Devuelve False.
