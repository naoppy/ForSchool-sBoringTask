import cv2
import numpy as np

print(cv2.__version__)
# 3.3.0

img = np.full((400, 400, 3), 128, dtype=np.uint8)


def w(point):
    point[0] += 200
    point[1] += 200
    point = tuple(point)
    print(point)
    cv2.arrowedLine(img, (200, 200), point, (0, 0, 0), thickness=3)


w([128, 96])
w([120, -160])
w([-48, 64])

cv2.imwrite('opencv_draw_argument.png', img)

cv2.imshow('vector', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
