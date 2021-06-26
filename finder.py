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
