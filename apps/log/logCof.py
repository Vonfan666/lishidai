#!/usr/bin/python3
# -*- coding:utf-8 -*-
#author=von-fan
import logging, os, time


def logger(name):
    logger = logging.getLogger(name)  # 创建一个日志对象
    # logger1 = logging.getLogger(name)

    consolelog = logging.StreamHandler()  # 创建一个输入到文件的日志对象
    filelog = logging.FileHandler(r'E:\PyFiles\lishidai\apps\log\test.log')  # 创建一个输入到控制台的文件日志

    logger.addHandler(consolelog)  # 将到输入到控制台的对象添加到日志对象
    logger.addHandler(filelog)  # 将输入到文件的对象添加到日志对象logger

    fmt = logging.Formatter('[%(asctime)s](%(levelname)s)%(name)s : %(message)s')  # 日志打印格式

    filelog.setFormatter(fmt)  # 为filelog添加时间格式
    consolelog.setFormatter(fmt)  # 为consolelog添加时间格式

    '''打印子级日志文件，每次运行全部py文件生成一个新的文件 path后续用时间戳定义全局变量'''
    a=time.localtime()
    timeCode=time.strftime('%Y%m%d',a)
    path= r'E:\PyFiles\lishidai\apps\log' + '\\' + timeCode + '.log'

    filelog1 = logging.FileHandler(path)
    logger.addHandler(filelog1)
    filelog1.setFormatter(fmt)

    logger.setLevel('INFO')  # 设置输出的控制台的日志为info+
    return logger

if __name__ == '__main__':
    logger = logger(os.path.basename(__file__))

