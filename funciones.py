#Creado por Gustavo López y Mel Acuña
#Fecha de creacion: 14/5/26
#Ultima fecha de modificacion: 18/5/26
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
    '''
    Funcionamiento:
    -Entrada:
        Se reciben los datos del donador y la matriz principal
    -Salida:
        Se registra el donador si todos los datos son válidos o se devuelve el error encontrado
    '''
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

#Funcion 3 del menu principal:

def actualizarDonador(pDonadores):
    '''
    Funcionamiento:
        Busca un donador por cédula y permite actualizar
        sus datos editables
    -Entrada:
        Se recibe la matriz principal de donadores
    -Salida:
        Se actualiza la información o se muestra mensaje
    '''
    cedula=input("Digite la cédula del donador: ")
    posicion=buscarDonadorCedulaAux(cedula,pDonadores)
    if posicion==-1:
        print("La persona con el número de cédula:",cedula,"no está registrada.")
        return pDonadores
    correo=input("Digite el nuevo correo: ")
    telefono=input("Digite el nuevo teléfono: ")
    peso=float(input("Digite el nuevo peso: "))
    actualizarDatosDonadorAux(posicion,pDonadores,correo,telefono,peso)
    guardarCambiosDonadorAux(pDonadores)
    print("Donador actualizado satisfactoriamente")
    return pDonadores

#Funcion 4 del menu principal:
def eliminarDonador(pDonadores):
    '''
    Funcionamiento:
        Busca un donador y cambia su estado
        a inactivo sin eliminarlo físicamente
    -Entrada:
        Se recibe la matriz principal de donadores
    -Salida:
        Se actualiza el estado o muestra mensaje
    '''
    cedula=input("Digite la cédula del donador: ")
    posicion=buscarDonadorCedulaAux(cedula,pDonadores)
    if posicion==-1:
        print("La persona con el número de cédula:",cedula,"no está registrada.")
        return pDonadores
    justificacion=input("Digite la justificación: ")
    respuesta=input("¿Desea confirmar la eliminación? " "(si/no): ")
    confirmar=confirmarEliminacionAux(respuesta)
    if confirmar==True:
        inactivarDonadorAux(posicion,pDonadores,justificacion)
        print("Donador eliminado satisfactoriamente")
    else:
        print("Donador NO eliminado")
    return pDonadores



#Funcion 5 del menu principal:
def insertarLugarDonacion(pLugaresDonacion):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe el diccionario de lugares de donación
    -Salida:
        Se agrega un nuevo lugar de donación según la provincia indicada
    '''
    print("\nSeleccione una opción\n1.San José\n2.Alajuela\n3.Cartago\n4.Heredia\n5.Guanacaste\n6.Puntarenas\n7.Limón")
    provincia=input("Digite el número de provincia: ")
    validarProvincia=validarProvinciaAux(provincia)
    if validarProvincia!=True:
        print(validarProvincia)
        return pLugaresDonacion
    lugar=input("Digite el nuevo lugar de donación: ").strip()
    validarLugar=validarLugarDonacionAux(lugar)
    if validarLugar!=True:
        print(validarLugar)
        return pLugaresDonacion
    validarRepetido=validarLugarRepetidoAux(provincia,lugar,pLugaresDonacion)
    if validarRepetido!=True:
        print(validarRepetido)
        return pLugaresDonacion
    provincia=int(provincia)
    if provincia not in pLugaresDonacion:
        pLugaresDonacion[provincia]=[]
    pLugaresDonacion[provincia].append(lugar)
    print("Lugar agregado correctamente")
    return pLugaresDonacion

def reporteTipoSangreProvincia(pDonadores,pTiposSangre):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores y la tupla de tipos de sangre
    -Salida:
        Se genera un reporte HTML con donadores activos filtrados por tipo de sangre y provincia
    '''
    print("\n1.O+\n2.O-\n3.A+\n4.A-\n5.B+\n6.B-\n7.AB+\n8.AB-")
    tipoSangre=input("Digite el tipo de sangre: ")
    validarTipoSangre=validarTipoSangreAux(tipoSangre,pTiposSangre)
    if validarTipoSangre!=True:
        print(validarTipoSangre)
        return
    print("\n1.San José\n2.Alajuela\n3.Cartago\n4.Heredia\n5.Guanacaste\n6.Puntarenas\n7.Limón")
    provincia=input("Digite el número de provincia: ")
    validarProvincia=validarProvinciaAux(provincia)
    if validarProvincia!=True:
        print(validarProvincia)
        return
    tipoSangre=int(tipoSangre)-1
    provincia=int(provincia)
    archivo=open("reporteTipoSangreProvincia.html","w",encoding="utf-8")
    iniciarHTML(archivo,"Reporte por tipo de sangre de una provincia dada")
    archivo.write("<table border='1'>\n<tr><th>Cédula</th><th>Nombre completo</th><th>Fecha de nacimiento</th><th>Teléfono</th><th>Correo</th></tr>\n")
    encontrados=0
    for donador in pDonadores:
        if len(donador)>=10:
            provinciaCedula=int(donador[1][0])
            if donador[8]==1 and donador[2]==tipoSangre and provinciaCedula==provincia:
                archivo.write("<tr>")
                archivo.write("<td>"+donador[1]+"</td>")
                archivo.write("<td>"+obtenerNombreCompleto(donador[0])+"</td>")
                archivo.write("<td>"+obtenerFechaTexto(donador[4])+"</td>")
                archivo.write("<td>"+donador[7]+"</td>")
                archivo.write("<td>"+donador[6]+"</td>")
                archivo.write("</tr>\n")
                encontrados+=1
    archivo.write("</table>\n")
    archivo.write("<p>Total encontrados: "+str(encontrados)+"</p>\n")
    finalizarHTML(archivo)
    archivo.close()
    print("Reporte creado satisfactoriamente")