import cv2

img=cv2.imread('galaxy.jpg',0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized=cv2.resize(img,(700,500))
cv2.imshow('galaxy',resized)
cv2.imwrite('galaxy_Re.jpg',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()