import numpy as np
import struct
import matplotlib.pyplot as plt
from PIL import Image


train_images_idx3_ubyte_file = './MINIST/train-images.idx3-ubyte'

train_labels_idx1_ubyte_file = './MINIST/train-labels.idx1-ubyte'

test_images_idx3_ubyte_file = './MINIST/t10k-images.idx3-ubyte'

test_labels_idx1_ubyte_file = './MINIST/t10k-labels.idx1-ubyte'


def decode_idx3_ubyte(idx3_ubyte_file):

    bin_data = open(idx3_ubyte_file, 'rb').read()

    offset = 0
    fmt_header = '>iiii'
    magic_number, num_images, num_rows, num_cols = struct.unpack_from(fmt_header, bin_data, offset)
    print('魔数:%d, 图片数量: %d张, 图片大小: %d*%d' % (magic_number, num_images, num_rows, num_cols))

    image_size = num_rows * num_cols
    offset += struct.calcsize(fmt_header)
    fmt_image = '>' + str(image_size) + 'B'
    images = np.empty((num_images, num_rows, num_cols))
    for i in range(num_images):
        if (i + 1) % 10000 == 0:
            print('已解析 %d' % (i + 1) + '张')
        images[i] = np.array(struct.unpack_from(fmt_image, bin_data, offset)).reshape((num_rows, num_cols))
        offset += struct.calcsize(fmt_image)
    return images


def decode_idx1_ubyte(idx1_ubyte_file):

    bin_data = open(idx1_ubyte_file, 'rb').read()

    offset = 0
    fmt_header = '>ii'
    magic_number, num_images = struct.unpack_from(fmt_header, bin_data, offset)
    print('魔数:%d, 图片数量: %d张' % (magic_number, num_images))

    offset += struct.calcsize(fmt_header)
    fmt_image = '>B'
    labels = np.empty(num_images)
    for i in range(num_images):
        if (i + 1) % 10000 == 0:
            print('已解析 %d' % (i + 1) + '张')
        labels[i] = struct.unpack_from(fmt_image, bin_data, offset)[0]
        offset += struct.calcsize(fmt_image)
    return labels


def load_train_images(idx_ubyte_file=train_images_idx3_ubyte_file):
    """
    TRAINING SET IMAGE FILE (train-images-idx3-ubyte):
    [offset] [type]          [value]          [description]
    0000     32 bit integer  0x00000803(2051) magic number
    0004     32 bit integer  60000            number of images
    0008     32 bit integer  28               number of rows
    0012     32 bit integer  28               number of columns
    0016     unsigned byte   ??               pixel
    0017     unsigned byte   ??               pixel
    ........
    xxxx     unsigned byte   ??               pixel
    Pixels are organized row-wise. Pixel values are 0 to 255. 0 means background (white), 255 means foreground (black).

    """
    return decode_idx3_ubyte(idx_ubyte_file)


def load_train_labels(idx_ubyte_file=train_labels_idx1_ubyte_file):
    """
    TRAINING SET LABEL FILE (train-labels-idx1-ubyte):
    [offset] [type]          [value]          [description]
    0000     32 bit integer  0x00000801(2049) magic number (MSB first)
    0004     32 bit integer  60000            number of items
    0008     unsigned byte   ??               label
    0009     unsigned byte   ??               label
    ........
    xxxx     unsigned byte   ??               label
    The labels values are 0 to 9.

    """
    return decode_idx1_ubyte(idx_ubyte_file)


def load_test_images(idx_ubyte_file=test_images_idx3_ubyte_file):
    """
    TEST SET IMAGE FILE (t10k-images-idx3-ubyte):
    [offset] [type]          [value]          [description]
    0000     32 bit integer  0x00000803(2051) magic number
    0004     32 bit integer  10000            number of images
    0008     32 bit integer  28               number of rows
    0012     32 bit integer  28               number of columns
    0016     unsigned byte   ??               pixel
    0017     unsigned byte   ??               pixel
    ........
    xxxx     unsigned byte   ??               pixel
    Pixels are organized row-wise. Pixel values are 0 to 255. 0 means background (white), 255 means foreground (black).

    """
    return decode_idx3_ubyte(idx_ubyte_file)


def load_test_labels(idx_ubyte_file=test_labels_idx1_ubyte_file):
    """
    TEST SET LABEL FILE (t10k-labels-idx1-ubyte):
    [offset] [type]          [value]          [description]
    0000     32 bit integer  0x00000801(2049) magic number (MSB first)
    0004     32 bit integer  10000            number of items
    0008     unsigned byte   ??               label
    0009     unsigned byte   ??               label
    ........
    xxxx     unsigned byte   ??               label
    The labels values are 0 to 9.

    """
    return decode_idx1_ubyte(idx_ubyte_file)




def run():
    train_images = load_train_images()
    train_labels = load_train_labels()
    test_images = load_test_images()
    test_labels = load_test_labels()
    NumDict = {0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0}
    # NumDict[1] += 1
    # print(NumDict)

    for i in range(10000):
        k = test_images[i].astype(int)
        aa = []
        kkk = test_images[i].astype(np.uint8).tolist()
        for j in kkk:
            for jj in j:
                aa.append(jj)
        kk = open('./queryset/' + str(int(test_labels[i])) + '/' 
                    + str(int(test_labels[i])) + '_' + str(NumDict[test_labels[i]]) + '.txt', 'w')
        kk.write(str(aa))
        kk.write(str(aa))
        kk.close()
        if NumDict[test_labels[i]] == 19:
            NumDict[test_labels[i]] = 19
        else:
            NumDict[test_labels[i]] += 1
        if (i % 1000) == 0:
            print('save ', i, ' images')

    for i in range(60000):
        k = train_images[i].astype(int)
        aa = []
        kkk = train_images[i].astype(np.uint8).tolist()
        for j in kkk:
            for jj in j:
                aa.append(jj)
        kk = open('./dataset/' + str(int(train_labels[i])) + '/' 
                    + str(int(train_labels[i])) + '_' + str(NumDict[train_labels[i]]) + '.txt', 'w')
        kk.write(str(aa))
        kk.close()
        img = Image.fromarray(train_images[i].astype(np.uint8))
        img.save('./dataset/' + str(int(train_labels[i])) + '/'
                    + str(int(train_labels[i])) +  '_' + str(NumDict[train_labels[i]]) + '.png')
        if  NumDict[train_labels[i]] == 1000:
             NumDict[train_labels[i]] = 1000
        else:
            NumDict[train_labels[i]] += 1
        if (i % 1000) == 0:
            print('save ', i, ' images')
    
    print('done')

if __name__ == '__main__':
    run()
