import socket
import threading

def recibir_mensajes(sock):
    while True:
        try:
            mensaje = sock.recv(1024).decode()
            if not mensaje:
                break
            print("\n" + mensaje)
        except:
            break

# Conexión
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#localhost tiene la direccion IP 127.0.0.1
client_socket.connect(("localhost", 12345))
print("Conectado al chat. Escribe tus mensajes:")

# Hilo receptor
threading.Thread(target=recibir_mensajes, args=(client_socket,), daemon=True).start()

# Enviar mensajes
while True:
    mensaje = input()
    if mensaje.lower() == "salir":
        break
    client_socket.send(mensaje.encode())

client_socket.close()


