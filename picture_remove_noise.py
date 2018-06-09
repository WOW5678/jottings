# -*- coding:utf-8 -*-
'''
实现图片去除噪音的功能
思路：
色素值越大表示颜色越深，越小表示颜色越浅
变量每个像素点，当色素值>n,把该点画成黑色点，当色素值<n 把该点画成百色点
'''

from PIL import Image
# 二值化处理
def two_value():
    image=Image.open('data/verificationCode.jpg')
    #灰度图
    lim=image.convert('L')
    # 灰度阈值设为165，低于这个值的点全部填为白色
    threshold=160
    table=[]
    for j in range(256):
        if j<threshold:
            table.append(0)
        else:
            table.append(1)
    bim=lim.point(table,'1')
    bim.save('data/removeNoise.jpg')

two_value()
