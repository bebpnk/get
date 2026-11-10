import matplotlib.pyplot as plt
def plot_voltage_vs_time(time, voltage, max_voltage,tau_time = None, tau_voltage = None):
    plt.figure(figsize = (10,6))
    plt.plot(time, voltage)
    if tau_time is not None and tau_voltage is not None:
        plt.scatter([tau_time], [tau_voltage], color = 'r', zorder = 5)
    plt.title('График зависимости напряжения на конденсаторе')
    plt.xlabel('Время, с')
    plt.ylabel('Напряжение, В')
    plt.ylim(0, max_voltage * 1.1)
    plt.legend()
    plt.grid(True)
    plt.show()
    plt.savefig('rc_plot.png')