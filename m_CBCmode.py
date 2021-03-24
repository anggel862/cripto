# -*- coding: utf-8 -*-

from m_simplifiedDES import *
from m_blocks_fill import *
import codecs
import locale
import sys

def bruteForceCBC(encryptedMessage, originalMessage):
    """
    Funcion que realiza el proceso de descifrado de un mensaje cifrado mediante CBC.
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
        print(repr(decryptedTryMessage))
        if(delta.total_seconds() >= 60*minsToRun):
            reachedMinLimit = True
    if(originalMessage == decryptedTryMessage):
        print("It was found. CipherKey: "+cipherKey+" IV: "+IV)
    else:
        print("Time exceeded. It wasn't found.")

def generateCipherKey():
    """
    Funcion que genera una clave de cifrado para simple DES aleatoria.
    """
    cipherKey = generatePseudoRandomBinary(9)
    return str(cipherKey)


def encryptMessage(originalMessage, IV, cipherKey):
    """
    Funcion que inicia el proceso de cifrado CBC del mensaje originalMessage
    """
    originalMessageInBinary = stringToBinaryASCIIcode(originalMessage)
    messageFilled = fillingBlockSchema(originalMessageInBinary)
    messageBlocks = generateMessageBlocks(messageFilled, int(len(messageFilled)/12))
    blockSize = 12
    encryptedMessage = encryptWithCBC(messageBlocks, IV, cipherKey)
    return encryptedMessage

def encryptWithCBC(MB, IV, cipherKey):
    """
    Funcion que realiza el proceso de cifrado CBC del mensaje a cifrar en forma de bloques MB.
    Es la codificacion del esquema de cifrado CBC.
    """
    C = []
    C.append(simplifiedDES_Encrypt(xor(MB[0],IV,12),cipherKey,8))
    for i in range(1, len(MB)):
        C.append(simplifiedDES_Encrypt(xor(MB[i],C[i-1],12),cipherKey,8))
    return C

def decryptWithCBC(CB, IV, cipherKey):
    """
    Funcion que realiza el proceso de descifrado CBC del mensaje cifrado en forma de bloques CB.
    Es la codificacion del esquema de descifrado CBC.
    """
    M = []
    M.append(xor(simplifiedDES_Decrypt(CB[0],cipherKey, 8),IV,12))
    for i in range(1, len(CB)):
        M.append(xor(simplifiedDES_Decrypt(CB[i],cipherKey,8),CB[i-1],12))
    return M
    
def decryptMessage(CB, IV, cipherKey):
    """
    Funcion que inicia el proceso de descifrado CBC del mensaje cifrado en forma de bloques CB
    """
    M = decryptWithCBC(CB, IV, cipherKey)
    m = ('').join(M)
    mOrig = m[0:len(m)-12-int(m[len(m)-12:len(m)][0:4],base=2)] 
    originalMessage = binaryToStringASCIIcode(mOrig)
    return originalMessage

def toStringBlocksSequence(seqCBCencryptedMessageBlocks):
    """
    Funcion que convierte una secuencia de bloques en una cadena de bits concatenando todos los bloques
    """
    return ('').join(seqCBCencryptedMessageBlocks)

def generateRandomIV():
    """
    Funcion que genera un vector de inicializacion aleatorio para el cifrado CBC
    """
    return generatePseudoRandomBinary(12)
    