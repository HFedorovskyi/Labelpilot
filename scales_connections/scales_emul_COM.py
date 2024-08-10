import time
import struct
import random
import serial
import threading


class ScaleEmulator:
    print(serial.__file__)

    def __init__(self, port='COM3', baudrate=19200):
        self.port = port
        self.baudrate = baudrate
        self.ser = None
        self.running = False
        self.current_weight = 12450
        self.division = 2  # Цена деления 10 г
        self.stable = 0  # Нестабильна
        self.net = 0
        self.zero = 0
        self.tare = 0
        self.stable_count = 0
        self.stability_threshold = 5  # Количество повторов для стабилизации
        self.max_weight_change = 50  # Максимальное изменение веса
        self.is_stable = False

    def calculate_crc(self, data):
        crc = 0xFFFF
        for byte in data:
            crc ^= byte << 8
            for _ in range(8):
                if crc & 0x8000:
                    crc = (crc << (1 ^ 0x1021))
                else:
                    crc <<= 1
        return crc & 0xFFFF

    def create_response(self):
        body = b'\xF8\x55\xCE' + struct.pack('<H', 7) + b'\x10'
        body += struct.pack('<i', self.current_weight)
        body += struct.pack('B', self.division)
        body += struct.pack('B', self.stable)
        crc = self.calculate_crc(body)
        response = body + struct.pack('<H', crc)
        return response

    def generate_weight(self):
        if self.stable_count >= self.stability_threshold:
            self.stable = 1
            if not self.is_stable:
                print("Вес стабилизировался:", self.current_weight)
                self.is_stable = True
        else:
            self.stable = 0
            change = random.randint(-self.max_weight_change, self.max_weight_change)
            self.current_weight += change
            # Убедимся, что вес остается в допустимом диапазоне (0 или выше)
            self.current_weight = max(0, self.current_weight)
            self.stable_count += 1
            self.is_stable = False

    def handle_request(self):
        while self.running:
            if self.ser.in_waiting > 0:
                request = self.ser.read(8)
                print(request)
                if request[:3] == b'\xF8\x55\xCE' and request[5] == 0xA0:
                    self.generate_weight()
                    response = self.create_response()
                    self.ser.write(response)
                    print("Отправлен ответ:", response)
            time.sleep(0.1)
            if self.is_stable and random.random() < 0.1:  # 10% вероятность сброса стабилизации
                self.stable_count = 0
                self.is_stable = False
            if random.random() < 0.05:  # 5% вероятность прохождения через 0
                self.current_weight = 0
                self.stable_count = 0
                self.is_stable = False
                print("Вес прошел через ноль")

    def start(self):
        self.ser = serial.Serial(self.port, self.baudrate, timeout=1)
        self.running = True
        self.thread = threading.Thread(target=self.handle_request)
        self.thread.start()
        print(f"Scale Emulator started on {self.port}")

    def stop(self):
        self.running = False
        if self.thread.is_alive():
            self.thread.join()
        if self.ser.is_open:
            self.ser.close()
        print("Scale Emulator stopped")


if __name__ == "__main__":
    emulator = ScaleEmulator(port='COM3')
    try:
        emulator.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        emulator.stop()
