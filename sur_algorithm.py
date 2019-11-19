# from skeleton_bigbig to sovle small space
# use sampling to limit small space

import numpy as np
import pandas as pd
import os
from tqdm import tqdm

def point_eud(a, b):
    ans = 0
    ans += (a[0]-b[0])*(a[0]-b[0])
    ans += (a[1]-b[1])*(a[1]-b[1])
    ans += (a[2]-b[2])*(a[2]-b[2])
    return ans

def point_fit(ponit_ar):
    # Calculate the mean of the points, i.e. the 'center' of the cloud
    datamean = ponit_ar.mean(axis=0)

    # Do an SVD on the mean-centered data.
    uu, dd, vv = np.linalg.svd(ponit_ar - datamean)

    # Now vv[0] contains the first principal component, i.e. the direction
    # vector of the 'best fit' line in the least squares sense.
    return vv[0]

    # Now generate some points along this best fit line, for plotting.
    # I use -7, 7 since the spread of the data is roughly 14
    # and we want it to have mean 0 (like the points we did
    # the svd on). Also, it's a straight line, so we only need 2 points.
    # linepts = vv[0] * np.mgrid[-7:7:2j][:, np.newaxis]

def calculate_one_pair(pair_dic_num, pair_to_num, skel_sample_num):
    skel_dic = np.array(pd.DataFrame(pd.read_csv('./skeleton_bigbig/'+str(pair_dic_num)+'.csv')))
    skel_to = np.array(pd.DataFrame(pd.read_csv('./skeleton_bigbig/'+str(pair_to_num)+'.csv')))
    piec_dic = np.array(pd.DataFrame(pd.read_csv('./piece_bigbig/'+str(pair_dic_num)+'.csv')))
    piec_to = np.array(pd.DataFrame(pd.read_csv('./piece_bigbig/'+str(pair_to_num)+'.csv')))
    # cal the dis of skel points sets
    dis_skel = np.zeros((skel_dic.shape[0], skel_to.shape[0]), dtype=int)
    for i in range(skel_dic.shape[0]):
        for j in range(skel_to.shape[0]):
            dis_skel[i,j] = point_eud(skel_dic[i], skel_to[j])
    skel_sample_num = np.min([skel_sample_num, skel_dic.shape[0], skel_to.shape[0]])
    skel_sample_dic = np.zeros((skel_sample_num, 3))
    skel_sample_to = np.zeros((skel_sample_num, 3))
    for i in range(skel_sample_num):
        pos = np.array(np.unravel_index(np.argmin(dis_skel), dis_skel.shape))
        skel_sample_dic[i] = skel_dic[pos[0]]
        skel_sample_to[i] = skel_to[pos[1]]
        dis_skel[:,pos[1]] = 9000000
        dis_skel[pos[0],:] = 9000000
    # fit the tangent
    skel_sample_dic_fit = point_fit(skel_sample_dic)
    skel_sample_to_fit = point_fit(skel_sample_to)
    print('Checking the {:d} and {:d} surface...'.format(pair_dic_num, pair_to_num))
    print('dic side:')
    sur_dic_list = []
    for i in tqdm(range(piec_dic.shape[0])):
        for j in range(skel_sample_dic.shape[0]):
            if (skel_sample_dic_fit[0]*(piec_dic[i][0]-skel_sample_dic[j][0])+skel_sample_dic_fit[1]*(piec_dic[i][1]-skel_sample_dic[j][1])+skel_sample_dic_fit[2]*(piec_dic[i][2]-skel_sample_dic[j][2]))<1e-1:
                sur_dic_list.append(list(piec_dic[i]))
                break
    print('to side:')
    sur_to_list = []
    for i in tqdm(range(piec_to.shape[0])):
        for j in range(skel_sample_to.shape[0]):
            if (skel_sample_to_fit[0]*(piec_to[i][0]-skel_sample_to[j][0])+skel_sample_to_fit[1]*(piec_to[i][1]-skel_sample_to[j][1])+skel_sample_to_fit[2]*(piec_to[i][2]-skel_sample_to[j][2]))<1e-1:
                sur_to_list.append(list(piec_to[i]))
                break
    print('check done.')
    # save the answer
    os.system('mkdir '+'.\\sur_dic_bigbig\\'+str(pair_dic_num)+'\\'+str(pair_to_num))
    pd.DataFrame(np.array(sur_dic_list)).to_csv('./sur_dic_bigbig/'+str(pair_dic_num)+'/'+str(pair_to_num)+'/sur_dic.csv', header=0, index=0)
    pd.DataFrame(np.array(sur_to_list)).to_csv('./sur_dic_bigbig/'+str(pair_dic_num)+'/'+str(pair_to_num)+'/sur_to.csv', header=0, index=0)
    pd.DataFrame(skel_sample_dic).to_csv('./sur_dic_bigbig/'+str(pair_dic_num)+'/'+str(pair_to_num)+'/ske_dic.csv', header=0, index=0)
    pd.DataFrame(skel_sample_to).to_csv('./sur_dic_bigbig/'+str(pair_dic_num)+'/'+str(pair_to_num)+'/ske_to.csv', header=0, index=0)
    pd.DataFrame([skel_sample_dic_fit, skel_sample_to_fit]).to_csv('./sur_dic_bigbig/'+str(pair_dic_num)+'/'+str(pair_to_num)+'/fit_dicto.csv', header=0, index=0)


if __name__ == '__main__':
    skel_sample_num = 100
    piec_sample_num = 10000

    pair_dic_list = os.listdir('./pair_dic_bigbig')
    for pair_dic in pair_dic_list:
        pair_dic_num = int(pair_dic.split('.')[0])
        os.system('mkdir '+'.\\sur_dic_bigbig\\'+str(pair_dic_num))
        f = open('./pair_dic_bigbig/'+pair_dic, mode='r')
        for line in f.readlines():
            line = line.strip()
            pair_to_num = int(line)
            calculate_one_pair(pair_dic_num, pair_to_num, skel_sample_num)
        f.close()