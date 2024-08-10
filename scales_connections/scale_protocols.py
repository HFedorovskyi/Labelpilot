import abc
import struct
from abc import ABC


class ScaleProtocol(ABC):
    '''Протокол для обмена с весами МАССА-К'''
    HEADER = b'\xF8\x55\xCE'
    CMD_GET_MASSA = b'\x23'  # Код команды CMD_GET_MASSA
    BRAUDRATE = 19200
    STOP = 1
    PARITY = 'S'
    STOPBITS = 1  # Четность

    @staticmethod
    def calculate_crc(data):
        crc = 0xFFFF
        for byte in data:
            crc ^= byte << 8
            for _ in range(8):
                if crc & 0x8000:
                    crc = (crc << 1) ^ 0x1021
                else:
                    crc <<= 1
        return crc & 0xFFFF

    @abc.abstractmethod
    def create_command(self):
        '''Создаём команду весовому оборудованию'''
        pass

    @abc.abstractmethod
    def parce_response(self, response):
        pass


class MassaKProtocol100(ScaleProtocol):

    #compatibility = '''Совместимо с весами Масса-К следующих моделей:
    #MK_A21(RI), MK_A21(UI), MK_A21(RU)-2, MK_A21(UE), MK_A21(RUW), MK_АВ11,
    #ТВ-S_А1, TB-S_А2, ТВ-S_А(RUEW)1, ТВ-S_А(RUEW)2, MK_ТB21(RU), MK_ТН21(RU),
    #TB-5040N_ АB(RUEW)1, TB-5040N_ АB(RUEW)3n, ТВ-S_АB(RUEW)1, ТВ-S_АB(RUEW)2,
    #'''

    def create_command(self):
        body = self.HEADER + struct.pack('!H', 1) + self.CMD_GET_MASSA
        crc = self.calculate_crc(body)
        return body + struct.pack('!H', crc)

    def parce_response(self, response):

        if response[:3] != self.HEADER:
            raise ValueError("Invalid response header")

        if response[5] == 0x24:
            weight = struct.unpack('!i', response[6:10])[0] / 1000.0
            return weight


class MassaKProtocol2(ScaleProtocol):
    BRAUDRATE = 4800
    PARITY = 'E'

    def create_command(self):
        return b'\x45'

    def parce_response(self, response):
        weight_bytes = response[1:3]
        sign_byte = response[5]
        weight_grams = struct.unpack('>h', weight_bytes)[0]
        weight_kilograms = weight_grams / 1000.0
        if not sign_byte:
            weight_kilograms = -weight_kilograms
        return weight_kilograms


class MassaKProtocolR(ScaleProtocol):
    '''Протокол для обмена с весами МАССА-К серии R(ТЕРМИНАЛЫ)'''
    HEADER = b'\xF8\x55\xCE'
    CMD_GET_MASSA = b'\xA0'
    BRAUDRATE = 19200
    STOP = 1
    PARITY = 'N'
    STOPBITS = 1  # Четность

    def create_command(self):
        length = struct.pack('<H', 1)  # длина тела сообщения
        command = self.CMD_GET_MASSA
        body = length + command
        crc = self.calculate_crc(body)
        crc_bytes = struct.pack('<H', crc)
        return self.HEADER + body + crc_bytes

    def parce_response(self, response):
        weight, division, stable = struct.unpack('<iBB', response[6:12])
        weight_kg = weight / 1000.0
        return weight_kg


PROTOCOLS_SERIAL = {
    'Масса-К : Протокол 100': MassaKProtocol100,
    'Масса-К: Протокол 2': MassaKProtocol2,
    'Масса-К: Протокол R': MassaKProtocolR,
}

PROTOCOLS_ETHERNET = {
    'Масса-К : Протокол 100': MassaKProtocol100,
    'Масса-К: Протокол R': MassaKProtocolR,
}
