import socket
import threading
from concurrent.futures import ThreadPoolExecutor

from PySide6.QtCore import QObject, Signal


class EthernetWorker(QObject):
    '''Класс запускает обмен данными с весами через Ethernet подключение.'''
    data_received = Signal(float)

    def __init__(self, ip, port, protocol):
        super().__init__()
        self.ip = ip
        self.protocol = protocol()
        self.port = port
        self.sock = None
        self.thread = None
        self._running = False
        self._lock = threading.Lock()
        self.executor = ThreadPoolExecutor(max_workers=1)
        self._stop_event = threading.Event()

    def start(self):
        if not self._running:
            self._stop_event.clear()
            self.thread = threading.Thread(target=self.run)
            self.thread.start()
            self._running = True

    def run(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.ip, self.port))
            while not self._stop_event.is_set():
                with self._lock:
                    command = self.protocol.create_command()
                    print(command)
                    self.sock.send(command)
                    response = self.sock.recv(1024)
                    if response:
                        weight = self.protocol.parce_response(response)
                        self.data_received.emit(weight)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self._running = False
            if self.sock:
                self.sock.close()
                print(f"Socket connection to {self.ip}:{self.port} closed")

    def stop(self):
        self._stop_event.set()
        if self.sock:
            self.sock.close()
        self._running = False

    @staticmethod
    def is_connected(ip, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.close()
            return  f'successfully connected to {ip}:{port}'
        except (socket.timeout, socket.error) as e:
            return e
