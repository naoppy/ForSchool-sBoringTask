import cv2
import numpy as np

scale = 100
size = 200

img = np.full((2 * size, 2 * size, 3), 128, dtype=np.uint8)


def w(point):
    # y座標の向きが逆なので戻す
    point[1] *= -1

    point[0] *= scale
    point[0] = int(point[0])
    point[1] *= scale
    point[1] = int(point[1])

    point[0] += size
    point[1] += size
    point = tuple(point)
    print(point)
    cv2.arrowedLine(img, (size, size), point, (0, 0, 0), thickness=2)


# x軸とy軸
cv2.line(img, (size, 0), (size, 2 * size), (255, 0, 0), thickness=1)
cv2.line(img, (0, size), (2 * size, size), (255, 0, 0), thickness=1)

w([32/5, 24/5])
w([1.28, 0.96])
w([1.20, -1.60])
w([-0.48, 0.64])

cv2.imwrite('opencv_draw_argument.png', img)

cv2.imshow('vector', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
