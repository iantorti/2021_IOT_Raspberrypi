import cv2

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print('Camera open failed')
    exit()

fourcc = cv2.VideoWriter_fourcc(*'DIVX')

out = cv2.VideoWriter('output.avi',fourcc, 30, (640,480))
#사진찍기
# ret, frame = cam.read()
# cv2.imshow('frame', frame)
# cv2.imwrite('output.jpg',frame)


#영상 찍기 
while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(frame, 50,100)
    if not ret:
        break
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    cv2.imshow('edge',edge)
    out.write(frame)

    if cv2.waitKey(10) == 13:
        break

cam.release()
out.release()
cv2.destroyAllWindows()     