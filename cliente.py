#Poplib Incrementa un protocolo real al momento de instanciar el tiempo de espera
#la funcion principal del cliente es conectarse con los zocalos del servidor
from poplib import POP3_PORT

#Implementar la libreria de python SOCKET
import socket

#Crea un variable CLIENTEMULTIUSUARIO para crear subprocesos multiples
ClienteMultiusuario = socket.socket()
#Establecer un puerto mayor de 65000 por motivos de seguridad y la direccion IP
HOST = "127.0.0.1"
PORT = 65432
print('Esperando respuesta de conexión')

#Conexión del HOST y PORT para que escuche la conexion del cliente enviando un mensaje de error
try:
    ClienteMultiusuario.connect((HOST, PORT))
except socket.error as e:
    print(str(e))
res = ClienteMultiusuario.recv(1024)

while True:
    Input = input('Escriba aquí: ')
    #Devuelve la respuesta del servidor a un cliente
    #Envia datos al socket ya que se conectan para la entrada de datos
    ClienteMultiusuario.send(str.encode(Input))
    res = ClienteMultiusuario.recv(1024)
    print(res.decode('utf-8'))
ClienteMultiusuario.close()
    #Este ejemplo fue buscado de 
    # https://www.positronx.io/create-socket-server-with-multiple-clients-in-python/