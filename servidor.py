import socket # para manejar la conexión de red
import threading #para manejar múltiples clientes con hilos al mismo tiempo

clientes = []
nombres = ["Cliente 1", "Cliente 2"]

def manejar_cliente(numero_cliente):
    cliente = clientes[numero_cliente]
    otro_cliente = clientes[1 - numero_cliente]
    nombre = nombres[numero_cliente]

    while True:
        try:
            mensaje = cliente.recv(1024)
            if not mensaje:
                break
            mensaje_formateado = f"{nombre}: {mensaje.decode()}"
            otro_cliente.send(mensaje_formateado.encode())
        except:
            break
    cliente.close()#cierra el socket del cliente

# Configuración del servidor
#esos argumentos indica que el socket sera con ipV4 y TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(2)

# Mensaje de bienvenida
print("Servidor escuchando en el puerto 12345...\n")
print("Comandos disponibles para los clientes:")
print("escribir un mensaje normal y presionar [Enter] para enviarlo")
print("escribir 'salir' para cerrar la conexión\n")

# Esperar dos clientes
while len(clientes) < 2:
    conn, addr = server_socket.accept()
    clientes.append(conn)
    print(f"Conectado: {addr} como {nombres[len(clientes)-1]}")

# Iniciar hilos para manejar a los clientes
threading.Thread(target=manejar_cliente, args=(0,)).start()
threading.Thread(target=manejar_cliente, args=(1,)).start()
