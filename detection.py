import os
from turtle import fillcolor
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import ImageOps
from PIL import Image
import os.path
import numpy as np

def detect(dataPath, clf):
    """
    Please read detectData.txt to understand the format. Load the image and get
    the face images. Transfer the face images to 19 x 19 and grayscale images.
    Use clf.classify() function to detect faces. Show face detection results.
    If the result is True, draw the green box on the image. Otherwise, draw
    the red box on the image.
      Parameters:
        dataPath: the path of detectData.txt
      Returns:
        No returns.
    """
    # Begin your code (Part 4)
    f=open(dataPath,"r")
    lines=f.readlines()
    n=0
    for line in lines:
      tem=line.split(' ')
      if tem[0][-1]=="g":
        pic=Image.open("data/detect/"+tem[0])
        pix=np.array(pic)
        n=int(tem[1])
        ax=plt.gca()
      else:
        n=n-1
        x=int(tem[0])
        y=int(tem[1])
        width=int(tem[2])
        height=int(tem[3])
        facearray=pix[y:y+height,x:x+width]
        facepic=Image.fromarray(facearray)
        facefordata=ImageOps.grayscale(facepic.resize((19,19), Image.BILINEAR))
        facefordataarray=np.array(facefordata)
        h=clf.classify(facefordataarray)
        if h==1:
          rect=Rectangle((x,y),width,height,edgecolor='green',fill=False)
        else:
          rect=Rectangle((x,y),width,height,edgecolor='red',fill=False)
        ax.add_patch(rect)
      if n==0:
        plt.imshow(pic)
        plt.show()
    # raise NotImplementedError("To be implemented")
    # End your code (Part 4)
