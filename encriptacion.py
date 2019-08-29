import math

print("\n-------------SISTEMA DE ENCRIPTACION------------- \n\n Que desea hacer? \n\n 1-encriptar mensaje \n 2-Desencriptar mensaje \n")

def key(x):
    return ((x+(x*3))*(37*x))%46

def encryp(string):
    lista = list(string)
    aux= []
    for i in lista:
        a = (ord(i))
        if(a == 32):
            aux.append(chr(a))
        else:
            a = (ord(i) + secret)
            if (a > 122):
                a = 65 + (a - 123)
            aux.append(chr(a))
    aux.reverse
    aux.append(" ")
    aux.append(str(clave))
    cad = "".join(aux)
    return cad

def desencryp(string):
    lista = list(string)
    aux= []
    for i in lista:
        a = (ord(i))
        if(a == 32):
            aux.append(chr(a))
        else:
            a = (ord(i) - secret)
            if (a < 65):
                a = 123 - (secret-(ord(i) - 65))
            aux.append(chr(a))
    aux.reverse
    cad = "".join(aux)
    return cad

opcion = int(input("seleccioone opción:"))
while opcion == 1 or opcion == 2:
    if(opcion == 1):
        mensage = input("ingrese la cadena a encriptar: ")
        clave = int(input("ingrese el numero clave: "))
        secret = key(clave)
        print("\n La cadena encriptada es:\n")
        print(encryp(mensage))
    else:
        mensage = input("ingrese la cadena a desencriptar: ")
        clave = int(input("ingrese el numero clave: "))
        secret = key(clave)
        print("\n La cadena desencriptada es:\n")
        print(desencryp(mensage))
    
    print("\n-------------SISTEMA DE ENCRIPTACION------------- \n\n Que desea hacer? \n\n 1-encriptar mensaje \n 2-Desencriptar mensaje \n")
    opcion = int(input("seleccioone opción:"))

