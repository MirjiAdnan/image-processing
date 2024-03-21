import cv2
import numpy as np

# Read the image

image = cv2.imread('Default.jpg')

# Check if the image was successfully loaded
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Define the amount of translation in x and y directions
    DELTA_X = 100  # Change this value according to your preference
    DELTA_Y =  60 # Change this value according to your preference

    # Define the transformation matrix for translation
    M = np.float32([[1, 0, DELTA_X],
                    [0, 1, DELTA_Y]])

    # Apply the translation transformation to the image
    translated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

    # Display the original and translated images
    cv2.imshow('Original Image', image)
    cv2.imshow('Translated Image', translated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()