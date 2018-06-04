import numpy as np
import scipy.constants as cs
from scipy.stats import norm


def lorentz(x, gamma):
    """
    Returns lorentzian profile.
    1/pi * 0.5*gamma / ((0.5*gamma)**2 + x**2)
    :param x: (array like) x
    :param gamma: (float) lorentzian width
    :return:
    """
    return 1 / cs.pi * 0.5 * gamma / ((0.5 * gamma**2) + x**2)


def gauss(x, gamma):
    """
    Returns gaussian profile.
    1/sqrt(2*pi) / gamma * exp((x/gamma)**2 / 2)
    :param x: (array like) x
    :param gamma: (float) gaussian width
    :return:
    """
    return 1 / np.sqrt(2*np.pi) / gamma * np.exp(-(x/gamma)**2 / 2)


def skew(x, center=0, gamma=1, alpha=0):
    t = (x - center) / gamma
    return 2 * norm.pdf(t) * norm.cdf(alpha*t)
