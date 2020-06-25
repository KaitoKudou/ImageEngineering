from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2

def color_hist(filename):
    img = np.asarray(Image.open(filename).convert("L")).reshape(-1,1)
    plt.hist(img, bins=256)
    plt.show()

def binarization(filename):
    img = cv2.imread(filename)
    # グレースケール変換
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # 方法2 （OpenCVで実装） cv2.THRESH_OTSUにすると自動で閾値を決めてくれる(便利すぎ！！！)
    ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    #閾値がいくつになったか確認
    print("閾値: {}".format(ret))
    # 結果を出力
    cv2.imwrite("/Users/kudoukaito/Documents/3年前期/画像工学/samples/output.png", th)

color_hist("sample3.pgm")
binarization("sample04.bmp")
