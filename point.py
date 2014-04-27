#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import Image,ImageDraw

if __name__ == '__main__' :
    width = height = int(sys.argv[1])
    im = Image.new("L",(width,height),255)
    draw = ImageDraw.Draw(im)
    draw.point((width/2,height/2), 0)
    im.save("point.png","PNG")
