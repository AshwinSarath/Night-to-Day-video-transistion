import cv2
import os

def getframes(path):
    cap= cv2.VideoCapture(path)
    saveat=r'D:\Projects\Night_video_Masking\generated'
      
    i=0
    while(cap.isOpened()):
        ret, frame = cap.read() #indent removed
        if ret == False:
            break
        cv2.imwrite(os.path.join(saveat,'frame'+str(i)+'.jpg'),frame) 
        i+=1
    


