from tkinter import *
from tkinter import ttk, messagebox
from code import *
import datetime

#****************************************INICIO METODOS GUI*************************

#Funcion que se ejecuta al pulsar el boton de cifrar
def fnOnCifrar():
    errores_entrada(1)

#Funcion que se ejecuta al pulsar el boton de Descifrar
def fnOnDescifrar():
    errores_entrada(2)
    
#Funcion que se ejecuta al pulsar el boton de ataque por fuerza bruta
def fnOnBruteForce():
    errores_entrada2()

#Funcion para la pantalla de Cifrar/Descifrar que validara los campos mensaje y clave
#y si falla la validacion informara al usuario mediante ventanas que informen de dichos
#errores. Si los valores son validos ejecuta el algoritmo de Cifrar/Descifrar. Y completa
#los valores de la GUI.
def errores_entrada(cifrado):
    reset(1) #reseteo de valores de la GUI
    b1erroresmensaje = [] #errores en el mensaje
    b1erroresclave = [] #errores en la clave
    errormensaje=False #variable de control de errores en el mensaje
    errorclave=False #variable de control de errores en la clave

    # CONTROL DE ERRORES
    
    #Campo mensaje vacio
    if(txt1f1tab1.get()==""):
        errormensaje=True 
        b1erroresmensaje.append(" No se ha introducido ningún mensaje")

    #Campo mensaje en base no binaria
    if(txt1f1tab1.get().count("0")+txt1f1tab1.get().count("1")!=len(txt1f1tab1.get())):
        errormensaje=True
        b1erroresmensaje.append(" Base binaria, solo valen el 0 y el 1")

    #Campo mensaje con extension no permitida
    if(len(txt1f1tab1.get())!=12):
        errormensaje=True
        b1erroresmensaje.append(" El mensaje no es de 12 bits")
    
    # CLAVE
    #Campo clave vacio
    if(txt2f1tab1.get()==""):
        errorclave=True 
        b1erroresclave.append(" No se ha introducido ninguna clave")
   
    #Campo clave en base no binaria
    if(txt2f1tab1.get().count("0")+txt2f1tab1.get().count("1")!=len(txt2f1tab1.get())):
        errorclave=True
        b1erroresclave.append(" Base binaria, solo valen el 0 y el 1")
   
    #Campo clave con extension no valida
    if(len(txt2f1tab1.get())!=9):
        errorclave=True
        b1erroresclave.append(" La clave no es de 9 bits")
   
    #Manejo de errores
    if(errormensaje or errorclave):
        stringerrores = ""
        if(errormensaje):
            stringerrores += "Mensaje: "+'.'.join(b1erroresmensaje)+"\n"
        if(errorclave):
            stringerrores += "Clave: "+'.'.join(b1erroresclave)+"."
        messagebox.showerror('Errores', stringerrores)
    #Control de funcionamiento sin errores
    else:
        mensaje = txt1f1tab1.get()
        clave = txt2f1tab1.get()

        listasubclaves = []
        # generacion de subclaves
        listasubclaves = subclaves(clave, cifrado)

        # escritura de subclaves
        for i in range(len(listasubclaves)):
            listbtxttab1[i].insert(0, listasubclaves[i])

        if(cifrado==1):
            # Ejecucion algoritmo de cifrado
            txt1f4tab1.insert(0, TestcifradoDESsimplificado(mensaje, clave, 8, 1))
            txt1f4tab1.place(x=350, y=10)
            varres.set("Mensaje Cifrado")
            lbl1f4tab1.place(x=140, y=10)
        elif(cifrado==2):
            # Ejecucion algoritmo de descifrado
            txt1f4tab1.insert(0, TestDescifradoDESsimplificado(mensaje, clave, 8, 1))
            txt1f4tab1.place(x=350, y=10)
            varres.set("Mensaje Descifrado")
            lbl1f4tab1.place(x=100, y=10)

#Funcion para la pantalla de Bruteforce que validara los campos mensaje original y mensaje cifrado
#y si falla la validacion informara al usuario mediante ventanas que informen de dichos
#errores. Si los valores son validos ejecuta el algoritmo de Bruteforce. Y completa
#los valores de la GUI.
def errores_entrada2():
    reset(2) # Reseteo de valores de la GUI
    b1erroresoriginal = [] #Errores en el mensaje original
    b1errorescifrado = [] #Errores en el mensaje cifrado
    errororiginal=False #Variable de control de errores en el mensaje original
    errorcifrado=False #Variable de control de errores en el mensaje cifrado

    #CONTROL DE ERRORES

    #MENSAJE ORIGINAL

    #Campo mensaje original vacio
    if(txt1f1tab2.get()==""):
        errororiginal=True 
        b1erroresoriginal.append(" No se ha introducido ningún mensaje")

    #Campo mensaje original en base no binaria
    if(txt1f1tab2.get().count("0")+txt1f1tab2.get().count("1")!=len(txt1f1tab2.get())):
        errororiginal=True
        b1erroresoriginal.append(" Base binaria, solo valen el 0 y el 1")

    #Campo mensaje original con extension no permitida
    if(len(txt1f1tab2.get())!=12):
        errororiginal=True
        b1erroresoriginal.append(" El mensaje no es de 12 bits")
    
    #MENSAJE CIFRADO

    #Campo mensaje cifrado vacio
    if(txt2f1tab2.get()==""):
        errorcifrado=True 
        b1errorescifrado.append(" No se ha introducido ningún mensaje")

    #Campo mensaje cifrado en base no binaria
    if(txt2f1tab2.get().count("0")+txt2f1tab2.get().count("1")!=len(txt2f1tab2.get())):
        errorcifrado=True
        b1errorescifrado.append(" Base binaria, solo valen el 0 y el 1")

    #Campo mensaje cifrado con extension no permitida
    if(len(txt2f1tab2.get())!=12):
        errorcifrado=True
        b1errorescifrado.append(" El mensaje no es de 12 bits")
          
    # Manejo de errores
    if(errororiginal or errorcifrado):
        stringerrores = ""
        if(errororiginal):
            stringerrores += "Mensaje original: "+'.'.join(b1erroresoriginal)+"\n"
        if(errorcifrado):
            stringerrores += "Mensaje cifrado: "+'.'.join(b1errorescifrado)+"."
        messagebox.showerror('Errores', stringerrores)
    #Control de funcionamiento sin errores
    else:
        mensajeoriginal = txt1f1tab2.get()
        mensajecifrado = txt2f1tab2.get()

        #Ejecucion del algoritmo de fuerza bruta 
        [clave, encontrado, tiempo] = BruteForcedescifradoDESsimplificado(mensajeoriginal, mensajecifrado, 8)

        txt1f4tab2.insert(0, clave)
        txt2f4tab2.insert(0, tiempo)

        txt1f4tab2.place(x=200, y=10)
        lbl1f4tab2.place(x=100, y=10)

        txt2f4tab2.place(x=500, y=10)
        lbl2f4tab2.place(x=400, y=10)        

        clave = txt1f4tab2.get()
        if(encontrado):
            #Ejecucion del cifrado con los datos encontrados para completar los campos intermedios de la ejecucion hallada
            TestcifradoDESsimplificado(mensajeoriginal, clave, 8, 2)
            cifrado=True
            listasubclaves = []
            #Generacion de subclaves
            listasubclaves = subclaves(clave, cifrado)
            #Escritura de subclaves
            for i in range(len(listasubclaves)):
                listbtxttab2[i].insert(0, listasubclaves[i])

#Funcion de reset, resetea los valores para que la salida en la interfaz
#sea independiente en cada ejecucion del cifrado/descifrado/ataque.
#Si el parametro numero es 1 significa que el reset se producira en la pantalla Cifrar/Descifrar.
#Si el parametro numero es 2 el reset se producira en la pantalla Bruteforce.
def reset(numero):
    if(numero==1):
        i = 0
        while(i < 8):
            listbtxttab1[i].delete(0, "end")
            i = i+1
        i = 0
        while(i < 24):
            listfasestxtf3tab1[i].delete(0, "end")
            i = i+1
        txt1f4tab1.delete(0, "end")
        txt1f4tab1.place(x=500, y=480)
    elif(numero==2):
        i=0
        while(i < 8):
            listbtxttab2[i].delete(0, "end")
            i = i+1
        i = 0
        while(i < 24):
            listfasestxtf3tab2[i].delete(0, "end")
            i = i+1
        txt1f4tab2.delete(0, "end")
        txt1f4tab2.place(x=500, y=480)
        txt2f4tab2.delete(0, "end")

#******************************FIN METODOS GUI***************************************

#******************************INICIO COMPUTATION*************************************

#Funcion para el ataque por fuerza bruta. Recibe el mensaje original, el mensaje cifrado y las iteraciones.
#A partir del mensaje original cifra con el numero de iteraciones indicado y con todas las claves posibles hasta encontrar
#la clave que produce el mensaje cifrado que tenemos como parametro. Si existe devolvera la clave encontrada y el tiempo que se ha
#tardado en hallarla.En caso de no haber clave que produzca el cifrado que se recibe como parametro devolvera como clave y como tiempo "ERROR"
def BruteForcedescifradoDESsimplificado(mensajeoriginal, mensajecifrado, iteraciones):
    ronda = iteraciones
    mi_1 = mensajecifrado
    indice = 0
    clave = "000000000"
    encontrado = False
    start = datetime.datetime.now()
    while(not encontrado and len(clave)==9):
        ronda=8
        while(ronda > 1 ):
            Li_1 = mi_1[0:6]
            Ri_1 = mi_1[6:12]
            Li = Ri_1
            Ki = subclave(clave, ronda)
            fRi_1Ki = f(Ri_1,Ki)
            Ri = xor(Li_1, fRi_1Ki, 6)
            mi = Li+Ri
            Ri_1 = Ri
            Li_1 = Li
            mi_1 = mi
            ronda=ronda-1

        Ri = Ri_1
        Ki = subclave(clave,ronda)
        Li = xor(Li_1,f(Ri_1,Ki),6)
        mi = Li+Ri
        mensajedescifrado = mi
        # Si existe clave
        if(mensajedescifrado==mensajeoriginal):
            end = datetime.datetime.now()
            delta = end-start
            encontrado=True
            tiempo = (str(delta.total_seconds()*1000))[0:7]+"ms"
            return clave, encontrado, tiempo
        # Si no existe clave y no se han probado todas las combinaciones
        # Se prueba con la siguiente clave.
        else:
            clave = int(clave,base=2)+1    
            clave = bin(clave)[2:].zfill(9)
    return "ERROR", encontrado, "ERROR" 

#Funcion para la generacion de subclaves.
#Si es para cifrado (cifrado=True) las claves las produce en el orden i,i+1,i+2,...n-1,n
#Si es para descifrado (cifrado=False) las claves se producen en el orden inverso n,n-1,...,i+2,i+1,i
#Devuelve la lista de subclaves generada.
def subclaves(clave, cifrado):
    listasubclaves = []
    if(cifrado):
        rondas = 8
        for ronda in range(0,rondas):
            nelem = 0
            n = 8
            nelem = 0
            claveaux=""
            i = ronda-1
            while nelem<8:
                claveaux = claveaux+clave[(i+1)%9]
                i = i+1
                nelem = nelem+1
            listasubclaves.append(claveaux)
    else:
        ronda = 7
        while(ronda>=0):
            nelem = 0
            n = 8
            nelem = 0
            claveaux=""
            i = ronda-1
            while nelem<8:
                claveaux = claveaux+clave[(i+1)%9]
                i = i+1
                nelem = nelem+1
            listasubclaves.append(claveaux)
            ronda = ronda - 1
    return listasubclaves

#Funcion para ejecutar el cifrado. 
#El parametro tab indica si la pantalla en la que hay que escribir los resultados es Cifrar/Descifrar(tab=1) o Bruteforce(tab=2)
def TestcifradoDESsimplificado(mensaje, clave, iteraciones, tab):
    iteraciones = 8
    mi_1 = mensaje
    ronda=1
    j=0
    while(ronda <= 7):
        Li_1 = mi_1[0:6]
        Ri_1 = mi_1[6:12]
        Li = Ri_1
        #Escritura de datos intermedios
        if(tab==1): #Cifrar/Descifrar
            listfasestxtf3tab1[j].insert(0,Ri_1)
            listfasestxtf3tab1[j+1].insert(0,Li_1)
            listfasestxtf3tab1[j+2].insert(0,mi_1)
        elif(tab==2):#Bruteforce
            listfasestxtf3tab2[j].insert(0,Ri_1)
            listfasestxtf3tab2[j+1].insert(0,Li_1)
            listfasestxtf3tab2[j+2].insert(0,mi_1)
        Ki = subclave(clave, ronda)
        fRi_1Ki = f(Ri_1,Ki)
        Ri = xor(Li_1, fRi_1Ki, 6)
        mi = Li+Ri
        Ri_1 = Ri
        Li_1 = Li
        mi_1 = mi
        j = ronda*3
        ronda=ronda+1

    Ri = Ri_1
    Ki = subclave(clave,ronda)
    Li = xor(Li_1,f(Ri_1,Ki),6)
    mi = Li+Ri
    #Escritura de datos intermedios
    if(tab==1):#Cifrar/Descifrar
        listfasestxtf3tab1[j].insert(0,Ri_1)
        listfasestxtf3tab1[j+1].insert(0,Li_1)
        listfasestxtf3tab1[j+2].insert(0,mi_1)
    elif(tab==2):#Bruteforce
        listfasestxtf3tab2[j].insert(0,Ri_1)
        listfasestxtf3tab2[j+1].insert(0,Li_1)
        listfasestxtf3tab2[j+2].insert(0,mi_1)
    return mi

#Funcion para generar la subclave i-esima.
#Recibe como parametro la clave (9b) y la ronda del algoritmo de cifrado.
#Devuelve la subclave de la ronda i-esima.
def subclave(clave, ronda):
    n = 8
    nelem = 0
    claveaux=""
    i = ronda-1
    while nelem!=8:
        claveaux = claveaux+clave[i%9]
        i = i+1
        nelem = nelem+1
    return claveaux

#Funcion f. Devuelve el resultado de la funcion f(Ri_1,Ki)
def f(Ri_1,Ki):
    expRi_1 = expansion(Ri_1)
    ERi_1_XOR_Ki = xor(expRi_1, Ki, 8)
    fRi_1Ki = scaja1(ERi_1_XOR_Ki[0:4])+scaja2(ERi_1_XOR_Ki[4:8])
    return fRi_1Ki

#Funcion para la S-Caja 1. Devuelve el valor correspondiente a la entrada dada como parametro.
def scaja1(entrada):
    s1 = [["101","010","001","110","011","100","111","000"],["001","100","110","010","000","111","101","011"]]

    fila = int(entrada[0])
    columna = entrada[1:4]
    columna = int(columna, base=2)

    return s1[fila][columna]

#Funcion para la S-Caja 1. Devuelve el valor correspondiente a la entrada dada como parametro.
def scaja2(entrada):
    s2 = [["100","000","110","101","111","001","011","010"],["101","011","000","111","110","010","001","100"]]

    fila = int(entrada[0])
    columna = entrada[1:4]
    columna = int(columna, base=2)

    return s2[fila][columna]

#Funcion de expansion. Recibe parte del mensaje (6b) y produce a la salida un mensaje de (8b).
def expansion(mensaje):
    mensajeexpandido = mensaje[0]
    mensajeexpandido = mensajeexpandido+mensaje[1]
    mensajeexpandido = mensajeexpandido+mensaje[3]
    mensajeexpandido = mensajeexpandido+mensaje[2]
    mensajeexpandido = mensajeexpandido+mensaje[3]
    mensajeexpandido = mensajeexpandido+mensaje[2]
    mensajeexpandido = mensajeexpandido+mensaje[4]
    mensajeexpandido = mensajeexpandido+mensaje[5]
    return mensajeexpandido

#Funcion XOR para n bits 
def xor(a,b,n):
    res = ""
    for i in range(0,n):
        ai = a[i]
        bi = b[i]
        res = res + operacion_xor(ai,bi)
    return res

#Funcion logica XOR para 1 bit
def operacion_xor(a,b):
    if(a=="0" and b=="0"):
        return "0"
    if(a=="1" and b=="0"):
        return "1"
    if(a=="0" and b=="1"):
        return "1"
    if(a=="1" and b=="1"):
        return "0"

#Funcion para ejecutar el descifrado. 
#El parametro tab indica si la pantalla en la que hay que escribir los resultados es Cifrar/Descifrar(tab=1) o Bruteforce(tab=2)
def TestDescifradoDESsimplificado(mensaje, clave, iteraciones, tab):
    iteraciones = 8
    mi_1 = mensaje
    ronda=1
    j=0
    while(ronda <= 7):
        Li_1 = mi_1[0:6]
        Ri_1 = mi_1[6:12]
        Li = Ri_1
        #Escritura de datos intermedios
        if(tab==1): #Cifrar/Descifrar
            listfasestxtf3tab1[j].insert(0,Ri_1)
            listfasestxtf3tab1[j+1].insert(0,Li_1)
            listfasestxtf3tab1[j+2].insert(0,mi_1)
        elif(tab==2): #Bruteforce
            listfasestxtf3tab2[j].insert(0,Ri_1)
            listfasestxtf3tab2[j+1].insert(0,Li_1)
            listfasestxtf3tab2[j+2].insert(0,mi_1)
        Ki = subclave(clave, 9-ronda)
        fRi_1Ki = f(Ri_1,Ki)
        Ri = xor(Li_1, fRi_1Ki, 6)
        mi = Li+Ri
        Ri_1 = Ri
        Li_1 = Li
        mi_1 = mi
        j = ronda*3
        ronda=ronda+1

    Ri = Ri_1
    Ki = subclave(clave,9-ronda)
    Li = xor(Li_1,f(Ri_1,Ki),6)
    mi = Li+Ri
    #Escritura de datos intermedios
    if(tab==1): #Cifrar/Descifrar
        listfasestxtf3tab1[j].insert(0,Ri_1)
        listfasestxtf3tab1[j+1].insert(0,Li_1)
        listfasestxtf3tab1[j+2].insert(0,mi_1)
    elif(tab==2): #Bruteforce
        listfasestxtf3tab2[j].insert(0,Ri_1)
        listfasestxtf3tab2[j+1].insert(0,Li_1)
        listfasestxtf3tab2[j+2].insert(0,mi_1)
    return mi


#******************************FIN COMPUTATION*************************************


#******************************INICIO GUI******************************************

root = Tk() #ventana principal
root.title("Práctica 1") #titulo ventana principal
root.geometry("800x600") #largo x ancho
root.resizable(0,0) #bloqueo de maximizacion o alteracion de las longitudes de la ventana

tab_control = ttk.Notebook(root) #Notebook para el control de las pantallas(pestanias)
tab1 = ttk.Frame(tab_control) #Pantalla Cifrar/Descifrar
tab2 = ttk.Frame(tab_control) #Pantalla Bruteforce

#---------------------------------TAB 1 CIFRAR/DESCIFRAR------------------------------
tab_control.add(tab1, text='Cifrar/Descifrar') #Titulo de la pantalla

#-----Primer bloque (mensaje clave y botones cifrar y descifrar)------
frame1tab1 = Frame(tab1,height=150, width=210,bg="lightskyblue") 
frame1tab1.place(x=10, y=10)

lbl1f1tab1 = Label(frame1tab1,text="Mensaje (12b)")
lbl1f1tab1.name="lblMensaje"
lbl1f1tab1.place(x=20,y=20)

lbl2f1tab1 = Label(frame1tab1,text="Clave (9b)")
lbl2f1tab1.name="lblClave"
lbl2f1tab1.place(x=20,y=50)

txt1f1tab1 = Entry(frame1tab1, width=12)
txt1f1tab1.name="txtMensaje"
txt1f1tab1.place(x=110, y=20)
txt1f1tab1.insert(0, "011100100110")

txt2f1tab1 = Entry(frame1tab1, width=12)
txt2f1tab1.name="txtClave"
txt2f1tab1.place(x=110, y=50)
txt2f1tab1.insert(0, "011001010")

b1btn1f1tab1 = Button(frame1tab1, text="Cifrar", bg="royalblue",command=fnOnCifrar)
b1btn1f1tab1.place(x=20,y=80)
b1btn1f1tab1.name = "btnCifrar"

b1btn2f1tab1 = Button(frame1tab1, text="Descifrar", bg="royalblue",command=fnOnDescifrar)
b1btn2f1tab1.place(x=130,y=80)
b1btn2f1tab1.name = "btnDescifrar"
#-----Fin Primer bloque (mensaje clave y botones cifrar y descifrar)------

#-----Segundo bloque (subclaves)------
frame2tab1 = Frame(tab1,height=150, width=600,bg="skyblue")
frame2tab1.place(x=230, y=10)

lbl1f2tab1 = Label(frame2tab1,text="Subclaves (8b)")
lbl1f2tab1.place(x=10, y=20)

listbtxttab1 = [] 
i = 0
_x=10
while i < 8:
    lblnf2tab1 = Label(frame2tab1, text="Subclave "+str(i))
    listbtxttab1.append(Entry(frame2tab1, width=8, state='normal'))
    if((i%2)==0):
        lblnf2tab1.place(x=_x+65*i, y=60)    
        listbtxttab1[i].place(x=_x+65*i+65, y=60)
    else:
        lblnf2tab1.place(x=_x+65*(i-1), y=100)    
        listbtxttab1[i].place(x=_x+65*(i-1)+65, y=100)
    i = i+1
#-----Fin Segundo bloque (subclaves)------

#-----Tercer bloque (Fases)------

frame3tab1 = Frame(tab1,height=300, width=800,bg="deepskyblue")
frame3tab1.place(x=10, y=170)

lbl1f3tab1 = Label(frame3tab1,text="Fases")
lbl1f3tab1.place(x=0, y=0)

i = 0
n = 8
j = 0
nj = 3
pasox=200
_y = 210
listfasestxtf3tab1 = [] 
while(i < 4):
    lbln1f3tab1 = Label(tab1, text="Fase "+str(i))
    lbln1f3tab1.place(x=10+pasox*i, y=_y)
    lbln2f3tab1 = Label(tab1, text="R"+str(i)+" (6b)")
    lbln2f3tab1.place(x=10+pasox*i, y=_y+30)
    lbln3f3tab1 = Label(tab1, text="L"+str(i)+" (6b)")
    lbln3f3tab1.place(x=10+pasox*i, y=_y+60)
    lbln4f3tab1 = Label(tab1, text="M"+str(i+1)+" (12b)")
    lbln4f3tab1.place(x=10+pasox*i, y=_y+90)
    
    listfasestxtf3tab1.append(Entry(tab1, width=8, state='normal'))
    listfasestxtf3tab1[j].place(x=80+pasox*i, y=_y+30)
    listfasestxtf3tab1.append(Entry(tab1, width=8, state='normal'))
    listfasestxtf3tab1[j+1].place(x=80+pasox*i, y=_y+60)
    listfasestxtf3tab1.append(Entry(tab1, width=12, state='normal'))
    listfasestxtf3tab1[j+2].place(x=80+pasox*i, y=_y+90)
    i = i+1
    j = j+3

i = 4
j =12
_y = 340
while(i < 8):
    lbln5f3tab1 = Label(tab1, text="Fase "+str(i))
    lbln5f3tab1.place(x=10+pasox*(i-4), y=_y)
    lbln6f3tab1 = Label(tab1, text="R"+str(i)+" (6b)")
    lbln6f3tab1.place(x=10+pasox*(i-4), y=_y+30)
    lbln7f3tab1 = Label(tab1, text="L"+str(i)+" (6b)")
    lbln7f3tab1.place(x=10+pasox*(i-4), y=_y+60)
    lbln8f3tab1 = Label(tab1, text="M"+str(i+1)+" (12b)")
    lbln8f3tab1.place(x=10+pasox*(i-4), y=_y+90)
    
    listfasestxtf3tab1.append(Entry(tab1, width=8, state='normal'))
    listfasestxtf3tab1[j].place(x=80+pasox*(i-4), y=_y+30)
    listfasestxtf3tab1.append(Entry(tab1, width=8, state='normal'))
    listfasestxtf3tab1[j+1].place(x=80+pasox*(i-4), y=_y+60)
    listfasestxtf3tab1.append(Entry(tab1, width=12, state='normal'))
    listfasestxtf3tab1[j+2].place(x=80+pasox*(i-4), y=_y+90)
    i = i+1
    j = j+3
#-----Tercer bloque (Fases)------

#-----Cuarto bloque (Resultado: Mensaje Cifrado/Descifrado)------

frame4tab1 = Frame(tab1,height=100, width=800,bg="steelblue")
frame4tab1.place(x=10, y=480)

varres = StringVar()
varres.set('Resultado')
lbl1f4tab1 = Label(frame4tab1,textvariable=varres,font="Arial, 20")
lbl1f4tab1.place(x=210, y=10)     
txt1f4tab1 = Entry(frame4tab1,font="Arial, 20", width=12)
txt1f4tab1.place(x=350, y=10)
#-----Fin Cuarto bloque (Resultado: Mensaje Cifrado/Descifrado)------

#---------------------------------FIN TAB 1------------------------------

#---------------------------------TAB 2 BRUTEFORCE------------------------------
tab_control.add(tab2, text='Bruteforce') #Titulo de la pantalla
tab_control.pack(expand=1, fill='both')

#-----Primer bloque (mensaje original y cifrado y boton bruteforce)------
frame1tab2 = Frame(tab2,height=150, width=230,bg="lightskyblue")
frame1tab2.place(x=10, y=10)

lbl1f1tab2 = Label(frame1tab2,text="Mensaje Cifrado (12b)")
lbl1f1tab2.place(x=20,y=20)
lbl2f1tab2 = Label(frame1tab2,text="Mensaje Original (12b)")
lbl2f1tab2.place(x=20,y=50)

txt1f1tab2 = Entry(frame1tab2, width=12)
txt1f1tab2.place(x=150, y=20)
txt1f1tab2.insert(0, "000111001110")

txt2f1tab2 = Entry(frame1tab2, width=12)
txt2f1tab2.place(x=150, y=50)
txt2f1tab2.insert(0, "011100100110")

b1btn1f1tab2 = Button(frame1tab2, text="Fuerza Bruta", bg="royalblue",command=fnOnBruteForce)
b1btn1f1tab2.place(x=20,y=80)
b1btn1f1tab2.name = "btnbruteforce"
#-----Fin Primer bloque (mensaje original y cifrado y boton bruteforce)------

#-----Segundo bloque (subclaves)------

frame2tab2 = Frame(tab2,height=150, width=600,bg="skyblue")
frame2tab2.place(x=250, y=10)

lbl1f2tab2 = Label(frame2tab2,text="Subclaves (8b)")
lbl1f2tab2.place(x=10, y=20)

listbtxttab2 = [] 
i = 0
_x=10
while i < 8:
    lblnf2tab1 = Label(frame2tab2, text="Subclave "+str(i))
    listbtxttab2.append(Entry(frame2tab2, width=8, state='normal'))
    if((i%2)==0):
        lblnf2tab1.place(x=_x+65*i, y=60)    
        listbtxttab2[i].place(x=_x+65*i+65, y=60)
    else:
        lblnf2tab1.place(x=_x+65*(i-1), y=100)    
        listbtxttab2[i].place(x=_x+65*(i-1)+65, y=100)
    i = i+1
#-----Fin Segundo bloque (subclaves)------

#-----Tercer bloque (Fases)------
frame3tab2 = Frame(tab2,height=300, width=800,bg="deepskyblue")
frame3tab2.place(x=10, y=170)

lbl1f3tab2 = Label(frame3tab2,text="Fases")
lbl1f3tab2.place(x=0, y=0)

i = 0
n = 8
j = 0
nj = 3
b2yi=200
b2xi=123
pasox=200
pasox2=200
_y = 210
listfasestxtf3tab2 = [] 
while(i < 4):
    lbln1f3tab2 = Label(tab2, text="Fase "+str(i))
    lbln1f3tab2.place(x=10+pasox*i, y=_y)
    lbln2f3tab2 = Label(tab2, text="R"+str(i)+" (6b)")
    lbln2f3tab2.place(x=10+pasox*i, y=_y+30)
    lbln3f3tab2 = Label(tab2, text="L"+str(i)+" (6b)")
    lbln3f3tab2.place(x=10+pasox*i, y=_y+60)
    lbln4f3tab2 = Label(tab2, text="M"+str(i+1)+" (12b)")
    lbln4f3tab2.place(x=10+pasox*i, y=_y+90)
    
    listfasestxtf3tab2.append(Entry(tab2, width=8, state='normal'))
    listfasestxtf3tab2[j].place(x=80+pasox*i, y=_y+30)
    listfasestxtf3tab2.append(Entry(tab2, width=8, state='normal'))
    listfasestxtf3tab2[j+1].place(x=80+pasox*i, y=_y+60)
    listfasestxtf3tab2.append(Entry(tab2, width=12, state='normal'))
    listfasestxtf3tab2[j+2].place(x=80+pasox*i, y=_y+90)
    i = i+1
    j = j+3

i = 4
j =12
_y = 340
while(i < 8):
    lbln5f3tab2 = Label(tab2, text="Fase "+str(i))
    lbln5f3tab2.place(x=10+pasox*(i-4), y=_y)
    lbln6f3tab2= Label(tab2, text="R"+str(i)+" (6b)")
    lbln6f3tab2.place(x=10+pasox*(i-4), y=_y+30)
    lbln7f3tab2 = Label(tab2, text="L"+str(i)+" (6b)")
    lbln7f3tab2.place(x=10+pasox*(i-4), y=_y+60)
    lbln8f3tab2 = Label(tab2, text="M"+str(i+1)+" (12b)")
    lbln8f3tab2.place(x=10+pasox*(i-4), y=_y+90)
    
    listfasestxtf3tab2.append(Entry(tab2, width=8, state='normal'))
    listfasestxtf3tab2[j].place(x=80+pasox*(i-4), y=_y+30)
    listfasestxtf3tab2.append(Entry(tab2, width=8, state='normal'))
    listfasestxtf3tab2[j+1].place(x=80+pasox*(i-4), y=_y+60)
    listfasestxtf3tab2.append(Entry(tab2, width=12, state='normal'))
    listfasestxtf3tab2[j+2].place(x=80+pasox*(i-4), y=_y+90)
    i = i+1
    j = j+3
#-----Fin Tercer bloque (Fases)------

#-----Cuarto bloque (Clave y tiempo)------
framebloque4 = Frame(tab2,height=100, width=800,bg="steelblue")
framebloque4.place(x=10, y=480)

lbl1f4tab2 = Label(framebloque4,text="Clave",font="Arial, 20")
lbl1f4tab2.place(x=100, y=10)
txt1f4tab2 = Entry(framebloque4,font="Arial, 20", width=9)
txt1f4tab2.place(x=200, y=10)

lbl2f4tab2 = Label(framebloque4,text="Tiempo",font="Arial, 20")
lbl2f4tab2.place(x=400, y=10)
txt2f4tab2 = Entry(framebloque4,font="Arial, 20", width=9)
txt2f4tab2.place(x=500, y=10)
#-----Fin Cuarto bloque (Fases)------

#-----------------------------------FIN TAB 2---------------------------------------

root.mainloop() #Ejecucion de la GUI
#***********************************FIN GUI******************************************
