import socket
import threading
import sys
import pickle
#from semaforo_ventana import SemaforoVentana

class semaforo_cliente:
	
    def __init__(self, host="127.0.0.1", port=9879):        
        # self.obj_semaforo_ventana = SemaforoVentana(sys.argv[1])        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((str(host), int(port)))
        msg_recv = threading.Thread(target=self.msg_recv)
        msg_recv.daemon = True
        msg_recv.start()
        
        while True:
            msg = input('-> Escoger operación: \n(1) Presionar rojo \n(2) Presionar verde \n(q) salir\n') 
            if msg == '1' or msg == '2':
                self.send_msg(msg)
            elif msg.lower() == 'q':
                self.sock.close()
                sys.exit(0)
    
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
    c = semaforo_cliente()