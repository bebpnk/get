import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, comp_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.comp_time = comp_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)
    def __del__(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()
    def number_to_dac(self, number):
        bits =  [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio,bits)
        if self.verbose:
            print(f"Число на вход ЦАП:{number}, биты:{bits}\n")
    def sequential_counting_adc(self):
        for value in range(256):
            self.number_to_dac(value)
            time.sleep(self.comp_time)
            if GPIO.input(self.comp_gpio) == 1:
                return value
        return 255
    def get_sc_voltage(self):
        digital_val = self.sequential_counting_adc()
        voltage = (digital_val / 255.0) * self.dynamic_range
        return voltage
if __name__ == "__main__":
    adc = R2R_ADC(3.3, verbose = False)
    try:
        while True:
            voltage = adc.get_sc_voltage()
            print(f"Напряжение: {voltage:.2f} В")
            
    finally:
        adc.deinit()