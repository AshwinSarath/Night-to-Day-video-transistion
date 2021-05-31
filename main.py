import time
from new_grab import *
from blender_D import *
import cv2
import numpy as np
import glob
 
# get frames
t0=time.time()
input_loc_night = r'...\Night_video_Masking\videos\night.mp4'
output_loc_night = r'...\Night_video_Masking\generated_night'

input_loc_day = r'...\Night_video_Masking\videos\day.mp4'
output_loc_day = r'...\Night_video_Masking\generated_day'

video_to_frames(input_loc_night, output_loc_night,600)
video_to_frames(input_loc_day,output_loc_day,600)
t1 = time.time()
tot=t1-t0
print("Processed time :",tot)

#do blender 

day_in= r'...\Night_video_Masking\generated_day'
night_in=r'...\Night_video_Masking\generated_night'


blend_out=r'...\Night_video_Masking\blender'

count=0
for night,day in zip(os.listdir(night_in),os.listdir(day_in)):
   
    night_orc=cv2.imread(night_in+'\\'+night)
    day_orc=cv2.imread(day_in+'\\'+day)
    print("LOOP RAN ",count)

    if night.endswith(".jpg"):
        final=blender(night_orc,day_orc,0.6,30)
        cv2.imwrite(blend_out + "/%#05d.jpg" % (count+1),final)
        count = count + 1
    else:
        continue
    




img_array = []
for filename in glob.glob('.../Night_video_Masking/blender/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter('.../Night_video_Masking/project.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 23, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()











