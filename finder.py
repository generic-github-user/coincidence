import nltk
import math
from nltk.corpus import brown
import string
import numpy as np
import zlib
import random
possible_functions = [
    [lambda x: x**2, 'square'],
    [lambda x: x**3, 'cube'],
    # [lambda x: x**4, 'x ^ 4'],
    # [lambda x: 2**x, '2 ^ x'],
    # np.sin,
    # np.cos,
    # np.tan,
    # np.round
]
reducing_functions = [
    np.sum,
    np.product,
    # np.mean,
]
criteria = [
    lambda x: np.sum(x),
    lambda x: np.product(x),
    lambda x: np.mean(x),
    lambda x: np.sum(np.array(x)**2),
    lambda x: np.sum(np.array(x)**3),
    lambda x: np.product(x**2),
    lambda x: np.product(x**3),
    lambda x: np.sum((x**2)+(x**2)),
    lambda x: np.sum((x**2)*(x**2)),
    lambda x: np.sum(np.sin(x)*(x**2)),
    lambda x: np.sum(x*np.arange(1, x.size+1, 1)),
    lambda x: np.sum(x*np.flip(x)),
    lambda x: np.sum(2**x),
]
