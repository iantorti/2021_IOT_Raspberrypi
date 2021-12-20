import cv2

img = cv2.imread('dfdf.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('dfdf',img)
cv2.imshow('gray',gray)

while True:
    if cv2.waitKey(0) == 13:
        break
cv2.imwrite('guktan.jpg' ,gray)
cv2.destroyAllWindows()