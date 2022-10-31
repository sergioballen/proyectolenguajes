import re
from cgi import print_environ
from re import M
from turtle import end_fill
import re
archivo=open("direcciones.txt","r")
direcciones=archivo.read().split(',')
for i in direcciones:
    print("--------------"+i+"------------")
#Ingresa la cadena
    C=i.lower()
    cadena=list(C.split(' '))
#la convierto en un arreglo dividio en espacios
    tam=len(cadena)

#Defino contador para recorrer el arreglo
    cont=0
    def contador():
        global cont
        cont+=1

#Defino los estados para las transiciones
    def Estado6():
        print("----------------------Estado 6")
        if cont < tam:
            if re.findall('[a-zA-Z]|[0-9]', cadena[cont]):
                print("-------------LA DIRECCION INGRESADA ES VALIDA------------")
            elif re.findall('(-)|[0-9]', cadena[cont]):
                contador()
                Estado5()
                print("-------------LA DIRECCION INGRESADA ES VALIDA------------")
            else:
                print("no es una direccion valida!!!!")
                


    def Estado5():
        print("----------------------Estado 5")
        if cont < tam:
            if re.findall('-', cadena[cont]):
                contador()
                Estado6()
            elif re.findall('[a-zA-Z]|[0-9]', cadena[cont]):
                print("-------------LA DIRECCION INGRESADA ES VALIDA------------")
            elif re.findall('n|#', cadena[cont]):
                contador()
                Estado5()
            else:
                print("no es una direccion valida!!!!")
                


    def Estado4():
        print("----------------------Estado 4")
        if cont < tam:
            if re.findall('([0-9]|[a-k])*-([0-9])*', cadena[cont]):
                print("-------------LA DIRECCION INGRESADA ES VALIDA------------")
            elif re.findall('[a-zA-Z]|[0-9]', cadena[cont]):
                contador()
                Estado5()
            elif re.findall('n|#|-', cadena[cont]):
                contador()
                Estado4()
            else:
                print("no es una direccion valida!!!!")
                
        else:
            print("no es una direccion valida!!!!")


    def Estado3():
        print("----------------------Estado 3")
        if cont < tam:
            if re.findall('(n|#)([0-9]|[a-k])*-([0-9])*', cadena[cont]):
                print("-------------LA DIRECCION INGRESADA ES VALIDA------------")
            elif re.findall('n|#', cadena[cont]):
                contador()
                Estado4()
            elif re.findall('([0-9]|[a-zA-Z])', cadena[cont]):
                contador()
                Estado4()
            else:
                print("no es una Direccion valida!!!!")
                
        else:
            print("no es una direccion valida!!!!")


    def Estado2():
        print("----------------------Estado 2")
        if cont < tam:
            if re.findall('[a-h]|[0-9]', cadena[cont]):
                contador()
                Estado3()
            elif re.findall('(autopista|au|avenida|av|ak|bis|bulevar|bl|carrera|calle|cl|kr|carretera|ct|circular|cq|circunvalar|cc|cv|paseo|ps|via|vi|vereda|vda|vd|kilometro|km|peatonal|pt|vt|variante|tc|tv|diagonal|troncal|dg|pasaje|pj|cll|krr|transversal)', cadena[cont]):
                contador()
                Estado01()
            else:
                print("no es un Direccion valida!!!!")
                
        else:
            print("no es una direccion valida!!!!")


    def Estado01():
        # entra cuando tiene sufijo de barrio
        print("----------------------Estado 01")
        if cont < tam:
            if re.findall('(autopista|au|ak|bis|bulevar|bl|carrera|calle|cl|kr|carretera|ct|circular|cq|avenida|av|circunvalar|cc|cv|paseo|ps|via|vi|vereda|vda|vd|kilometro|km|peatonal|pt|vt|variante|tc|tv|diagonal|troncal|dg|pasaje|pj|cll|krr|transversal)', cadena[cont]):
                contador()
                Estado2()
            elif re.findall('[a-zA-Z]', cadena[cont]):
                contador()
                Estado01()
            else:
                print("no es una direccion valida!!!!")
                
        else:
            print("no es una direccion valida!!!!")


    def Estado1():
        # Ingresa el primer elemento de la cadena
        print("----------------------Estado 1")
        if cont < tam:
            if re.findall('(autopista|au|avenida|av|ak|bis|bulevar|bl|carrera|calle|cl|kr|carretera|ct|circular|cq|circunvalar|cc|cv|paseo|ps|via|vi|vereda|vda|vd|kilometro|km|peatonal|pt|vt|transversal|variante|tc|tv|diagonal|troncal|dg|pasaje|pj|cll|krr)', cadena[cont]):
                contador()
                Estado2()
            elif re.findall('(barrio|localidad|ed|edificio|vereda|torre|conjunto|corregimiento|apartado)', cadena[cont]):
                contador()
                Estado01()
                # trato de validar calle pegado del numero "calle2a" pero aun no me sirve
            elif re.findall('(calle|carrera)([a-f]|[0-9])*', cadena[cont]):
                contador()
                Estado01()
            elif re.findall('[0-9]', cadena[cont]):
                Estado4()
            else:
                print("no es una direccion valida!!!!")
                
        else:
            print("no es una direccion valida!!!!")


    Estado1()