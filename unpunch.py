import cv2
import os
import shutil
from PIL import Image
import numpy as np
import glob
# Opens the Video file
temp = r'C:\unpunch_temp'
location = input("Enter file location: ")
fps = int(input("Enter framerate: "))
fname = input("Enter the name of the result: ")
ftype = input("Enter file extension (with dot): ")
tfn = (fname + ftype)
if os.path.isfile(location) == True:
    cap= cv2.VideoCapture(location)
else:
    print ("Failed to find file")
    quit()
i=0
e=0
print ("creating dir")
if os.path.isdir(temp) == False:
    os.mkdir(temp)
else:
    shutil.rmtree(temp)
    os.mkdir(temp)
print("extracting files...")
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('C:/unpunch_temp/kang'+str(i)+'.jpg',frame)
    i+=1
print ("upscaling...")
list = os.listdir(temp)
for item in list:
    c = Image.open('C:/unpunch_temp/kang'+str(e)+'.jpg')
    d = c.resize((4096,2160), resample=Image.BOX)
    d.save('C:/unpunch_temp/kang'+str(e)+'.jpg')
print("making video")
img_array = []
for filename in glob.glob('C:/unpunch_temp/*.jpg'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
out = cv2.VideoWriter(tfn,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()


cap.release()
cv2.destroyAllWindows()
shutil.rmtree(temp)
print("finished cleaning")
