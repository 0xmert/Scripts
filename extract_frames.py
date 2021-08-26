import cv2
 
# Opens the Video file and extract the frames from the video and saves it into current folder.
cap= cv2.VideoCapture('annotate_person.mp4')
i=0
count=0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if count% 4 == 0:            # I am extracting 1 frame in every 4 frames you can change this. !!!!!make 0 indices part fixed !!
        cv2.imwrite('frame_'+str(i)+'.jpg',frame)
        count+=1
        i+=1
    else:
        count+=1
 
cap.release()
