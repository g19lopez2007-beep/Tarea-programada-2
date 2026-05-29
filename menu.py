#Creado por Gustavo López y Mel Acuña
#Fecha de creacion: 14/5/26
#Ultima fecha de modificacion: 27/5/26
#Version de python:3.14

from funciones import *
from funcionesAux import validarBotonesMenuAux
from tkinter import *

def abrirSubmenuReportes(pVentana,pDonadores,pTiposSangre,pLugaresDonacion):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la ventana principal, donadores, tipos de sangre y lugares de donación
    -Salida:
        Se muestra el submenú de reportes
    '''
    pVentana.withdraw()
    ventanaReportes=Toplevel()
    ventanaReportes.title("Reportes")
    ventanaReportes.geometry("500x600")
    Label(ventanaReportes,text="REPORTES",font=("Century Gothic",14,"bold")).pack(pady=15)
    crearBoton(ventanaReportes,"1.Donantes por provincia",lambda:mostrarMensaje(reporteListaCompletaDonadores(pDonadores,pTiposSangre)))
    crearBoton(ventanaReportes,"2.Por rango de edad",lambda:mostrarMensaje(reporteRangoEdad(pDonadores)))
    crearBoton(ventanaReportes,"3.Por tipo de sangre de una provincia",lambda:mostrarMensaje(reporteTipoSangreProvincia(pDonadores,pTiposSangre)))
    crearBoton(ventanaReportes,"4.Lista completa de donadores",lambda:mostrarMensaje(reporteListaCompletaDonadores(pDonadores,pTiposSangre)))
    crearBoton(ventanaReportes,"5.Mujeres donantes O-",lambda:mostrarMensaje(reporteMujeresONegativo(pDonadores)))
    crearBoton(ventanaReportes,"6.¿A quién puede donar?",lambda:mostrarMensaje(reportePuedeDonar(pDonadores,pTiposSangre)))
    crearBoton(ventanaReportes,"7.¿De quién puede recibir?",lambda:mostrarMensaje(reportePuedeRecibir(pDonadores,pTiposSangre)))
    crearBoton(ventanaReportes,"8.Donantes NO activos",lambda:mostrarMensaje(reporteDonantesNoActivos(pDonadores,pTiposSangre)))
    crearBoton(ventanaReportes,"9.Lugares de donación",lambda:mostrarMensaje(reporteLugaresDonacion(pDonadores,pLugaresDonacion)))
    crearBoton(ventanaReportes,"10.Regresar",lambda:regresarMenuPrincipal(pVentana,ventanaReportes))

def menuPrincipal(pDonadores):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores
    -Salida:
        Se muestra el menú principal usando tkinter
    '''
    tiposSangre=("O+","O-","A+","A-","B+","B-","AB+","AB-")
    correos=("gmail.com","costarricense.cr","racsa.go.cr","ccss.sa.cr")
    lugaresDonacion={}
    ventana=Tk()
    ventana.title("Banco de Sangre")
    ventana.geometry("500x500")
    Label(ventana,text="BANCO DE SANGRE",font=("Century Gothic",14,"bold")).pack(pady=15)
    crearBoton(ventana,"1.Insertar donador",lambda:abrirInsertarDonador(ventana,pDonadores,tiposSangre))
    crearBoton(ventana,"2.Generar donadores",lambda:abrirGenerarDonadores(ventana,pDonadores,tiposSangre,correos,boton3,boton4,boton6))
    boton3=crearBoton(ventana,"3.Actualizar datos del donador",lambda:mostrarMensaje("Aquí irá actualizarDonador"))
    boton4=crearBoton(ventana,"4.Eliminar donador",lambda:ventanaEliminarDonador(pDonadores))
    crearBoton(ventana,"5.Insertar lugar de donación",lambda:mostrarMensaje("Aquí irá insertarLugarDonacion"))
    boton6=crearBoton(ventana,"6.Reportes",lambda:abrirSubmenuReportes(ventana,pDonadores,tiposSangre,lugaresDonacion))
    crearBoton(ventana,"7.Salir",ventana.destroy)
    validarBotonesMenuAux(pDonadores,boton3,boton4,boton6)
    ventana.mainloop()
donadores=cargarDonadores()
menuPrincipal(donadores)