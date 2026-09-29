import RPi.GPIO as GPIO
class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)
    def definit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
    def set_number(self, number):
        bits =  [int(element) for element in bin(number)[2:].zfill(8)]
        GPIO.output(self.gpio_bits,bits)
        if self.verbose:
            print(f"Число на вход ЦАП:{number}, биты:{bits}\n")
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит на динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
            print("Устанавливаем 0.0 В")
            number =  0
        else:
            number = int(voltage / self.dynamic_range * 255)
        self.set_number(number)
if __name__ == "__main__":
    dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
    try:
        while True:
            try:
                voltage = float(input("Введите напряжение в вольтах: "))
                dac.set_voltage(voltage)
            
            except ValueError:
                print("Вы не ввели число\n")
            
    finally:
        dac.deinit()