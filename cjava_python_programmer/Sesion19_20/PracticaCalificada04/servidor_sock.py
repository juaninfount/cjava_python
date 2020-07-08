import socket
import threading
import os
import sys
import pickle

class servidor_sock:

    def __init__(self, host="127.0.0.1", port=9879):                     
        self.clientes = []                
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((str(host), int(port)))
        self.sock.listen(10)
        self.sock.setblocking(False)        
        aceptar  = threading.Thread(target=self.aceptar_conexion)
        procesar = threading.Thread(target=self.procesar_conexion)
        aceptar.daemon = True
        aceptar.start()
        procesar.daemon = True
        procesar.start()      

        while True:
            msg = input('->\n')
            if msg == 'q':
                self.sock.close()
                sys.exit()
            else:
                pass  
                                                
    def msg_to_all(self, msg, cliente):
        for c in self.clientes:
            try:                
                if c != cliente:
                   c.send(msg) 
            except:
                self.clientes.remove(c)
            
    def procesar_conexion(self):
        print("procesar_conexion iniciado")
        
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        msg = c.recv(1024)                        
                        if msg:
                            self.msg_to_all(msg,c)                            
                            print(pickle.loads(msg))
                            
                    except Exception as e: print(e)                        

    def aceptar_conexion(self):
        print("aceptar_conexion iniciado")
        while True:
            try:
                conn, addr = self.sock.accept() 
                conn.setblocking(True)                
                self.clientes.append(conn)
            except:
                pass                    
    
if __name__ == '__main__':
    s = servidor_sock()