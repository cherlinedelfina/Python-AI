import cv2
import numpy as np

img = np.zeros((500,500,3),np.uint8)

pt1 = (250,300)
pt2 = (150,350)
pt3 = (350,350)
cv2.rectangle(img,(150,350),(350,450),(0,0,255),cv2.FILLED)

triangle_cnt = np.array([pt1,pt2,pt3])
cv2.drawContours(img, [triangle_cnt], 0, (0, 255, 0), -1)

cv2.putText(img, "house", (200,50), cv2.FONT_ITALIC, 1, (200,255,10),2)

cv2.imshow("output",img)
cv2.waitKey(0)