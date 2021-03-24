from tkinter import *
from tkinter import ttk, messagebox
from code import *
from m_simplifiedDES import *
from m_blocks_fill import *
from m_CBCmode import *
from ttkthemes import ThemedStyle
from tkinter import ttk, scrolledtext
import tkinter as tk
import datetime

#*******************MISCELANEA----------------------------------

#Variables de tema seleccionables
THEME2 = "equilux"
THEME1 = "aquativo"

#Funcion que cambia el tema de Claro a Oscuro y de Oscuro a Claro
def changeTheme(root):
    if(currentTheme.get()==THEME1):
        style.theme_use(THEME2)
        currentTheme.set(THEME2)
    else:
        style.theme_use(THEME1)
        currentTheme.set(THEME1)

#*******************PRACTICA 1 CIFRADO DES SIMPLIFICADO METODOS GUI----------------------------------

#Funcion que se ejecuta al pulsar el boton de cifrar 
def fnOnEncrypt():
    message = txt1f1tab1.get()
    cipherKey = txt2f1tab1.get()
    try:
        if(inputErrors("message", message) == 0 and inputErrors("cipherkey", cipherKey) == 0):
            iterations=8
            try:
                (encryptedMessage, dictIntermediateValues)= simplifiedDES_EncryptGUI(message, cipherKey, iterations)
            except TypeError as e:
                messagebox.showerror("Error", e)
            resetIntermediateValuesGUI(1)
            setSubkeyListOnGUI(1,cipherKey, iterations)
            setFasesOnGui(1,dictIntermediateValues)
            txt1f4tab1.insert(0,encryptedMessage)
    except (ValueError,TypeError) as e:
        messagebox.showerror("Error", e)

#Funcion que se ejecuta al pulsar el boton de Descifrar
def fnOnDecrypt():
    encryptedMessage = txt1f1tab1.get()
    cipherKey = txt2f1tab1.get()
    try:
        if(inputErrors("message", encryptedMessage) == 0 and inputErrors("cipherkey", cipherKey) == 0):
            iterations=8
            try:
                (encryptedMessage, dictIntermediateValues)= simplifiedDES_DecryptGUI(encryptedMessage, cipherKey, iterations)
            except TypeError as e:
                messagebox.showerror("Error", e)
            resetIntermediateValuesGUI(1)
            setSubkeyListOnGUI(1, cipherKey, iterations)
            setFasesOnGui(1, dictIntermediateValues)
            txt1f4tab1.insert(0,encryptedMessage)
    except (ValueError,TypeError) as e:
        messagebox.showerror("Error", e)

#Funcion que se ejecuta al pulsar el boton de ataque por fuerza bruta
def fnBruteForce():
    encryptedMessage = txt1f1tab2.get()
    originalMessage = txt2f1tab2.get()
    try:
        if(inputErrors("message", encryptedMessage) == 0 and inputErrors("message", originalMessage) == 0):
            iterations=8
            try:
                (cipherKey, found, time, dictIntermediateValues)= bruteForce_simplifiedDESGUI(originalMessage, encryptedMessage, iterations)
            except TypeError as e:
                messagebox.showerror("Error", e)
            if(found):                
                resetIntermediateValuesGUI(2)
                setSubkeyListOnGUI(2, cipherKey, iterations)
                setFasesOnGui(2, dictIntermediateValues)
            else:
                resetIntermediateValuesGUI(2)
                raise ValueError("No existe clave que desencripte el mensaje cifrado y lo convierta en el mensaje original.")
            txt1f4tab2.insert(0,encryptedMessage)
    except (ValueError,TypeError) as e:
        messagebox.showerror("Error", e)
    txt1f4tab2.insert(0, cipherKey)
    if(found):
        txt2f4tab2.insert(0, time[0:6]+"ms")
    else:
        txt2f4tab2.insert(0, time)

"""
Funcion de reset, resetea los valores para que la salida en la interfaz sea
independiente en cada ejecucion del cifrado/descifrado/ataque.
Si el parametro tab es 1 significa que el reset se producira en la pantalla Cifrar/Descifrar.
Si el parametro tab es 2 significa que el reset se producira en la pantalla BruteForce
"""
def resetIntermediateValuesGUI(tab):
    resetSubKeyListGUI(tab)
    resetFasesGUI(tab)
    resetResultGUI(tab)

#Funcion para resetear las fases del algoritmo de cifrado
#Si el parametro tab es 1 significa que el reset se producira en la pantalla Cifrar/Descifrar.
#Si el parametro tab es 2 significa que el reset se producira en la pantalla BruteForce
def resetFasesGUI(tab):
    if(tab==1):
        for i in range(0, 24):
            listfasestxtf3tab1[i].delete(0, "end")
            i = i+1
    elif(tab==2):
        for i in range(0, 24):
            listfasestxtf3tab2[i].delete(0, "end")
            i = i+1

#Funcion para resetear el resultado del Cifrado/Descifrado/Fuerza Bruta
#Si el parametro tab es 1 significa que el reset se producira en la pantalla Cifrar/Descifrar.
#Si el parametro tab es 2 significa que el reset se producira en la pantalla BruteForce
def resetResultGUI(tab):
    if(tab==1):
        txt1f4tab1.delete(0, "end")
        txt1f4tab1.place(x=500, y=480)
    elif(tab==2):
        txt1f4tab2.delete(0, "end")
        txt2f4tab2.delete(0, "end")

#Funcion para resetear las subclaves
#Si el parametro tab es 1 significa que el reset se producira en la pantalla Cifrar/Descifrar.
#Si el parametro tab es 2 significa que el reset se producira en la pantalla BruteForce
def resetSubKeyListGUI(tab):
    if(tab==1):    
        for i in range(0, 8):
            listbtxttab1[i].delete(0, "end")
    elif(tab==2):
        for i in range(0, 8):
            listbtxttab2[i].delete(0, "end")

#Funcion para escribir los valores intermedios de las fases del algoritmo de cifrado simple DES
#Si el parametro tab es 1 significa que el reset se producira en la pantalla Cifrar/Descifrar.
#Si el parametro tab es 2 significa que el reset se producira en la pantalla BruteForce
def setFasesOnGui(tab, dictIntermediateValues):
    j = 0
    iterations = 8
    if(tab==1):
        for i in range(0, iterations):
            data = dictIntermediateValues["Fase"+str(i)]
            listfasestxtf3tab1[j].insert(0,data[0])
            listfasestxtf3tab1[j+1].insert(0,data[1])
            listfasestxtf3tab1[j+2].insert(0,data[2])
            j = j+3
    elif(tab==2):
        for i in range(0, iterations):
            data = dictIntermediateValues["Fase"+str(i)]
            listfasestxtf3tab2[j].insert(0,data[0])
            listfasestxtf3tab2[j+1].insert(0,data[1])
            listfasestxtf3tab2[j+2].insert(0,data[2])
            j = j+3

#Funcion para escribir los valores intermedios de las subclaves del algoritmo de cifrado simple DES
#Si el parametro tab es 1 significa que el reset se producira en la pantalla Cifrar/Descifrar.
#Si el parametro tab es 2 significa que el reset se producira en la pantalla BruteForce
def setSubkeyListOnGUI(tab, cipherKey, iterations):
    subKeyList = getSubKeyList(cipherKey, iterations=8)
    if(tab==1):
        for i in range(len(subKeyList)):
            listbtxttab1[i].insert(0, subKeyList[i])
        txt1f4tab1.place(x=350, y=10)
        varres.set("Mensaje Cifrado")
        lbl1f4tab1.place(x=140, y=10)
    elif(tab==2):
        for i in range(len(subKeyList)):
            listbtxttab2[i].insert(0, subKeyList[i])

#*******************PRACTICA 1 FIN METODOS GUI------------------------------------

#*******************PRACTICA 2 METODOS GUI------------------------------------
def setMessageFilledBlocksGUI(frame, messageFilled):
    """
    Funcion para escribir los bloques CBC de cifrado/descifrado
    Si el parametro frame es 1 entonces los bloques que se escriben son de cifrado CBC
    Si el parametro frame es 2 entonces los bloques que se escriben son de descifrado CBC
    """
    if(frame==1):
        for i in range(0, len(messageFilled)):
            listtxtfntab3[i].insert(0, messageFilled[i])
    elif(frame==2):
        for i in range(0, len(messageFilled)):
            list2txtfntab3[i].insert(0, messageFilled[i])

def fnOnCBCEncrypt():
    """
    Funcion que se ejecuta al pulsar el boton Cifrar en la pantalla CBC Cifrar/Descifrar.
    Es la funcion que inicia la ejecucion del proceso de cifrado CBC.
    """
    message = txt1f1tab3.get()
    IV = txt2f1tab3.get()
    cipherKey = txt3f1tab3.get()
    try:
        if(inputErrors2("CBCmessageToEncrypt", message) == 0 and inputErrors2("cipherkey", cipherKey)==0 and inputErrors2("IV", IV)==0):
            try:
                resetIntermediateValuesGUI2(1)
                txt2f2tab3.insert(0, IV)
                txt3f2tab3.insert(0, cipherKey)
                messageInBinary = stringToBinaryASCIIcode(message)
                txt4f1tab3.insert(INSERT, messageInBinary)
                messageFilled = fillingBlockSchema(messageInBinary)
                messageFilledBlocks = generateMessageBlocks(messageFilled, int(len(messageFilled)/12))
                setMessageFilledBlocksGUI(1, messageFilledBlocks)
                encryptedMessageBlocks = encryptWithCBC(messageFilledBlocks, IV, cipherKey)
                setMessageFilledBlocksGUI(2, encryptedMessageBlocks)
                txt1f2tab3.insert(INSERT, ''.join(encryptedMessageBlocks))
            except (ValueError, TypeError) as e:
                messagebox.showerror("Error", e) 
    except (ValueError, TypeError) as e:
        messagebox.showerror("Error", e)


def fnOnCBCDecrypt(): 
    """
    Funcion que se ejecuta al pulsar el boton Descifrar en la pantalla CBC Cifrar/Descifrar.
    Es la funcion que inicia la ejecucion del proceso de descifrado CBC.
    """
    encryptedMessage = txt1f2tab3.get("1.0",END).replace('\n','')
    IV = txt2f2tab3.get()
    cipherKey = txt3f2tab3.get()
    try:
        if(inputErrors2("CBCmessageEncrypted", encryptedMessage) == 0 and inputErrors2("cipherkey", cipherKey)==0 and inputErrors2("IV", IV)==0):
            try:
                CB = generateMessageBlocks(encryptedMessage, int(len(encryptedMessage)/12))
                resetFilledBlocks(2)
                setMessageFilledBlocksGUI(2, CB)
                M = decryptWithCBC(CB, IV, cipherKey)
                setMessageFilledBlocksGUI(1, M)
                m = ('').join(M)
                resetMessageBinary()
                txt4f1tab3.insert(INSERT, m)
                mOrig = m[0:len(m)-12-int(m[len(m)-12:len(m)][0:4],base=2)] 
                originalMessage = binaryToStringASCIIcode(mOrig)
                resetOriginalMessage()
                txt1f1tab3.insert(0,  repr(originalMessage)[0:52])
            except (ValueError, TypeError) as e:
                messagebox.showerror("Error", e) 
    except (ValueError, TypeError) as e:
        messagebox.showerror("Error", e)

def resetIntermediateValuesGUI2(frame):
    """
    Funcion que resetea los valores intermedios del cifrado CBC
    """
    resetMessageBinary()
    resetFilledBlocks(frame)
    resetEncryptedMessage()

def resetOriginalMessage():
    """
    Funcion que resetea el mensaje original
    """
    txt1f1tab3.delete(0, "end")

def resetEncryptedMessage():
    """
    Funcion que resetea el mensaje cifrado con CBC
    """
    txt1f2tab3.delete('1.0', "end")
    
def resetFilledBlocks(frame):
    """
    Funcion que resetea los bloques de cifrado y descifrado CBC
    Si el parametro frame es 1 entonces los bloques que se escriben son de cifrado CBC
    Si el parametro frame es 2 entonces los bloques que se escriben son de descifrado CBC
    """
    if(frame==1):
        for i in range(0, 35):
            listtxtfntab3[i].delete(0, "end")
    elif(frame==2):
        for i in range(0, 35):
            list2txtfntab3[i].delete(0, "end")

def resetMessageBinary():
    """
    Funcion que resetea el mensaje tras pasar el procedimiento de relleno de bloques en binario
    """
    txt4f1tab3.delete('1.0', "end")

def resetAttemptsCBC():
    """
    Funcion que resetea la salida de los intentos de descifrado CBC por fuerza bruta
    """
    txt1f3tab4.delete('1.0', "end")

def fnOnCBCBruteForce():
    """
    Funcion que se ejecuta al pulsar el boton Fuerza Bruta en la pantalla CBC Fuerza Bruta.
    Es la funcion que inicia la ejecucion del proceso de descifrado CBC por fuerza bruta. 
    """
    encryptedMessage = txt1f2tab4.get("1.0",END).replace('\n','')
    originalMessage = txt2f1tab4.get()
    try:
        if(inputErrors2("CBCmessageToEncrypt", originalMessage) == 0 and inputErrors2("CBCmessageEncrypted", encryptedMessage)== 0):
            CBCencryptedMessageBlocks = generateMessageBlocks(encryptedMessage, len(encryptedMessage)/12)
            resetAttemptsCBC()
            bruteForceCBCGUI(CBCencryptedMessageBlocks, originalMessage)
    except(ValueError, TypeError) as e:
        messagebox.showerror("Error", e)
    
def bruteForceCBCGUI(encryptedMessage, originalMessage):
    """
    Funcion sobreescrita del modulo m_CBCmode debido a la complejidad y a la relacion tan
    interna con la GUI.
    """
    decryptedTryMessage = ""
    minsToRun = 1
    reachedMinLimit = False
    startTime = datetime.datetime.now()
    valuesTry = [] 
    while(originalMessage != decryptedTryMessage and not reachedMinLimit):
        cipherKey = generateCipherKey()
        IV = generateRandomIV()
        decryptedTryMessage = decryptMessage(encryptedMessage, IV, cipherKey)
        valuesTry.append(decryptedTryMessage)
        delta = datetime.datetime.now() - startTime
        time.set(delta.total_seconds())
        txt1f3tab4.insert(INSERT, repr(decryptedTryMessage))
        txt1f3tab4.see("end")
        if(delta.total_seconds() >= 60*minsToRun):
            reachedMinLimit = True
        root.update()
    if(originalMessage == decryptedTryMessage):
        txt1f3tab4.insert(INSERT, "\n\nIt was found. CipherKey: "+cipherKey+" IV: "+IV+"\n\n")
        result.set("Encontrado.")
    else:
        txt1f3tab4.insert(INSERT, "Time exceeded. It wasn't found.")
        result.set("Error.")

#******************************INICIO GUI******************************************

root = tk.Tk() #ventana principal

style = ThemedStyle(root) #Aplicacion de estilo a la GUI 
currentTheme = StringVar() 
currentTheme.set(THEME1) #Aplicacion tema claro
style.set_theme(currentTheme.get()) 
root.title("Práctica 2") #titulo ventana principal
root.geometry("810x680") #area: largo x ancho
root.resizable(0,0) #bloqueo de maximizacion o alteracion de las longitudes de la ventana

#Creacion para menu de accesibilidad para cambio de tema (Apariencia)
menu = tk.Menu(root, tearoff=False) 
subMenu = tk.Menu(menu, tearoff=False)
subMenu.add_command(label="Cambiar Tema", command= lambda: changeTheme(root))
menu.add_cascade(label="Tema", menu=subMenu)
root.config(menu=menu)

tab_control = ttk.Notebook(root) #Notebook para el control de las pantallas(pestanias)

tab1 = ttk.Frame(tab_control) #Pantalla Cifrar/Descifrar
tab2 = ttk.Frame(tab_control) #Pantalla Bruteforce
tab3 = ttk.Frame(tab_control) #Pantalla Cifrar/Descifrar modo CBC
tab4 = ttk.Frame(tab_control) #Pantalla Fuerza Bruta CBC


#---------------------------------TAB 1 CIFRAR/DESCIFRAR------------------------------
tab_control.add(tab1, text='Cifrar/Descifrar') #Titulo de la pantalla

#-----Primer bloque (mensaje clave y botones cifrar y descifrar)------
frame1tab1 = ttk.Frame(tab1,height=150, width=210) 
frame1tab1.place(x=10, y=10)

lbl1f1tab1 = ttk.Label(frame1tab1,text="Mensaje (12b)")
lbl1f1tab1.name="lblMensaje"
lbl1f1tab1.place(x=5,y=20)

lbl2f1tab1 = ttk.Label(frame1tab1,text="Clave (9b)")
lbl2f1tab1.name="lblClave"
lbl2f1tab1.place(x=5,y=50)

txt1f1tab1 = ttk.Entry(frame1tab1, width=12)
txt1f1tab1.name="txtMensaje"
txt1f1tab1.place(x=110, y=20)
txt1f1tab1.insert(0, "011100100110")

txt2f1tab1 = ttk.Entry(frame1tab1, width=12)
txt2f1tab1.name="txtClave"
txt2f1tab1.place(x=110, y=50)
txt2f1tab1.insert(0, "011001010")

b1btn1f1tab1 = ttk.Button(frame1tab1, text="Cifrar", command=fnOnEncrypt)
b1btn1f1tab1.place(x=0,y=80)
b1btn1f1tab1.name = "btnCifrar"

b1btn2f1tab1 = ttk.Button(frame1tab1, text="Descifrar", command=fnOnDecrypt)
b1btn2f1tab1.place(x=110,y=80)
b1btn2f1tab1.name = "btnDescifrar"
#-----Fin Primer bloque (mensaje clave y botones cifrar y descifrar)------

#-----Segundo bloque (subclaves)------
frame2tab1 = ttk.Frame(tab1,height=150, width=550,relief="groove")
frame2tab1.place(x=230, y=10)

lbl1f2tab1 = ttk.Label(frame2tab1,text="Subclaves (8b)")
lbl1f2tab1.place(x=10, y=20)

listbtxttab1 = [] 
i = 0
_x=10
while i < 8:
    lblnf2tab1 = ttk.Label(frame2tab1, text="Subclave "+str(i))
    listbtxttab1.append(ttk.Entry(frame2tab1, width=8, state='normal'))
    if((i%2)==0):
        lblnf2tab1.place(x=_x+65*i, y=60)    
        listbtxttab1[i].place(x=_x+65*i+65, y=60)
    else:
        lblnf2tab1.place(x=_x+65*(i-1), y=100)    
        listbtxttab1[i].place(x=_x+65*(i-1)+65, y=100)
    i = i+1
#-----Fin Segundo bloque (subclaves)------

#-----Tercer bloque (Fases)------
frame3tab1 = ttk.Frame(tab1,height=300, width=770, relief="groove")
frame3tab1.place(x=10, y=170)

lbl1f3tab1 = ttk.Label(frame3tab1,text="Fases")
lbl1f3tab1.place(x=5, y=5)

i = 0
n = 8
j = 0
nj = 3
pasox=200
_y = 210
listfasestxtf3tab1 = [] 
marginxfasestab1 = 15
while(i < 4):
    lbln1f3tab1 =ttk.Label(tab1, text="Fase "+str(i))
    lbln1f3tab1.place(x=marginxfasestab1+pasox*i, y=_y)
    lbln2f3tab1 =ttk.Label(tab1, text="R"+str(i)+" (6b)")
    lbln2f3tab1.place(x=marginxfasestab1+pasox*i, y=_y+30)
    lbln3f3tab1 =ttk.Label(tab1, text="L"+str(i)+" (6b)")
    lbln3f3tab1.place(x=marginxfasestab1+pasox*i, y=_y+60)
    lbln4f3tab1 =ttk.Label(tab1, text="M"+str(i+1)+" (12b)")
    lbln4f3tab1.place(x=marginxfasestab1+pasox*i, y=_y+90)
    
    listfasestxtf3tab1.append(ttk.Entry(tab1, width=8, state='normal'))
    listfasestxtf3tab1[j].place(x=80+pasox*i, y=_y+30)
    listfasestxtf3tab1.append(ttk.Entry(tab1, width=8, state='normal'))
    listfasestxtf3tab1[j+1].place(x=80+pasox*i, y=_y+60)
    listfasestxtf3tab1.append(ttk.Entry(tab1, width=12, state='normal'))
    listfasestxtf3tab1[j+2].place(x=80+pasox*i, y=_y+90)
    i = i+1
    j = j+3

i = 4
j =12
_y = 340
while(i < 8):
    lbln5f3tab1 =ttk.Label(tab1, text="Fase "+str(i))
    lbln5f3tab1.place(x=marginxfasestab1+pasox*(i-4), y=_y)
    lbln6f3tab1 =ttk.Label(tab1, text="R"+str(i)+" (6b)")
    lbln6f3tab1.place(x=marginxfasestab1+pasox*(i-4), y=_y+30)
    lbln7f3tab1 =ttk.Label(tab1, text="L"+str(i)+" (6b)")
    lbln7f3tab1.place(x=marginxfasestab1+pasox*(i-4), y=_y+60)
    lbln8f3tab1 =ttk.Label(tab1, text="M"+str(i+1)+" (12b)")
    lbln8f3tab1.place(x=marginxfasestab1+pasox*(i-4), y=_y+90)
    
    listfasestxtf3tab1.append(ttk.Entry(tab1, width=8, state='normal'))
    listfasestxtf3tab1[j].place(x=80+pasox*(i-4), y=_y+30)
    listfasestxtf3tab1.append(ttk.Entry(tab1, width=8, state='normal'))
    listfasestxtf3tab1[j+1].place(x=80+pasox*(i-4), y=_y+60)
    listfasestxtf3tab1.append(ttk.Entry(tab1, width=12, state='normal'))
    listfasestxtf3tab1[j+2].place(x=80+pasox*(i-4), y=_y+90)
    i = i+1
    j = j+3
#-----Tercer bloque (Fases)------

#-----Cuarto bloque (Resultado: Mensaje Cifrado/Descifrado)------
frame4tab1 = ttk.Frame(tab1,height=100, width=800)
frame4tab1.place(x=10, y=480)

varres = StringVar()
varres.set('Resultado')
lbl1f4tab1 =ttk.Label(frame4tab1,textvariable=varres,font="Arial, 20")
lbl1f4tab1.place(x=210, y=10)     
txt1f4tab1 =ttk.Entry(frame4tab1,font="Arial, 20", width=12)
txt1f4tab1.place(x=350, y=10)
#-----Fin Cuarto bloque (Resultado: Mensaje Cifrado/Descifrado)------
#---------------------------------FIN TAB 1------------------------------

#---------------------------------TAB 2 BRUTEFORCE------------------------------
tab_control.add(tab2, text='Bruteforce') #Titulo de la pantalla
tab_control.pack(expand=1, fill='both')

#-----Primer bloque (mensaje original y cifrado y boton bruteforce)------
frame1tab2 = ttk.Frame(tab2,height=150, width=230)
frame1tab2.place(x=10, y=10)

lbl1f1tab2 =ttk.Label(frame1tab2,text="Mensaje Cifrado (12b)")
lbl1f1tab2.place(x=5,y=20)
lbl2f1tab2 =ttk.Label(frame1tab2,text="Mensaje Original (12b)")
lbl2f1tab2.place(x=5,y=50)

txt1f1tab2 =ttk.Entry(frame1tab2, width=12)
txt1f1tab2.place(x=140, y=20)
txt1f1tab2.insert(0, "000111001110")

txt2f1tab2 =ttk.Entry(frame1tab2, width=12)
txt2f1tab2.place(x=140, y=50)
txt2f1tab2.insert(0, "011100100110")

b1btn1f1tab2 = ttk.Button(frame1tab2, text="Fuerza Bruta", command=fnBruteForce)
b1btn1f1tab2.place(x=20,y=80)
b1btn1f1tab2.name = "btnbruteforce"
#-----Fin Primer bloque (mensaje original y cifrado y boton bruteforce)------

#-----Segundo bloque (subclaves)------
frame2tab2 = ttk.Frame(tab2,height=150, width=530, relief="groove")
frame2tab2.place(x=250, y=10)

lbl1f2tab2 =ttk.Label(frame2tab2,text="Subclaves (8b)")
lbl1f2tab2.place(x=10, y=20)

listbtxttab2 = [] 
i = 0
_x=10
while i < 8:
    lblnf2tab1 =ttk.Label(frame2tab2, text="Subclave "+str(i))
    listbtxttab2.append(ttk.Entry(frame2tab2, width=8, state='normal'))
    if((i%2)==0):
        lblnf2tab1.place(x=_x+65*i, y=60)    
        listbtxttab2[i].place(x=_x+65*i+65, y=60)
    else:
        lblnf2tab1.place(x=_x+65*(i-1), y=100)    
        listbtxttab2[i].place(x=_x+65*(i-1)+65, y=100)
    i = i+1
#-----Fin Segundo bloque (subclaves)------

#-----Tercer bloque (Fases)------
frame3tab2 = ttk.Frame(tab2,height=300, width=770, relief="groove")
frame3tab2.place(x=10, y=170)

lbl1f3tab2 =ttk.Label(frame3tab2,text="Fases")
lbl1f3tab2.place(x=5, y=5)

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
marginxfasestab2 = 15
while(i < 4):
    lbln1f3tab2 =ttk.Label(tab2, text="Fase "+str(i))
    lbln1f3tab2.place(x=marginxfasestab2+pasox*i, y=_y)
    lbln2f3tab2 =ttk.Label(tab2, text="R"+str(i)+" (6b)")
    lbln2f3tab2.place(x=marginxfasestab2+pasox*i, y=_y+30)
    lbln3f3tab2 =ttk.Label(tab2, text="L"+str(i)+" (6b)")
    lbln3f3tab2.place(x=marginxfasestab2+pasox*i, y=_y+60)
    lbln4f3tab2 =ttk.Label(tab2, text="M"+str(i+1)+" (12b)")
    lbln4f3tab2.place(x=marginxfasestab2+pasox*i, y=_y+90)
    
    listfasestxtf3tab2.append(ttk.Entry(tab2, width=8, state='normal'))
    listfasestxtf3tab2[j].place(x=80+pasox*i, y=_y+30)
    listfasestxtf3tab2.append(ttk.Entry(tab2, width=8, state='normal'))
    listfasestxtf3tab2[j+1].place(x=80+pasox*i, y=_y+60)
    listfasestxtf3tab2.append(ttk.Entry(tab2, width=12, state='normal'))
    listfasestxtf3tab2[j+2].place(x=80+pasox*i, y=_y+90)
    i = i+1
    j = j+3

i = 4
j =12
_y = 340
while(i < 8):
    lbln5f3tab2 =ttk.Label(tab2, text="Fase "+str(i))
    lbln5f3tab2.place(x=marginxfasestab2+pasox*(i-4), y=_y)
    lbln6f3tab2=ttk.Label(tab2, text="R"+str(i)+" (6b)")
    lbln6f3tab2.place(x=marginxfasestab2+pasox*(i-4), y=_y+30)
    lbln7f3tab2 =ttk.Label(tab2, text="L"+str(i)+" (6b)")
    lbln7f3tab2.place(x=marginxfasestab2+pasox*(i-4), y=_y+60)
    lbln8f3tab2 =ttk.Label(tab2, text="M"+str(i+1)+" (12b)")
    lbln8f3tab2.place(x=marginxfasestab2+pasox*(i-4), y=_y+90)
    
    listfasestxtf3tab2.append(ttk.Entry(tab2, width=8, state='normal'))
    listfasestxtf3tab2[j].place(x=80+pasox*(i-4), y=_y+30)
    listfasestxtf3tab2.append(ttk.Entry(tab2, width=8, state='normal'))
    listfasestxtf3tab2[j+1].place(x=80+pasox*(i-4), y=_y+60)
    listfasestxtf3tab2.append(ttk.Entry(tab2, width=12, state='normal'))
    listfasestxtf3tab2[j+2].place(x=80+pasox*(i-4), y=_y+90)
    i = i+1
    j = j+3
#-----Fin Tercer bloque (Fases)------

#-----Cuarto bloque (Clave y tiempo)------
framebloque4 = ttk.Frame(tab2,height=100, width=800)
framebloque4.place(x=10, y=480)

lbl1f4tab2 =ttk.Label(framebloque4,text="Clave",font="Arial, 20")
lbl1f4tab2.place(x=100, y=10)
txt1f4tab2 =ttk.Entry(framebloque4,font="Arial, 20", width=9)
txt1f4tab2.place(x=200, y=10)


lbl2f4tab2 =ttk.Label(framebloque4,text="Tiempo",font="Arial, 20")
lbl2f4tab2.place(x=400, y=10)
txt2f4tab2 =ttk.Entry(framebloque4,font="Arial, 20", width=9)
txt2f4tab2.place(x=500, y=10) 
#-----Fin Cuarto bloque (Fases)------

#-----------------------------------FIN TAB 2---------------------------------------

#---------------------------------TAB 3 CBC CIFRAR/DESCIFRAR------------------------------
tab_control.add(tab3, text='CBC Cifrar/Descifrar') #Titulo de la pantalla

#-----Primer bloque (mensaje clave y botones cifrar y descifrar)------
frame1tab3 = ttk.Frame(tab3,height=630, width=400, relief="groove") 
frame1tab3.place(x=10, y=10)

#-----Frame 1------------------------------------------------------------------------------
    #-Mensaje para cifrar (cadena de caracteres)
    #-Vector de inicializacion VI y clave de cifrado 
    #-Mensaje convertido a binario y con proceso de relleno de bloques
    #-Mensaje convertido a binario y con proceso de relleno de bloques en forma de bloques
#------------------------------------------------------------------------------------------
lbl1f1tab3 = ttk.Label(frame1tab3,text="Mensaje (50 palabras)")
lbl1f1tab3.name="lblCBCMensaje"
lbl1f1tab3.place(x=5,y=20)

txt1f1tab3 = ttk.Entry(frame1tab3, width=50)
txt1f1tab3.name="txtCBCMensaje"
txt1f1tab3.place(x=5, y=40)

lbl2f1tab3 = ttk.Label(frame1tab3,text="IV (12b)")
lbl2f1tab3.name="lblIV"
lbl2f1tab3.place(x=5,y=60)

txt2f1tab3 = ttk.Entry(frame1tab3, width=12)
txt2f1tab3.name="txtIV"
txt2f1tab3.place(x=5, y=80)

lbl3f1tab3 = ttk.Label(frame1tab3,text="Clave cifrado sDES (9b)")
lbl3f1tab3.name="lblCipherKey"
lbl3f1tab3.place(x=5,y=100)

txt3f1tab3 = ttk.Entry(frame1tab3, width=9)
txt3f1tab3.name="txtCipherKey"
txt3f1tab3.place(x=5, y=120)

b1btn1f1tab3 = ttk.Button(frame1tab3, text="Cifrar >>", command=fnOnCBCEncrypt)
b1btn1f1tab3.place(x=340,y=5)
b1btn1f1tab3.name = "btnCifrar"

lbl4f1tab3 = ttk.Label(frame1tab3,text="Mensaje en binario (Máx. 400b)")
lbl4f1tab3.name="lblMensajeBinario"
lbl4f1tab3.place(x=5, y=140)

txt4f1tab3 = Text(frame1tab3, width=47, height=11)
txt4f1tab3.name="txtMensaje"
txt4f1tab3.place(x=5, y=160)
tab_control.select(tab3)

lbl4f1tab3 =ttk.Label(frame1tab3, text="Bloques (12b)")
lbl4f1tab3.place(x=5, y=350)

listtxtfntab3 = [] 
i = 0
j = 0
paso = 135
xlbl_ant = 5
xtxt_ant = 25
n = 0
while n < 36:
    lblnf1tab3 =ttk.Label(frame1tab3, text="B"+str(n))
    lblnf1tab3.place(x=5+135*i, y=380+20*j)
    txtnf1tab3 = ttk.Entry(frame1tab3, width=12, state='normal')
    txtnf1tab3.place(x=35+135*i, y=380+20*j)
    listtxtfntab3.append(txtnf1tab3)
    i = i + 1
    if( (i%3)==0 ):
        j = j+1
        i = 0 
    n = n + 1

#------------------------------FIN FRAME 1------------------------------------

#------------------------------INICIO SEGUNDO FRAME --------------------------------

#-----Frame 2------------------------------------------------------------------------------
    #-Mensaje para descifrar (cadena de bits despues de proceso CBC de Cifrado)
    #-Vector de inicializacion VI y clave de cifrado
    #-Mensaje convertido a binario y con proceso de relleno de bloques en forma de bloques
#------------------------------------------------------------------------------------------
frame2tab3 = ttk.Frame(tab3,height=630, width=390, relief="groove") 
frame2tab3.place(x=408, y=10)

lbl1f2tab3 = ttk.Label(frame2tab3,text="Mensaje Encriptado")
lbl1f2tab3.name="lblMensaje"
lbl1f2tab3.place(x=280,y=20)

txt1f2tab3 = Text(frame2tab3, width=47, height=12)
txt1f2tab3.name="txtCBCMensaje"
txt1f2tab3.place(x=5, y=40)

lbl2f2tab3 = ttk.Label(frame2tab3,text="IV (12b)")
lbl2f2tab3.name="lblIV"
lbl2f2tab3.place(x=340,y=240)

txt2f2tab3 = ttk.Entry(frame2tab3, width=12)
txt2f2tab3.name="txtIV"
txt2f2tab3.place(x=307, y=260)

lbl3f2tab3 = ttk.Label(frame2tab3,text="Clave cifrado sDES (9b)")
lbl3f2tab3.name="lblCipherKey"
lbl3f2tab3.place(x=260,y=290)

txt3f2tab3 = ttk.Entry(frame2tab3, width=9)
txt3f2tab3.name="txtCipherKey"
txt3f2tab3.place(x=325, y=310)

b1btn1f2tab3 = ttk.Button(frame2tab3, text="<< Descifrar", command=fnOnCBCDecrypt)
b1btn1f2tab3.place(x=5,y=5)
b1btn1f2tab3.name = "btnCBCDescifrar"

lbl4f2tab3 =ttk.Label(frame2tab3, text="Bloques (12b)")
lbl4f2tab3.place(x=305, y=350)

list2txtfntab3 = [] 
i = 0
j = 0
paso = 135
xlbl_ant = 5
xtxt_ant = 25
n = 0
while n < 36:
    lblnf2tab3 =ttk.Label(frame2tab3, text="B"+str(n))
    lblnf2tab3.place(x=5+135*i, y=380+20*j)
    txtnf2tab3 = ttk.Entry(frame2tab3, width=12, state='normal')
    txtnf2tab3.place(x=35+135*i, y=380+20*j)
    list2txtfntab3.append(txtnf2tab3)
    i = i + 1
    if( (i%3)==0 ):
        j = j+1
        i = 0 
    n = n + 1

#***********************************FIN FRAME 2****************************************
#***********************************FIN TAB 3******************************************

#---------------------------------TAB 4 CBC FUERZA BRUTA------------------------------

    #-----Frame 1------------------------------------------------------------------------------
        #-Mensaje cifrado CBC
        #-Mensaje original (cadena de caracteres)
        #-Tiempo 1 min
        #-Resultado
    #------------------------------------------------------------------------------------------

tab_control.add(tab4, text='CBC Fuerza Bruta')

frame1tab4 = ttk.Frame(tab4,height=630, width=795, relief="groove") 
frame1tab4.place(x=5, y=10)

lbl1f1tab4 = ttk.Label(frame1tab4,text="Mensaje Encriptado")
lbl1f1tab4.name="lblMensaje"
lbl1f1tab4.place(x=5,y=20)


lbl2f1tab4 = ttk.Label(frame1tab4,text="Mensaje Original (50 palabras)")
lbl2f1tab4.name="lblCBCMensaje"
lbl2f1tab4.place(x=5,y=160)

txt2f1tab4 = ttk.Entry(frame1tab4, width=50)
txt2f1tab4.name="txtCBCMensaje"
txt2f1tab4.place(x=5, y=180)

b1btn1f1tab4 = ttk.Button(frame1tab4, text="Fuerza Bruta", command=fnOnCBCBruteForce)
b1btn1f1tab4.place(x=5,y=215)
b1btn1f1tab4.name = "btnCBCFuerzaBruta"

frame3tab4 = ttk.Frame(tab4,height=255, width=780, relief="groove") 
frame3tab4.place(x=10, y=270)

txt1f3tab4 = scrolledtext.ScrolledText(frame3tab4, width=95, height=16)
txt1f3tab4.name="txtCBCMensaje"
txt1f3tab4.place(x=0, y=0)

lbl3f1tab4 =ttk.Label(frame1tab4,text="Tiempo",font="Arial, 20")
lbl3f1tab4.place(x=10, y=530)

time = StringVar()
time.set("")
txt3f1tab4 = ttk.Entry(frame1tab4, textvariable=time, width=11, font="Arial 18")
txt3f1tab4.insert(0, time.get())
txt3f1tab4.place(x=10, y=570)

lbl4f1tab4 =ttk.Label(frame1tab4,text="Resultado",font="Arial, 20")
lbl4f1tab4.place(x=550, y=530)

result = StringVar()
result.set("")
txt4f1tab4 = ttk.Entry(frame1tab4, textvariable=result, width=15, font="Arial 18")
txt4f1tab4.place(x=550, y=570)

#-----Frame 2------------------------------------------------------------------------------
    #-Pruebas de fuerza bruta de descifrado CBC
#------------------------------------------------------------------------------------------

frame2tab4 = ttk.Frame(tab4,height=100, width=780, relief="groove") 
frame2tab4.place(x=10, y=50)

txt1f2tab4 = Text(frame2tab4, width=97, height=6)
txt1f2tab4.name="txtCBCMensaje"
txt1f2tab4.place(x=0, y=0)

tab_control.select(tab1)

root.mainloop() #Ejecucion de la GUI
#***********************************FIN GUI******************************************
