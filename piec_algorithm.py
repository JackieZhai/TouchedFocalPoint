# Generate bigbig pieces from origin data

import numpy as np
import pickle
from PIL import Image
import pandas
from tqdm import tqdm

labels = np.load('./origin.npy')
labels1 = labels[0:150]
labels2 = labels[150:300]
del labels

labels1 = np.concatenate((np.zeros((1,labels1.shape[1],labels1.shape[2])),labels1,np.zeros((1,labels1.shape[1],labels1.shape[2]))), axis=0)
labels1 = np.concatenate((np.zeros((labels1.shape[0],1,labels1.shape[2])),labels1,np.zeros((labels1.shape[0],1,labels1.shape[2]))), axis=1)
labels1 = np.concatenate((np.zeros((labels1.shape[0],labels1.shape[1],1)),labels1,np.zeros((labels1.shape[0],labels1.shape[1],1))), axis=2)
labels2 = np.concatenate((np.zeros((1,labels2.shape[1],labels2.shape[2])),labels2,np.zeros((1,labels2.shape[1],labels2.shape[2]))), axis=0)
labels2 = np.concatenate((np.zeros((labels2.shape[0],1,labels2.shape[2])),labels2,np.zeros((labels2.shape[0],1,labels2.shape[2]))), axis=1)
labels2 = np.concatenate((np.zeros((labels2.shape[0],labels2.shape[1],1)),labels2,np.zeros((labels2.shape[0],labels2.shape[1],1))), axis=2)

f = open('./count_bigbig.txt', mode='r')
bigbig_set = set()
for line in f.readlines():
    line = line.strip()
    num1 = int(line.split(' ')[0])
    num2 = int(line.split(' ')[1])
    bigbig_set.add(num1)
f.close()

# piec_dic1 = {}
# for z in tqdm(range(len(labels1))):
#     for y in range(len(labels1[z])):
#         for x in range(len(labels1[z, y])):
#             if labels1[z, y, x] in bigbig_set:
#                 this_label = int(labels1[z, y, x])
#                 if not ((labels1[z+1, y+1, x+1]==this_label)and(labels1[z+1, y+1, x]==this_label)and(labels1[z+1, y+1, x-1]==this_label)and(labels1[z+1, y, x+1]==this_label)and(labels1[z+1, y, x]==this_label)and(labels1[z+1, y, x-1]==this_label)and(labels1[z+1, y-1, x+1]==this_label)and(labels1[z+1, y-1, x]==this_label)and(labels1[z+1, y-1, x-1]==this_label)and \
#                 (labels1[z, y+1, x+1]==this_label)and(labels1[z, y+1, x]==this_label)and(labels1[z, y+1, x-1]==this_label)and(labels1[z, y, x+1]==this_label)and(labels1[z, y, x-1]==this_label)and(labels1[z, y-1, x+1]==this_label)and(labels1[z, y-1, x]==this_label)and(labels1[z, y-1, x-1]==this_label)and \
#                 (labels1[z-1, y+1, x+1]==this_label)and(labels1[z-1, y+1, x]==this_label)and(labels1[z-1, y+1, x-1]==this_label)and(labels1[z-1, y, x+1]==this_label)and(labels1[z-1, y, x]==this_label)and(labels1[z-1, y, x-1]==this_label)and(labels1[z-1, y-1, x+1]==this_label)and(labels1[z-1, y-1, x]==this_label)and(labels1[z-1, y-1, x-1]==this_label) \
#                 ):
#                     if this_label in piec_dic1.keys():
#                         piec_dic1[this_label].append([z*30, y*3, x*3])
#                     else:
#                         piec_dic1[this_label] = [[z*30, y*3, x*3]]
# del labels1

# save_loc = './piece_bigbig1/'
# for key in tqdm(piec_dic1.keys()):
#     pandas.DataFrame(piec_dic1[key]).to_csv(save_loc+'{:d}.csv'.format(key), header=0, index=0)
# del piec_dic1
# print('The first half done.')

piec_dic2 = {}
for z in tqdm(range(len(labels2))):
    for y in range(len(labels2[z])):
        for x in range(len(labels2[z, y])):
            if labels2[z, y, x] in bigbig_set:
                this_label = int(labels2[z, y, x])
                if not ((labels2[z+1, y+1, x+1]==this_label)and(labels2[z+1, y+1, x]==this_label)and(labels2[z+1, y+1, x-1]==this_label)and(labels2[z+1, y, x+1]==this_label)and(labels2[z+1, y, x]==this_label)and(labels2[z+1, y, x-1]==this_label)and(labels2[z+1, y-1, x+1]==this_label)and(labels2[z+1, y-1, x]==this_label)and(labels2[z+1, y-1, x-1]==this_label)and \
                (labels2[z, y+1, x+1]==this_label)and(labels2[z, y+1, x]==this_label)and(labels2[z, y+1, x-1]==this_label)and(labels2[z, y, x+1]==this_label)and(labels2[z, y, x-1]==this_label)and(labels2[z, y-1, x+1]==this_label)and(labels2[z, y-1, x]==this_label)and(labels2[z, y-1, x-1]==this_label)and \
                (labels2[z-1, y+1, x+1]==this_label)and(labels2[z-1, y+1, x]==this_label)and(labels2[z-1, y+1, x-1]==this_label)and(labels2[z-1, y, x+1]==this_label)and(labels2[z-1, y, x]==this_label)and(labels2[z-1, y, x-1]==this_label)and(labels2[z-1, y-1, x+1]==this_label)and(labels2[z-1, y-1, x]==this_label)and(labels2[z-1, y-1, x-1]==this_label) \
                ):
                    if this_label in piec_dic2.keys():
                        piec_dic2[this_label].append([z*30, y*3, x*3])
                    else:
                        piec_dic2[this_label] = [[z*30, y*3, x*3]]
del labels2

save_loc = './piece_bigbig2/'
for key in tqdm(piec_dic2.keys()):
    pandas.DataFrame(piec_dic2[key]).to_csv(save_loc+'{:d}.csv'.format(key), header=0, index=0)
print('The second half done.')