import socket
from threading import Thread

class Server:
    def __init__(self, servaddress):
        self.server_address = servaddress
        self.BUFFERSIZE = 1024

        self.clients_names = {}
        self.clients_addrs = {}

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(self.server_address)

    def connecting(self):
        self.server_socket.listen(3)
        print('Waiting for connection')
        while True:
            client, client_address = self.server_socket.accept()
            print(f'{client_address} has connected')
            self.clients_addrs[client] = client_address

            welcome_msg = 'Wazzzzzzzuuuuup!! You`re online now'
            client.sendall(welcome_msg.encode('utf-8'))

            name = client.recv(self.BUFFERSIZE).decode('utf-8')
            self.clients_names[client] = name
            self.broadcast(client, f'Say hello to my little friend {name} \n')

            Thread(target=self.process_connection, args=(client,)).start()

    def process_connection(self, client: socket):
        try:
            while True:
                message = client.recv(self.BUFFERSIZE).decode()
                if message == 'fluggegecheimen':
                    self.broadcast(client, f'{self.clients_names[client]} betrayed us\n')
                    print(f'{self.clients_addrs[client]} disconnected')
                    del self.clients_names[client], self.clients_addrs[client]
                    client.close()
                    break
                else:
                    self.broadcast(client, f'{self.clients_names[client]}: {message}\n')
        except ConnectionResetError:
            print(f'{self.clients_addrs[client]} connection lost')
            del self.clients_names[client], self.clients_addrs[client]
            client.close()


    def broadcast(self, client: socket, message):
        for client_name in self.clients_names.keys():
            if client_name != client:
                client_name.sendall(message.encode('utf-8'))


if __name__ == '__main__':
    server_host = input('Enter server host: ')
    server_port = int(input('Enter server port: '))
    server_address = (server_host, server_port)
    chat = Server(server_address)
    conn_thread = Thread(target=chat.connecting)
    conn_thread.start()
    conn_thread.join()
    chat.server_socket.close()
