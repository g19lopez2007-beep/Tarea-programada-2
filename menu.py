#Creado por Gustavo López y Mel Acuña
#Fecha de creacion: 14/5/26
#Ultima fecha de modificacion: 18/5/26
#Version de python:3.14

from funciones import *

def submenuReportes():
    '''
    Funcionamiento:
    -Entrada:
        El usuario selecciona una opción del submenú de reportes
    -Salida:
    '''
    while True:
        print("\n===== REPORTES =====\n1.Donantes por provincia\n2.Por rango de edad\n3.Por tipo de sangre de una provincia dada\n4.Lista completa de donadores\n5.Mujeres donantes O-\n6.¿A quién puede donar?\n7.¿De quién puede recibir?\n8.Donantes NO activos\n9.Lugares de donación\n10.Regresar")
        opcion=input("Digite una opción: ")
        if opcion=="1":
            print("Aqui tiene que estar la funcion reporteDonantesProvincia")
        elif opcion=="2":
            print("Aqui tiene que estar la funcion reporteRangoEdad")
        elif opcion=="3":
            print("Aqui tiene que estar la funcion reporteTipoSangreProvincia")
        elif opcion=="4":
            print("Aqui tiene que estar la funcion reporteListaCompletaDonadores")
        elif opcion=="5":
            print("Aqui tiene que estar la funcion reporteMujeresONegativo")
        elif opcion=="6":
            print("Aqui tiene que estar la funcion reportePuedeDonar")
        elif opcion=="7":
            print("Aqui tiene que estar la funcion reportePuedeRecibir")
        elif opcion=="8":
            print("Aqui tiene que estar la funcion reporteDonantesNoActivos")
        elif opcion=="9":
            print("Aqui tiene que estar la funcion reporteLugaresDonacion")
        elif opcion=="10":
            print("Regresando al menú principal")
            break
        else:
            print("Opción inválida")

def menuPrincipal(pDonadores):
    '''
    Funcionamiento:
    -Entrada:
        El usuario selecciona una opción del menú principal
    -Salida:
        Se muestra el espacio donde luego irá la función correspondiente
    '''
    tiposSangre=("O+","O-","A+","A-","B+","B-","AB+","AB-")
    nombres=("Carlos","María","José","Ana","Luis","Sofía","Pedro","Valeria","Andrés","Camila")
    apellidos=("López","Mora","Castro","Vargas","Soto","Jiménez","Rojas","Ramírez","Arias","Solís")
    correos=("gmail.com","costarricense.cr","racsa.go.cr","ccss.sa.cr")
    lugaresDonacion={}
    while True:
        print("\n===== BANCO DE SANGRE =====\n1.Insertar donador\n2.Generar donadores\n3.Actualizar datos del donador\n4.Eliminar donador\n5.Insertar lugar de donación según provincia\n6.Reportes\n7.Salir")
        opcion=input("Digite una opción: ")
        if opcion=="1":
            cedula=input("Digite la cédula (#-####-####): ")
            fecha=input("Digite la fecha de nacimiento (DD/MM/AAAA): ")
            correo=input("Digite el correo: ")
            telefono=input("Digite el teléfono (####-####): ")
            peso=input("Digite el peso: ")
            print(insertarDonador(pDonadores,cedula,fecha,correo,telefono,peso))
        elif opcion=="2":
            pDonadores=generarDonadores(pDonadores,tiposSangre,nombres,apellidos,correos)
        elif opcion=="3":
            print("Aqui tiene que estar la funcion actualizarDonador")
        elif opcion=="4":
            print("Aqui tiene que estar la funcion eliminarDonador")
        elif opcion=="5":
            lugaresDonacion=insertarLugarDonacion(lugaresDonacion)
        elif opcion=="6":
            submenuReportes()
        elif opcion=="7":
            print("Donar sangre, es donar vida")
            break
        else:
            print("Opción inválida")
donadores=cargarDonadores()
menuPrincipal(donadores)