import cv2
import numpy as np


def redDetect(img):
    height, width, _ = img.shape
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img2 = np.zeros((height, width), np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for Y in range(0, width):
        for X in range(0, height):
            H = int(img[X, Y, 0])
            S = int(img[X, Y, 1])
            V = int(img[X, Y, 2])
            if ((H < 10 and S > 80 and V > 140) or (H > 156 and S > 80 and V > 100)):
                img2[X, Y] = 255
            else:
                img2[X, Y] = 0
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    img2 = cv2.morphologyEx(img2, cv2.MORPH_OPEN, kernel)
    return img2


# cap = cv2.VideoCapture(0)

# while(cap.isOpened()):
#     if cv2.waitKey(1) & 0xFF == ord('1'):  # 按1退出
#         break
#     ret, frame = cap.read()
#     frame = redDetect(frame)
#     cv2.imshow('frame', frame)
# cap.release()
# cv2.destroyAllWindows()

img1 = cv2.imread('test/test1.jpg')
img1 = redDetect(img1)
cv2.imshow('img1', img1)

img2 = cv2.imread('test/test2.jpeg')
img2 = redDetect(img2)
cv2.imshow('img2', img2)

img3 = cv2.imread('test/test3.jpeg')
img3 = redDetect(img3)
cv2.imshow('img3', img3)

img4 = cv2.imread('test/test4.jpg')
img4 = redDetect(img4)
cv2.imshow('img4', img4)

# 0表示永久等待键盘输入，waitKey()是键盘绑定函数，时间尺度是毫秒级，特定的几毫秒内，如果有键盘输入，函数会返回按键的ASCII码值
cv2.waitKey(0)
# 删除建立的窗口，删除特定的窗口用cv2.destroyWindow(),参数是想删除的窗口名
cv2.destroyAllWindows()
