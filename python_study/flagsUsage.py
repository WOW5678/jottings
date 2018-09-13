# -*- coding: utf-8 -*-
"""
 @Time    : 2018/9/13 0013 下午 4:05
 @Author  : Shanshan Wang
 @Version : Python3.5


# 学习使用 tf.app.flags 使用，全局变量
# 可以再命令行中运行也是比较方便，如果只写 python app_flags.py 则代码运行时默认程序里面设置的默认设置
# 若 python app_flags.py --train_data_path <绝对路径 train.txt> --max_sentence_len 100
#    --embedding_size 100 --learning_rate 0.05  代码再执行的时候将会按照上面的参数来运行程序

"""
import tensorflow as tf
FLAGS=tf.app.flags.FLAGS
flags=tf.app.flags

flags.DEFINE_string('train_data_path','','training data dir')
flags.DEFINE_string('log_dir','E:\codePractices','the log dir')
flags.DEFINE_integer('max_sentence_len',80,'max num of tokens per query')
flags.DEFINE_integer('embedding_size',50,'embedding size')

flags.DEFINE_float('learning_rate',0.001,'learning_rate')

def main(unused_argv):
    train_data_path=FLAGS.train_data_path
    print('train data path:',train_data_path)
    max_sentence_len=FLAGS.max_sentence_len
    print('max_sentence_len:',max_sentence_len)
    embedding_size=FLAGS.embedding_size
    print('embedding_size:',embedding_size)
    abc=tf.add(max_sentence_len,embedding_size)

    init=tf.global_variables_initializer()

    sv=tf.train.Supervisor(logdir=FLAGS.log_dir,init_op=init)
    with sv.managed_session() as sess:
        print('abc:',sess.run(abc))

# 使用这种方法保证了当此文件被import的时候不会执行main函数
if __name__ == '__main__':
    tf.app.run()