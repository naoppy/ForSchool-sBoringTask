﻿import cv2
import numpy as np

# ====setting====
scale = 30
windowSize = 600
# ===============

size = int(windowSize / 2)
img = np.full((windowSize, windowSize, 3), 128, dtype=np.uint8)


def w(x, y):
    print("{}{:+}j".format(x, y))

    # y座標の向きが逆なので戻す
    y *= -1

    x *= scale
    x = int(x)
    y *= scale
    y = int(y)

    x += size
    y += size
    point = x, y
    cv2.arrowedLine(img, (size, size), point, (0, 0, 0), thickness=2)


# x軸とy軸
cv2.line(img, (size, 0), (size, windowSize), (255, 0, 0), thickness=1)
cv2.line(img, (0, size), (windowSize, size), (255, 0, 0), thickness=1)

# ====plotData====
w(2 / 5, -1 / 5)
w(8, -4)
w(4, 8)
w(-2, -4)
w(10, 0)
# ================

cv2.imwrite('opencv_draw_argument.png', img)

cv2.imshow('vector', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
