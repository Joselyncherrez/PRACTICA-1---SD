#Implementar la libreria de python SOCKET
import socket 

#Estabalecer un puerto mayor de 65000 por motivos de seguridad
#Y tambien indicar la IP del servidor
HOST="127.0.0.1" 
PORT= 65432

#Crear una variable s que se conecte con IPv4 o IPv6 implementando un protocolo SOCK_DGRAM de UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s : 
    #Imprime un mensaje que se esta enviando el texto correctamente al servidor
    s.connect((HOST,PORT)) 
    s.sendall(b'Enviando un mensaje al servidor UDP ') 
    #Guarda datos de 1024 en 1024 y recibo 
    #los datos y envio los datos al servidor
    data=s.recv(1024) 
    #Imprime un mensaje que se ha conectado exitosamente y enviado el texto al servidor
    print(f" Conexion exitosa al servidor UPD \n Se recibió \n {data!r}")