# Writing Board
A python program for writing number recongnition, implementing and comparing for multiple NN algorithm(kd-tree, LSH) 

Introduction
---

The Writing Board is an local application which could help user quickly using several different algorithms to search a large database for the nearest neighbor of a given sample. Also user could compare the performances of each algorithm by program outputs data of time/space consuming and accuracy of results.

Brief Instructions
---


Clone whole project into local computer.

    git clone https://github.com/sunwu555/MultiAlgoForNNProb.git
    
There are four major functions of this repository

## Run GUI

The GUI can be run by

    python top.py

Since training procedure for the kd-tree and LSH takes a while, so it needs about 30s to open the application.

The application is pretty easy to use, writing on the top right grey area, and hit the query button, the below form will show the result classfication(which number each algorithm thinks your writting is), nearest result it finds, and running time of each algorithm.

Sometimes LSH couldn't return enough result, so it won't show the full result. That's mostly because we only using 10000 sample data for training. More training data could solve this problem, however it will takes much longer time for each query(about 40s every time), and also loger time for training(may take 2min to open the application).

## Extract MNIST Dataset

To extrat MNIST dataset

    python MNIST_process.py

The program will extract the MNIST file to text and png files in ./dataset and ./queryset as a program acceptiable format.

## Generate your own Dataset

To generate your own dataset

    python generate_own_dataset.py

The Writing Board application has modified for accept MNIST data. So generate own dataset function may need modify for using.

## Testing Script

    python statistic.py

This program is program for us to analyze two algorithms, using MNIST data, it could generate the result accuracy for different K value of two algorithms, 200 query time consuming, training time for different amount of data. However single query on a kd-tree of 30000 would spend over 30s, we do not recommand run this program on your PC. 


Reference
---

For the implementing of LSHash, 

>This function was built from (https://github.com/kayzhu/LSHash).

For the implementing of KD-TREE,, 

> function was built from (https://github.com/stefankoegl/kdtree).
