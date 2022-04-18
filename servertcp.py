#1 TCP - Servidor
#Importar la libreria socket
import socket

#Declarar las variables para el host y el puerto de conexion
HOST = ""
PORT = 65432

# Crear un objeto socket - Los argumentos pasados ​​a socket() son constantes 
# que se utilizan para especificar la familia de direcciones y el tipo de socket. 
# AF_INET es la familia de direcciones de Internet para IPv4. 
# SOCK_STREAM es el tipo de socket para TCP.
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    print ("Esperando conexion")
    # El método .bind() se usa para asociar el socket 
    # con una interfaz de red y un número de puerto específico
    s.bind ((HOST, PORT))
    # .listen() permite que el servidor acepte conexiones. 
    # Hace que el servidor sea un socket de "escucha":
    s.listen()
    # El método .accept() bloquea la ejecución y espera una conexión entrante. 
    # Cuando un cliente se conecta, devuelve un nuevo objeto socket que representa 
    # la conexión y una tupla que contiene la dirección del cliente. 
    # La tupla contendrá (host, puerto) 
    conn,addr=s.accept()
    # Después de que .accept() proporciona el objeto de socket del cliente conn, 
    # se usa un bucle while infinito para pasar las llamadas de bloqueo a conn.recv(). 
    # Esto lee los datos que envía el cliente y los repite usando conn.sendall().
with conn:
    print(f"Conectado al cliente {addr}")
    # Se crea un bucle infinito en la cual guarda datos de 1024 en 1024 y recibe
    # los datos y envia los datos al cliente
    while True:
        data=conn.recv(1024)
        if not data:
            break
        conn.sendall(data)