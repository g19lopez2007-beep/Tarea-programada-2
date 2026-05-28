#Creado por Gustavo López y Mel Acuña
#Fecha de creacion: 14/5/26
#Ultima fecha de modificacion: 27/5/26
#Version de python:3.14

import pickle
import random
from funcionesAux import *
from tkinter import *

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

#Funcion 1 del menu principal:
def insertarDonador(pDonadores,pNombre,pApellido1,pApellido2,pCedula,pTipoSangre,pFecha,pSexo,pCorreo,pTelefono,pPeso):
    '''
    Funcionamiento:
    -Entrada:
        Se reciben los datos del donador y la matriz principal
    -Salida:
        Se registra el donador si todos los datos son válidos o se devuelve el error encontrado
    '''
    cedula=validarCedulaAux(pCedula)
    fecha=validarFechaAux(pFecha)
    correo=validarCorreoAux(pCorreo)
    telefono=validarTelefonoAux(pTelefono)
    peso=validarPesoAux(pPeso)
    tipoSangre=validarTipoSangreAux(pTipoSangre,("O+","O-","A+","A-","B+","B-","AB+","AB-"))
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
    if tipoSangre!=True:
        return tipoSangre
    if pSexo!="1" and pSexo!="2":
        return "El sexo debe ser 1 o 2"
    nombre=[pNombre,pApellido1,pApellido2]
    fechaNacimiento=(int(pFecha[0:2]),int(pFecha[3:5]),int(pFecha[6:10]))
    tipoSangre=int(pTipoSangre)-1
    if pSexo=="1":
        sexo=True
    else:
        sexo=False
    justificacionEstado=obtenerJustificacionEstadoAux(fechaNacimiento,pPeso)
    if justificacionEstado==True:
        estado=1
        justificacion=0
    else:
        estado=0
        justificacion=justificacionEstado
    nuevo=[nombre,pCedula,tipoSangre,sexo,fechaNacimiento,float(pPeso),pCorreo,pTelefono,estado,justificacion]
    pDonadores.append(nuevo)
    guardarDonadoresAux(pDonadores)
    if estado==1:
        return "Donador registrado correctamente"
    return "Donador registrado correctamente (Estado inactivo: "+justificacion+")"

#Funcion 2 del menu principal:
def generarDonadores(pBaseDatos,pTiposSangre,pCorreos,pCantidad):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz principal y las estructuras necesarias para generar donadores
    -Salida:
        Se agregan donadores generados automáticamente a la matriz principal
    '''
    validarCantidad=validarCantidadAux(pCantidad)
    if validarCantidad!=True:
        return validarCantidad
    cantidad=int(pCantidad)
    contadorActivos=0
    for i in range(cantidad):
        nombre=generarNombreAux()
        cedula=generarCedulaAux()
        tipoSangre=random.randint(0,len(pTiposSangre)-1)
        sexo=random.choice((True,False))
        fechaNacimiento=generarFechaNacimientoAux()
        peso=random.randint(51,119)
        correo=generarCorreoAux(nombre[0],nombre[1],pCorreos)
        telefono=generarTelefonoAux()
        estado=1
        justificacion=0
        contadorActivos+=1
        pBaseDatos.append([nombre,cedula,tipoSangre,sexo,fechaNacimiento,float(peso),correo,telefono,estado,justificacion])
    guardarDonadoresAux(pBaseDatos)
    return "Se generaron correctamente "+str(cantidad)+" donadores"

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
    validarCorreo=validarCorreoAux(correo)
    if validarCorreo!=True:
        print(validarCorreo)
        return pDonadores
    telefono=input("Digite el nuevo teléfono: ")
    validarTelefono=validarTelefonoAux(telefono)
    if validarTelefono!=True:
        print(validarTelefono)
        return pDonadores
    peso=input("Digite el nuevo peso: ")
    validarPeso=validarPesoAux(peso)
    if validarPeso!=True:
        print(validarPeso)
        return pDonadores
    peso=float(peso)
    actualizarDatosDonadorAux(posicion,pDonadores,correo,telefono,peso)
    guardarDonadoresAux(pDonadores)
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

def eliminarDonadorTk(pDonadores,pCedula,pJustificacion):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores, la cédula y la justificación ingresada desde tkinter
    -Salida:
        Se cambia el estado del donador a inactivo o se devuelve un mensaje
    '''
    validarCedula=validarCedulaAux(pCedula)
    if validarCedula!=True:
        return validarCedula
    posicion=buscarDonadorCedulaAux(pCedula,pDonadores)
    if posicion==-1:
        return "La persona con el número de cédula: "+pCedula+" no está registrada."
    if pJustificacion.strip()=="":
        return "Debe ingresar una justificación"
    pDonadores[posicion][8]=0
    pDonadores[posicion][9]=pJustificacion
    guardarDonadoresAux(pDonadores)
    return "Donador eliminado satisfactoriamente"

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

#Funcion 1 submenu reportes:
def reporteDonantesProvincia(pDonadores):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores
    -Salida:
        Se genera un reporte HTML con los donadores activos
        de la provincia indicada
    '''
    provincia=input("Digite el número de provincia: ")
    try:
        provincia=int(provincia)
    except:
        print("La provincia debe ser numérica")
        return
    if provincia<1 or provincia>7:
        print("Provincia inválida")
        return
    encontrados=0
    for donador in pDonadores:
        if len(donador)>=10:
            if donador[8]==1 and int(donador[1][0])==provincia:
                encontrados+=1
    if encontrados==0:
        print("No hay donadores activos en esa provincia")
        return
    archivo=open("reporteDonantesProvincia.html","w",encoding="utf-8")
    iniciarHtmlAux(archivo,"Reporte de donantes por provincia")
    archivo.write("<table border='1'>\n")
    archivo.write("<tr>")
    archivo.write("<th>Cédula</th>")
    archivo.write("<th>Nombre completo</th>")
    archivo.write("<th>Fecha de nacimiento</th>")
    archivo.write("<th>Teléfono</th>")
    archivo.write("<th>Correo</th>")
    archivo.write("</tr>\n")
    for donador in pDonadores:
        if len(donador)>=10:
            if donador[8]==1 and int(donador[1][0])==provincia:
                archivo.write("<tr>")
                archivo.write("<td>"+donador[1]+"</td>")
                archivo.write("<td>"+obtenerNombreCompletoAux(donador[0])+"</td>")
                archivo.write("<td>"+obtenerFechaTextoAux(donador[4])+"</td>")
                archivo.write("<td>"+donador[7]+"</td>")
                archivo.write("<td>"+donador[6]+"</td>")
                archivo.write("</tr>\n")
    archivo.write("</table>\n")
    archivo.write("<p>Total encontrados: "+str(encontrados)+"</p>\n")
    finalizarHtmlAux(archivo)
    archivo.close()
    print("Reporte creado satisfactoriamente")

#Funcion 2 submenu reportes:
def reporteRangoEdad(pDonadores):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores
    -Salida:
        Se genera un reporte HTML con los donadores
        activos que estén dentro del rango de edad indicado
    '''
    edadMinima=input("Digite la edad mínima: ")
    edadMaxima=input("Digite la edad máxima: ")
    try:
        edadMinima=int(edadMinima)
        edadMaxima=int(edadMaxima)
    except:
        print("Las edades deben ser numéricas")
        return
    if edadMinima<18 or edadMaxima>65:
        print("Las edades deben estar entre 18 y 65 años")
        return
    encontrados=0
    for donador in pDonadores:
        if len(donador)>=10:
            edad=calcularEdadAux(donador[4])
            if donador[8]==1 and edad>=edadMinima and edad<=edadMaxima:
                encontrados+=1
    if encontrados==0:
        print("No hay donadores en ese rango de edad")
        return
    archivo=open("reporteRangoEdad.html","w",encoding="utf-8")
    iniciarHtmlAux(archivo,"Reporte por rango de edad")
    archivo.write("<table border='1'>\n")
    archivo.write("<tr>")
    archivo.write("<th>Cédula</th>")
    archivo.write("<th>Nombre completo</th>")
    archivo.write("<th>Fecha nacimiento</th>")
    archivo.write("<th>Teléfono</th>")
    archivo.write("<th>Correo</th>")
    archivo.write("</tr>\n")
    for donador in pDonadores:
        if len(donador)>=10:
            edad=calcularEdadAux(donador[4])
            if donador[8]==1 and edad>=edadMinima and edad<=edadMaxima:
                archivo.write("<tr>")
                archivo.write("<td>"+donador[1]+"</td>")
                archivo.write("<td>"+obtenerNombreCompletoAux(donador[0])+"</td>")
                archivo.write("<td>"+obtenerFechaTextoAux(donador[4])+"</td>")
                archivo.write("<td>"+donador[7]+"</td>")
                archivo.write("<td>"+donador[6]+"</td>")
                archivo.write("</tr>\n")
    archivo.write("</table>\n")
    archivo.write("<p>Total encontrados: "+str(encontrados)+"</p>\n")
    finalizarHtmlAux(archivo)
    archivo.close()
    print("Reporte creado satisfactoriamente")

#Funcion 3 submenu reportes:
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
    encontrados=0
    for donador in pDonadores:
        if len(donador)>=10:
            provinciaCedula=int(donador[1][0])
            if donador[8]==1 and donador[2]==tipoSangre and provinciaCedula==provincia:
                encontrados+=1
    if encontrados==0:
        print("No hay donadores que cumplan con los requisitos")
        return
    archivo=open("reporteTipoSangreProvincia.html","w",encoding="utf-8")
    iniciarHtmlAux(archivo,"Reporte por tipo de sangre de una provincia dada")
    archivo.write("<table border='1'>\n<tr><th>Cédula</th><th>Nombre completo</th><th>Fecha de nacimiento</th><th>Teléfono</th><th>Correo</th></tr>\n")
    encontrados=0
    for donador in pDonadores:
        if len(donador)>=10:
            provinciaCedula=int(donador[1][0])
            if donador[8]==1 and donador[2]==tipoSangre and provinciaCedula==provincia:
                archivo.write("<tr>")
                archivo.write("<td>"+donador[1]+"</td>")
                archivo.write("<td>"+obtenerNombreCompletoAux(donador[0])+"</td>")
                archivo.write("<td>"+obtenerFechaTextoAux(donador[4])+"</td>")
                archivo.write("<td>"+donador[7]+"</td>")
                archivo.write("<td>"+donador[6]+"</td>")
                archivo.write("</tr>\n")
                encontrados+=1
    archivo.write("</table>\n")
    archivo.write("<p>Total encontrados: "+str(encontrados)+"</p>\n")
    finalizarHtmlAux(archivo)
    archivo.close()
    print("Reporte creado satisfactoriamente")


#Funcion 4 submenu reportes:
def reporteListaCompletaDonadores(pDonadores,pTiposSangre):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores y la tupla de tipos de sangre
    -Salida:
        Se genera un reporte HTML con la lista completa de donadores
    '''
    encontrados=0
    for provincia in range(1,8):
        for donador in pDonadores:
            if len(donador)>=10:
                provinciaCedula=int(donador[1][0])
                if provinciaCedula==provincia:
                    encontrados+=1
    if encontrados==0:
        print("No hay donadores que cumplan con los requisitos")
        return
    archivo=open("reporteListaCompletaDonadores.html","w",encoding="utf-8")
    iniciarHtmlAux(archivo,"Lista completa de donadores")
    archivo.write("<table border='1'>\n<tr><th>Cédula</th><th>Nombre completo</th><th>Tipo de sangre</th><th>Fecha de nacimiento</th><th>Peso</th><th>Sexo</th><th>Teléfono</th><th>Correo</th></tr>\n")
    for provincia in range(1,8):
        for donador in pDonadores:
            if len(donador)>=10:
                provinciaCedula=int(donador[1][0])
                if provinciaCedula==provincia:
                    archivo.write("<tr>")
                    archivo.write("<td>"+donador[1]+"</td>")
                    archivo.write("<td>"+obtenerNombreCompletoAux(donador[0])+"</td>")
                    archivo.write("<td>"+pTiposSangre[donador[2]]+"</td>")
                    archivo.write("<td>"+obtenerFechaTextoAux(donador[4])+"</td>")
                    archivo.write("<td>"+str(donador[5])+"</td>")
                    archivo.write("<td>"+obtenerSexoTextoAux(donador[3])+"</td>")
                    archivo.write("<td>"+donador[7]+"</td>")
                    archivo.write("<td>"+donador[6]+"</td>")
                    archivo.write("</tr>\n")
    archivo.write("</table>\n")
    finalizarHtmlAux(archivo)
    archivo.close()
    print("Reporte creado satisfactoriamente")

#Funcion 5 submenu reportes:
def reporteMujeresONegativo(pDonadores):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores
    -Salida:
        Se genera un reporte HTML con mujeres donantes O- menores de 45 años
    '''
    encontrados=0
    for donador in pDonadores:
        if len(donador)>=10:
            edad=calcularEdadAux(donador[4])
            if donador[8]==1 and donador[3]==False and donador[2]==1 and edad<45:
                encontrados+=1
    if encontrados==0:
        print("No hay donadores que cumplan con los requisitos")
        return
    archivo=open("reporteMujeresONegativo.html","w",encoding="utf-8")
    iniciarHtmlAux(archivo,"Mujeres donantes O- menores de 45 años")
    archivo.write("<table border='1'>\n<tr><th>Cédula</th><th>Nombre completo</th><th>Fecha de nacimiento</th><th>Teléfono</th><th>Correo</th></tr>\n")
    for donador in pDonadores:
        if len(donador)>=10:
            edad=calcularEdadAux(donador[4])
            if donador[8]==1 and donador[3]==False and donador[2]==1 and edad<45:
                archivo.write("<tr>")
                archivo.write("<td>"+donador[1]+"</td>")
                archivo.write("<td>"+obtenerNombreCompletoAux(donador[0])+"</td>")
                archivo.write("<td>"+obtenerFechaTextoAux(donador[4])+"</td>")
                archivo.write("<td>"+donador[7]+"</td>")
                archivo.write("<td>"+donador[6]+"</td>")
                archivo.write("</tr>\n")
    archivo.write("</table>\n")
    archivo.write("<p>Total encontrados: "+str(encontrados)+"</p>\n")
    finalizarHtmlAux(archivo)
    archivo.close()
    print("Reporte creado satisfactoriamente")

#Funcion 6 submenu reportes:
def reportePuedeDonar(pDonadores,pTiposSangre):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores y la tupla de tipos de sangre
    -Salida:
        Se genera un reporte HTML con las personas a quienes puede donar
        el tipo de sangre seleccionado, agrupadas por provincia ascendentemente
    '''
    print("\nTipos de sangre")
    i=0
    while i<len(pTiposSangre):
        print(str(i)+".",pTiposSangre[i])
        i+=1
    tipo=input("Digite el número del tipo de sangre: ")
    try:
        tipo=int(tipo)
    except:
        print("El tipo de sangre debe ser numérico")
        return
    if tipo<0 or tipo>=len(pTiposSangre):
        print("Tipo de sangre inválido")
        return
    tipoDonante=obtenerTipoSangreTextoAux(tipo,pTiposSangre)
    encontrados=0
    provincia=1
    while provincia<=7:
        for donador in pDonadores:
            if len(donador)>=10:
                tipoReceptor=obtenerTipoSangreTextoAux(donador[2],pTiposSangre)
                if donador[8]==1 and int(donador[1][0])==provincia and puedeDonarAux(tipoDonante,tipoReceptor)==True:
                    encontrados+=1
        provincia+=1
    if encontrados==0:
        print("No hay donadores compatibles registrados")
        return
    archivo=open("reportePuedeDonar.html","w",encoding="utf-8")
    iniciarHtmlAux(archivo,"Reporte de a quién puede donar")
    archivo.write("<p>Tipo de sangre seleccionado: "+tipoDonante+"</p>\n")
    archivo.write("<table border='1'>\n")
    archivo.write("<tr>")
    archivo.write("<th>Provincia</th>")
    archivo.write("<th>Cédula</th>")
    archivo.write("<th>Nombre completo</th>")
    archivo.write("<th>Tipo de sangre</th>")
    archivo.write("<th>Teléfono</th>")
    archivo.write("<th>Correo</th>")
    archivo.write("</tr>\n")
    provincia=1
    while provincia<=7:
        for donador in pDonadores:
            if len(donador)>=10:
                tipoReceptor=obtenerTipoSangreTextoAux(donador[2],pTiposSangre)
                if donador[8]==1 and int(donador[1][0])==provincia and puedeDonarAux(tipoDonante,tipoReceptor)==True:
                    archivo.write("<tr>")
                    archivo.write("<td>"+str(provincia)+"</td>")
                    archivo.write("<td>"+donador[1]+"</td>")
                    archivo.write("<td>"+obtenerNombreCompletoAux(donador[0])+"</td>")
                    archivo.write("<td>"+tipoReceptor+"</td>")
                    archivo.write("<td>"+donador[7]+"</td>")
                    archivo.write("<td>"+donador[6]+"</td>")
                    archivo.write("</tr>\n")
        provincia+=1
    archivo.write("</table>\n")
    archivo.write("<p>Total encontrados: "+str(encontrados)+"</p>\n")
    finalizarHtmlAux(archivo)
    archivo.close()
    print("Reporte creado satisfactoriamente")

#Funcion 7 submenu reportes:
def reportePuedeRecibir(pDonadores,pTiposSangre):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores y la tupla de tipos de sangre
    -Salida:
        Se genera un reporte HTML con los donadores de quienes puede recibir
        el tipo de sangre seleccionado, agrupados por provincia descendentemente
    '''
    print("\nTipos de sangre")
    i=0
    while i<len(pTiposSangre):
        print(str(i)+".",pTiposSangre[i])
        i+=1
    tipo=input("Digite el número del tipo de sangre: ")
    try:
        tipo=int(tipo)
    except:
        print("El tipo de sangre debe ser numérico")
        return
    if tipo<0 or tipo>=len(pTiposSangre):
        print("Tipo de sangre inválido")
        return
    tipoReceptor=obtenerTipoSangreTextoAux(tipo,pTiposSangre)
    encontrados=0
    provincia=7
    while provincia>=1:
        for donador in pDonadores:
            if len(donador)>=10:
                tipoDonante=obtenerTipoSangreTextoAux(donador[2],pTiposSangre)
                if donador[8]==1 and int(donador[1][0])==provincia and puedeRecibirAux(tipoReceptor,tipoDonante)==True:
                    encontrados+=1
        provincia-=1
    if encontrados==0:
        print("No hay donadores compatibles registrados")
        return
    archivo=open("reportePuedeRecibir.html","w",encoding="utf-8")
    iniciarHtmlAux(archivo,"Reporte de quién puede recibir")
    archivo.write("<p>Tipo de sangre seleccionado: "+tipoReceptor+"</p>\n")
    archivo.write("<table border='1'>\n")
    archivo.write("<tr>")
    archivo.write("<th>Provincia</th>")
    archivo.write("<th>Cédula</th>")
    archivo.write("<th>Nombre completo</th>")
    archivo.write("<th>Tipo de sangre</th>")
    archivo.write("<th>Teléfono</th>")
    archivo.write("<th>Correo</th>")
    archivo.write("</tr>\n")
    provincia=7
    while provincia>=1:
        for donador in pDonadores:
            if len(donador)>=10:
                tipoDonante=obtenerTipoSangreTextoAux(donador[2],pTiposSangre)
                if donador[8]==1 and int(donador[1][0])==provincia and puedeRecibirAux(tipoReceptor,tipoDonante)==True:
                    archivo.write("<tr>")
                    archivo.write("<td>"+str(provincia)+"</td>")
                    archivo.write("<td>"+donador[1]+"</td>")
                    archivo.write("<td>"+obtenerNombreCompletoAux(donador[0])+"</td>")
                    archivo.write("<td>"+tipoDonante+"</td>")
                    archivo.write("<td>"+donador[7]+"</td>")
                    archivo.write("<td>"+donador[6]+"</td>")
                    archivo.write("</tr>\n")
        provincia-=1
    archivo.write("</table>\n")
    archivo.write("<p>Total encontrados: "+str(encontrados)+"</p>\n")
    finalizarHtmlAux(archivo)
    archivo.close()
    print("Reporte creado satisfactoriamente")

#Funcion 8 submenu reportes:
def reporteDonantesNoActivos(pDonadores,pTiposSangre):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores y la tupla de tipos de sangre
    -Salida:
        Se genera un reporte HTML con los donadores no activos
    '''
    encontrados=0
    for donador in pDonadores:
        if len(donador)>=10:
            if donador[8]==0:
                encontrados+=1
    if encontrados==0:
        print("No hay donadores no activos registrados")
        return
    archivo=open("reporteDonantesNoActivos.html","w",encoding="utf-8")
    iniciarHtmlAux(archivo,"Reporte de donantes NO activos")
    archivo.write("<table border='1'>\n")
    archivo.write("<tr>")
    archivo.write("<th>Justificación</th>")
    archivo.write("<th>Cédula</th>")
    archivo.write("<th>Nombre completo</th>")
    archivo.write("<th>Tipo de sangre</th>")
    archivo.write("<th>Fecha de nacimiento</th>")
    archivo.write("<th>Peso</th>")
    archivo.write("<th>Sexo</th>")
    archivo.write("<th>Teléfono</th>")
    archivo.write("<th>Correo</th>")
    archivo.write("</tr>\n")
    for donador in pDonadores:
        if len(donador)>=10:
            if donador[8]==0:
                archivo.write("<tr>")
                archivo.write("<td>"+obtenerJustificacionAux(donador[9])+"</td>")
                archivo.write("<td>"+donador[1]+"</td>")
                archivo.write("<td>"+obtenerNombreCompletoAux(donador[0])+"</td>")
                archivo.write("<td>"+obtenerTipoSangreTextoAux(donador[2],pTiposSangre)+"</td>")
                archivo.write("<td>"+obtenerFechaTextoAux(donador[4])+"</td>")
                archivo.write("<td>"+str(donador[5])+"</td>")
                archivo.write("<td>"+obtenerSexoTextoAux(donador[3])+"</td>")
                archivo.write("<td>"+donador[7]+"</td>")
                archivo.write("<td>"+donador[6]+"</td>")
                archivo.write("</tr>\n")
    archivo.write("</table>\n")
    archivo.write("<p>Total encontrados: "+str(encontrados)+"</p>\n")
    finalizarHtmlAux(archivo)
    archivo.close()
    print("Reporte creado satisfactoriamente")

#Funcion 9 submenu reportes:
def reporteLugaresDonacion(pDonadores,pLugaresDonacion):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores y el diccionario de lugares de donación
    -Salida:
        Se genera un reporte HTML con la cantidad de donadores por provincia
        y los recintos posibles de recaudación
    '''
    archivo=open("reporteLugaresDonacion.html","w",encoding="utf-8")
    iniciarHtmlAux(archivo,"Reporte de lugares de donación")
    archivo.write("<table border='1'>\n")
    archivo.write("<tr>")
    archivo.write("<th>Provincia</th>")
    archivo.write("<th>Cantidad de donadores registrados</th>")
    archivo.write("<th>Recintos posibles de recaudación</th>")
    archivo.write("</tr>\n")
    provincia=1
    while provincia<=7:
        cantidad=0
        for donador in pDonadores:
            if len(donador)>=10:
                if int(donador[1][0])==provincia:
                    cantidad+=1
        archivo.write("<tr>")
        archivo.write("<td>"+obtenerProvinciaTextoAux(provincia)+"</td>")
        archivo.write("<td>"+str(cantidad)+"</td>")
        if provincia in pLugaresDonacion:
            archivo.write("<td>")
            i=0
            while i<len(pLugaresDonacion[provincia]):
                archivo.write(pLugaresDonacion[provincia][i])
                if i<len(pLugaresDonacion[provincia])-1:
                    archivo.write("<br>")
                i+=1
            archivo.write("</td>")
        else:
            archivo.write("<td>No hay lugares registrados</td>")
        archivo.write("</tr>\n")
        provincia+=1
    archivo.write("</table>\n")
    finalizarHtmlAux(archivo)
    archivo.close()
    print("Reporte creado satisfactoriamente")

def crearBoton(pVentana,pTexto,pComando):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la ventana, el texto del botón y la función que ejecutará
    -Salida:
        Se crea y muestra un botón en la ventana
    '''
    boton=Button(pVentana,text=pTexto,font=("Century Gothic",11),width=35,command=pComando)
    boton.pack(pady=5)
    return boton

def mostrarMensaje(pTexto):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe el texto que se desea mostrar
    -Salida:
        Se muestra una ventana pequeña con el mensaje indicado
    '''
    ventanaMensaje=Toplevel()
    ventanaMensaje.title("Mensaje")
    Label(ventanaMensaje,text=pTexto,font=("Century Gothic",14)).pack(padx=20,pady=20)

def regresarMenuPrincipal(pVentanaPrincipal,pVentanaActual):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la ventana principal y la ventana actual
    -Salida:
        Se cierra la ventana actual y se muestra la principal
    '''
    pVentanaActual.destroy()
    pVentanaPrincipal.deiconify()

def registrarDonadorTk(pVentanaPrincipal,pVentanaInsertar,pDonadores,pNombre,pApellido1,pApellido2,pCedula,pTipoSangre,pTiposSangre,pFecha,pSexo,pCorreo,pTelefono,pPeso,pBoton3,pBoton4,pBoton6):
    '''
    Funcionamiento:
    -Entrada:
        Se reciben las cajas de texto y variables usadas en la ventana de insertar donador
    -Salida:
        Se llama a la función insertarDonador y se muestra el mensaje correspondiente
    '''
    tipoSangre="0"
    for i in range(len(pTiposSangre)):
        if pTiposSangre[i]==pTipoSangre.get():
            tipoSangre=str(i+1)
    mensaje=insertarDonador(pDonadores,pNombre.get(),pApellido1.get(),pApellido2.get(),pCedula.get(),tipoSangre,pFecha.get(),pSexo.get(),pCorreo.get(),pTelefono.get(),pPeso.get())
    mostrarMensaje(mensaje)
    if "Donador registrado correctamente" in mensaje:
        pBoton3.config(state="normal")
        pBoton4.config(state="normal")
        pBoton6.config(state="normal")
        regresarMenuPrincipal(pVentanaPrincipal,pVentanaInsertar)

def limpiarInsertarDonadorTk(pNombre,pApellido1,pApellido2,pCedula,pTipoSangre,pFecha,pSexo,pCorreo,pTelefono,pPeso):
    '''
    Funcionamiento:
    -Entrada:
        Se reciben las cajas de texto y variables del formulario
    -Salida:
        Se limpian todos los datos de la ventana
    '''
    pNombre.delete(0,END)
    pApellido1.delete(0,END)
    pApellido2.delete(0,END)
    pCedula.delete(0,END)
    pFecha.delete(0,END)
    pCorreo.delete(0,END)
    pTelefono.delete(0,END)
    pPeso.delete(0,END)
    pTipoSangre.set("O+")
    pSexo.set("1")

def abrirInsertarDonador(pVentana,pDonadores,pTiposSangre):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la ventana principal, la matriz de donadores y la tupla de tipos de sangre
    -Salida:
        Se muestra la ventana para insertar un nuevo donador
    '''
    pVentana.withdraw()
    ventanaInsertar=Toplevel()
    ventanaInsertar.title("Insertar donador")
    ventanaInsertar.geometry("600x650")
    Label(ventanaInsertar,text="INSERTAR DONADOR",font=("Century Gothic",14,"bold")).pack(pady=15)
    frame=Frame(ventanaInsertar)
    frame.pack()
    Label(frame,text="Nombre:",font=("Century Gothic",12)).grid(row=0,column=0,pady=5,sticky="w")
    nombre=Entry(frame,font=("Century Gothic",12))
    nombre.grid(row=0,column=1,pady=5)
    Label(frame,text="Primer apellido:",font=("Century Gothic",12)).grid(row=1,column=0,pady=5,sticky="w")
    apellido1=Entry(frame,font=("Century Gothic",12))
    apellido1.grid(row=1,column=1,pady=5)
    Label(frame,text="Segundo apellido:",font=("Century Gothic",12)).grid(row=2,column=0,pady=5,sticky="w")
    apellido2=Entry(frame,font=("Century Gothic",12))
    apellido2.grid(row=2,column=1,pady=5)
    Label(frame,text="Cédula (#-####-####):",font=("Century Gothic",12)).grid(row=3,column=0,pady=5,sticky="w")
    cedula=Entry(frame,font=("Century Gothic",12))
    cedula.grid(row=3,column=1,pady=5)
    Label(frame,text="Tipo de sangre:",font=("Century Gothic",12)).grid(row=4,column=0,pady=5,sticky="w")
    tipoSangre=StringVar()
    tipoSangre.set(pTiposSangre[0])
    OptionMenu(frame,tipoSangre,*pTiposSangre).grid(row=4,column=1,pady=5,sticky="w")
    sexo=StringVar()
    sexo.set("1")
    Radiobutton(frame,text="Masculino",variable=sexo,value="1",font=("Century Gothic",12)).grid(row=5,column=1,sticky="w")
    Radiobutton(frame,text="Femenino",variable=sexo,value="2",font=("Century Gothic",12)).grid(row=6,column=1,sticky="w")
    Label(frame,text="Fecha nacimiento (DD/MM/AAAA):",font=("Century Gothic",12)).grid(row=7,column=0,pady=5,sticky="w")
    fecha=Entry(frame,font=("Century Gothic",12))
    fecha.grid(row=7,column=1,pady=5)
    Label(frame,text="Correo:",font=("Century Gothic",12)).grid(row=8,column=0,pady=5,sticky="w")
    correo=Entry(frame,font=("Century Gothic",12))
    correo.grid(row=8,column=1,pady=5)
    Label(frame,text="Teléfono (####-####):",font=("Century Gothic",12)).grid(row=9,column=0,pady=5,sticky="w")
    telefono=Entry(frame,font=("Century Gothic",12))
    telefono.grid(row=9,column=1,pady=5)
    Label(frame,text="Peso:",font=("Century Gothic",12)).grid(row=10,column=0,pady=5,sticky="w")
    peso=Entry(frame,font=("Century Gothic",12))
    peso.grid(row=10,column=1,pady=5)
    Button(ventanaInsertar,text="Registrar",font=("Century Gothic",12,"bold"),width=35,command=lambda:registrarDonadorTk(pVentana,ventanaInsertar,pDonadores,nombre,apellido1,apellido2,cedula,tipoSangre,pTiposSangre,fecha,sexo,correo,telefono,peso)).pack(pady=5)
    Button(ventanaInsertar,text="Limpiar",font=("Century Gothic",12,"bold"),width=35,command=lambda:limpiarInsertarDonadorTk(nombre,apellido1,apellido2,cedula,tipoSangre,fecha,sexo,correo,telefono,peso)).pack(pady=5)
    Button(ventanaInsertar,text="Regresar",font=("Century Gothic",12,"bold"),width=35,command=lambda:regresarMenuPrincipal(pVentana,ventanaInsertar)).pack(pady=5)

def generarDonadoresTk(pVentanaPrincipal,pVentanaGenerar,pDonadores,pTiposSangre,pCorreos,pCantidad,pBoton3,pBoton4,pBoton6):
    '''
    Funcionamiento:
    -Entrada:
        Se reciben los datos escritos en la ventana para generar donadores
    -Salida:
        Se generan donadores y se muestra el mensaje correspondiente
    '''
    mensaje=generarDonadores(pDonadores,pTiposSangre,pCorreos,pCantidad.get())
    mostrarMensaje(mensaje)
    if "Se generaron correctamente" in mensaje:
        pBoton3.config(state="normal")
        pBoton4.config(state="normal")
        pBoton6.config(state="normal")
        regresarMenuPrincipal(pVentanaPrincipal,pVentanaGenerar)

def abrirGenerarDonadores(pVentana,pDonadores,pTiposSangre,pCorreos,pBoton3,pBoton4,pBoton6):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la ventana principal, la matriz de donadores, tipos de sangre y correos
    -Salida:
        Se muestra la ventana para generar donadores
    '''
    pVentana.withdraw()
    ventanaGenerar=Toplevel()
    ventanaGenerar.title("Generar donadores")
    ventanaGenerar.geometry("500x250")
    Label(ventanaGenerar,text="GENERAR DONADORES",font=("Century Gothic",14,"bold")).pack(pady=15)
    Label(ventanaGenerar,text="Cantidad:",font=("Century Gothic",12)).pack()
    cantidad=Entry(ventanaGenerar,font=("Century Gothic",12),width=35)
    cantidad.pack(pady=5)
    Button(ventanaGenerar,text="Generar",font=("Century Gothic",12,"bold"),width=35,command=lambda:generarDonadoresTk(pVentana,ventanaGenerar,pDonadores,pTiposSangre,pCorreos,cantidad,pBoton3,pBoton4,pBoton6)).pack(pady=5)
    Button(ventanaGenerar,text="Regresar",font=("Century Gothic",12,"bold"),width=35,command=lambda:regresarMenuPrincipal(pVentana,ventanaGenerar)).pack(pady=5)