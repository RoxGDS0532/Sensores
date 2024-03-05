from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep

# Configuración de pines
emisor_ir_pin = Pin(19, Pin.OUT)  # Pin para el emisor IR
receptor_ir_pin = Pin(18, Pin.IN)  # Pin para el receptor IR
led_pin = Pin(17, Pin.OUT)  # Pin para el LED

# Configura el objeto para la pantalla OLED
i2c = I2C(-1, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(128, 64, i2c)

# Ciclo infinito
while True:
    # Limpia la pantalla OLED
    oled.fill(0)
    
    # Muestra un mensaje en la pantalla OLED
    oled.text("Enviando Infrarrojo", 0, 0)
    oled.show()
    
    # Configura el emisor IR y lo activa
    emisor_ir_pin.on()
    
    # Espera un momento antes de apagar el emisor IR
    sleep(1)
    emisor_ir_pin.off()
    sleep(1)
    
    # Verifica si se recibió una señal IR
    if receptor_ir_pin.value() == 1:
        oled.fill(0)
        oled.text("Se recibio la señal", 0, 0)
        oled.show()
        led_pin.on()
        sleep(0.5)
        led_pin.off()
    
    # Imprime el estado
    print("Estado del receptor IR:", receptor_ir_pin.value())

