import numpy as np
import cv2

#img=np.zeros((300,512,3),np.uint8)
img=cv2.imread('cat.png',0)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.DestroyAllWindows()


#cap=cv2.VideoCapture(0)



#while True:
#    ret, frame=cap.read()

#    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#    cv2.imshow('frame',gray)

#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break

#cap.release()
#cv2.destroyAllwindows()

