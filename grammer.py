# import tensorflow as tf
# mytuple = ("c", "python", "java")

# myit = iter(mytuple) # 用iter()方法创建了一个iterator对象

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(myit)

# for x in myit:
#     print(x)
# a = tf.constant([1,2,3])
# print(a)
# # c = tf.expand_dims(a,[2,3])
# # print(c)

'''/**
!/usr/bin/env tensorflow
# -*- coding: utf-8 -*-
 * Copyright © 2019 Jianfeng_Wu. All rights reserved.
 * 
 * @author: Jianfeng_Wu
 * @date: 2022-04-23 
 * @time: 21:53:50 
 * Version:1.0.0
 */'''
# from mimetypes import init
# from sklearn.decomposition import KernelPCA
# import tensorflow as tf

# class student(object):
#     def __init__(self,name =12 ,age=175,*args,**kwargs) -> None:
#         self.name = name
#         self.age = age
#         print(self.name,self.age)
#         print(args,kwargs)
#     def __call__(self,*args,**kwargs):
#         print('my friend is',args)
#         print('my friends age is',kwargs)

# stu1 = student('Good Student',13,174,143,ti = 1, ha =2) # 实例化为对象stu1
# stu1('tim','harry',tim = 1, harry =2)  # stu1这时候可以当作函数来用，输入参数之后，默认执行类中的_call_方法

# '''/**
# !/usr/bin/env tensorflow
# # -*- coding: utf-8 -*-
#  * Copyright © 2019 Jianfeng_Wu. All rights reserved.
#  * 
#  * @author: Jianfeng_Wu
#  * @date: 2022-04-29 
#  * @time: 21:36:31 
#  * Version:1.0.0
#  * description:打印输出tensor的值
#  */'''
# from operator import le
# import tensorflow as tf
# x = tf.constant([[1., 1.], [2., 2.]])
# a = tf.reduce_sum(x,reduction_indices=[0]) # reduction_indices计算tensor指定轴方向上的所有元素的累加和;

# c = [[1,0],[0,1],[1,0],[0,1]]

# print(len(c))

# # print只能打印输出shape的信息，而要打印输出tensor的值，需要借助class tf.Session, class tf.InteractiveSession。
# # 因为我们在建立graph的时候，只建立tensor的结构形状信息，并没有执行数据的操作。
# with tf.Session() as sess:
#     print(a)
#     a = sess.run(a)
#     print(a)
#     print(len(a))

# '''/**
# !/usr/bin/env tensorflow
# # -*- coding: utf-8 -*-
#  * Copyright © 2019 Jianfeng_Wu. All rights reserved.
#  * 
#  * @author: Jianfeng_Wu
#  * @date: 2022-04-30 
#  * @time: 12:18:45 
#  * Version:1.0.0
#  * description:生成随机数
#  */'''

# import random

# k1,k2 = 0,0
# for i in range(100):
#     Uniform = random.uniform(0,9)
#     # print(Uniform)    
#     if Uniform<1.4:
#         k1 += 1
#         print(Uniform)
#     elif Uniform<2:
#         k2 += 1
#         print("0.3")
# print("小于1.4:",k1,'小于2:',k2)
    
# '''/**
# !/usr/bin/env tensorflow
# # -*- coding: utf-8 -*-
#  * Copyright © 2019 Jianfeng_Wu. All rights reserved.
#  * 
#  * @author: Jianfeng_Wu
#  * @date: 2022-04-30 
#  * @time: 20:20:32 
#  * Version:1.0.0
#  * description:用tensorflow构建数据集
#  */'''

# import tensorflow as tf
# import tensorflow.contrib.eager as tfe
# import os
# # tf.enable_eager_execution()

# import numpy as np



# classes={'1','2'}  #人为设定2类

# cwd='./PicClassTest/'
# data = []
# label = []
# for index,name in enumerate(classes):
#     file_path = cwd+name+'/'
#     # file_path = r'./PicClassTest/'
#     # print(os.listdir(file_path)) #os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。['1', '2']

#     data= [os.path.join(file_path,i) for i in os.listdir(file_path)] # os.path.join()函数用于路径拼接文件路径，可以传入多个路径
#     label = [int(name)]*np.ones(len(data))
#     # print(data)
#     # print(label)
#     dataset = tf.data.Dataset.from_tensor_slices((data,label))
#     print(dataset)

#     iterator = dataset.make_one_shot_iterator()
#     img_name, label = iterator.get_next()

#     with tf.Session() as sess:
#         while 1:
#             try:
#                 name, num = sess.run([img_name,label])
#                 print(name,num)
#                 assert num != 0, "fail to read label"
#             except tf.errors.OutOfRangeError:
#                 print("iterator done")
#                 break




# #  <DatasetV1Adapter shapes: ((), ()), types: (tf.string, tf.int32)>


#     #['E:\\dataset\\DAVIS\\JPEGImages\\480p\\bear\\00000.jpg', 'E:\\dataset\\DAVIS\\JPEGImages\\480p\\bear\\00001.jpg', ......]
#     #82


# # data = [1,2,3]
# # data.extend([1,3,54])
# # print(data)


# from requests import Session, session
# import tensorflow as tf

# filenames = tf.placeholder(tf.string, shape=[None])
# dataset = tf.data.TFRecordDataset(filenames)
# #如何将数据解析（parse）为Tensor见 3.1 节
# dataset = dataset.map(...)  # Parse the record into tensors.
# dataset = dataset.repeat()  # Repeat the input indefinitely.
# dataset = dataset.batch(32)
# iterator = dataset.make_initializable_iterator()

# # You can feed the initializer with the appropriate filenames for the current
# # phase of execution, e.g. training vs. validation.
# with tf.Session() as sess:
#     # Initialize `iterator` with training data.
#     training_filenames = "123train.tfrecords"
#     sess.run(iterator.initializer, feed_dict={filenames: training_filenames})

#     # Initialize `iterator` with validation data.
#     validation_filenames = "123test.tfrecords"
#     sess.run(iterator.initializer, feed_dict={filenames: validation_filenames})


# a = 500
# c = 7*a/2600
# print(type(c))
# import numpy as np

# def one_hot(labels,Label_class):
#     one_hot_label = np.array([[int(i == int(labels[j])) for i in range(Label_class)] for j in range(len(labels))])   
#     return one_hot_label

# a = [1,0,1,2]
# print(one_hot(a,3))
# print(one_hot(2,2))

import os
import shutil
def setDir(filepath):
    '''
    如果文件夹不存在就创建，如果文件存在就清空！
    :param filepath:需要创建的文件夹路径
    :return:
    '''
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    else:
        shutil.rmtree(filepath)  # 递归删除filepath目录的内容
        os.mkdir(filepath)

setDir('PicClassTrain\\2')