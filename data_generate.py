import os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import pickle

def FontSourceHanJPG(hanzi, size, font):
    im = Image.new("L", (size,size), color=0)
    draw = ImageDraw.Draw( im )
    font=ImageFont.truetype( font, size)
    draw.text ( (0,-(size/3.75)), hanzi, fill=255, font=font )
    return im

size = 64
File=open("unicode.txt",'r')
chrlist=File.read()
fontpath="Korea/"
font_count = 0

for font in os.listdir(fontpath):
    code_hanzi = []
    image = []
    data = (code_hanzi, image)
    font_status=[]
    #font_status=''
    hanzi_count=0
    print(font)
    hanzi_num=0
    for hanzi in chrlist:
        hanzi_num+=1

        temp=np.array(FontSourceHanJPG(hanzi, size, fontpath+font))

        code_hanzi.append(hanzi)
        image.append((temp-127.5)/127.5)

        hanzi_count+=1
        print(font + hanzi + " done {}%".format((hanzi_count)/len(chrlist)*100))
    
    image = np.array(image)
    print("saving "+font[:-4]+"_{}".format(size))
    output = open(font[:-4] +'_{}.pkl'.format(size),'wb')
    pickle.dump(data, output)
    print("done")
    font_count+=1
    print(font[:-4] + " done {}/{}".format((font_count),(len(os.listdir(fontpath)))))
    
fontpath="Japanese/"
font_count = 0

for font in os.listdir(fontpath):
    code_hanzi = []
    image = []
    data = (code_hanzi, image)
    font_status=[]
    #font_status=''
    hanzi_count=0
    print(font)
    hanzi_num=0
    for hanzi in chrlist:
        hanzi_num+=1

        temp=np.array(FontSourceHanJPG(hanzi, size, fontpath+font))

        code_hanzi.append(hanzi)
        image.append((temp-127.5)/127.5)

        hanzi_count+=1
        print(font + hanzi + " done {}%".format((hanzi_count)/len(chrlist)*100))
    
    image = np.array(image)
    print("saving "+font[:-4]+"_{}".format(size))
    output = open(font[:-4] +'_{}.pkl'.format(size),'wb')
    pickle.dump(data, output)
    print("done")
    font_count+=1
    print(font[:-4] + " done {}/{}".format((font_count),(len(os.listdir(fontpath)))))
    
fontpath="SimplifiedChinese/"
font_count = 0

for font in os.listdir(fontpath):
    code_hanzi = []
    image = []
    data = (code_hanzi, image)
    font_status=[]
    #font_status=''
    hanzi_count=0
    print(font)
    hanzi_num=0
    for hanzi in chrlist:
        hanzi_num+=1

        temp=np.array(FontSourceHanJPG(hanzi, size, fontpath+font))

        code_hanzi.append(hanzi)
        image.append((temp-127.5)/127.5)

        hanzi_count+=1
        print(font + hanzi + " done {}%".format((hanzi_count)/len(chrlist)*100))
    
    image = np.array(image)
    print("saving "+font[:-4]+"_{}".format(size))
    output = open(font[:-4] +'_{}.pkl'.format(size),'wb')
    pickle.dump(data, output)
    print("done")
    font_count+=1
    print(font[:-4] + " done {}/{}".format((font_count),(len(os.listdir(fontpath)))))
    
fontpath="TraditionalChinese/"
font_count = 0

for font in os.listdir(fontpath):
    code_hanzi = []
    image = []
    data = (code_hanzi, image)
    font_status=[]
    #font_status=''
    hanzi_count=0
    print(font)
    hanzi_num=0
    for hanzi in chrlist:
        hanzi_num+=1

        temp=np.array(FontSourceHanJPG(hanzi, size, fontpath+font))

        code_hanzi.append(hanzi)
        image.append((temp-127.5)/127.5)

        hanzi_count+=1
        print(font + hanzi + " done {}%".format((hanzi_count)/len(chrlist)*100))
    
    image = np.array(image)
    print("saving "+font[:-4]+"_{}".format(size))
    output = open(font[:-4] +'_{}.pkl'.format(size),'wb')
    pickle.dump(data, output)
    print("done")
    font_count+=1
    print(font[:-4] + " done {}/{}".format((font_count),(len(os.listdir(fontpath)))))