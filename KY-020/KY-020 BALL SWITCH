from machine import Pin, I2C
import ssd1306
import time

led_pin = Pin(2, Pin.OUT)  
tilt_pin = Pin(34, Pin.IN, Pin.PULL_UP)  

i2c = I2C(-1, scl=Pin(22), sda=Pin(21))  
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def display_message(message):
    oled.fill(0)
    oled.text(message, 0, 0)
    oled.show()

oled.fill(0)
oled.text("Sensor de Inclinacion", 0, 0)
oled.show()
time.sleep(2)
oled.fill(0)
oled.show()

while True:
    if tilt_pin.value() == 1:  
        led_pin.value(1) 
        display_message("Inclinacion")
    else:
        led_pin.value(0)  
        display_message("Sin inclinacion")
    
 

