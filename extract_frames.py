import cv2
 
# Opens the Video file
cap= cv2.VideoCapture('annotate_person.mp4')
i=0
count=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if count% 4 == 0:
        cv2.imwrite('frame_'+str(i)+'.jpg',frame)
        count+=1
        i+=1
    else:
        count+=1
 
cap.release()