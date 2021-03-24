import datetime

errors = dict()
    
def bruteForce_simplifiedDES(originalMessage, encryptedMessage, iterations):
    """
    Funcion que realiza el proceso de ataque por fuerza bruta al algoritmo de cifrado simple DES.
    """
    round = iterations
    mi_1 = encryptedMessage
    index = 0
    cipherKeyFoo = "000000000"
    found = False
    startTime = datetime.datetime.now()
    while(not found and len(cipherKeyFoo)==9):
        if(simplifiedDES_Decrypt(encryptedMessage, cipherKeyFoo, iterations)==originalMessage):
            endTime = datetime.datetime.now()
            deltaTime = endTime - startTime
            elapsedTime = (str(deltaTime.total_seconds()*1000))[0:7]+"ms"
            found = True
        else:
            cipherKeyFoo = bin(int(cipherKeyFoo,base=2)+1)[2:].zfill(9)
    if(found):
        print("Succesful: La clave de cifrado es "+cipherKeyFoo+" y fue encontrada en "+elapsedTime)
    else:
        print("Failed: No se ha encontrado la clave.")
    return found        

def bruteForce_simplifiedDESGUI(originalMessage, encryptedMessage, iterations):
    """
    Funcion adaptada para la GUI de la funcion bruteForce_simplifiedDES.
    """
    round = iterations
    mi_1 = encryptedMessage
    index = 0
    cipherKeyFoo = "000000000"
    found = False
    startTime = datetime.datetime.now()
    while(not found and len(cipherKeyFoo)==9):
        if(simplifiedDES_Decrypt(encryptedMessage, cipherKeyFoo, iterations)==originalMessage):
            endTime = datetime.datetime.now()
            deltaTime = endTime - startTime
            elapsedTime = (str(deltaTime.total_seconds()*1000))[0:7]#ms
            found = True
        else:
            cipherKeyFoo = bin(int(cipherKeyFoo,base=2)+1)[2:].zfill(9)
    if(found):
        (mi, intermediateData) = simplifiedDES_DecryptGUI(encryptedMessage, cipherKeyFoo, iterations=8)
        return (cipherKeyFoo, found, elapsedTime, intermediateData)        
    else:
        return ("Error", found, "Error", "Error")        

def simplifiedDES_Decrypt(messageToDecrypt, cipherKey, iterations):
    """
    Funcion que lleva a cabo el proceso de descifrado mediante el algoritmo simple DES.
    """
    if(type(iterations) is not int): raise TypeError("El numero de iteraciones debe ser un integer")
    if(type(messageToDecrypt) is not str): raise TypeError("El mensaje para descifrar debe ser un string.")
    if(type(cipherKey) is not str): raise TypeError("La clave de cifrado debe ser un string.")

    mi_1 = messageToDecrypt
    currentRound = 1
    index = 0
    while(currentRound <= iterations-1):
        Li_1 = mi_1[0:6]
        Ri_1 = mi_1[6:12]
        Li = Ri_1
        Ki = generateSubKey(cipherKey, iterations+1-currentRound, iterations)
        fRi_1Ki = f(Ri_1, Ki)
        Ri = xor(Li_1, fRi_1Ki, 6)
        mi = Li + Ri
        Ri_1 = Ri
        Li_1 = Li
        mi_1 = mi
        currentRound = currentRound + 1

    Ri = Ri_1
    Ki = generateSubKey(cipherKey, iterations+1-currentRound, iterations)
    Li = xor(Li_1, f(Ri_1, Ki), 6)
    mi = Li + Ri
    return mi

def simplifiedDES_DecryptGUI(messageToDecrypt, cipherKey, iterations):
    """
    Funcion adaptada para la GUI de la funcion simplifiedDES_Decrypt
    """
    if(type(iterations) is not int): raise TypeError("El numero de iteraciones debe ser un integer")
    if(type(messageToDecrypt) is not str): raise TypeError("El mensaje para descifrar debe ser un string.")
    if(type(cipherKey) is not str): raise TypeError("La clave de cifrado debe ser un string.")


    intermediateData = dict()

    mi_1 = messageToDecrypt
    currentRound = 1
    index = 0
    while(currentRound <= iterations-1):
        Li_1 = mi_1[0:6]
        Ri_1 = mi_1[6:12]
        Li = Ri_1
        intermediateDataTuple = (Ri_1, Li_1, mi_1)
        intermediateData["Fase"+str(currentRound-1)] = intermediateDataTuple
        Ki = generateSubKey(cipherKey, iterations+1-currentRound, iterations)
        fRi_1Ki = f(Ri_1, Ki)
        Ri = xor(Li_1, fRi_1Ki, 6)
        mi = Li + Ri
        Ri_1 = Ri
        Li_1 = Li
        mi_1 = mi
        currentRound = currentRound + 1

    Ri = Ri_1
    Ki = generateSubKey(cipherKey, iterations+1-currentRound, iterations)
    Li = xor(Li_1, f(Ri_1, Ki), 6)
    mi = Li + Ri
    intermediateDataTuple = (Ri_1, Li_1, mi_1)
    intermediateData["Fase"+str(currentRound-1)] = intermediateDataTuple
    return (mi, intermediateData)
    
def simplifiedDES_Encrypt(messageToEncrypt, cipherKey, iterations):
    """
    Funcion que realiza el proceso de cifrado simple DES.
    """
    if(type(iterations) is not int): raise TypeError("El numero de iteraciones debe ser un integer")
    if(type(messageToEncrypt) is not str): raise TypeError("El mensaje para cifrar debe ser un string.")
    if(type(cipherKey) is not str): raise TypeError("La clave de cifrado debe ser un string.")

    mi_1 = messageToEncrypt
    currentRound = 1
    while(currentRound <= iterations-1):
        Li_1 = mi_1[0:6]
        Ri_1 = mi_1[6:12]
        Li = Ri_1
        Ki = generateSubKey(cipherKey, currentRound, iterations)
        fRi_1Ki = f(Ri_1, Ki)
        Ri = xor(Li_1, fRi_1Ki, 6)
        mi = Li + Ri
        Ri_1 = Ri
        Li_1 = Li
        mi_1 = mi
        currentRound = currentRound + 1

    Ri = Ri_1
    Ki = generateSubKey(cipherKey, currentRound, iterations)
    Li = xor(Li_1, f(Ri_1, Ki), 6)
    mi = Li + Ri
    return mi
    
def simplifiedDES_EncryptGUI(messageToEncrypt, cipherKey, iterations):
    """
    Funcion que adapta a la GUI la funcion simplifiedDES_Encrypt.
    """
    if(type(iterations) is not int): raise TypeError("El numero de iteraciones debe ser un integer")
    if(type(messageToEncrypt) is not str): raise TypeError("El mensaje para cifrar debe ser un string.")
    if(type(cipherKey) is not str): raise TypeError("La clave de cifrado debe ser un string.")

    intermediateData = dict()

    mi_1 = messageToEncrypt
    currentRound = 1
    while(currentRound <= iterations-1):
        Li_1 = mi_1[0:6]
        Ri_1 = mi_1[6:12]
        Li = Ri_1
        intermediateDataTuple = (Ri_1, Li_1, mi_1)
        intermediateData["Fase"+str(currentRound-1)] = intermediateDataTuple
        Ki = generateSubKey(cipherKey, currentRound, iterations)
        fRi_1Ki = f(Ri_1, Ki)
        Ri = xor(Li_1, fRi_1Ki, 6)
        mi = Li + Ri
        Ri_1 = Ri
        Li_1 = Li
        mi_1 = mi
        currentRound = currentRound + 1

    Ri = Ri_1
    Ki = generateSubKey(cipherKey, currentRound, iterations)
    Li = xor(Li_1, f(Ri_1, Ki), 6)
    mi = Li + Ri
    intermediateDataTuple = (Ri_1, Li_1, mi_1)
    intermediateData["Fase"+str(currentRound-1)] = intermediateDataTuple
    return (mi, intermediateData)

def f(Ri_1, Ki):
    """
    Funcion que devuelve el resultado de la funcion f(Ri_1,Ki)
    """
    expRi_1 = expand(Ri_1)
    Eri_1_XOR_Ki = xor(expRi_1, Ki, len(Ki))
    fRi_1Ki = sBox(1, Eri_1_XOR_Ki[0:4])+sBox(2, Eri_1_XOR_Ki[4:8])
    return fRi_1Ki


def sBox(which, entry):
    """
    Funcion para las S-Caja 1 y S-Caja 2. Devuelve el valor correspondiente a la entrada dada como parametro.
    """
    s1 = [["101","010","001","110","011","100","111","000"],["001","100","110","010","000","111","101","011"]]
    s2 = [["100","000","110","101","111","001","011","010"],["101","011","000","111","110","010","001","100"]]
    
    if(which == 1):
        s = s1
    if(which == 2):       
        s = s2 
    
    return s[int(entry[0])][int(entry[1:4],base=2)]

def xor(a, b, n):
    """
    Funcion XOR para n bits
    """
    res = ""
    for i in range(0,n):
        ai = a[i]
        bi = b[i]
        res += operationXOR(ai, bi)
    return res

def operationXOR(a, b):
    """
    Funcion logica XOR para 1 bit 
    """
    if(a=="0" and b=="0"):
        return "0"
    if(a=="1" and b=="0"):
        return "1"
    if(a=="0" and b=="1"):
        return "1"
    if(a=="1" and b=="1"):
        return "0"

def expand(message):
    """Funcion de expansion. Recibe parte del mensaje (6b) y produce a la salida un mensaje de (8b)."""
    return message[0]+message[1]+message[3]+message[2]+message[3]+message[2]+message[4]+message[5]

def getSubKeyList(cipherKey, iterations):
    """Funcion que devuelve la lista de subclaves"""
    subKeyList = []
    for i in range(0, iterations):
        subKeyList.append(generateSubKey(cipherKey, i, iterations))
    return subKeyList

def generateSubKey(cipherKey, currentRound, iterations):
    """ Funcion que devuelve la subclave correspondiente a la clave y ronda dadas"""
    index = currentRound - 1
    keyFoo = ""
    while len(keyFoo) < iterations:
        keyFoo = keyFoo + cipherKey[index % len(cipherKey)]    
        index = index + 1
    return keyFoo

def inputErrors(fieldType, fieldToCheck):
    """ 
    Funcion que recibe una cadena y chequea si el formato es valido.
    Devuelve True si hay errores y False si no los hay.
    """
    if(type(fieldType) is not str): raise TypeError("El parametro fieldType debe ser un string.")
    if(type(fieldToCheck) is not str): raise TypeError("El parametro fieldToCheck debe ser un string.")

    if(fieldType not in ("message","cipherkey")): 
        raise ValueError("Los valores permitidos para fieldType son message o cipherkey")

    if(fieldType=="message"):
        permittedLength = 12
    elif(fieldType=="cipherkey"):
        permittedLength = 9

    errors = []
    if(fieldToCheck == ""):
        raise ValueError("El campo "+ fieldType+" esta vacio.")
    if(fieldToCheck.count("0") + fieldToCheck.count("1") != len(fieldToCheck)):
        raise ValueError("El campo "+fieldType+" no esta en binario.")
    if(len(fieldToCheck) != permittedLength):
        raise ValueError("El campo "+fieldType+" debe ser como maximo de "+str(permittedLength)+" digitos. Longitud actual: "+str(len(fieldType)))

    if(len(errors)!=0):
        print(""+errors)
        errors["inputErrors"] = errors
    
    return (len(errors)!=0)

def inputErrors2(fieldType, fieldToCheck):
    """ 
    Funcion que recibe una cadena y chequea si el formato es valido.
    Devuelve True si hay errores y False si no los hay.
    """
    if(type(fieldType) is not str): raise TypeError("El parametro fieldType debe ser un string.")
    if(type(fieldToCheck) is not str): raise TypeError("El parametro fieldType debe ser un string.")

    if(fieldType not in ("message","cipherkey","IV","CBCmessageToEncrypt","CBCmessageEncrypted")): 
        raise ValueError("Los valores permitidos para fieldType son message, cipherkey, IV, CBCmessageToEncrypt o CBCmessageEncrypted")

    if(fieldType=="message"):
        permittedLength = 12
    elif(fieldType=="cipherkey"):
        permittedLength = 9
    elif(fieldType=="IV"):
        permittedLength = 12
    elif(fieldType=="CBCmessageToEncrypt"):
        permittedLength = 50    
    elif(fieldType=="CBCmessageEncrypted"):
        permittedLength = 421
    
    errors = []
    
    if(fieldType == "CBCmessageToEncrypt"):
        if(len(fieldToCheck) > permittedLength):
            raise ValueError("El campo "+fieldType+" debe ser de "+str(permittedLength)+" digitos. Longitud actual: "+str(len(fieldToCheck)))
    
    if(fieldToCheck == ""):
        raise ValueError("El campo "+ fieldType+" esta vacio.")
           
    if(fieldType == "CBCmessageEncrypted"):
        if(fieldToCheck.count("0") + fieldToCheck.count("1") != len(fieldToCheck)):
            raise ValueError("El campo "+fieldType+" no esta en binario.")
        if(len(fieldToCheck) > permittedLength or len(fieldToCheck) < 24):
            raise ValueError("El campo "+fieldType+" debe ser mayor que 24 bits e igual o menor que "+str(permittedLength)+" . Longitud actual: "+str(len(fieldToCheck)))
        if(len(fieldToCheck) % 12 != 0):
            raise ValueError("El campo "+fieldType+" debe ser divisible por 12."+" . Longitud actual: "+str(len(fieldToCheck)))
        if(fieldToCheck.count("0") + fieldToCheck.count("1") != len(fieldToCheck)):
            raise ValueError("El campo "+fieldType+" no esta en base binaria.") 
        
    if(len(errors)!=0):
        print(""+errors)
        errors["inputErrors"] = errors
    
    return (len(errors)!=0)