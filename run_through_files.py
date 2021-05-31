import os
import cv2 as cv

blend_out=r'D:\Projects\Night_video_Masking\blender_genertor'
src1= cv.imread(r'D:\Projects\Night_video_Masking\k_day.jpg')

directory = r'D:\Projects\Night_video_Masking\generated'
for filename in os.listdir(directory):
    count=1
    alpha=0.5
    beta=1.0-alpha
    if filename.endswith(".jpg"):
        
        src2=cv.imread((os.path.join(directory, filename)))
        print(src2)
        dst=cv.addWeighted(src1,alpha,src2,beta,0.0)
        cv.imwrite(blend_out + "/%#05d.jpg" % (count+1), dst )
        count+=1


    else:
        continue
