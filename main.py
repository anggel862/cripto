# -*- coding: utf-8 -*-
from m_simplifiedDES import *
from m_blocks_fill import generatePseudoRandomBinary

def main():
    #Fase 1 funcion de compresion
    #h(generatePseudoRandomBinary(21),9) 
    lengths = [0, 1, 10, 100, 1000, 10000, 100000, 1000000]
    """ for x in lengths:
        xi = generatePseudoRandomBinary(x)
        print(xi)
        print("Hash: "+h(xi)) """
    print("Fin")   

def get_x1x2(X,r):
    #Obtener X1
    #1- agregar a X en las posiciones MSB '0' hasta que len(X) sea multiplo de r
    xRmultiple = addZerosUntilMultiple(X,r)
    #2- agregar en las posiciones LSB r '0'
    xRmultiple0 = xRmultiple+''.zfill(r)
    x1 = xRmultiple0
    #Obtener X2
    #1- agregar en las posiciones MSB de la representacion en binario de la cadena original X '0' hasta que len(X) sea multiplo de r-1
    binaryRep = bin(len(X)).replace('0b','')
    binaryRepR_1 = addZerosUntilMultiple(binaryRep,r-1)
    #2- agregar al inicio de las subsecuencias de (r-1) en xR_1multiple0 un '1'
    x2 = addOneToEachSubseq(binaryRepR_1, r)
    x1x2 = x1+x2
    return x1x2

#Fase 2 funcion hash
def h(X):
    r=9
    x1x2 = get_x1x2(str(X),r)
    #Calculo de hash
    #t secuencias de longitud r
    Xparts = [ x1x2[i:i+r] for i in range(0, len(x1x2), r)]
    #H0=0..0 (n=12)
    Hi = ''.zfill(12)
    t=len(Xparts)-1
    for i in range(0, t):
        Hi = g(Hi+Xparts[i])
        #print("H"+str(i)+"="+Hi)
    return Hi

#Fase 1 funcion de compresion
def g(kx):
    k = kx[0:9]
    x = kx[9:21]
    ek_x = simplifiedDES_Encrypt(x,k,8)
    gkx = xor(ek_x,x,12)
    return gkx

def addZerosUntilMultiple(X,divisibleBy):
    zeros='0'
    while(len(X) % divisibleBy != 0):
        X=zeros+X
    return X

def addOneToEachSubseq(x1,r):
    iterations = int(len(x1)/(r-1))
    x1res = ''
    for i in range(0,iterations):
        x1res += '1'+x1[0+(r-1)*i:(r-1)*i+(r-1)]
    return x1res



if __name__ == '__main__':
    main()