import cv2
import os

# Absolute path to Haar cascade file
haar_file = "C:/Users/Dell/Documents/Silverline_projects/Face_detetion/haarcascade_frontalface_default.xml"

# Check if file exists
if not os.path.exists(haar_file):
    print(f"Error: File {haar_file} does not exist.")
    exit()

# Load Haar cascade
face_cascade = cv2.CascadeClassifier(haar_file)
if face_cascade.empty():
    print("Error: Unable to load the Haar cascade file.")
    exit()

# Loading the test image
image = cv2.imread("beautiful_lady.jpeg")
if image is None:
    print("Error: Unable to load the image.")
    exit()

# Converting to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect all the faces in the image
faces = face_cascade.detectMultiScale(image_gray)
print(f"{len(faces)} faces detected in the image.")

# For every face, draw a blue rectangle
for x, y, width, height in faces:
    cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)

# Save the image with rectangles
cv2.imwrite("women_detected.jpg", image)
print("Image saved as 'women_detected.jpg'.")
