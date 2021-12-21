import cv2
i=cv2.imread("monalisa.jpg",0)
bblur=cv2.bilateralFilter(i,30,60,5)
cv2.imshow("original",i)
cv2.waitKey(0)
cv2.imshow("BILATERAL FILTER", bblur)
cv2.waitKey(0)
