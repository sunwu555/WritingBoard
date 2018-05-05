# encoding: utf-8

import kd_noclass
import lsh_find

import os 
import time
from PIL import Image, ImageTk, ImageDraw  
import numpy as np

import kdtree

def main():

    # lsh, lshbuildtime = lsh_find.building_lsh()
    # empty = kdtree.create(dimensions = 784)
    # kd_noclass.add_tree('./dataset', empty)

    DataSet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # DataSet = ['1']
    k = 0
    kdright = 0
    kdwrong = 0
    lshright = 0
    lshwrong = 0
    lsh, lshbuildtime = lsh_find.building_lsh()
    empty = kdtree.create(dimensions = 784)
    empty, kdbuildtime = kd_noclass.add_tree('./dataset', empty)
    print('build time ', kdbuildtime)
    print('lsh build time ', lshbuildtime)
    StartTime = time.clock()
    for i in DataSet:
        g = os.walk(r'./queryset/' + i + '/')  
        for path,dir_list,file_list in g:  
            for file_name in file_list:  
                if (k % 10) == 0:
                    print('now is ' + str(k) + 'th query')
                k += 1

                FilePath = os.path.join(path, file_name)
                img = Image.open(FilePath)
                pix = np.array(img)
                a = []
                for i1 in pix:
                    for j in i1:
                        a.append(j)
                # print(a)

                kdname = kd_noclass.output(empty,a)
                SetAcc = {'0' : 0, '1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0}
                for ii in range(7):
                    SetAcc[kdname[ii][0]] += 1
                MaxClassCount = 0   
                MaxClass = 0
                for ii in SetAcc:
                    if SetAcc[ii] > MaxClassCount:
                        MaxClassCount = SetAcc[ii]
                        MaxClass = ii
                print('class is ', MaxClass)
                print('now check', i)
                if MaxClass == i:
                    kdright += 1
                else:
                    kdwrong += 1

                # lshname,lsh_time = lsh_find.query(lsh, a)
                # SetAcc = {'0' : 0, '1' : 0, '2' : 0, '3' : 0, '4' : 0, '5' : 0, '6' : 0, '7' : 0, '8' : 0, '9' : 0}
                # for ii in range(1):
                #     try:
                #         SetAcc[lshname[ii][0]] += 1
                #     except Exception as e:
                #         print('ERROR ')
                # MaxClassCount = 0   
                # MaxClass = 0
                # for ii in SetAcc:
                #     if SetAcc[ii] > MaxClassCount:
                #         MaxClassCount = SetAcc[ii]
                #         MaxClass = ii
                # print('class is ', MaxClass)
                # print('now check', i)
                # if MaxClass == i:
                #     lshright += 1
                #     print('right')
                # else:
                #     lshwrong += 1
                #     print('wrong')

    kdaccuracy = kdright / (kdright + kdwrong)
    print('kd accuracy is ', kdaccuracy)
    # lshaccuracy = lshright / (lshright + lshwrong)
    # print('lsh accuracy is ', lshaccuracy)
    Costtime = time.clock() - StartTime
    print(Costtime)
    # print('build time ', lshbuildtime)
                
    

if __name__ == '__main__':
    main()