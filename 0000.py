# -*- coding:utf-8 -*-

import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

image_file = "8370277.png"
text='10'
im = Image.open(image_file)
font = ImageFont.truetype(r'C:\Windows\WinSxS\amd64_microsoft-windows-font-truetype-arial_31bf3856ad364e35_10.0.14393.0_none_9ff7dbaac40db853\arial.ttf', 46) #设置字体大小

# 在图片上添加文字 1
draw = ImageDraw.Draw(im)
# print font.getsize('10')
fontsize = font.getsize(text)
draw.text((im.size[0]-fontsize[0], 0), text , (255,0,0), font=font)
draw = ImageDraw.Draw(im)

# 保存
# windows目录前加r或R，则字符串不会对\转议
im.save("target.jpg")
im.show()