import socket
import threading
import sys
import pickle
from chat import chat
from dbclient import dbclient

class cliente_sock:
	
    def __init__(self, host="127.0.0.1", port=9879):        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((str(host), int(port)))
        msg_recv = threading.Thread(target=self.msg_recv)
        msg_recv.daemon = True
        msg_recv.start()        

        self.dbclient = dbclient()
        nombre = input('(CLI) Ingresar nombre:')

        while True:
            msg = input('-> Ingresar Texto (q) salir\n')
            if msg.lower() == 'q':
                self.sock.close()
                sys.exit(0)
            else:
                cliente = chat(nombre, msg)
                self.dbclient.insert_new_record(cliente)
                self.send_msg(msg)
    
    def msg_recv(self):
        while True:
            try:
                data = self.sock.recv(1024)
                if data:
                    print(pickle.loads(data))
            except:
                pass

    def send_msg(self, msg):
        self.sock.send(pickle.dumps(msg))

if __name__ == '__main__':
    c = cliente_sock()