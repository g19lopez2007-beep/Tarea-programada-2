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
    nuevo=[nombre,pCedula,tipoSangre,sexo,fechaNacimiento,float(pPeso),pCorreo,pTelefono,1,0]
    pDonadores.append(nuevo)
    guardarDonadoresAux(pDonadores)
    return "Donador registrado correctamente"

#Funcion 2 del menu principal:
def generarDonadores(pBaseDatos,pTiposSangre,pCorreos):
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
        nombre=generarNombreAux()
        cedula=generarCedulaAux()
        tipoSangre=random.randint(0,len(pTiposSangre)-1)
        sexo=random.choice((True,False))
        fechaNacimiento=generarFechaNacimientoAux(añoMinimo)
        peso=random.randint(45,130)
        correo=generarCorreoAux(nombre[0],nombre[1],pCorreos)
        telefono=generarTelefonoAux()
        estado=random.choice((1,0))
        if estado==1:
            justificacion=0
            contadorActivos+=1
        else:
            justificacion=random.randint(1,7)
            contadorInactivos+=1
        pBaseDatos.append([nombre,cedula,tipoSangre,sexo,fechaNacimiento,float(peso),correo,telefono,estado,justificacion])
    print("Se generaron correctamente",cantidad,"donadores\nDonadores activos:",contadorActivos,"\nDonadores no activos:",contadorInactivos)
    guardarDonadoresAux(pBaseDatos)
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





#Funcion 6 del menu principal:

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
