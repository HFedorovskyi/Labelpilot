import serial
import threading
from concurrent.futures import ThreadPoolExecutor
import serial.tools.list_ports
from PySide6.QtCore import QObject, Signal
from app_logging.logging_config import logger


class SerialWorker(QObject):
    '''Класс запускает обмен данными с весами через COM подключение.'''
    data_received = Signal(float)

    def __init__(self, port, protocol):
        super().__init__()
        self.protocol = protocol()
        self.serial_port = None
        self.port = port
        self._stop_event = threading.Event()
        self._running = False
        self.thread = None
        self._lock = threading.Lock()
        self.executor = ThreadPoolExecutor(max_workers=1)

    def start(self):
        logger.debug('Start serial connections worker')
        if not self._running:  # Запускать поток только если он не запущен
            logger.debug('Thread not running! Creating new thread...')
            self._stop_event.clear()
            self.thread = threading.Thread(target=self.run)
            self.thread.start()
            self._running = True

    def run(self):
        try:
            self.serial_port = serial.Serial(port=self.port,
                                             baudrate=self.protocol.BRAUDRATE,
                                             parity=self.protocol.PARITY,
                                             stopbits=self.protocol.STOPBITS,
                                             timeout=1)
            while not self._stop_event.is_set():
                with self._lock:
                    logger.debug('Serial worker running...')
                    self.serial_port.write(self.protocol.create_command())
                    response = self.serial_port.read(20)
                    if response:
                        weight = self.protocol.parce_response(response)
                        self.data_received.emit(weight)
        except serial.SerialException as e:
            print(f"Error: {e}")
        finally:
            self._running = False
            if self.serial_port:
                self.serial_port.close()
                print(f"Serial port {self.port} closed")

    def stop(self):
        logger.debug('Stop serial connections worker')
        self._stop_event.set()
        self.executor.submit(self._close_port_async)
        logger.debug('Stop serial connections worker finished')

    def _close_port_async(self):
        with self._lock:
            if self.serial_port:
                try:
                    self.serial_port.close()
                    logger.debug('Serial port closed')
                except Exception as e:
                    print(f"Unexpected error during serial port closure: {e}")
            self._running = False

    @staticmethod
    def get_ports():
        ports = serial.tools.list_ports.comports()
        return [port.device for port in ports]

    @staticmethod
    def is_connected(port):
        try:
            with serial.Serial(port, 9600, timeout=1):
                return f'Подключение к {port} успешно!'
        except serial.SerialException as e:
            print(f"Error: {e}")
            return e