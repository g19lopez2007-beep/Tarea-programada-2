#Creado por Gustavo López y Mel Acuña
#Fecha de creacion: 14/5/26
#Ultima fecha de modificacion: 16/5/26
#Version de python:3.14

import pickle
import random
from funcionesAux import *

#Funcion para cargar automaticamente los donadores
def cargarDonadores():
    '''
    Funcionamiento:
    -Entrada:
        No recibe datos
    -Salida:
        Se devuelve la matriz de donadores cargada desde memoria secundaria
    '''
    try:
        archivo=open("donadores.dat","rb")
        donadores=pickle.load(archivo)
        archivo.close()
        return donadores
    except:
        return []

def generarCedula():
    '''
    Funcionamiento:
    -Entrada:
    No recibe datos
    -Salida:
    Se devuelve una cédula generada con el formato #-####-####
    '''
    provincia=random.randint(1,8)
    tomo=random.randint(1000,9999)
    asiento=random.randint(1000,9999)
    return str(provincia)+"-"+str(tomo)+"-"+str(asiento)

def generarNombre(pNombres,pApellidos):
    '''
    Funcionamiento:
    -Entrada:
    Se reciben nombres y apellidos
    -Salida:
    Se devuelve una lista con nombre, primer apellido y segundo apellido
    '''
    return [random.choice(pNombres),random.choice(pApellidos),random.choice(pApellidos)]

def generarFechaNacimiento(pAnnoMinimo):
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

def generarTelefono():
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

def generarCorreo(pNombre,pApellido,pCorreos):
    '''
    Funcionamiento:
    -Entrada:
    Se recibe el nombre, apellido y correos permitidos
    -Salida:
    Se devuelve un correo generado automáticamente
    '''
    numero=random.randint(10,99)
    return pNombre.lower()+pApellido.lower()+str(numero)+"@"+random.choice(pCorreos)

#Funcion 1 del menu principal:
def insertarDonador(pDonadores,pCedula,pFecha,pCorreo,pTelefono,pPeso):
    cedula=validarCedula(pCedula)
    fecha=validarFecha(pFecha)
    correo=validarCorreo(pCorreo)
    telefono=validarTelefono(pTelefono)
    peso=validarPeso(pPeso)
    if cedula!=True:
        return cedula
    if fecha!=True:
        return fecha
    if correo!=True:
        return correo
    if telefono!=True:
        return telefono
    if peso!=True:
        return peso
    nuevo=[pCedula,pFecha,pCorreo,pTelefono,pPeso]
    pDonadores.append(nuevo)
    guardarDonadores(pDonadores)
    return "Donador registrado correctamente"

#Funcion 2 del menu principal:
def generarDonadores(pBaseDatos,pTiposSangre,pNombres,pApellidos,pCorreos):
    '''
    Funcionamiento:
    -Entrada:
    Se recibe la matriz principal y las estructuras necesarias para generar donadores
    -Salida:
    Se agregan donadores generados automáticamente a la matriz principal
    '''
    cantidad=input("Digite la cantidad de donadores que desea generar: ")
    validarCantidad=validarCantidadAux(cantidad)
    if validarCantidad!=True:
        print(validarCantidad)
        return pBaseDatos
    añoMinimo=input("Digite el año mínimo de nacimiento: ")
    validarAño=validarAñoAux(añoMinimo)
    if validarAño!=True:
        print(validarAño)
        return pBaseDatos
    validar=confirmarAñoAux(añoMinimo)
    if validar!=True:
        print(validar)
        return pBaseDatos
    cantidad=int(cantidad)
    añoMinimo=int(añoMinimo)
    contadorActivos=0
    contadorInactivos=0
    for i in range(cantidad):
        nombre=generarNombre(pNombres,pApellidos)
        cedula=generarCedula()
        tipoSangre=random.randint(0,len(pTiposSangre)-1)
        sexo=random.choice((True,False))
        fechaNacimiento=generarFechaNacimiento(añoMinimo)
        peso=random.randint(45,130)
        correo=generarCorreo(nombre[0],nombre[1],pCorreos)
        telefono=generarTelefono()
        estado=random.choice((1,0))
        if estado==1:
            justificacion=0
            contadorActivos+=1
        else:
            justificacion=random.randint(1,7)
            contadorInactivos+=1
        pBaseDatos.append([nombre,cedula,tipoSangre,sexo,fechaNacimiento,float(peso),correo,telefono,estado,justificacion])
    print("Se generaron correctamente",cantidad,"donadores")
    print("Donadores activos:",contadorActivos)
    print("Donadores no activos:",contadorInactivos)
    return pBaseDatos