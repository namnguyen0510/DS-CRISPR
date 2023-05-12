import numpy as np
from icecream import ic
from utils import *
import pandas as pd
import tqdm as tqdm
from model_gsds import *
from model_gfds import *
from model_csds import *


def DSseq2DNA(input_str, method, max_iter = 20):
    input_str = [x for x in list(input_str)]

    # METHOD SELECTION
    if method == 'GSDS':
        d = [GSDS[x] for x in input_str]
    elif method == 'GFDS':
        d = [GFDS[x] for x in input_str]
    elif method == 'CSDS':
        d = [CSDS[x] for x in input_str]
    elif method == 'CFDS':
        d = [CFDS[x] for x in input_str]
    elif method == 'CSMDS':
        d = [CSMDS[x] for x in input_str]
    else:
        ic('Method is not implemented! Support methods are: GSDS, GFDS, CSDS, CFDS, CSMDS')



    # RANDOM SAMPLING FROM LIST THE GROUP BASIS
    l = []
    R_STR = []
    O_STR = []
    r_str = random_sample(d)
    keys = list(r_str.keys())
    l.append(len(keys[0]))
    R_STR.append(r_str)
    for _ in range(max_iter):
        # CHECK LENGTH OF GENERATED BASES LESS OR EQUAL TO 4
        if len(l) < 5:
            r_str = random_sample(d)
            keys = list(r_str.keys())
            n = len(keys[0])
            # PREVENT OVER-LAPPING ELEMENT
            if n not in l:
                l.append(n)
                R_STR.append(r_str)
        else:
            pass
    #ic(r_str)
    #ic(keys)
    #ic(l)
    #ic(R_STR)
    obits = [sample_from_dict(x)[0] for x in R_STR]
    ostr = ''.join(obits)
    ostr = [ostr[i:i+2] for i in range(0, len(ostr), 2)]
    #ic(obits)
    for b in ostr:
        if b == 'b0':
            O_STR.append(sample_from_dict(b0))
        elif b == 'b1':
            O_STR.append(sample_from_dict(b1))
        elif b == 'b2':
            O_STR.append(sample_from_dict(b2))
    return O_STR