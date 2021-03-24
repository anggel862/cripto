from m_blocks_fill import *;
from m_simplifiedDES import *;

def main():
    messageToEncrypt =  generatePseudoRandomBinary(12)
    cipherKey = generatePseudoRandomBinary(9)
    iterations = 8
    messageEncrypted = simplifiedDES_Encrypt(messageToEncrypt=messageToEncrypt, cipherKey=cipherKey, iterations=8)
    #print ("m:"+messageToEncrypt+" k:"+cipherKey+" iterations: "+str(iterations)+"-->mE:"+messageEncrypted)
    print("m:"+messageToEncrypt+" "+str(int(messageToEncrypt,2))+" k:"+cipherKey+" "+str(int(cipherKey,2)))
    k=cipherKey
    x = messageToEncrypt
    print("mEncrypted= "+messageEncrypted+" "+str(int(messageEncrypted,2)))

    #g(k,x) = ek(x) XOR x
    resultadoG = xor(simplifiedDES_Encrypt(x,k,iterations),x,12)

    compressed1 = g(k+x)

    h1(compressed1)

    print("ok")

def h1(compressed):
    print("Compressed="+compressed+" "+str(int(compressed,2)))
    n = 12
    r = len(compressed)-n 
    X = compressed
    Xr = addZerosUntilMultiple(X,12)
    x1 = X1(Xr)
    print("ok")

def addZerosUntilMultiple12(X):
    zeros='0'
    while(len(X)%12 != 0):
        X=zeros+X
        #print("zeros="+zeros+" X="+X)
    return X

def addZerosUntilMultiple(X,divisibleBy):
    zeros='0'
    while(len(X) % divisibleBy != 0):
        X=zeros+X
        #print("zeros="+zeros+" X="+X)
    return X

def X1(X):
    Xorig = X
    #Agregamos a X en las posiciones MSB tantos ceros como sea necesario para que sea multiplo de r
    r = 9
    X = addZerosUntilMultiple(X,r) 
    #En las posiciones LSB agregamos r ceros para obtener x1
    x1 =X+''.zfill(r)
    #En las posiciones MSB significativas de la cadena original X(Xorig) tantos ceros como sea necesario para que sea multiplo de r-1
    x2_1 = addZerosUntilMultiple(Xorig,(r-1))
    #En las subsecuencias de (r-1) de la cadena agregamos un '1'
    x2 = addOneToEachSubseq(x2_1,r)
    h(x2)
    return x2

def h(X):
    Xparts = [ X[i:i+9] for i in range(0, len(X), 9)]
    H0 = ''.zfill(12)
    res = ''
    Hi = H0
    for i in range(0,len(Xparts)):
        Hi = g(Hi+Xparts[i])
        print("ok")
    return Hi

def addOneToEachSubseq(x1,r):
    iterations = int(len(x1)/(r-1))
    x1res = ''
    for i in range(0,iterations):
        x1res += '1'+x1[0+(r-1)*i:(r-1)*i+(r-1)]
        print("i="+str(i)+" "+x1res+" "+str(int(x1res,2)))
        print("i="+str(i)+" "+x1[0+8*i:8*i+8]+" "+str(int(x1[0+8*i:8*i+8],2)))
    return x1res

def g(kx):
    k = kx[0:9]
    x = kx[9:21]
    #print("x:"+x+" "+str(int(x,2))+" k:"+k+" "+str(int(k,2)))
    ek_x = simplifiedDES_Encrypt(x,k,8)
    #print("ek(x)="+ek_x+" "+str(int(ek_x,2)))
    gkx = xor(ek_x,x,12)
    #print("gkx="+gkx+" "+str(int(gkx,2)))
    return gkx
    #print("ok")

if __name__ == '__main__':
    main()