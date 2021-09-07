import os
import time
import numpy as np 
import math 
from math import pow, sin, cos, asin, sqrt, radians
os.system("cls")
"""#Reto1:
a="51607"
b="70615"
c = "607"
captcha2 = int ((5-1)/7*0)
Contraseña = 0
#R1RF01: El programa dispone de un mensaje de bienvenida al sistema previo a la solicitud de las credenciales de acceso
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
#RF02: El programa dispone de un usuario y una contraseña predefinidos para el inicio de sesión en consola los condicionales if usuario==a y contraseña ==b 
#se encargan de validar la contraseña y usuario en caso de no funcionar bota un error en la consola
Usuario=(input("Ingrese su Usuario:")) 
if  Usuario == a:
    Contraseña= (input("Ingrese su Contraseña:"))
else:
    print("Error")
    quit() 
if Contraseña == b:
#R1RF03: El programa dispone de un captcha de seguridad que confirma que el inicio de sesión corresponde a un usuario.
        Captcha = (input(str(c)+"+"+str(captcha2)+"=")) 
else:
    print("Error")
    quit() 

#R1RF04: El programa confirma el ingreso al sistema con un mensaje de éxito en el inicio de sesión
if Captcha == c:
            print ("Sesión iniciada")
else:
    print("Error")
    quit()"""  
#Reto2
#RF01: El programa muestra el siguiente menú de opciones en consola para el uso del programa: 
#1. Cambiar contraseña, 2. Ingresar coordenadas actuales, 3. Ubicar zona wifi más cercana, 4. Guardar archivo con ubicación cercana, 5. Actualizar registros de zonas wifi
#desde archivo, 6. Elegir opción de menú favorita, 7. Cerrar sesión
lopciones= ["Cambiar contraseña","Ingresar coordenadas actuales","Ubicar zona wifi más cercana",
"Guardar archivo con ubicación cercana","Actualizar registros de zonas wifi desde archivo",
"Elegir opción de menú favorita","Cerrar sesión"]
import os 
import time
os.system("cls")
contador=0
coordenadas=[]
lapromedio=0
lopromedio=0
actualizarcoor=0
for i, opciones in list(enumerate(lopciones,1)):
    print("{}".format(i), opciones)


#RF02 y parte de RF01: El programa permite elegir una opción del menú como favorito
#while para el manejo y control del menu y opciones favoritas
while contador < 3:
    
    #elija la opcion del menu
    opcion=int(input("Elija una opción:"))
    #condicion para que cuando se escoja el 6 se pida una opcion del 1 al 5
    if opcion ==6:
            opcfav = int(input("Seleccione opción favorita:"))
        #condicion para evaluar que el dato seleccionado sea entre 1 y 5
            if opcfav <=5  and opcfav > 0:
            #primera adivinanza junto a su input para pedir la respuesta
                os.system("cls")
                print("Primera adivinanza: Para confirmar por favor responda:\nRedondo soy y es cosa anunciada que a la derecha algo valgo,\n pero a la izquierda nada.")
                acertijo1=int(input("la respuesta es:"))
            #condicion para verificar la respuesta de la primera adivinanza
                if acertijo1 == 0:
                #segunda adivinanza junto a su input para pedir la respuesta
                    os.system("cls")
                    print("Segunda adivinanza:Cuenta los dedos de tu mano derecha\n y cuenta los de tu mano izquierda menos el dedo del medio, el indice y el pulgar\n ¿cuantos dedos contaste? ")
                    acertijo2=int(input("la respuesta es:"))
                #condicioon para verificar la respuesta de la segunda adivinanza
                    if acertijo2 ==7:
                        os.system("cls")
                        if opcfav >= 1 and opcfav <=5:
                            lopciones.insert(0,lopciones[opcfav-1])
                            del lopciones[opcfav] 
                            for i, opciones in list(enumerate(lopciones,1)):
                                print("{}".format(i), opciones)
                #en caso de que la condicion no se cumpla limpia la consola y presenta nuevamente el menu
                    else:
                        print("Error")
                        time.sleep(1)
                        os.system("cls")
                        for i, opciones in list(enumerate(lopciones,1)):
                            print("{}".format(i), opciones)
            #en caso de que la condicion no se cumpla limpia la consola y presenta nuevamente el menu
                else:
                    print("Error")
                    time.sleep(1)
                    os.system("cls")
                    for i, opciones in list(enumerate(lopciones,1)):
                        print("{}".format(i), opciones)
        #si la opcion favorita no esta entre 1 y 5 marca error y cierra el programa    
            else:
                print("Error")
                time.sleep(1)
                os.system("cls")
                quit()
#RF03: El programa genera una alerta si el usuario elige una opción incorrecta 
    elif opcion < 1 or opcion > 7:
        print("Error")
        time.sleep(1)
        os.system("cls")
        contador +=1
        for i, opciones in list(enumerate(lopciones,1)):
            print("{}".format(i), opciones)
#RF04: El programa permite acceder a las opciones del menú
#Reto3
#RF01: El programa permite al usuario actualizar su contraseña.
#ESTE elif tiene dentro if y elif esto permiten acceder a la opciones del menu
    elif opcion >=1 and opcion <=5:
        print("Usted ha elegido la opción: {}".format(opcion))
        #condicion para el cambio de contraseña
        if lopciones[opcion-1] == "Cambiar contraseña":#opcion para cambio de contraseña
            #bn es contraseña nueva y b la actual
            b=int(input("Digite la contraseña actual:"))
            if b == 70615:
                bn=int(input("Digite la nueva contraseña:"))
                #si la condicion de contraseña se cumple es exitoso el cambio de contraseña 
                if bn != b:
                    print("Cambio de contraseña exitoso")
                    time.sleep(2)
                    os.system("cls")
                    for i, opciones in list(enumerate(lopciones,1)):
                        print("{}".format(i), opciones)        
                #la condicion no se cumplio por lo tanto salta el mensaje
                else:
                    os.system("cls")
                    print("La nueva contraseña no puede ser igual a la anterior")
                    time.sleep(2)
                    quit()
            #error salta por contraseña que no es correcta 
            else:
                os.system("cls")
                print("Error")
                quit()
#RF02: El programa permite al usuario ingresar las coordenadas de los
#tres sitios que más frecuenta (trabajo, casa, parque)  
        elif lopciones[opcion-1] == "Ingresar coordenadas actuales":#opcion para ingresar coordenadas
            if len(coordenadas)==0:
                coordenadas=[[0]*2 for i in range(3)]
                for i in range(3):
                    for j in range(2):
                        try:
                            if j==0:
                                coordenadas[i][j] = float(input("Digite la latitud para la coordenada "+str(i+1)+":"))
                                coordenadas[i][j] = round(coordenadas[i][j],3)
                                if coordenadas[i][j] >  -3.002 or coordenadas[i][j]<-4.227:
                                    print("Error coordenada")
                                    exit()
                            else:
                                coordenadas[i][j] = float(input("Digite la longitud para la coordenada "+str(i+1)+":"))
                                coordenadas[i][j] = round(coordenadas[i][j],3)
                                if coordenadas[i][j] >  -69.714 or coordenadas[i][j]<-70.365:
                                    print("Error coordenada")
                                    exit()
                                else:
                                    os.system("cls")
                                    for i, opciones in list(enumerate(lopciones,1)):
                                        print("{}".format(i), opciones) 
                        except ValueError:
                            print("Error")
                            exit()
            #RF03: El programa permite al usuario actualizar las coordenadas de los tres sitios más frecuentados
            else:
                for i in range(3):
                    print("coordenada[latitud,longitud] "+str(i+1)+" :",coordenadas[i])
                print("la coordenada "+str(coordenadas.index(max(coordenadas))+1)+" es la que esta más ubicada al norte")
                print("la coordenada "+str(coordenadas.index(min(coordenadas))+1)+" es la que esta más ubicada al sur")
                for i in range(3):
                    for j in range(2):
                        if j==0:
                            lapromedio+=coordenadas[i][j]
                        else:
                            lopromedio+=coordenadas[i][j]
                lapromedio/=3
                lopromedio/=3
                lapromedio=round(lapromedio,3)
                lopromedio=round(lopromedio,3)
                print("La coordenada promedio de todos los puntos[latitud,longitud] :["+str(lapromedio)+","+str(lopromedio)+"]")
                time.sleep(2)
                try:
                    actualizarcoor=int(input("Presione 1,2 ó 3 para actualizar la respectiva coordenada \nPresione 0 para regresar al menú: "))
                    if actualizarcoor>=1 and actualizarcoor<= 3:
                        coordenadas[actualizarcoor-1][0]= round(float(input("Digite la latitud para la coordenada "+str(actualizarcoor)+":")),3)
                        if coordenadas[int(actualizarcoor)-1][0]>  -3.002 or coordenadas[int(actualizarcoor)-1][0] <-4.227:
                            print("Error coordenada")
                            exit()
                        coordenadas[actualizarcoor-1][1]= round(float(input("Digite la longitud para la coordenada "+str(actualizarcoor)+":")),3)
                        if coordenadas[i][j]>  -69.714 or coordenadas[i][j] <-70.365:
                            print("Error coordenada")
                            exit()
                        else:
                            os.system("cls")
                            for i, opciones in list(enumerate(lopciones,1)):
                                print("{}".format(i), opciones) 
                    elif actualizarcoor==0:
                        os.system("cls")
                        for i, opciones in list(enumerate(lopciones,1)):
                            print("{}".format(i), opciones) 
                    else:
                        print("Error actualización")
                        exit()
                except:
                    print("Error actualización")
                    exit()
            #Reto4 
            #RF01: El programa dispone de manera predefinida la ubicación de cuatro zonas wifi con su respectivo promedio de usuarios.
            #se espera que la información esté almacenada en una matriz de 4 filas y 3 columnas según el penúltimo digito del código del grupo “Fundamentos de programación” y la tabla anexa al final de este documento
            #acontinuacion pasare a definir todas las funciones para el reto 4
            ubicaciondeusuarioscercanos = [[-3.777, -70.302, 91],  # Tabla de coordenadas predefinidas con promedio de usuarios
                           [-4.134, -69.983, 233],
                           [-4.006, -70.132, 149],
                           [-3.846, -70.222, 211]]
            def recorrido(p1, p2):  # funcion que hallara la recorrido entre coordenadas -->RETO4
                R = 6372.795477598
    #p1 = (radians(p1[0]), radians(p1[1]))
    #p2 = (radians(p2[0]), radians(p2[1]))
                dellat = p2[0]-p1[0]
                dellon = p2[1]-p1[1]
                a = pow(sin(dellat/2), 2)+cos(p1[0])*cos(p2[0])*pow(sin(dellon/2), 2)
                return 2*R*asin(sqrt(a))
    


            def matriz_lugares(p,e): #funcion que imprimira la tabla de la RF02 --> RETO4
                e = int(e)
                print("Zonas wifi cercanas con menos ususarios")
                for j in range(len(p)):
                    i = 0
                    print("La zona wifi", j+1, ': ubicada en [ ', "{0:.3f}".format(p[j][i]),
                    "{0:.3f}".format(p[j][i+1]), "] a", int(
                    recorrido(coordenadas[e-1], lista[j])),
                    "metros, tiene en promedio", p[j][i+2], "usuarios")
            def direccion_recorrido(x, y,e): # -->RETO4
                e = int(e)
                procesosdeindicaciones = input("Elija 1 o 2 para recibir indicaciones de llegada")
                os.system("cls")
                if procesosdeindicaciones == "1":
                    if y[0][0] > x[0]:
                        if y[0][1] > x[1]:
                            print( "Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el norte")
                        else:
                            print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el norte")
                    else:
                        if y[0][1] > x[1]:
                            print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el sur")
                        else:
                            print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el sur")
                    tiempo_a_pie = (recorrido(x, lista[0]))/0.483
                    tiempo_en_auto = (recorrido(x, lista[0]))/20.83
                    print("Tardara en promedio"+ str(tiempo_a_pie//60) +"minutos si se dirige a pie.")
                    print("Tardara en promedio"+str(tiempo_en_auto//60) +"minutos si se dirige en auto.")
                elif procesosdeindicaciones == "2":
                    if y[1][0] > x[0]:
                        if y[1][1] > x[1]:
                            print( "Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el norte")
                        else:
                            print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el norte")
                    else:    
                        if y[1][1] > x[1]:
                            print("Para llegar a la zona wifi dirigirse primero al oriente y luego hacia el sur")
                        else:
                            print("Para llegar a la zona wifi dirigirse primero al occidente y luego hacia el sur")
                            tiempo_a_pie = (recorrido(x, lista[1]))/0.483
                            tiempo_en_auto = (recorrido(x, lista[1]))/20.83
                            print("Tardara en promedio"+ str(tiempo_a_pie//60) +"minutos si se dirige a pie.")
                            print("Tardara en promedio"+ str(tiempo_en_auto//60) +"minutos si se dirige en auto.")
                else:
                    print("Error zona wifi")
                    quit()
        elif lopciones[opcion-1] == 'Ubicar zona wifi más cercana':
            os.system("cls")
            if len(coordenadas) == 0:  # RF02 --> RETO4  si el usuario no ha ingresado antes sus lugares frecuentes ejecutara error y fin del programa
                print("Error sin registro de coordenadas")
                quit()
            else:
                os.system("cls")
                # recorreremos e imprimiremos nuestra matriz de coordenadas
                for j in range(0, len(coordenadas)):
                    i = 0
                    print("Coordenada [latitud,longitud]", j+1, '= [ ', "{0:.3f}".format(
                        coordenadas[j][i]), "{0:.3f}".format(coordenadas[j][i+1]), "]")
                ubicacion_actual = input(
                    "Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión ")
                os.system("cls")
                lista = [[-3.777, -70.302, 91],  # Tabla de coordenadas predefinidas con promedio de usuarios que podremos modificar sin dañar la original
                           [-4.134, -69.983, 233],
                           [-4.006, -70.132, 149],
                           [-3.846, -70.222, 211]]
                '''
                en esta serie de if y elif hallaremos y ordenaremos las coordenadas mas cercanas y con menor promedio de usuarios.
                '''
                if ubicacion_actual == "1":
                    for i in range(len(ubicaciondeusuarioscercanos)):
                        lista[i].append(recorrido(coordenadas[0], ubicaciondeusuarioscercanos[i]))
                    lista.sort(key=lambda x: x[3])
                    del lista[2:]
                    lista.sort(key=lambda x: x[2])
                    matriz_lugares(lista,ubicacion_actual)
                    direccion_recorrido(coordenadas[0], lista,ubicacion_actual)
                    salir = int(input("Presione 0 para salir"))
                    if salir == 0:
                        continue
                elif ubicacion_actual == "2":
                    for i in range(len(ubicaciondeusuarioscercanos)):
                        lista[i].append(recorrido(coordenadas[1], ubicaciondeusuarioscercanos[i]))
                    lista.sort(key=lambda x: x[3])
                    del lista[2:]
                    lista.sort(key=lambda x: x[2])
                    matriz_lugares(lista,ubicacion_actual)
                    direccion_recorrido(coordenadas[1], lista,ubicacion_actual)
                    salir = int(input("Presione 0 para salir"))
                    if salir == 0:
                        for i, opciones in list(enumerate(lopciones,1)):
                                        print("{}".format(i), opciones) 
                elif ubicacion_actual == "3":
                    for i in range(len(ubicaciondeusuarioscercanos)):
                        lista[i].append(recorrido(coordenadas[2], ubicaciondeusuarioscercanos[i]))
                    lista.sort(key=lambda x: x[3])
                    del lista[2:]
                    lista.sort(key=lambda x: x[2])
                    matriz_lugares(lista,ubicacion_actual)
                    direccion_recorrido(coordenadas[2], lista,ubicacion_actual)
                    salir = int(input("Presione 0 para salir"))
                    if salir == 0:
                        for i, opciones in list(enumerate(lopciones,1)):
                                        print("{}".format(i), opciones) 
                        continue
                else:
                    print("Error ubicación")
                    quit()
        elif lopciones[opcion-1] == "Guardar archivo con ubicación cercana":   
            if len (coordenadas)==0:
                print("Error de alistamiento")
                time.sleep(2)
                quit()
            if len(ubicacion_actual)==0:
                print("Error de alistamiento")
                time.sleep(2)
                quit()
            wifi_cercano={"actual":ubicacion_actual,"zonawifi":[ubicaciondeusuarioscercanos[0][0:3]],"recorrido":[ubicaciondeusuarioscercanos[0][3],"auto",tiempo_en_auto]} 
            print(wifi_cercano)                            
#RF05: El programa permite al usuario salir del menú.
    elif opcion == 7:
        os.system("cls")
        print("Hasta pronto")
        quit()
else:
    print("Error")
    quit()