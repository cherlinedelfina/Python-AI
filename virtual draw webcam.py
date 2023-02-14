import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10,150)

myColors = [[0,133,182,179,183,255],[0,91,182,10,197,255],[22,133,126,27,255,193],[83,139,136,88,191,171]]
myColorValues = [[0,128,255],[178,102,255],[0,255,255],[102,204,0]]
myPoints = [] #[x, y, colorID]

def findColor(img,myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count += 1
    return newPoints

def getContours(img):
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area>500:
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y

def drawss(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgResult = img.copy()

    newPoints = findColor(img,myColors,myColorValues)
    if len(newPoints)!=0:
        for pts in newPoints:
            myPoints.append(pts)
    if len(newPoints)!=0:
        drawss(myPoints,myColorValues)

    cv2.imshow("Outputss", imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break