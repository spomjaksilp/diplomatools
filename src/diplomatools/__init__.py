# import system libraries
import os
import logging
logging.basicConfig(level=logging.INFO)

# science stutt
import numpy as np
import pandas as pd
import scipy.constants as cs
import matplotlib as mpl
import matplotlib.ticker as tck
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

# utils from this packages
from .utils import *