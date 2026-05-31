#Creado por Gustavo López y Mel Acuña
#Fecha de creacion: 14/5/26
#Ultima fecha de modificacion: 30/5/26
#Version de python: 3.14

import pickle
import random
from tkinter import messagebox
from funcionesAux import *
from tkinter import *
import webbrowser

#Funcion principal de carga inicial del menu
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

#Funcion principal de la opcion 1 del menu
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
    nuevo=[nombre,pCedula,tipoSangre,sexo,fechaNacimiento,round(float(pPeso),2),pCorreo,pTelefono,estado,justificacion]
    pDonadores.append(nuevo)
    guardarDonadoresAux(pDonadores)
    if estado==1:
        return "Donador registrado correctamente"
    return "Donador registrado correctamente (Estado inactivo: "+justificacion+")"

#Funcion principal de la opcion 1 del menu
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
    if "Donador registrado correctamente" in mensaje:
        pBoton3.config(state="normal")
        pBoton4.config(state="normal")
        pBoton6.config(state="normal")
        messagebox.showinfo("Banco de Sangre",mensaje)
        regresarMenuPrincipal(pVentanaPrincipal,pVentanaInsertar)
    else:
        messagebox.showinfo("Error",mensaje)

#Funcion principal de la opcion 1 del menu
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

#Funcion principal de la opcion 1 del menu
def abrirInsertarDonador(pVentana,pDonadores,pTiposSangre,pBoton3,pBoton4,pBoton6):
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
    Button(ventanaInsertar,text="Registrar",font=("Century Gothic",12,"bold"),width=35,command=lambda:registrarDonadorTk(pVentana,ventanaInsertar,pDonadores,nombre,apellido1,apellido2,cedula,tipoSangre,pTiposSangre,fecha,sexo,correo,telefono,peso,pBoton3,pBoton4,pBoton6)).pack(pady=5)
    Button(ventanaInsertar,text="Limpiar",font=("Century Gothic",12,"bold"),width=35,command=lambda:limpiarInsertarDonadorTk(nombre,apellido1,apellido2,cedula,tipoSangre,fecha,sexo,correo,telefono,peso)).pack(pady=5)
    Button(ventanaInsertar,text="Regresar",font=("Century Gothic",12,"bold"),width=35,command=lambda:regresarMenuPrincipal(pVentana,ventanaInsertar)).pack(pady=5)

#Funcion principal de la opcion 2 del menu
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
        peso=round(random.uniform(51,119),2)
        correo=generarCorreoAux(nombre[0],nombre[1],pCorreos)
        telefono=generarTelefonoAux()
        estado=1
        justificacion=0
        contadorActivos+=1
        pBaseDatos.append([nombre,cedula,tipoSangre,sexo,fechaNacimiento,peso,correo,telefono,estado,justificacion])
    guardarDonadoresAux(pBaseDatos)
    return "Se generaron correctamente "+str(cantidad)+" donadores"

#Funcion principal de la opcion 2 del menu
def generarDonadoresTk(pVentanaPrincipal,pVentanaGenerar,pDonadores,pTiposSangre,pCorreos,pCantidad,pBoton3,pBoton4,pBoton6):
    '''
    Funcionamiento:
    -Entrada:
        Se reciben los datos escritos en la ventana para generar donadores
    -Salida:
        Se generan donadores y se muestra el mensaje correspondiente
    '''
    mensaje=generarDonadores(pDonadores,pTiposSangre,pCorreos,pCantidad.get())
    if "Se generaron correctamente" in mensaje:
        pBoton3.config(state="normal")
        pBoton4.config(state="normal")
        pBoton6.config(state="normal")
        messagebox.showinfo("Banco de Sangre",mensaje)
        regresarMenuPrincipal(pVentanaPrincipal,pVentanaGenerar)
    else:
        messagebox.showinfo("Error",mensaje)

#Funcion principal de la opcion 2 del menu
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

#Funcion principal de la opcion 3 del menu
def actualizarDonadorTk(pDonadores,pPosicion,pNombre,pApellido1,pApellido2,pTipoSangre,pTiposSangre,pFecha,pSexo,pCorreo,pTelefono,pPeso):
    '''
    Funcionamiento:
    -Entrada:
        Se reciben los nuevos datos del donador y la posición en la matriz
    -Salida:
        Se actualiza el donador si los datos son válidos o se devuelve un mensaje de error
    '''
    if pNombre.strip()=="" or pApellido1.strip()=="" or pApellido2.strip()=="" or pFecha.strip()=="" or pCorreo.strip()=="" or pTelefono.strip()=="" or pPeso.strip()=="":
        return "Todos los datos son requeridos"
    fecha=validarFechaAux(pFecha)
    correo=validarCorreoAux(pCorreo)
    telefono=validarTelefonoAux(pTelefono)
    pesoValido=validarPesoAux(pPeso)
    tipoSangreValido=validarTipoSangreAux(pTipoSangre,pTiposSangre)
    if fecha!=True:
        return fecha
    if correo!=True:
        return correo
    if telefono!=True:
        return telefono
    if pesoValido!=True:
        return pesoValido
    if tipoSangreValido!=True:
        return tipoSangreValido
    if pSexo!="1" and pSexo!="2":
        return "El sexo debe ser 1 o 2"
    nombre=[pNombre,pApellido1,pApellido2]
    tipoSangre=int(pTipoSangre)-1
    if pSexo=="1":
        sexo=True
    else:
        sexo=False
    fechaNacimiento=(int(pFecha[0:2]),int(pFecha[3:5]),int(pFecha[6:10]))
    peso=round(float(pPeso),2)
    justificacionEstado=obtenerJustificacionEstadoAux(fechaNacimiento,pPeso)
    if justificacionEstado==True:
        estado=1
        justificacion=0
    else:
        estado=0
        justificacion=justificacionEstado
    actualizarDatosDonadorAux(pPosicion,pDonadores,nombre,tipoSangre,sexo,fechaNacimiento,peso,pCorreo,pTelefono,estado,justificacion)
    guardarDonadoresAux(pDonadores)
    return "Datos actualizados correctamente"

#Funcion principal de la opcion 3 del menu
def confirmarActualizarDonadorTk(pVentanaPrincipal,pVentanaActualizar,pDonadores,pPosicion,pNombre,pApellido1,pApellido2,pTipoSangre,pTiposSangre,pFecha,pSexo,pCorreo,pTelefono,pPeso):
    '''
    Funcionamiento:
    -Entrada:
        Se reciben las entradas del formulario de actualización
    -Salida:
        Se valida, se confirma la actualización y se muestra el mensaje correspondiente
    '''
    tipoSangre="0"
    for i in range(len(pTiposSangre)):
        if pTiposSangre[i]==pTipoSangre.get():
            tipoSangre=str(i+1)
    mensaje=actualizarDonadorTk(pDonadores,pPosicion,pNombre.get(),pApellido1.get(),pApellido2.get(),tipoSangre,pTiposSangre,pFecha.get(),pSexo.get(),pCorreo.get(),pTelefono.get(),pPeso.get())
    if mensaje!="Datos actualizados correctamente":
        messagebox.showinfo("Banco de Sangre",mensaje)
        return
    respuesta=messagebox.askyesno("Confirmar actualización","¿Desea actualizar los datos del donador?")
    if respuesta==False:
        messagebox.showinfo("Banco de Sangre","Datos No actualizados.")
        return
    messagebox.showinfo("Banco de Sangre",mensaje)
    regresarMenuPrincipal(pVentanaPrincipal,pVentanaActualizar)

#Funcion principal de la opcion 3 del menu
def abrirFormularioActualizarDonador(pVentanaPrincipal,pVentanaBuscar,pDonadores,pPosicion,pTiposSangre):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la ventana de búsqueda, la matriz, la posición del donador y los tipos de sangre
    -Salida:
        Se muestra el formulario completo para actualizar el donador
    '''
    pVentanaBuscar.destroy()
    ventanaActualizar=Toplevel()
    ventanaActualizar.title("Actualizar donador")
    ventanaActualizar.geometry("600x650")
    donador=pDonadores[pPosicion]
    Label(ventanaActualizar,text="ACTUALIZAR DONADOR",font=("Century Gothic",14,"bold")).pack(pady=15)
    frame=Frame(ventanaActualizar)
    frame.pack()
    Label(frame,text="Nombre:",font=("Century Gothic",12)).grid(row=0,column=0,pady=5,sticky="w")
    nombre=Entry(frame,font=("Century Gothic",12))
    nombre.insert(0,donador[0][0])
    nombre.grid(row=0,column=1,pady=5)
    Label(frame,text="Primer apellido:",font=("Century Gothic",12)).grid(row=1,column=0,pady=5,sticky="w")
    apellido1=Entry(frame,font=("Century Gothic",12))
    apellido1.insert(0,donador[0][1])
    apellido1.grid(row=1,column=1,pady=5)
    Label(frame,text="Segundo apellido:",font=("Century Gothic",12)).grid(row=2,column=0,pady=5,sticky="w")
    apellido2=Entry(frame,font=("Century Gothic",12))
    apellido2.insert(0,donador[0][2])
    apellido2.grid(row=2,column=1,pady=5)
    Label(frame,text="Cédula:",font=("Century Gothic",12)).grid(row=3,column=0,pady=5,sticky="w")
    cedula=Entry(frame,font=("Century Gothic",12))
    cedula.insert(0,donador[1])
    cedula.config(state="readonly")
    cedula.grid(row=3,column=1,pady=5)
    Label(frame,text="Tipo de sangre:",font=("Century Gothic",12)).grid(row=4,column=0,pady=5,sticky="w")
    tipoSangre=StringVar()
    tipoSangre.set(pTiposSangre[donador[2]])
    OptionMenu(frame,tipoSangre,*pTiposSangre).grid(row=4,column=1,pady=5,sticky="w")
    sexo=StringVar()
    if donador[3]==True:
        sexo.set("1")
    else:
        sexo.set("2")
    Radiobutton(frame,text="Masculino",variable=sexo,value="1",font=("Century Gothic",12)).grid(row=5,column=1,sticky="w")
    Radiobutton(frame,text="Femenino",variable=sexo,value="2",font=("Century Gothic",12)).grid(row=6,column=1,sticky="w")
    Label(frame,text="Fecha nacimiento (DD/MM/AAAA):",font=("Century Gothic",12)).grid(row=7,column=0,pady=5,sticky="w")
    fecha=Entry(frame,font=("Century Gothic",12))
    fecha.insert(0,obtenerFechaTextoAux(donador[4]))
    fecha.grid(row=7,column=1,pady=5)
    Label(frame,text="Correo:",font=("Century Gothic",12)).grid(row=8,column=0,pady=5,sticky="w")
    correo=Entry(frame,font=("Century Gothic",12))
    correo.insert(0,donador[6])
    correo.grid(row=8,column=1,pady=5)
    Label(frame,text="Teléfono (####-####):",font=("Century Gothic",12)).grid(row=9,column=0,pady=5,sticky="w")
    telefono=Entry(frame,font=("Century Gothic",12))
    telefono.insert(0,donador[7])
    telefono.grid(row=9,column=1,pady=5)
    Label(frame,text="Peso:",font=("Century Gothic",12)).grid(row=10,column=0,pady=5,sticky="w")
    peso=Entry(frame,font=("Century Gothic",12))
    peso.insert(0,str(donador[5]))
    peso.grid(row=10,column=1,pady=5)
    Button(ventanaActualizar,text="Actualizar",font=("Century Gothic",12,"bold"),width=35,command=lambda:confirmarActualizarDonadorTk(pVentanaPrincipal,ventanaActualizar,pDonadores,pPosicion,nombre,apellido1,apellido2,tipoSangre,pTiposSangre,fecha,sexo,correo,telefono,peso)).pack(pady=5)
    Button(ventanaActualizar,text="Regresar",font=("Century Gothic",12,"bold"),width=35,command=lambda:regresarMenuPrincipal(pVentanaPrincipal,ventanaActualizar)).pack(pady=5)

#Funcion principal de la opcion 3 del menu
def buscarActualizarDonadorTk(pVentanaPrincipal,pVentanaBuscar,pDonadores,pCedula,pTiposSangre):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la cédula ingresada para buscar el donador
    -Salida:
        Se abre el formulario de actualización o se muestra un mensaje de error
    '''
    cedula=pCedula.get()
    validarCedula=validarCedulaAux(cedula)
    if validarCedula!=True:
        messagebox.showinfo("Banco de Sangre",validarCedula)
        return
    posicion=buscarDonadorCedulaAux(cedula,pDonadores)
    if posicion==-1:
        messagebox.showinfo("Banco de Sangre","La persona con el número de cédula: "+cedula+" no está registrada en la base de datos del Banco de Sangre aún.")
        return
    abrirFormularioActualizarDonador(pVentanaPrincipal,pVentanaBuscar,pDonadores,posicion,pTiposSangre)

#Funcion principal de la opcion 3 del menu
def abrirActualizarDonador(pVentana,pDonadores,pTiposSangre):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la ventana principal, la matriz de donadores y los tipos de sangre
    -Salida:
        Se muestra la ventana para buscar el donador que se desea actualizar
    '''
    pVentana.withdraw()
    ventanaBuscar=Toplevel()
    ventanaBuscar.title("Actualizar donador")
    ventanaBuscar.geometry("500x250")
    Label(ventanaBuscar,text="BUSCAR DONADOR",font=("Century Gothic",14,"bold")).pack(pady=15)
    Label(ventanaBuscar,text="Cédula (#-####-####):",font=("Century Gothic",12)).pack()
    cedula=Entry(ventanaBuscar,font=("Century Gothic",12),width=35)
    cedula.pack(pady=5)
    Button(ventanaBuscar,text="Buscar",font=("Century Gothic",12,"bold"),width=35,command=lambda:buscarActualizarDonadorTk(pVentana,ventanaBuscar,pDonadores,cedula,pTiposSangre)).pack(pady=5)
    Button(ventanaBuscar,text="Regresar",font=("Century Gothic",12,"bold"),width=35,command=lambda:regresarMenuPrincipal(pVentana,ventanaBuscar)).pack(pady=5)

#Funcion principal de la opcion 4 del menu
def eliminarDonadorTk(pDonadores,pCedula,pJustificacion):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores, la cédula y la justificación ingresada desde tkinter
    -Salida:
        Se cambia el estado del donador a inactivo sin eliminarlo físicamente
    '''
    validarCedula=validarCedulaAux(pCedula)
    if validarCedula!=True:
        return validarCedula
    posicion=buscarDonadorCedulaAux(pCedula,pDonadores)
    if posicion==-1:
        return "La persona con el número de cédula: "+pCedula+" no está registrada."
    if pJustificacion.strip()=="":
        return "Debe ingresar una justificación"
    try:
        justificacion=int(pJustificacion)
    except:
        return "La justificación debe ser un número del 1 al 7"
    if justificacion<1 or justificacion>7:
        return "La justificación debe ser un número del 1 al 7"
    justificacionCompleta=obtenerJustificacionAux(justificacion)
    inactivarDonadorAux(posicion,pDonadores,justificacionCompleta)
    return "Donador eliminado correctamente"

#Funcion principal de la opcion 4 del menu
def confirmarEliminarDonadorTk(pVentanaEliminar,pDonadores,pEntradaCedula,pEntradaJustificacion):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la ventana de eliminar, la matriz de donadores, la cédula y la justificación
    -Salida:
        Se confirma la eliminación del donador y se muestra el resultado
    '''
    respuesta=messagebox.askyesno("Confirmar eliminación","¿Desea confirmar la eliminación del donador?")
    if respuesta==True:
        mensaje=eliminarDonadorTk(pDonadores,pEntradaCedula.get(),pEntradaJustificacion.get())
        messagebox.showinfo("Banco de Sangre",mensaje)
        if mensaje=="Donador eliminado correctamente":
            pVentanaEliminar.destroy()
    else:
        messagebox.showinfo("Banco de Sangre","Donador NO eliminado")

#Funcion principal de la opcion 4 del menu
def mostrarJustificacionesTk():
    '''
    Funcionamiento:
    -Entrada:
        No recibe datos
    -Salida:
        Se muestran las justificaciones disponibles para eliminar un donador
    '''
    ventanaJustificaciones=Toplevel()
    ventanaJustificaciones.title("Justificaciones")
    ventanaJustificaciones.geometry("700x350")
    texto="1.Enfermedades infecciosas o crónicas\n2.Conductas de riesgo\n3.Factores de salud física\n4.Procedimientos médicos recientes\n5.Uso de medicamentos\n6.Estilo de vida o viajes recientes\n7.Embarazo, lactancia o menstruación"
    Label(ventanaJustificaciones,text=texto,font=("Century Gothic",12),justify="left").pack(padx=20,pady=20)
    Button(ventanaJustificaciones,text="Cerrar",font=("Century Gothic",12,"bold"),width=35,command=ventanaJustificaciones.destroy).pack(pady=10)

#Funcion principal de la opcion 4 del menu
def ventanaEliminarDonador(pDonadores):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores
    -Salida:
        Se muestra una ventana para eliminar lógicamente un donador
    '''
    ventanaEliminar=Toplevel()
    ventanaEliminar.title("Eliminar donador")
    ventanaEliminar.geometry("400x400")
    Label(ventanaEliminar,text="ELIMINAR DONADOR",font=("Century Gothic",14,"bold")).pack(pady=10)
    Label(ventanaEliminar,text="Digite la cédula").pack()
    entradaCedula=Entry(ventanaEliminar)
    entradaCedula.pack(pady=5)
    Label(ventanaEliminar,text="Digite la justificación").pack()
    entradaJustificacion=Entry(ventanaEliminar)
    entradaJustificacion.pack(pady=5)
    Button(ventanaEliminar,text="Eliminar",font=("Century Gothic",12,"bold"),width=35,command=lambda:confirmarEliminarDonadorTk(ventanaEliminar,pDonadores,entradaCedula,entradaJustificacion)).pack(pady=10)
    Button(ventanaEliminar,text="Ver justificaciones",font=("Century Gothic",12,"bold"),width=35,command=mostrarJustificacionesTk).pack(pady=5)
    Button(ventanaEliminar,text="Regresar",font=("Century Gothic",12,"bold"),width=35,command=ventanaEliminar.destroy).pack(pady=5)

#Funcion principal de la opcion 5 del menu
def insertarLugarDonacionTk(pLugaresDonacion,pProvincia,pLugar):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe el diccionario de lugares, la provincia y el lugar ingresado
    -Salida:
        Se agrega el lugar si cumple con las validaciones o se devuelve un mensaje de error
    '''
    validarProvincia=validarProvinciaAux(pProvincia)
    if validarProvincia!=True:
        return validarProvincia
    lugar=pLugar.strip()
    validarLugar=validarLugarDonacionAux(lugar)
    if validarLugar!=True:
        return validarLugar
    validarRepetido=validarLugarRepetidoAux(pProvincia,lugar,pLugaresDonacion)
    if validarRepetido!=True:
        return validarRepetido
    provincia=int(pProvincia)
    if provincia not in pLugaresDonacion:
        pLugaresDonacion[provincia]=[]
    pLugaresDonacion[provincia].append(lugar)
    guardarLugaresDonacionAux(pLugaresDonacion)
    return "Lugar agregado correctamente"

#Funcion principal de la opcion 5 del menu
def confirmarInsertarLugarDonacionTk(pVentanaPrincipal,pVentanaLugar,pLugaresDonacion,pProvincia,pLugar):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la ventana principal, la ventana de lugar, el diccionario de lugares, la provincia seleccionada y el lugar escrito
    -Salida:
        Se muestra el resultado y regresa al menú solo si se insertó correctamente
    '''
    provincia="0"
    if pProvincia.get()=="San José":
        provincia="1"
    elif pProvincia.get()=="Alajuela":
        provincia="2"
    elif pProvincia.get()=="Cartago":
        provincia="3"
    elif pProvincia.get()=="Heredia":
        provincia="4"
    elif pProvincia.get()=="Guanacaste":
        provincia="5"
    elif pProvincia.get()=="Puntarenas":
        provincia="6"
    elif pProvincia.get()=="Limón":
        provincia="7"
    mensaje=insertarLugarDonacionTk(pLugaresDonacion,provincia,pLugar.get("1.0",END))
    messagebox.showinfo("Banco de Sangre",mensaje)
    if mensaje=="Lugar agregado correctamente":
        regresarMenuPrincipal(pVentanaPrincipal,pVentanaLugar)

#Funcion principal de la opcion 5 del menu
def abrirInsertarLugarDonacion(pVentana,pLugaresDonacion):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la ventana principal y el diccionario de lugares de donación
    -Salida:
        Se muestra la ventana para insertar lugares de donación usando tkinter
    '''
    pVentana.withdraw()
    ventanaLugar=Toplevel()
    ventanaLugar.title("Insertar lugar de donación")
    ventanaLugar.geometry("550x400")
    Label(ventanaLugar,text="INSERTAR LUGAR DE DONACIÓN",font=("Century Gothic",14,"bold")).pack(pady=15)
    Label(ventanaLugar,text="Provincia:",font=("Century Gothic",12)).pack()
    provincia=StringVar()
    provincia.set("San José")
    OptionMenu(ventanaLugar,provincia,"San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón").pack(pady=5)
    Label(ventanaLugar,text="Nuevo lugar:",font=("Century Gothic",12)).pack()
    lugar=Text(ventanaLugar,font=("Century Gothic",12),width=35,height=4)
    lugar.pack(pady=5)
    Button(ventanaLugar,text="Insertar",font=("Century Gothic",12,"bold"),width=35,command=lambda:confirmarInsertarLugarDonacionTk(pVentana,ventanaLugar,pLugaresDonacion,provincia,lugar)).pack(pady=5)
    Button(ventanaLugar,text="Salir",font=("Century Gothic",12,"bold"),width=35,command=lambda:regresarMenuPrincipal(pVentana,ventanaLugar)).pack(pady=5)

#Funcion principal de la opcion 1 del submenu reportes
def reporteDonantesProvincia(pDonadores):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores
    -Salida:
        Se muestra ventana Tkinter para seleccionar provincia y generar reporte HTML
    '''
    ventana=Toplevel()
    ventana.title("Donantes por provincia")
    ventana.geometry("500x250")
    Label(ventana,text="DONANTES POR PROVINCIA",font=("Century Gothic",14,"bold")).pack(pady=15)
    Label(ventana,text="Provincia:",font=("Century Gothic",12)).pack()
    provincia=StringVar()
    provincia.set("San José")
    OptionMenu(ventana,provincia,"San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón").pack(pady=5)
    Button(ventana,text="Generar reporte",font=("Century Gothic",12,"bold"),width=35,command=lambda:generarReporteDonantesProvincia(ventana,pDonadores,provincia)).pack(pady=5)
    Button(ventana,text="Regresar",font=("Century Gothic",12,"bold"),width=35,command=ventana.destroy).pack(pady=5)

#Funcion principal de la opcion 1 del submenu reportes
def generarReporteDonantesProvincia(pVentana,pDonadores,pProvincia):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la ventana, la matriz de donadores y la provincia seleccionada
    -Salida:
        Se genera el reporte HTML con los donadores activos de esa provincia, ordenados por nombre
    '''
    nombresProvincia={"San José":1,"Alajuela":2,"Cartago":3,"Heredia":4,"Guanacaste":5,"Puntarenas":6,"Limón":7}
    numeroProvincia=nombresProvincia[pProvincia.get()]
    lista=[]
    for donador in pDonadores:
        if len(donador)>=10:
            if donador[8]==1 and int(donador[1][0])==numeroProvincia:
                lista.append(donador)
    if len(lista)==0:
        messagebox.showinfo("Banco de Sangre","Reporte no creado.")
        return
    i=0
    while i<len(lista)-1:
        j=0
        while j<len(lista)-1-i:
            if obtenerNombreCompletoAux(lista[j][0])>obtenerNombreCompletoAux(lista[j+1][0]):
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
            j+=1
        i+=1
    archivo=open("reporteDonantesProvincia.html","w",encoding="utf-8")
    iniciarHtmlAux(archivo,"Reporte de donantes por provincia: "+pProvincia.get())
    archivo.write("<table border='1'>\n<tr><th>Cédula</th><th>Nombre completo</th><th>Fecha de nacimiento</th><th>Teléfono</th><th>Correo</th></tr>\n")
    for donador in lista:
        archivo.write("<tr>")
        archivo.write("<td>"+donador[1]+"</td>")
        archivo.write("<td>"+obtenerNombreCompletoAux(donador[0])+"</td>")
        archivo.write("<td>"+obtenerFechaTextoAux(donador[4])+"</td>")
        archivo.write("<td>"+donador[7]+"</td>")
        archivo.write("<td>"+donador[6]+"</td>")
        archivo.write("</tr>\n")
    archivo.write("</table>\n")
    archivo.write("<p>Total encontrados: "+str(len(lista))+"</p>\n")
    finalizarHtmlAux(archivo)
    archivo.close()
    webbrowser.open("reporteDonantesProvincia.html")
    messagebox.showinfo("Banco de Sangre","Reporte creado satisfactoriamente")
    pVentana.destroy()

#Funcion principal de la opcion 2 del submenu reportes
def reporteRangoEdad(pDonadores):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores
    -Salida:
        Se muestra ventana Tkinter para ingresar rango de edad y generar reporte HTML
    '''
    ventana=Toplevel()
    ventana.title("Por rango de edad")
    ventana.geometry("500x300")
    Label(ventana,text="POR RANGO DE EDAD",font=("Century Gothic",14,"bold")).pack(pady=15)
    frame=Frame(ventana)
    frame.pack()
    Label(frame,text="Edad inicial (18-65):",font=("Century Gothic",12)).grid(row=0,column=0,pady=5,sticky="w")
    edadInicial=Entry(frame,font=("Century Gothic",12))
    edadInicial.grid(row=0,column=1,pady=5)
    Label(frame,text="Edad final (18-65):",font=("Century Gothic",12)).grid(row=1,column=0,pady=5,sticky="w")
    edadFinal=Entry(frame,font=("Century Gothic",12),state="disabled")
    edadFinal.grid(row=1,column=1,pady=5)
    def activarEdadFinal(event):
        try:
            val=int(edadInicial.get())
            if 18<=val<=65:
                edadFinal.config(state="normal")
            else:
                edadFinal.config(state="disabled")
                edadFinal.delete(0,END)
        except:
            edadFinal.config(state="disabled")
            edadFinal.delete(0,END)
    edadInicial.bind("<KeyRelease>",activarEdadFinal)
    Button(ventana,text="Generar reporte",font=("Century Gothic",12,"bold"),width=35,command=lambda:generarReporteRangoEdad(ventana,pDonadores,edadInicial,edadFinal)).pack(pady=5)
    Button(ventana,text="Regresar",font=("Century Gothic",12,"bold"),width=35,command=ventana.destroy).pack(pady=5)

#Funcion principal de la opcion 2 del submenu reportes
def generarReporteRangoEdad(pVentana,pDonadores,pEdadInicial,pEdadFinal):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la ventana, la matriz de donadores y las entradas de edad
    -Salida:
        Se genera el reporte HTML con donadores activos en el rango de edad indicado
    '''
    try:
        edadMinima=int(pEdadInicial.get())
    except:
        messagebox.showinfo("Banco de Sangre","La edad inicial debe ser numérica")
        return
    if edadMinima<18 or edadMinima>65:
        messagebox.showinfo("Banco de Sangre","La edad inicial debe estar entre 18 y 65 años")
        return
    edadMaxima=edadMinima
    if pEdadFinal.get().strip()!="":
        try:
            edadMaxima=int(pEdadFinal.get())
        except:
            messagebox.showinfo("Banco de Sangre","La edad final debe ser numérica")
            return
        if edadMaxima<18 or edadMaxima>65:
            messagebox.showinfo("Banco de Sangre","La edad final debe estar entre 18 y 65 años")
            return
        if edadMaxima<edadMinima:
            messagebox.showinfo("Banco de Sangre","La edad final no puede ser menor a la edad inicial")
            return
    lista=[]
    for donador in pDonadores:
        if len(donador)>=10:
            edad=calcularEdadAux(donador[4])
            if donador[8]==1 and edad>=edadMinima and edad<=edadMaxima:
                lista.append(donador)
    if len(lista)==0:
        messagebox.showinfo("Banco de Sangre","Reporte no creado.")
        return
    archivo=open("reporteRangoEdad.html","w",encoding="utf-8")
    iniciarHtmlAux(archivo,"Reporte por rango de edad")
    archivo.write("<table border='1'>\n<tr><th>Cédula</th><th>Nombre completo</th><th>Fecha de nacimiento</th><th>Teléfono</th><th>Correo</th></tr>\n")
    for donador in lista:
        archivo.write("<tr>")
        archivo.write("<td>"+donador[1]+"</td>")
        archivo.write("<td>"+obtenerNombreCompletoAux(donador[0])+"</td>")
        archivo.write("<td>"+obtenerFechaTextoAux(donador[4])+"</td>")
        archivo.write("<td>"+donador[7]+"</td>")
        archivo.write("<td>"+donador[6]+"</td>")
        archivo.write("</tr>\n")
    archivo.write("</table>\n")
    archivo.write("<p>Total encontrados: "+str(len(lista))+"</p>\n")
    finalizarHtmlAux(archivo)
    archivo.close()
    webbrowser.open("reporteRangoEdad.html")
    messagebox.showinfo("Banco de Sangre","Reporte creado satisfactoriamente")
    pVentana.destroy()

#Funcion principal de la opcion 3 del submenu reportes
def reporteTipoSangreProvincia(pDonadores,pTiposSangre):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores y la tupla de tipos de sangre
    -Salida:
        Se muestra ventana Tkinter para seleccionar tipo de sangre y provincia, y generar reporte HTML
    '''
    ventana=Toplevel()
    ventana.title("Por tipo de sangre de una provincia")
    ventana.geometry("500x300")
    Label(ventana,text="POR TIPO DE SANGRE DE UNA PROVINCIA",font=("Century Gothic",12,"bold")).pack(pady=15)
    Label(ventana,text="Tipo de sangre:",font=("Century Gothic",12)).pack()
    tipoSangre=StringVar()
    tipoSangre.set(pTiposSangre[0])
    OptionMenu(ventana,tipoSangre,*pTiposSangre).pack(pady=5)
    Label(ventana,text="Provincia:",font=("Century Gothic",12)).pack()
    provincia=StringVar()
    provincia.set("San José")
    OptionMenu(ventana,provincia,"San José","Alajuela","Cartago","Heredia","Guanacaste","Puntarenas","Limón").pack(pady=5)
    Button(ventana,text="Generar reporte",font=("Century Gothic",12,"bold"),width=35,command=lambda:generarReporteTipoSangreProvincia(ventana,pDonadores,pTiposSangre,tipoSangre,provincia)).pack(pady=5)
    Button(ventana,text="Regresar",font=("Century Gothic",12,"bold"),width=35,command=ventana.destroy).pack(pady=5)

#Funcion principal de la opcion 3 del submenu reportes
def generarReporteTipoSangreProvincia(pVentana,pDonadores,pTiposSangre,pTipoSangre,pProvincia):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la ventana, la matriz, los tipos de sangre, el tipo seleccionado y la provincia seleccionada
    -Salida:
        Se genera el reporte HTML filtrado por tipo de sangre y provincia
    '''
    nombresProvincia={"San José":1,"Alajuela":2,"Cartago":3,"Heredia":4,"Guanacaste":5,"Puntarenas":6,"Limón":7}
    numeroProvincia=nombresProvincia[pProvincia.get()]
    indice=0
    for i in range(len(pTiposSangre)):
        if pTiposSangre[i]==pTipoSangre.get():
            indice=i
    lista=[]
    for donador in pDonadores:
        if len(donador)>=10:
            provinciaCedula=int(donador[1][0])
            if donador[8]==1 and donador[2]==indice and provinciaCedula==numeroProvincia:
                lista.append(donador)
    if len(lista)==0:
        messagebox.showinfo("Banco de Sangre","Reporte no creado.")
        return
    archivo=open("reporteTipoSangreProvincia.html","w",encoding="utf-8")
    iniciarHtmlAux(archivo,"Reporte por tipo de sangre de una provincia dada")
    archivo.write("<table border='1'>\n<tr><th>Cédula</th><th>Nombre completo</th><th>Fecha de nacimiento</th><th>Teléfono</th><th>Correo</th></tr>\n")
    for donador in lista:
        archivo.write("<tr>")
        archivo.write("<td>"+donador[1]+"</td>")
        archivo.write("<td>"+obtenerNombreCompletoAux(donador[0])+"</td>")
        archivo.write("<td>"+obtenerFechaTextoAux(donador[4])+"</td>")
        archivo.write("<td>"+donador[7]+"</td>")
        archivo.write("<td>"+donador[6]+"</td>")
        archivo.write("</tr>\n")
    archivo.write("</table>\n")
    archivo.write("<p>Total encontrados: "+str(len(lista))+"</p>\n")
    finalizarHtmlAux(archivo)
    archivo.close()
    webbrowser.open("reporteTipoSangreProvincia.html")
    messagebox.showinfo("Banco de Sangre","Reporte creado satisfactoriamente")
    pVentana.destroy()

#Funcion principal de la opcion 4 del submenu reportes
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
        messagebox.showinfo("Banco de Sangre","No hay donadores que cumplan con los requisitos")
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
    webbrowser.open("reporteListaCompletaDonadores.html")
    messagebox.showinfo("Banco de Sangre","Reporte creado satisfactoriamente")

#Funcion principal de la opcion 5 del submenu reportes
def reporteMujeresONegativo(pDonadores):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores
    -Salida:
        Se genera un reporte HTML con mujeres donantes O- menores de 45 años, ordenadas por edad
    '''
    lista=[]
    for donador in pDonadores:
        if len(donador)>=10:
            edad=calcularEdadAux(donador[4])
            if donador[8]==1 and donador[3]==False and donador[2]==1 and edad<45:
                lista.append(donador)
    if len(lista)==0:
        messagebox.showinfo("Banco de Sangre","No hay donadores que cumplan con los requisitos")
        return
    i=0
    while i<len(lista)-1:
        j=0
        while j<len(lista)-1-i:
            if calcularEdadAux(lista[j][4])<calcularEdadAux(lista[j+1][4]):
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
            j+=1
        i+=1
    archivo=open("reporteMujeresONegativo.html","w",encoding="utf-8")
    iniciarHtmlAux(archivo,"Mujeres donantes O- menores de 45 años")
    archivo.write("<table border='1'>\n<tr><th>Cédula</th><th>Nombre completo</th><th>Fecha de nacimiento</th><th>Teléfono</th><th>Correo</th></tr>\n")
    for donador in lista:
        archivo.write("<tr>")
        archivo.write("<td>"+donador[1]+"</td>")
        archivo.write("<td>"+obtenerNombreCompletoAux(donador[0])+"</td>")
        archivo.write("<td>"+obtenerFechaTextoAux(donador[4])+"</td>")
        archivo.write("<td>"+donador[7]+"</td>")
        archivo.write("<td>"+donador[6]+"</td>")
        archivo.write("</tr>\n")
    archivo.write("</table>\n")
    archivo.write("<p>Total encontrados: "+str(len(lista))+"</p>\n")
    finalizarHtmlAux(archivo)
    archivo.close()
    webbrowser.open("reporteMujeresONegativo.html")
    messagebox.showinfo("Banco de Sangre","Reporte creado satisfactoriamente")

#Funcion principal de la opcion 6 del submenu reportes
def reportePuedeDonar(pDonadores,pTiposSangre):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores y la tupla de tipos de sangre
    -Salida:
        Se muestra ventana Tkinter para seleccionar tipo de sangre y generar reporte HTML
    '''
    ventana=Toplevel()
    ventana.title("¿A quién puede donar?")
    ventana.geometry("500x250")
    Label(ventana,text="¿A QUIÉN PUEDE DONAR?",font=("Century Gothic",14,"bold")).pack(pady=15)
    Label(ventana,text="Tipo de sangre:",font=("Century Gothic",12)).pack()
    tipoSangre=StringVar()
    tipoSangre.set(pTiposSangre[0])
    OptionMenu(ventana,tipoSangre,*pTiposSangre).pack(pady=5)
    Button(ventana,text="Generar reporte",font=("Century Gothic",12,"bold"),width=35,command=lambda:generarReportePuedeDonar(ventana,pDonadores,pTiposSangre,tipoSangre)).pack(pady=5)
    Button(ventana,text="Regresar",font=("Century Gothic",12,"bold"),width=35,command=ventana.destroy).pack(pady=5)

#Funcion principal de la opcion 6 del submenu reportes
def generarReportePuedeDonar(pVentana,pDonadores,pTiposSangre,pTipoSangre):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la ventana, la matriz, los tipos de sangre y el tipo seleccionado
    -Salida:
        Se genera el reporte HTML agrupado por provincia ascendentemente
    '''
    tipoDonante=pTipoSangre.get()
    lista=[]
    provincia=1
    while provincia<=7:
        for donador in pDonadores:
            if len(donador)>=10:
                tipoReceptor=obtenerTipoSangreTextoAux(donador[2],pTiposSangre)
                if donador[8]==1 and int(donador[1][0])==provincia and puedeDonarAux(tipoDonante,tipoReceptor)==True:
                    lista.append((provincia,donador))
        provincia+=1
    if len(lista)==0:
        messagebox.showinfo("Banco de Sangre","Reporte no creado.")
        return
    archivo=open("reportePuedeDonar.html","w",encoding="utf-8")
    iniciarHtmlAux(archivo,"Reporte de a quién puede donar")
    archivo.write("<p>Tipo de sangre seleccionado: "+tipoDonante+"</p>\n")
    archivo.write("<table border='1'>\n<tr><th>Provincia</th><th>Cédula</th><th>Nombre completo</th><th>Tipo de sangre</th><th>Teléfono</th><th>Correo</th></tr>\n")
    for entrada in lista:
        prov=entrada[0]
        donador=entrada[1]
        tipoReceptor=obtenerTipoSangreTextoAux(donador[2],pTiposSangre)
        archivo.write("<tr>")
        archivo.write("<td>"+obtenerProvinciaTextoAux(prov)+"</td>")
        archivo.write("<td>"+donador[1]+"</td>")
        archivo.write("<td>"+obtenerNombreCompletoAux(donador[0])+"</td>")
        archivo.write("<td>"+tipoReceptor+"</td>")
        archivo.write("<td>"+donador[7]+"</td>")
        archivo.write("<td>"+donador[6]+"</td>")
        archivo.write("</tr>\n")
    archivo.write("</table>\n")
    archivo.write("<p>Total encontrados: "+str(len(lista))+"</p>\n")
    finalizarHtmlAux(archivo)
    archivo.close()
    webbrowser.open("reportePuedeDonar.html")
    messagebox.showinfo("Banco de Sangre","Reporte creado satisfactoriamente")
    pVentana.destroy()

#Funcion principal de la opcion 7 del submenu reportes
def reportePuedeRecibir(pDonadores,pTiposSangre):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la matriz de donadores y la tupla de tipos de sangre
    -Salida:
        Se muestra ventana Tkinter para seleccionar tipo de sangre y generar reporte HTML
    '''
    ventana=Toplevel()
    ventana.title("¿De quién puede recibir?")
    ventana.geometry("500x250")
    Label(ventana,text="¿DE QUIÉN PUEDE RECIBIR?",font=("Century Gothic",14,"bold")).pack(pady=15)
    Label(ventana,text="Tipo de sangre:",font=("Century Gothic",12)).pack()
    tipoSangre=StringVar()
    tipoSangre.set(pTiposSangre[0])
    OptionMenu(ventana,tipoSangre,*pTiposSangre).pack(pady=5)
    Button(ventana,text="Generar reporte",font=("Century Gothic",12,"bold"),width=35,command=lambda:generarReportePuedeRecibir(ventana,pDonadores,pTiposSangre,tipoSangre)).pack(pady=5)
    Button(ventana,text="Regresar",font=("Century Gothic",12,"bold"),width=35,command=ventana.destroy).pack(pady=5)

#Funcion principal de la opcion 7 del submenu reportes
def generarReportePuedeRecibir(pVentana,pDonadores,pTiposSangre,pTipoSangre):
    '''
    Funcionamiento:
    -Entrada:
        Se recibe la ventana, la matriz, los tipos de sangre y el tipo seleccionado
    -Salida:
        Se genera el reporte HTML agrupado por provincia descendentemente
    '''
    tipoReceptor=pTipoSangre.get()
    lista=[]
    provincia=7
    while provincia>=1:
        for donador in pDonadores:
            if len(donador)>=10:
                tipoDonante=obtenerTipoSangreTextoAux(donador[2],pTiposSangre)
                if donador[8]==1 and int(donador[1][0])==provincia and puedeRecibirAux(tipoReceptor,tipoDonante)==True:
                    lista.append((provincia,donador))
        provincia-=1
    if len(lista)==0:
        messagebox.showinfo("Banco de Sangre","Reporte no creado.")
        return
    archivo=open("reportePuedeRecibir.html","w",encoding="utf-8")
    iniciarHtmlAux(archivo,"Reporte de quién puede recibir")
    archivo.write("<p>Tipo de sangre seleccionado: "+tipoReceptor+"</p>\n")
    archivo.write("<table border='1'>\n<tr><th>Provincia</th><th>Cédula</th><th>Nombre completo</th><th>Tipo de sangre</th><th>Teléfono</th><th>Correo</th></tr>\n")
    for entrada in lista:
        prov=entrada[0]
        donador=entrada[1]
        tipoDonante=obtenerTipoSangreTextoAux(donador[2],pTiposSangre)
        archivo.write("<tr>")
        archivo.write("<td>"+obtenerProvinciaTextoAux(prov)+"</td>")
        archivo.write("<td>"+donador[1]+"</td>")
        archivo.write("<td>"+obtenerNombreCompletoAux(donador[0])+"</td>")
        archivo.write("<td>"+tipoDonante+"</td>")
        archivo.write("<td>"+donador[7]+"</td>")
        archivo.write("<td>"+donador[6]+"</td>")
        archivo.write("</tr>\n")
    archivo.write("</table>\n")
    archivo.write("<p>Total encontrados: "+str(len(lista))+"</p>\n")
    finalizarHtmlAux(archivo)
    archivo.close()
    webbrowser.open("reportePuedeRecibir.html")
    messagebox.showinfo("Banco de Sangre","Reporte creado satisfactoriamente")
    pVentana.destroy()

#Funcion principal de la opcion 8 del submenu reportes
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
        messagebox.showinfo("Banco de Sangre","No hay donadores no activos registrados")
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
    webbrowser.open("reporteDonantesNoActivos.html")
    messagebox.showinfo("Banco de Sangre","Reporte creado satisfactoriamente")

#Funcion principal de la opcion 9 del submenu reportes
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
    webbrowser.open("reporteLugaresDonacion.html")
    messagebox.showinfo("Banco de Sangre","Reporte creado satisfactoriamente")

#Funcion principal de las opciones del menu y submenu reportes
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

#Funcion principal de las opciones del menu y submenu reportes
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