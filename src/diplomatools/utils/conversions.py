import numpy as np

def watt(power):
    """
    Converts power in dBm to watt
    :param power: (float) in dBm
    :return: (float) power in watt
    """
    return 1e-3 * 10**(power/10)

def dbm(power):
    """
    Converts power in watt to dBm
    :param power: (float) in watt
    :return: (float) power in dBm
    """
    return 10 * np.log10(power) + 30
