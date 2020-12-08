import cv2
import matplotlib.pyplot as plt

imageFile = './data/lena.jpg'
img_bgr = cv2.imread(imageFile)

plt.axis('off')
plt.imshow(img_bgr)
plt.show()  # BGR채널이라 색상 왜곡됨

plt.axis('off')
# convert color
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)  # BGR채널을 RGB채널로 바꿈
plt.imshow(img_rgb)
plt.show()