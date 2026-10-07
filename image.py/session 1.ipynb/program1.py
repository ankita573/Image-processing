import cv2
import matplotlib.pyplot as plt

image = cv2.imread("lenaa.png")

if image is None:
    print("❌ Image not found")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    plt.imshow(gray, cmap="gray")
    plt.title("Grayscale Image")
    plt.axis("off")
    plt.show()