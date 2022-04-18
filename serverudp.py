#Implementar la libreria de python SOCKET
import socket
#Crear una variable s que se conecte con IPv4 o IPv6 
# implementando un protocolo SOCK_DGRAM de UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Estabalecer un puerto mayor de 65000 por motivos de seguridad
HOST = ""
PORT = 65432
#Imprime un mensaje de conexión enlazada con el HOST y PORT establecido
#Esta pequeña parte del codigo fue buscado de https://pythontic.com/modules/socket/recvfrom 
print(f"Conectandose al servidor en el puerto {PORT}")
s.bind((HOST,PORT))

    #crea un bucle infinito en la cual guarda datos de 1024 en 1024 y recibo
    # #los datos y envio los datos al cliente
while True:
    print('\nEsperando mensaje')
    data, address = s.recvfrom(1024)
    #Puede utilizarse con un servidor UDP para recibir datos de un cliente UDP o puede utilizarse 
    #con un cliente UDP para recibir datos de un servidor UDP.
    print(f"Conectado al cliente {address}")
    print(data)

    if data:
        #El método sendto() de la clase socket de Python,
        #se utiliza para enviar datagramas a un socket UDP.
        sent = s.sendto(data, address)
        #Se imprime que el mensaje fue enviado correctamente
        print(f"Mensaje enviado a {address}")
    
    break