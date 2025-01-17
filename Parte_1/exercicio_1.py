import smbus2
import bme280
# Biblioteca p/ display
import RPi_I2C_driver
from time import *


porta_i2c = 1
endereco = 0x76
bus = smbus2.SMBus(porta_i2c)
calibracao_paramentros = bme280.load_calibration_params(bus, endereco)
displaylcd = RPi_I2C_driver.lcd()

while True:
    dado = bme280.sample(bus, endereco, calibracao_paramentros)
    # Exibir no terminal
    print("\n\nID: " + str(dado.id))
    print("Data/Hora: " + str(dado.timestamp))
    print("Temperatura: {:.2f} °C".format(dado.temperature))
    print("Umidade: {:.2f} %".format(dado.humidity))
    print("Pressão atmosférica: {:.2f} hPa".format(dado.pressure))
    
    # Exibir no display LCD
    displaylcd.lcd_display_string("P: {:.2f} hPa".format(dado.pressure),1)
    displaylcd.lcd_display_string("U:{:.2f}%".format(dado.humidity) + "T:{:.2f}C".format(dado.temperature),2)
    
    sleep(1)


