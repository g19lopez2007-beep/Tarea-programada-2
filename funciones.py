#Creado por Gustavo López y Mel Acuña
#Fecha de creacion: 14/5/26
#Ultima fecha de modificacion: 16/5/26
#Version de python:3.14

import pickle
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
