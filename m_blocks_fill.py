import datetime
import random


def stringToBinaryASCIIcode(stringToConvert):
    """Funcion que recibe una cadena de 50 caracteres como maximo para convertirla al formato binario de acuerdo al codigo ASCII"""
    if(len(stringToConvert)>50): 
        raise ValueError("La longitud de la cadena debe ser menor de 50 caracteres.")
    if(len(stringToConvert)<0): 
        raise ValueError("La longitud de la cadena debe ser mayor que 0 caracteres.")
    binaryConvertedFromString = ""
    for i in range(0, len(stringToConvert)):
        binaryCharTh = bin(ord(stringToConvert[i])).replace('0b','').zfill(8)
        binaryConvertedFromString += binaryCharTh    
    return binaryConvertedFromString

def binaryToStringASCIIcode(binaryStringToConvert):
    """Funcion que recibe una cadena de 400 caracteres en formato binario y la convierte al formato ASCII con la equivalencia
    caracter a caracter.
    """
    if(len(binaryStringToConvert)>421): 
        raise ValueError("La longitud de la cadena en binario debe ser menor de 421 caracteres")
    stringConvertedFromBinary = ""

    for i in range(0, len(binaryStringToConvert), 8):
        binaryCharTh = chr(int(binaryStringToConvert[i:i+8], base=2))
        stringConvertedFromBinary += binaryCharTh
    return stringConvertedFromBinary

def fillingBlockSchema(messageInBinaryToDivide):
    """
    Funcion para el procedimiento de relleno de bloques. El penultimo bloque contiene bits del mensaje original concatenados con los 
    bits necesarios generados aleatoriamente para completar la longitud del bloque del criptosistema. 
    El ultimo bloque contiene en los 8 MSB bits aleatorios y en los 4 LSB contiene bits del mensaje original.
    """
    m = messageInBinaryToDivide
    currentNblocks = int(len(m)/12)
    nbitsToFill = 12-(len(m)-12*currentNblocks)
    m += generatePseudoRandomBinary(nbitsToFill)
    blockController = bin(nbitsToFill).replace('0b','').zfill(4) + generatePseudoRandomBinary(8)
    m += ('').join(blockController)
    return m

def generateMessageBlocks(messageToDivide, nBlocks):
    """
    Este metodo genera los bloques correspondientes al mensaje messageToDivide y al numero de bloques nBlocks.
    """
    listMessageBlocks = []
    if(nBlocks==0):
        listMessageBlocks.append(messageToDivide)
    else:
        blockSize = 12
        for i in range(0,len(messageToDivide), 12):
            listMessageBlocks.append(messageToDivide[i:i+12])
        if(len(messageToDivide) % nBlocks != 0):
            listMessageBlocks = listMessageBlocks[0:len(listMessageBlocks)-1]
    return listMessageBlocks

def generatePseudoRandomBinary(length):
    """
    Funcion que genera un numero binario pseudoaleatorio de longitud length.
    """
    if(length < 0): raise ValueError("La longitud debe ser mayor que 0.")
    res = "0"
    if(length != 0):
        for i in range(1, length):
            res += str(random.randint(0,1))
    return res


