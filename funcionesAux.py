#Creado por Gustavo López y Mel Acuña
#Fecha de creacion: 14/5/26
#Ultima fecha de modificacion: 16/5/26
#Version de python:3.14

import re
import pickle
import time

def validarCedula(pCedula):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la cédula del donador
    -Salida:
        Se devuelve True si la cédula cumple el formato #-####-#### y False si no cumple
    '''
    if not re.match("^[1-9]-[0-9]{4}-[0-9]{4}$",pCedula):
        return "El formato de cédula esta malo"
    return True

def validarFecha(pFecha):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la fecha de nacimiento del donador
    -Salida:
        Se devuelve True si la fecha cumple el formato DD/MM/AAAA correctamente y False si no cumple
    '''
    if not re.match("^[0-9]{2}/[0-9]{2}/[0-9]{4}$",pFecha):
        return "Debe ingresar el formato DD/MM/AAAA"
    dia=int(pFecha[0:2])
    mes=int(pFecha[3:5])
    anno=int(pFecha[6:10])
    if mes<1 or mes>12:
        return "Mes invalido"
    if dia<1:
        return "Dia invalido"
    if mes==2:
        if anno%4==0 and (anno%100!=0 or anno%400==0):
            if dia<=29:
                return True
        else:
            if dia<=28:
                return True
    elif mes==4 or mes==6 or mes==9 or mes==11:
        if dia<=30:
            return True
    else:
        if dia<=31:
            return True
    return "Fecha invalida"

def validarCorreo(pCorreo):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe el correo electrónico del donador
    -Salida:
        Se devuelve True si el correo cumple con los dominios permitidos y False si no cumple
    '''
    if not re.match("^[a-zA-Z0-9]+@(costarricense\\.cr|racsa\\.go\\.cr|ccss\\.sa\\.cr|gmail\\.com)$",pCorreo):
        return "El correo no cumple con un dominio permitido"
    return True

def validarTelefono(pTelefono):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe el número de teléfono del donador
    -Salida:
        Se devuelve True si el teléfono cumple el formato ####-#### y False si no cumple
    '''
    if not re.match("^[246789][0-9]{3}-[0-9]{4}$",pTelefono):
        return "El telefono debe cumplir el formato ####-#### y no puede iniciar en 0,1,3 o 5"
    return True

def validarPeso(pPeso):
    '''
    Funcionamiento:
    -Entrada:
    Se recibe el peso del donador
    -Salida:
    Se devuelve True si el peso es válido o un mensaje indicando el error encontrado
    '''
    if not re.match("^[0-9]{2,3}$",pPeso):
        return "El peso minimo debe ser de 2 digitos y maximo de 3 digitos"
    peso=float(pPeso)
    if peso<=50:
        return "El peso debe ser mayor a 50"
    if peso>=120:
        return "El peso debe ser menor a 120"
    return True

#Funcion Aux 1 del menu principal:
def guardarDonadores(pDonadores):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores
    -Salida:
        Se guarda la matriz de donadores en memoria secundaria
    '''
    archivo=open("donadores.dat","wb")
    pickle.dump(pDonadores,archivo)
    archivo.close()

#Funcion Aux 2 del menu principal:
def validarCantidadAux(pCantidad):
    '''
    Funcionamiento:
    -Entrada:
    Se recibe la cantidad ingresada por el usuario
    -Salida:
    Se devuelve True si la cantidad es válida o un mensaje de error
    '''
    try:
        pCantidad=int(pCantidad)
    except:
        return "La cantidad debe ser numérica"
    if pCantidad<=0:
        return "La cantidad debe ser mayor a 0"
    return True

#Funcion Aux 2 del menu principal:
def validarAñoAux(pAño):
    '''
    Funcionamiento:
    -Entrada:
    Se recibe el año mínimo ingresado por el usuario
    -Salida:
    Se devuelve True si el año es válido o un mensaje de error
    '''
    añoActual=time.localtime().tm_year
    try:
        pAño=int(pAño)
    except:
        return "El año debe ser numérico"
    if pAño>añoActual:
        return "El año no puede ser mayor al actual"
    return True

#Funcion Aux 2 del menu principal:
def confirmarAñoAux(pAño):
    '''
    Funcionamiento:
    -Entrada:
    Se recibe el año mínimo ingresado por el usuario
    -Salida:
    Se devuelve True si el año permite generar personas entre 18 y 70 años o un mensaje de error
    '''
    añoActual=time.localtime().tm_year
    edadMaxima=añoActual-int(pAño)
    if edadMaxima<18:
        return "No se puede usar ese año porque generaría personas menores de 18 años"
    if edadMaxima>70:
        return "No se puede usar ese año porque generaría personas mayores de 70 años"
    return True