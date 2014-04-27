#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
import Image

def count(img, x, y, b):
    """ img: 対象画像、x,y: 画像のサイズ、b: ボックスのサイズ """
    i = 0
    j = 0
    c = 0
    while i < x and j < y:
        flag = False
        for k in range(0, b):
            for l in range(0, b):
                if i+k < x and j+l < y:
                    if img.getpixel((i+k,j+l)) == 0:
                        """ ボックスに図形が含まれていたらカウントして次の図形へ """
                        c += 1
                        flag = True
                        break
            if flag:
                break
        i += b
        if i >= x:
            """ ボックスが右端に達したら左端に戻す """
            i = 0
            j += b

    return c # 図形が含まれていたボックスの数を返す


img = Image.open(sys.argv[1]).convert('1')  # 画像を読み込んで二値化
x, y = img.size                             # 画像サイズを取得

i = x/10
while i > x/1000:
    n = count(img, x, y, i)
    print math.log(i), math.log(n)
    i = i / 2
