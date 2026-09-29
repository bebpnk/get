import RPi.GPIO as GPIO
dac = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
dynamic_range = 3.17
def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит на динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print("Устанавливаем 0.0 В")
        return 0
    return int(voltage / dynamic_range * 255)
def number_to_dac(number):
    bits =  [int(element) for element in bin(number)[2:].zfill(8)]
    GPIO.output(dac,bits)
    print(f"Число на вход ЦАП:{number}, биты:{bits}\n")
try:
    while True:
        try:
            voltage = float(input("Введите напряжение в вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)

        except ValueError:
            print("Вы не ввели число\n")
finally:
    GPIO.output(dac,0)
    GPIO.cleanup()