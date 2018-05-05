import numpy as np
import os
import sys
import kdtree
import time
class Item(object):
    def __init__(self, _list):
        self.coords = _list[:len(_list) - 1]
        self.name = _list[-1]

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, i):
        return self.coords[i]

    def __repr__(self):
        s = "("
        for i in range(len(self.coords)):
            s += str(self.coords[i])
            if i != len(self.coords) - 1:
                s += ","
        s += ")"
        s += ","
        s += str(self.name)
        return s


def output(empty, Q):
    r = []
    start_time = time.time()
    result = empty.search_knn(Q, 7)
    for i in result:
        r.append(i[0].data.name.split('.')[0])
    r.append(time.time() - start_time)
    return r

def add_tree(path):
    start_time = time.time()
    empty = kdtree.create(dimensions=784)
    for root, dirs, files in os.walk(path):
        for dir in dirs:
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
                f = open(filename)
                c = f.read().strip('[').strip(']').split(r',')
                c = list(map(int, c))
                c.append(i)
                point = Item(c)
                empty.add(point)
    build_time = time.time() - start_time
    return empty,build_time
