# Postprocessing of pieces data

import os
import sys
import numpy as np
import pandas as pd
from tqdm import tqdm

big1_set = set(os.listdir('./big1'))
big2_set = set(os.listdir('./big2'))
both_set = set()
for item in big1_set:
    if item in big2_set:
        both_set.add(item)
for item in both_set:
    big1_set.remove(item)
    big2_set.remove(item)

for item in tqdm(both_set):
    df1 = pd.DataFrame(pd.read_csv('./big1/'+item))
    df2 = pd.DataFrame(pd.read_csv('./big2/'+item))
    ar1 = np.array(df1)
    ar2 = np.array(df2)
    # ar1[:,0] *= 30
    # ar1[:,1] *= 3
    # ar1[:,2] *= 3
    # ar2[:,0] *= 30
    # ar2[:,1] *= 3
    # ar2[:,2] *= 3
    ar = np.vstack((ar1, ar2))
    df = pd.DataFrame(ar)
    df.to_csv('./piece_bigbig/'+item, header=0, index=0)

for item in tqdm(big1_set):
    df = pd.DataFrame(pd.read_csv('./big1/'+item))
    ar = np.array(df)
    # ar[:,0] *= 30
    # ar[:,1] *= 3
    # ar[:,2] *= 3
    df = pd.DataFrame(ar)
    df.to_csv('./piece_bigbig/'+item, header=0, index=0)
for item in tqdm(big2_set):
    df = pd.DataFrame(pd.read_csv('./big2/'+item))
    ar = np.array(df)
    # ar[:,0] *= 30
    # ar[:,1] *= 3
    # ar[:,2] *= 3
    df = pd.DataFrame(ar)
    df.to_csv('./piece_bigbig/'+item, header=0, index=0)