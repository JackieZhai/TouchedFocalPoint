# Which of the bigbig left in 'skel_algorithm' procedure?

from PIL import Image
import numpy as np
import os
import sys
import pickle
import pandas

save_loc = './skeleton_bigbig/'
f = open('./skel_ans.pkl', 'rb')
label1, label2, label3 = pickle.load(f)
f.close()
skel_set = set(label1.keys())

f = open('./count_bigbig.txt', mode='r')
bigbig_set = set()
for line in f.readlines():
    line = line.strip()
    num1 = int(line.split(' ')[0])
    num2 = int(line.split(' ')[1])
    bigbig_set.add(num1)
f.close()

for skel_set_item in skel_set:
    bigbig_set.remove(skel_set_item)
print(bigbig_set)

# ANS:
# {84293, 86245, 22308}