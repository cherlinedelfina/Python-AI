import cv2
import numpy as np

#define what is considered road, range of white
def thresholds(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    minWhite = np.array([80, 0, 0])
    maxWhite = np.array([255, 160, 255])
    maskWhite = cv2.inRange(imgHSV, minWhite, maxWhite)
    return maskWhite

#function to transform car pov to top pov
def warp(img, points, w, h, inv=False):
    # car pov
    carPTS = np.float32(points)

    # top pov
    topPTS = np.float32([[0, 0], [w, 0], [0, h], [w, h]])

    # transform from current car pov to top pov
    if inv:
        matrix = cv2.getPerspectiveTransform(topPTS, carPTS)
    else:
        matrix = cv2.getPerspectiveTransform(carPTS, topPTS)

    imgWarp = cv2.warpPerspective(img, matrix, (w, h))
    return imgWarp

### TRACKBARS (just to make things easier)
#meh function for trackbar pass nothing
def meh(a):
    pass

#function for trackbar
def TrackBar(TrackbarVals, wT=480, hT=240):
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Width Top", "Trackbars", TrackbarVals[0], wT // 2, meh)
    cv2.createTrackbar("Height Top", "Trackbars", TrackbarVals[1], hT, meh)
    cv2.createTrackbar("Width Bottom", "Trackbars", TrackbarVals[2], wT // 2, meh)
    cv2.createTrackbar("Height Bottom", "Trackbars", TrackbarVals[3], hT, meh)

#function to get real time points
def livePTS(wT=480, hT=240):
    widthTop = cv2.getTrackbarPos("Width Top", "Trackbars")
    heightTop = cv2.getTrackbarPos("Height Top", "Trackbars")
    widthBottom = cv2.getTrackbarPos("Width Bottom", "Trackbars")
    heightBottom = cv2.getTrackbarPos("Height Bottom", "Trackbars")
    points = np.float32([(widthTop, heightTop), (wT - widthTop, heightTop),
                         (widthBottom, heightBottom), (wT - widthBottom, heightBottom)])
    return points

#use circle to mark all points so we can see it
def drawPoints(img,points):
    #loop through all 4 points edges
    for x in range(0,4):
        cv2.circle(img,(int(points[x][0]),int(points[x][1])),12,(0,0,255),cv2.FILLED)
    return img


#region = instead of getting middle of whole pixel sum, limit sum to certain pixel range at the bottom
def getHist(img, minPer=0.1, display = False,region=1):
    #sum pixel of whole image
    if region == 1:
        # sum all columns (axis0 = height)
        histValues = np.sum(img, axis=0)

    #limit sum to certain pixel range at the bottom
    else:
        histValues = np.sum(img[int(img.shape[0] // region):, :], axis=0)


    #large value (>=10%) = path, small value (<10%) = noise
    maxVal = np.max(histValues)
    minVal = minPer*maxVal

    #get index of columns
    indexList = np.where(histValues >= minVal)

    # take average of the index list to find the curve
    indexAvg = int(np.average(indexList))


    if display:
        # create empty image & plot (0=height, 1=width)
        imgHist = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
        for x, sum_col in enumerate(histValues):
            sum_col = round(sum_col//2)

            cv2.line(imgHist, (x, img.shape[0]), (x, img.shape[0] - (sum_col // 255 // region)), (255, 0, 0), 1)
            cv2.circle(imgHist, (indexAvg, img.shape[0]), 20, (0, 255, 255), cv2.FILLED) #divide by 255 so not too high

            #use circle to mark the middle
            cv2.circle(imgHist, (indexAvg, img.shape[0]), 20, (0, 255, 255), cv2.FILLED)

        return indexAvg, imgHist
    return indexAvg





