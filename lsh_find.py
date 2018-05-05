# from lshash import LSHash
# import numpy as np
# from PIL import Image
# import skimage.io
# from skimage import transform,data
# import os
# import time

# class LSH():
#     def __init__(self,path,lsh):
#         #lsh = LSHash(7,2500)
#         pathDir = os.listdir(path)
#         txt_list = []
#         filename = ""
#         for file in pathDir:
#             if file.endswith('txt'):
#                 txt_list.append(file)

#         for i in txt_list:
#             filename = ""
#             filename += path
#             filename += "\\"
#             filename += i
#             #print(filename)
#             f = open(filename)
#             c = f.read().strip('[').strip(']').split(r',')
#             c = list(map(int, c))
#             #print(type(c))
#             lsh.index(c,i)
#     def query(self,_list = []):
#         ss = "C:\\Users\\Leo\\Documents\\WeChat Files\\jweixuan1995\\Files\\dataset\\dataset"
        
#         cost_time = float()
# #        __init(ss,lsh)
#         q = get10_test("0_4.png")
#         st = time.time()
#         result = lsh.query(q)
#         cost_time = [time.time() - st]
#         print(cost_time)
#         result_file_name = []


#         if len(result) == 0:
#             return [],cost_time
#         elif len(result) <=3:
#             for i in result:
#                 result_file_name.append(i[0][1])
#         else:
#             for i in range(3):
#                 result_file_name.append(result[i][0][1])

#         return result_file_name, cost_time


import lshash
import numpy as np
import os
import time


def building_lsh():
    stime = time.time()
    lsh = lshash.LSHash(10,784)

    for root, dirs, files in os.walk(r"./dataset"):
        print(dirs)
        for dir in dirs:
            print(dir)
            s = "" + root +"/"+dir
            pathDir = os.listdir(s)
            txt_list = []
            for file in pathDir:
                if file.endswith('txt'):
                    txt_list.append(file)

            for i in txt_list:
                filename = ""
                filename += s
                filename += "/"
                filename += i
                #print(filename)
                f = open(filename)
                c = f.read().strip('[').strip(']').split(r',')
                c = list(map(int, c))
                lsh.index(c,i)
    build_time = time.time() - stime
    return lsh,build_time

def query(lsh,Q):

    file_name = []
    st = time.time()
    result = lsh.query(Q)
    cost = time.time()-st
    if len(result) >= 7:
        result = result[:7]
    
    for i in range(len(result)):
        tmp = "" + result[i][0][1].split(".")[0]
        file_name.append(tmp)
    
    return file_name,cost