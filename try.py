import cv2
import time
import os

import HandTrackingModule as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "fingers" # name of the folder, where there are images of fingers
fingerList = os.listdir(folderPath) # list of image titles in 'fingers' folder
overlayList = []
for imgPath in fingerList:
    image = cv2.imread(f'{folderPath}/{imgPath}')
    overlayList.append(image)

pTime = 0

detector = htm.handDetector(detectionCon=0.75)
totalFingers = 0

while True:
    sucess, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=False)

    if lmList:
        fingersUp = detector.fingersUp()
        print(fingersUp)
        totalFingers = fingersUp.count(1)

    h, w, c = overlayList[totalFingers].shape
    img[0:h, 0:w] = overlayList[totalFingers]

    cTime = time.time()
    fps = 1/ (cTime-pTime)
    pTime = cTime

    cv2.imshow("Image", img)
    cv2.waitKey(1)