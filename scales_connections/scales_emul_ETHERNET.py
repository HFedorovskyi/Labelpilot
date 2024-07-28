import socket
import struct
import random
import threading
import time

class ScaleEmulator:
    def __init__(self, ip='127.0.0.1', port=12345):
        self.ip = ip
        self.port = port
        self.server_socket = None
        self.client_socket = None
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
                    crc = (crc << 1) ^ 0x1021
                else:
                    crc <<= 1
        return crc & 0xFFFF

    def create_response(self):
        body = b'\xF8\x55\xCE' + struct.pack('!H', 9) + b'\x24'
        body += struct.pack('!i', self.current_weight)
        body += struct.pack('!B', self.division)
        body += struct.pack('!B', self.stable)
        body += struct.pack('!B', self.net)
        body += struct.pack('!B', self.zero)
        body += struct.pack('!i', self.tare)
        crc = self.calculate_crc(body)
        response = body + struct.pack('!H', crc)
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
            self.current_weight = max(0, self.current_weight)
            self.stable_count += 1
            self.is_stable = False

    def handle_client(self, conn, addr):
        print(f"Connection from {addr}")
        while self.running:
            request = conn.recv(8)
            print(request)
            if request[:3] == b'\xF8\x55\xCE' and request[5] == 0x23:
                self.generate_weight()
                response = self.create_response()
                conn.sendall(response)
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
        conn.close()

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen(1)
        self.running = True
        print(f"Scale Emulator started on {self.ip}:{self.port}")
        while self.running:
            self.client_socket, addr = self.server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(self.client_socket, addr))
            client_thread.start()

    def stop(self):
        self.running = False
        if self.client_socket:
            self.client_socket.close()
        if self.server_socket:
            self.server_socket.close()
        print("Scale Emulator stopped")

if __name__ == "__main__":
    emulator = ScaleEmulator(ip='127.0.0.1', port=12345)
    try:
        emulator.start()
    except KeyboardInterrupt:
        emulator.stop()
