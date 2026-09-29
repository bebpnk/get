import numpy as np
import time
def get_sin_wave_amplitude(freq, time):
    sin_val = np.sin(2 * np.pi * freq * time)
    normilized = (sin_val + 1) / 2
    return normilized
def wait_for_sampling_period(sampling_frequency):
    sampling_period = 1 / sampling_frequency
    time.sleep(sampling_period)
def get_triangle_wave_amplitude(freq, time):
    t_norm = (freq * time) % 1.0
    if t_norm < 0.5:
        return 2 * t_norm
    else:
        return 2 * (1 - t_norm)