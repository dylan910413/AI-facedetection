import os
import os.path
from PIL import Image
import numpy as np

def loadImages(dataPath):
    """
    load all Images in the folder and transfer a list of tuples. The first 
    element is the numpy array of shape (m, n) representing the image. 
    The second element is its classification (1 or 0)
      Parameters:
        dataPath: The folder path.
      Returns:
        dataset: The list of tuples.
    """
    # Begin your code (Part 1)
    dataset=[]
    categories=["face","non-face"]
    for category in categories:
        path=os.path.join(dataPath,category)
        for f in os.listdir(path):
            pic=Image.open(os.path.join(path,f))
            pix=np.array(pic)
            if category=='face':
                dataset.append((pix,1))
            if category=='non-face':
                dataset.append((pix,0))
    # raise NotImplementedError("To be implemented")
    # End your code (Part 1)
    return dataset
