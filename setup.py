from machine import Pin, ADC
import time



p_hi = Pin(16,Pin.OUT)
p_hi.on()
p_lo = Pin(4,Pin.IN)
check = p_lo.value()
p_hi.off()

if check:
    p_status = Pin(2,Pin.OUT)
    p_status.on()
    import configurator
    
else:
    pass  #MQTT