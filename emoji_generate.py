# -*- coding:utf-8 -*-
'''
演示如何使用python自动生成表情包
'''
from PIL import Image,ImageDraw,ImageFont

##图片叠加
img=Image.open('data/pandas.webp')
jgz=Image.open('data/face.png')
img.paste(jgz,(130,100))
img.save('data/pandas_face.jpg')

## 文字叠加
draw=ImageDraw.Draw(img)
#设置字体
ttfront=ImageFont.truetype('simhei.ttf',24)
draw.text((70,320),'我的内心毫无波动，甚至还想笑',fill=(0,0,0),font=ttfront)
img.save('data/emoji.jpg')