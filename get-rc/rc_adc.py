import smbus
import time
from rc_plot import plot_voltage_vs_time
import numpy as np

class MCP3021:
    def __init__(self, dynamic_range, verbose = False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose
    def deinit(self):
        self.bus.close()
    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"Принятые данные: {data}, Старший байт: {upper_data_byte:x}, Младший байт: {lower_data_byte:x}, Число : {number}")
        return number
    def get_voltage(self):
        number = self.get_number()
        voltage = (number * self.dynamic_range) / 1024
        return voltage

if __name__ == "__main__":
    adc = MCP3021(5.1, False)

    voltage_values = []
    time_values = []
    duration = 10.0
    try:
        start_time = time.time()
        while((time.time() - start_time) < duration):
            voltage_values.append(adc.get_voltage())
            time_values.append(time.time() - start_time)
        
        t_arr = np.array(time_values)
        v_arr = np.array(voltage_values)
        v_max = v_arr.max()
        target_v = 0.63 * v_max
        tau_idx = np.argmax(v_arr >= target_v)
        tau_time = t_arr[tau_idx]
        tau_voltage = v_arr[tau_idx]
        plot_voltage_vs_time(t_arr, v_arr, 5.1, tau_time, tau_voltage)

        data = np.column_stack((time_values, voltage_values))
        np.savetxt(
            'data.csv', data, delimiter = ',', fmt = '%.4f',
            header = 'Время[с],Напряжение[В]',comments='',
            encoding='utf-8'
        )
    finally:
        adc.deinit()