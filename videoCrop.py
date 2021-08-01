import cv2
import numpy as np
import csv

result = [[], [] ,[]]

address = "StateLite_DATA/KO/20210603/20210603_ir105.mp4"
video = cv2.VideoCapture(address)
w, h = int(video.get(3)), int(video.get(4))
print(w, h)

while True:
    has_frame, frame = video.read()
    if(not has_frame):
        break
    crop_black = frame[1:1080, 420:1500]
    crop_daegu = crop_black[588:788, 570:770]
    crop_final = cv2.resize(crop_daegu, None, fx=3, fy=3)
    #print(np.array(crop_final[260, 310]).mean(), np.array(crop_final[310, 290]).mean(), np.array(crop_final[360, 270]).mean())

    a = np.array(crop_final[260, 310]).mean()
    b = np.array(crop_final[310, 290]).mean()
    c = np.array(crop_final[360, 270]).mean()

    result[0].append(a)
    result[1].append(b)
    result[2].append(c)

    cv2.circle(crop_final, (310, 290), 2, (0, 0, 255), 5) #daegu
    cv2.circle(crop_final, (260, 310), 2, (0, 255, 0), 5) #left
    cv2.circle(crop_final, (360, 270), 2, (255, 255, 0), 5) #right

    cv2.imshow("VIDEO", crop_final)
    key = cv2.waitKey(3)
    if key == 27:
        break

cv2.destroyAllWindows()

print(np.array(result[0][1350:1550]).mean())
print(np.array(result[1][1350:1550]).mean())
print(np.array(result[2][1350:1550]).mean())

f = open('result2_ir105.csv', 'w', newline='')
write = csv.writer(f)
write.writerow(result[0])
write.writerow(result[1])
write.writerow(result[2])
f.close()