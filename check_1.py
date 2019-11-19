# Convert 'skel_ans.pkl' to '.csv' file

from PIL import Image
import numpy as np
import os
import sys
import pickle
import pandas

save_loc = './skeleton_bigbig/'
f = open('./skel_ans_extra.pkl', 'rb')
label1, label2, label3 = pickle.load(f)
f.close()
print(label1.keys())

for key in label1.keys():
	pandas.DataFrame(label1[key]).to_csv(save_loc+'{:d}.csv'.format(key), header=0, index=0)
