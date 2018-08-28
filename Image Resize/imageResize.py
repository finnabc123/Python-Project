import cv2

img = cv2.imread("galaxy.jpg", 3)

# print(type(img))
# print(img)
# print(img.shape)
# print(img.ndim)

resizedImg = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy", resizedImg)
cv2.imwrite("Galaxy_Resized.jpg", resizedImg)
cv2.waitKey(0)
cv2.destroyAllWindows()