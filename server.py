#Implementar la libreria de python SOCKET
import socket
#Implementar la funcion dependiente del sistema operativo para manipular la estructura de directorios
#Para poder leer o escribir archivos
import os
#Es un hilo de implemento de multiusuarios para que no tenga una sola comunicación sino varias
from _thread import *
ServerMultiusuario = socket.socket()


#Establecer un puerto mayor de 65000 por motivos de seguridad y tambien enlazar conexion hacia los clientes
HOST = ""
PORT = 65432
hilo = 0

#Conexión del HOST y PORT para que escuche la conexion del cliente enviando un mensaje de error
try:
    ServerMultiusuario.bind((HOST, PORT))
except socket.error as e:
    print(str(e))
print('Servidor conectado...')
ServerMultiusuario.listen(5)

#Conexion por diversas direcciones a varios clientes
def hilo_multiusuario(connection):
    connection.send(str.encode('Servidor trabajando:'))
    while True:
        data = connection.recv(2048)

        #Captura de datos por separado de cada cliente en especifico
        response = 'Mensaje del servidor: ' + data.decode('utf-8')
        if not data:
            break

        #Devuelve la respuesta del servidor a un cliente
        #Envia datos al socket ya que se conecta remotamente enviando una respuesta
        connection.sendall(str.encode(response))
    connection.close()

#While ayuda al servidor a tener una conexión constante
while True:
    Client, address = ServerMultiusuario.accept()

    #Devuelve la informacion a los clientes conectados
    print('Conectado con: ' + address[0] + ':' + str(address[1]))

    #Especifica las conexiones del cliente realizando un hilo de usuarios en linea
    start_new_thread(hilo_multiusuario, (Client, ))
    hilo += 1
    print('Número de conexión: ' + str(hilo))
ServerMultiusuario.close()