import cv2

cam = cv2.VideoCapture('output.avi')

if not cam.isOpened():
    print('Camera open failed')
    exit()

fourcc = cv2.VideoWriter_fourcc(*'DIVX')

out = cv2.VideoWriter('output.avi',fourcc, 30, (640,480))
#사진찍기
ret, frame = cam.read()
cv2.imshow('frame', frame)
cv2.imwrite('output.jpg',frame)


#영상 찍기 
# while True:
#     ret, frame = cam.read()
#     if not ret:
#         break
#     cv2.imshow('frame',frame)
#     out.write(frame)

#     if cv2.waitKey(10) == 13:
#         break

cam.release()
out.release()
cv2.destroyAllWindows() 