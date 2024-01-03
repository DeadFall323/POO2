import threading
import socket
import time


class ClientThread(threading.Thread):
    def __init__(self, nome, contador, delay, sinc):
        threading.Thread.__init__(self)
        self.nome = nome
        self.contador = contador
        self.delay = delay
        self.sinc = sinc

    def run(self):
        print("Iniciando " + self.nome)
        #self.sinc.acquire()
        print_time(self.nome, self.contador, self.delay)
        #self.sinc.release()
        print("Finalizando " + self.nome)


def print_time(threadName, contador, delay):
    while contador:
        time.sleep(delay)
        print("{} : {}".format(threadName, time.ctime(time.time())))
        contador -= 1


sinc = threading.Lock()
thread1 = myThread("Thread-1 ", 5,1,sinc)
thread2 = myThread("Thread-2 ", 5,1,sinc)

thread1.start()
thread2.start()

#thread1.join()
#thread2.join()

print("Finalizando a thread principal...")


