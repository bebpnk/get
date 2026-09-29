import pwm_dac as pwm
import signal_generator as sg
import time
import RPi.GPIO as GPIO
amplitude = 3.290
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        dac = pwm.PWM_DAC(12, 500, 3.290, True)
        start_time = time.time()
        while True:
            current_time = time.time() - start_time
            amp = sg.get_sin_wave_amplitude(signal_frequency, current_time)
            voltage = amp * amplitude
            dac.set_voltage(voltage)
            sg.wait_for_sampling_period(sampling_frequency)
    finally:
        dac.set_voltage(0)
        GPIO.cleanup()