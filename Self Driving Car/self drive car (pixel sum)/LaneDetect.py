import cv2
import numpy as np
import util as ut

#put all curve into list, find avg
curveList = []
avgVal = 8

def LaneCurve(img, display=2):
    imgCopy = img.copy()

    #threshold
    imgThres = ut.thresholds(img)

    #car pov to top pov
    hT, wT, c = img.shape
    points = ut.livePTS()
    imgWarp = ut.warp(imgThres, points, wT, hT)
    imgPTS = ut.drawPoints(img, points)

    #histogram (region=4 means 1/4 bottom)
    midPoint, imgHist = ut.getHist(imgWarp, display = True, minPer=0.5, region=4)

    #whole region
    curvePoint, imgHist = ut.getHist(imgWarp, display=True, minPer=0.9)

    #curve value
    curveVal = curvePoint-midPoint

    #curve average (so car will be smooth, reduce noise)
    curveList.append(curveVal)
    if len(curveList)>avgVal:
        curveList.pop(0)
    curve = int(sum(curveList)/len(curveList))

    #display
    if display != 0:
        InvWarp = ut.warp(imgWarp, points, wT, hT, inv=True)
        InvWarp = cv2.cvtColor(InvWarp, cv2.COLOR_GRAY2BGR)
        InvWarp[0:hT // 3, 0:wT] = 0, 0, 0
        imgLaneColor = np.zeros_like(img)
        imgLaneColor[:] = 0, 255, 0
        imgLaneColor = cv2.bitwise_and(InvWarp, imgLaneColor)
        imgCopy = cv2.addWeighted(imgCopy, 1, imgLaneColor, 1, 0)
        midY = 450
        cv2.putText(imgCopy, str(curve), (wT // 2 - 80, 85), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
        cv2.line(imgCopy, (wT // 2, midY), (wT // 2 + (curve * 3), midY), (255, 0, 255), 5)
        cv2.line(imgCopy, ((wT // 2 + (curve * 3)), midY - 25), (wT // 2 + (curve * 3), midY + 25), (0, 255, 0), 5)
        for x in range(-30, 30):
            w = wT // 20
            cv2.line(imgCopy, (w * x + int(curve // 50), midY - 10),
                     (w * x + int(curve // 50), midY + 10), (0, 0, 255), 2)
    if display == 2:
        cv2.imshow("Thres", imgThres)
        cv2.imshow("warp", imgWarp)
        cv2.imshow("warp PTS", imgPTS)
        cv2.imshow("Hist", imgHist)
        cv2.imshow("Lane",imgLaneColor)
        cv2.imshow("Result", imgCopy)

    elif display == 1:
        cv2.imshow('Result', imgCopy)

    return curve

if __name__ == "__main__":
    cap = cv2.VideoCapture("vid.mp4")
    intialTracbarVals = [102,80,20,214]

if __name__ == "__main__":
    cap = cv2.VideoCapture("vid.mp4")
    TrackbarVals = [102,80,20,214]

    ut.TrackBar(TrackbarVals)

    while True:
        success, img = cap.read()
        img = cv2.resize(img,(480,240))
        LaneCurve(img)
        cv2.imshow("vid", img)
        cv2.waitKey(1)




