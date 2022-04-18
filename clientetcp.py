#1 TCP - Cliente
#Importar la libreria socket
import socket

#Declarar las variables para el host y el puerto de conexion
HOST = "127.0.0.1"
PORT = 65432

# Crear un objeto socket - Los argumentos pasados ​​a socket() son constantes 
# que se utilizan para especificar la familia de direcciones y el tipo de socket. 
# AF_INET es la familia de direcciones de Internet para IPv4. 
# SOCK_STREAM es el tipo de socket para TCP.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # En comparación con el servidor, el cliente es bastante simple. 
    # Crea un objeto socket, usa .connect() para conectarse al servidor y llama 
    # a s.sendall() para enviar su mensaje. Por último, llama a s.recv() 
    # para leer la respuesta del servidor y luego la imprime.
    s. connect((HOST, PORT))
    s.sendall (b' Hola mundo desde el cliente')
    data = s.recv(1024)
    print (f"Recibido {data!r}")

