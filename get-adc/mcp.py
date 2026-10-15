from adc_plot import plot_voltage_vs_time,plot_sampling_period_hist
import time
from mcp3021_driver import MCP3021
if __name__ == "__main__":
    adc = MCP3021(5.0, False)

    voltage_values = []
    time_values = []
    duration = 3.0
    try:
        start_time = time.time()
        while((time.time() - start_time) < duration):
            voltage_values.append(adc.get_voltage())
            time_values.append(time.time() - start_time)
        plot_voltage_vs_time(time_values, voltage_values, 5.0)
        plot_sampling_period_hist(time_values)
    finally:
        del adc