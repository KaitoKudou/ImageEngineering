from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def color_hist(filename):
    img = np.asarray(Image.open(filename).convert("L")).reshape(-1,1)
    plt.hist(img, bins=128)
    plt.show()
    Image.open(filename).show()

color_hist("sample4.pgm")
