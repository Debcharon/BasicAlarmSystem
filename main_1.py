from GPIOLibrary import GPIOProcessor
from GPIOLibrary import GPIO
import os
import serial
from time import sleep


class GasLight:

    def __init__(self):
        self.gpio = GPIOProcessor()
        self.port = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, bytesize=8, stopbits=1, timeout=2)

        self.gas_message_sent = False
        self.light_message_sent = False

        if self.port.isOpen():
            print("Serial is opened!")
            print(self.port)
            print(self.port.name)
        else:
            print("Serial do not open!")

    def gpio_close(self, pin):
        self.export_path = f"/sys/class/gpio/gpio{pin}"
        if os.path.exists(self.export_path):
            self.gpioControl = GPIO(pin)
            self.gpioControl.closePin()

    def gpio_input(self):
        self.gpio_30 = self.gpio.getPin30()
        self.gpio_30.setDirection("in")
        self.gpio_34 = self.gpio.getPin34()
        self.gpio_34.setDirection("in")

    def get_gpio_value(self):
        self.gas = self.gpio_30.getValue()
        self.light = self.gpio_34.getValue()
        return self.gas, self.light

    def dbg_sim800a(self, data):
        self.res_ser = ""
        if data != "":
            self.port.write(data.encode())
            sleep(1)
            print("send to sim800a: " + data)
            if "AT" == str(data):
                sleep(3)
            if self.port.inWaiting() > 0:
                while True:
                    self.res_ser = self.port.readall()
                    if self.res_ser == "":
                        continue
                    else:
                        break
                if ">" in str(self.res_ser):
                    print(data + "successfully!")
                    print(self.res_ser)
                    print("you can send message!")
                    self.res_ser = ""
                if "OK" in str(self.res_ser):
                    print(data + "successfully！\n")
                    print(self.res_ser)
                    self.res_ser = ""
                else:
                    print(data + "unsuccessfully！\n")
                    print(self.res_ser)
                    self.res_ser = ""

    def send_gas_message(self):
        if not self.gas_message_sent:
            self.port.write(f"AT+CMGS=\"{phone_num}\"\r\n".encode())
            sleep(1)
            self.port.write("Gas leakage.".encode())
            sleep(1)
            self.port.write("\x1A".encode())
            sleep(5)
            self.gas_message_sent = True

    def send_light_message(self):
        if not self.light_message_sent:
            self.port.write(f"AT+CMGS=\"{phone_num}\"\r\n".encode())
            sleep(1)
            self.port.write("It's dark now!!".encode())
            sleep(1)
            self.port.write("\x1A".encode())
            sleep(5)
            self.light_message_sent = True


if __name__ == '__main__':

    phone_num = ''

    my_board = GasLight()
    my_board.dbg_sim800a("AT\r\n")
    my_board.dbg_sim800a("AT+CMGF=1\r\n")
    my_board.dbg_sim800a("AT+CSCS=\"GSM\"\r\n")
    my_board.dbg_sim800a("AT+CSMP=17,167,0,0\r\n")
    my_board.gpio_close(415)
    my_board.gpio_close(423)
    sleep(1)
    my_board.gpio_input()
    sleep(2)

    while True:
        gas_value, light_value = my_board.get_gpio_value()
        if gas_value == 0:
            print(f"gas: {gas_value}, message will be sent!")
            my_board.send_gas_message()
            my_board.gas_message_sent = False
        else:
            print(f"gas: {gas_value}, status fine.")
            sleep(5)
        if light_value == 1:
            print(f"light: {light_value}, message will be sent.")
            my_board.send_light_message()
            my_board.light_message_sent = False
        else:
            print(f"light: {light_value}, status fine.")
            sleep(5)
