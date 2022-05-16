'''/**
!/usr/bin/env tensorflow
# -*- coding: utf-8 -*-
 * Copyright © 2019 Jianfeng_Wu. All rights reserved.
 * 
 * @author: Jianfeng_Wu
 * @date: 2022-05-02 
 * @time: 16:04:37 
 * Version:1.0.0
 * description:
 */'''
from PIL import Image
import re
from RL2class import RL2class, setDir
import random 
# import os
# import shutil

'''
将RGB的txt文件转化成图片
修改循环始末位置和文件(filesave)写入位置
'''

HEIGTH = 128*2          #x坐标  通过对txt里的行数进行整数分解160
WIDTH =64               #y坐标  x*y = 行数70
num_samples = 1100      #采集样本的数目
# num_train_img ,num_test_img= 0,0

def imgStore2TrainTest(num_img:int,num_samples:int,RGB_dir:str):
    '''
    将图片按照测试集和训练集分别存储
    '''
    num_train_img,num_test_img = 0,0
    for i in range(0,num_img,1): # 0:800;800:1000;##800:1200 # 2100,2600,   
        im = Image.new("RGB",(HEIGTH,WIDTH))#创建图片
        # file_path = r'imagergb\%s' % (i+1) + '.txt' # 前面加'r'可以防止字符串在时候的时候不被转义
        file_path = RGB_dir+'\%s' % (i+1) + '.txt'
        cla = RL2class(i) # cla = RL2class(i)
        Random = random.uniform(0,10)

        if Random < 7*num_samples/num_img:
            fileSave= 'PicClassTrain\%s' % (cla)+'\%s' % (i+1)+'.jpg' # 存储到测训练集
            num_train_img +=1

            file = open(file_path) #打开rbg值文件
            # fileSave = 'scenario_pic\\1.jpg' #打开rbg值文件
            #通过一个个RGB点生成图片
            for i in range(0,HEIGTH):
                for j in range(0,WIDTH):
                    line = file.readline()#获取一行
                    rgb = line.split(",")#分离rgb
                    im.putpixel((i,j),(int(rgb[0]),int(rgb[1]),int(rgb[2])))#rgb转化为像素
            # im.show()
            im.save(fileSave)

        elif Random < 10*num_samples/num_img:
            fileSave= 'PicClassTest\%s' % (cla)+'\%s' % (i+1)+'.jpg' # 存储到测试集
            num_test_img +=1

            file = open(file_path) #打开rbg值文件
            # fileSave = 'scenario_pic\\1.jpg' #打开rbg值文件
            #通过一个个RGB点生成图片
            for i in range(0,HEIGTH):
                for j in range(0,WIDTH):
                    line = file.readline()#获取一行
                    rgb = line.split(",")#分离rgb
                    im.putpixel((i,j),(int(rgb[0]),int(rgb[1]),int(rgb[2])))#rgb转化为像素
            # im.show()
            im.save(fileSave)
        else:continue
    return num_train_img,num_test_img


def allImgStore(num_img:int,RGB_dir:str):
    '''
    将所图片全部放入训练文件夹
    '''
    for i in range(0,num_img,1): # 0:800;800:1000;##800:1200 # 2100,2600,   
        im = Image.new("RGB",(HEIGTH,WIDTH))#创建图片
        # file_path = r'imagergb\%s' % (i+1) + '.txt'
        file_path = RGB_dir + '\%s' % (i+1) + '.txt'
        cla = RL2class(i) # cla = RL2class(i)

        fileSave= 'PicClassTrain\%s' % (cla)+'\%s' % (i+1)+'.jpg' # 存储到测训练集
        file = open(file_path) #打开rbg值文件
        # fileSave = 'scenario_pic\\1.jpg' #打开rbg值文件
        #通过一个个RGB点生成图片
        for i in range(0,HEIGTH):
            for j in range(0,WIDTH):
                line = file.readline()#获取一行
                rgb = line.split(",")#分离rgb
                im.putpixel((i,j),(int(rgb[0]),int(rgb[1]),int(rgb[2])))#rgb转化为像素
        # im.show()
        im.save(fileSave)
    return num_img



def traTest(file_path:str,fileSave:str):
    '''书写轨迹的测试函数'''
    im = Image.new("RGB",(HEIGTH,WIDTH))#创建图片

    # fileWriter = open(file_path2, 'w+')

    file = open(file_path) # 打开rbg值文件
    # fileSave = 'scenario_pic\\1.jpg' #打开rbg值文件

    #通过一个个rgb点生成图片
    for i in range(0,HEIGTH):
        for j in range(0,WIDTH):
            line = file.readline()#获取一行
            rgb = line.split(",")#分离rgb
            im.putpixel((i,j),(int(rgb[0]),int(rgb[1]),int(rgb[2])))#rgb转化为像素
    im.show()
    im.save(fileSave)


if __name__=='__main__':
    # 清空存有图片的文件夹
    setDir('PicClassTest\\1')
    setDir('PicClassTest\\2')
    setDir('PicClassTrain\\1')
    setDir('PicClassTrain\\2')
    print("文件夹清空，正在准备放入新的图片")

    RGB_path = 'imageRGBwithouV'

    num_train_img,num_test_img = imgStore2TrainTest(2601,num_samples,RGB_path)
    print("训练集照片:",num_train_img,"测试集照片:",num_test_img)
    print("图片准备完成！","共",num_train_img+num_test_img,"张")


    # '''全部转为训练文件'''
    # num_img_all = allImgStore(2601,RGB_path)
    # print("图片准备完成！","共",num_img_all,"张")

    '''
    traDraw的绘图文件
    下面是转RGB算法调试文件
    '''
    # file_path = r"imageRGBwithouV\\1.txt"
    # fileSave= 'PicClass.jpg'
    # traTest(file_path,fileSave)

