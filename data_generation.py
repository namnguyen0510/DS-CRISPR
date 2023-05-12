import numpy as np
from icecream import ic
import random
import itertools
import pandas as pd
import tqdm as tqdm
from utils import *
from sampler import *
import os
import time




n_iters = 10000

_gen_ds = pd.read_csv('gen_0.txt', header = None)



methods = ['GSDS', 'GFDS', 'CSDS', 'CFDS']

max_lens = [26,30,32]


for method in methods:
    for max_len in max_lens:
        start_time = time.time()
        save_dir = '{}_{}'.format(method,max_len)
        try:
            os.mkdir(save_dir)
        except:
            pass
        ic(method)
        for k in range(len(_gen_ds)):
            _ds = _gen_ds.iloc[k,0]
            _MG = []
            _STR = []
            _BIN = []
            DF = pd.DataFrame([])
            for i in range(n_iters):
                O_STR = DSseq2DNA(str(_ds), method)
                random.shuffle(O_STR)
                bs = ''.join([x[0] for x in O_STR])
                ns = ''.join([x[1] for x in O_STR])
                if len(bs) == max_len:
                    _MG.append(_ds)
                    _STR.append(bs)
                    _BIN.append(ns)
                else:
                    pass
            DF['DS-Seq'] = _MG
            DF['sgRNA'] = _STR
            DF['bits'] = _BIN
            #DF.to_csv('{}/eff_{}_{}_{}.csv'.format(save_dir,_ds,max_len,len(DF)), index=False)

        end_time = time.time()
        running_time = end_time - start_time
        print("{}|{}|Time: {}|Successful Rate: {}".format(method,max_len,running_time, len(DF)/n_iters), "seconds")
