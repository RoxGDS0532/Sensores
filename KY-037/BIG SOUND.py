from machine import Pin, ADC, I2C
import ssd1306
import time


led_pin = Pin(2, Pin.OUT)  
sound_pin = ADC(Pin(35))    


i2c = I2C(-1, scl=Pin(22), sda=Pin(21))  
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


def display_message(message):
    oled.fill(0)
    oled.text(message, 0, 0)
    oled.show()

oled.fill(0)
oled.text("Sensor de Sonido", 0, 0)
oled.show()
time.sleep(2)
oled.fill(0)
oled.show()

while True:
    sound_value = sound_pin.read()

    sound_intensity = int(sound_value / 1023 * 100)

    print("Valor de sonido leído:", sound_value)

    if sound_value > 5:  
        led_pin.value(1) 
        message = "Intensidad: {}%".format(sound_intensity)
        display_message(message)
        time.sleep(1)  
        oled.fill(0)
        oled.show()
    else:
        led_pin.value(0)  
        display_message("Intensidad del sonido: {}%".format(sound_intensity))
    
    time.sleep(0.1) 

