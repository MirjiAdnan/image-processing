import cv2
import matplotlib.pyplot as plt
import numpy as np
input_image_path = "D:\DIP\Default.jpg"
image = cv2.imread(input_image_path)
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('output_image.png', image)
cv2.imwrite('output_image.jpeg', image)
image_arrray=np.array(image)
#visualization of image in matrix form
print(image_arrray)

# Split the image into its RGB channels
blue_channel, green_channel, red_channel = cv2.split(image)

# Plot histograms for each channel
plt.figure(figsize=(15, 5))

# Blue channel histogram
plt.subplot(1, 3, 1)
plt.hist(blue_channel.ravel(), bins=256, color='blue', alpha=0.5)
plt.title('Blue Channel')
plt.xlim([0, 255])

# Green channel histogram
plt.subplot(1, 3, 2)
plt.hist(green_channel.ravel(), bins=256, color='green', alpha=0.5)
plt.title('Green Channel')
plt.xlim([0, 255])

# Red channel histogram
plt.subplot(1, 3, 3)
plt.hist(red_channel.ravel(), bins=256, color='red', alpha=0.5)
plt.title('Red Channel')
plt.xlim([0, 255])

plt.show()