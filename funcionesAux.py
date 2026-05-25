#Creado por Gustavo López y Mel Acuña
#Fecha de creacion: 14/5/26
#Ultima fecha de modificacion: 18/5/26
#Version de python:3.14

import re
import pickle
import time
import names
import random

def validarCedulaAux(pCedula):
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

def validarFechaAux(pFecha):
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

def validarCorreoAux(pCorreo):
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

def validarTelefonoAux(pTelefono):
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

def validarPesoAux(pPeso):
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
def guardarDonadoresAux(pDonadores):
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

def generarCedulaAux():
    '''
    Funcionamiento:
    -Entrada:
        No recibe datos
    -Salida:
        Se devuelve una cédula generada con el formato #-####-####
    '''
    provincia=random.randint(1,7)
    tomo=random.randint(1000,9999)
    asiento=random.randint(1000,9999)
    return str(provincia)+"-"+str(tomo)+"-"+str(asiento)

def generarNombreAux():
    '''
    Funcionamiento:
    -Entrada:
        No recibe datos
    -Salida:
        Se devuelve una lista con nombre, primer apellido y segundo apellido generados aleatoriamente
    '''
    nombre=names.get_first_name()
    apellido1=names.get_last_name()
    apellido2=names.get_last_name()
    return [nombre,apellido1,apellido2]

def generarFechaNacimientoAux(pAnnoMinimo):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe el año mínimo permitido
    -Salida:
        Se devuelve una fecha de nacimiento aleatoria desde ese año hasta el año actual
    '''
    annoActual=time.localtime().tm_year
    dia=random.randint(1,28)
    mes=random.randint(1,12)
    anno=random.randint(pAnnoMinimo,annoActual)
    return (dia,mes,anno)

def generarTelefonoAux():
    '''
    Funcionamiento:
    -Entrada:
        No recibe datos
    -Salida:
        Se devuelve un teléfono generado con el formato ####-####
    '''
    primerDigito=random.choice(("2","4","6","7","8","9"))
    resto=str(random.randint(100,999))
    segundaParte=str(random.randint(1000,9999))
    return primerDigito+resto+"-"+segundaParte

def generarCorreoAux(pNombre,pApellido,pCorreos):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe el nombre, apellido y correos permitidos
    -Salida:
        Se devuelve un correo generado automáticamente
    '''
    numero=random.randint(10,99)
    return pNombre.lower()+pApellido.lower()+str(numero)+"@"+random.choice(pCorreos)

#Funcion Aux 3 del menu principal:
def buscarDonadorCedulaAux(pCedula,pDonadores):
    '''
    Funcionamiento:
        Busca un donador en la matriz usando la cédula
    -Entrada:
        Se recibe la cédula y la matriz de donadores
    -Salida:
        Se devuelve la posición del donador o -1 si no existe
    '''
    for i in range(len(pDonadores)):
        if pDonadores[i][1]==pCedula:
            return i
    return -1

#Funcion Aux 3 del menu principal:
def actualizarDatosDonadorAux(pPosicion,pDonadores,pCorreo,pTelefono,pPeso):
    '''
    Funcionamiento:
        Actualiza los datos editables del donador
    -Entrada:
        Se recibe la posición, matriz, correo, teléfono y peso
    -Salida:
        Se actualiza la información del donador
    '''
    pDonadores[pPosicion][5]=pPeso
    pDonadores[pPosicion][6]=pCorreo
    pDonadores[pPosicion][7]=pTelefono

#Funcion Aux 4 del menu principal:
def confirmarEliminacionAux(pRespuesta):
    '''
    Funcionamiento:
        Valida si el usuario confirmó la eliminación
    -Entrada:
        Se recibe la respuesta del usuario
    -Salida:
        Se devuelve True o False
    '''
    pRespuesta=pRespuesta.lower().strip()
    if pRespuesta=="si":
        return True
    if pRespuesta=="sí":
        return True
    return False

#Funcion Aux 4 del menu principal:
def inactivarDonadorAux(pPosicion,pDonadores,pJustificacion):
    '''
    Funcionamiento:
        Cambia el estado del donador a inactivo
        y guarda la justificación
    -Entrada:
        Se recibe posición, matriz y justificación
    -Salida:
        Se actualiza la matriz
    '''
    pDonadores[pPosicion][8]=0
    pDonadores[pPosicion][9]=pJustificacion
    guardarDonadoresAux(pDonadores)
    
#Funcion Aux 5 del menu principal:
def validarProvinciaAux(pProvincia):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la provincia ingresada por el usuario
    -Salida:
        Se devuelve True si la provincia es válida o un mensaje de error
    '''
    try:
        pProvincia=int(pProvincia)
    except:
        return "La provincia debe ser numérica"
    if pProvincia<1 or pProvincia>7:
        return "Provincia inválida"
    return True

#Funcion Aux 5 del menu principal:
def validarLugarDonacionAux(pLugar):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe el lugar de donación ingresado por el usuario
    -Salida:
        Se devuelve True si el lugar es válido o un mensaje de error
    '''
    if pLugar.strip()=="":
        return "El lugar no puede estar vacío"
    return True

#Funcion Aux 5 del menu principal:
def validarLugarRepetidoAux(pProvincia,pLugar,pLugaresDonacion):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la provincia, el lugar ingresado y el diccionario de lugares
    -Salida:
        Se devuelve True si el lugar no está repetido o un mensaje de error
    '''
    pProvincia=int(pProvincia)
    if pProvincia not in pLugaresDonacion:
        return True
    for lugarActual in pLugaresDonacion[pProvincia]:
        if pLugar.lower()==lugarActual.lower():
            return "Ese lugar ya está registrado en esa provincia"
    return True

#Funcion Aux 3 del submenu:
def obtenerNombreCompletoAux(pNombre):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la lista del nombre del donador
    -Salida:
        Se devuelve el nombre completo en un string
    '''
    return pNombre[0]+" "+pNombre[1]+" "+pNombre[2]

def validarTipoSangreAux(pTipoSangre,pTiposSangre):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe el tipo de sangre ingresado y la tupla de tipos de sangre
    -Salida:
        Se devuelve True si el tipo de sangre es válido o un mensaje de error
    '''
    try:
        pTipoSangre=int(pTipoSangre)
    except:
        return "El tipo de sangre debe ser un número"
    if pTipoSangre<1 or pTipoSangre>len(pTiposSangre):
        return "Tipo de sangre inválido"
    return True

def obtenerFechaTextoAux(pFecha):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la fecha del donador
    -Salida:
        Se devuelve la fecha en formato texto
    '''
    return str(pFecha[0])+"/"+str(pFecha[1])+"/"+str(pFecha[2])

def iniciarHtmlAux(pArchivo,pTitulo):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe el archivo y el título del reporte
    -Salida:
        Se escribe el encabezado inicial del HTML
    '''
    fechaHora=time.strftime("%d/%m/%Y %H:%M:%S")
    pArchivo.write("<!DOCTYPE html>\n<html>\n<head>\n<meta charset='utf-8'>\n<title>"+pTitulo+"</title>\n</head>\n<body>\n")
    pArchivo.write("<h1>"+pTitulo+"</h1>\n")
    pArchivo.write("<p>Fecha y hora del sistema: "+fechaHora+"</p>\n")

def finalizarHtmlAux(pArchivo):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe el archivo HTML
    -Salida:
        Se cierra el HTML
    '''
    pArchivo.write("</body>\n</html>")

def obtenerSexoTextoAux(pSexo):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe el sexo del donador
    -Salida:
        Se devuelve Masculino o Femenino según corresponda
    '''
    if pSexo==True:
        return "Masculino"
    return "Femenino"

def calcularEdadAux(pFecha):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la fecha de nacimiento en tupla
    -Salida:
        Se devuelve la edad actual de la persona
    '''
    fechaActual=time.localtime()
    edad=fechaActual.tm_year-pFecha[2]
    if fechaActual.tm_mon<pFecha[1] or (fechaActual.tm_mon==pFecha[1] and fechaActual.tm_mday<pFecha[0]):
        edad-=1
    return edad