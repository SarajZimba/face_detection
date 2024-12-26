import cv2
import os

haar_file = "C:/Users/Dell/Documents/Silverline_projects/Face_detetion/haarcascade_frontalface_default.xml"

# All the faces data will be present in this folder
datasets = 'datasets'

# # These are sub data sets of folder,
# # for my faces I've used my name, you can
# # change the label here
# sub_data = 'saraj'

# # Ensure the 'datasets' directory exists
# if not os.path.isdir(datasets):
#     os.mkdir(datasets)

# # Create the subdirectory for the current person's data
# path = os.path.join(datasets, sub_data)
# if not os.path.isdir(path):
#     os.mkdir(path)

# # Defining the size of images
# (width, height) = (130, 100)

# # Load Haar cascade
# face_cascade = cv2.CascadeClassifier(haar_file)
# if face_cascade.empty():
#     print("Error: Unable to load Haar cascade file.")
#     exit()

# # Initialize webcam
# webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# if not webcam.isOpened():
#     print("Error: Could not access the webcam.")
#     exit()

# # The program loops until it has 30 images of the face.
# count = 1
# while count <= 30:
#     ret, im = webcam.read()
#     if not ret or im is None:
#         print("Error: Failed to capture frame from webcam.")
#         break

#     gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 4)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
#         face = gray[y:y + h, x:x + w]
#         face_resize = cv2.resize(face, (width, height))
#         cv2.imwrite(f'{path}/{count}.png', face_resize)
#         count += 1

#     cv2.imshow('OpenCV', im)
#     key = cv2.waitKey(10)
#     if key == 27:  # Exit on 'Esc' key
#         break

# webcam.release()
# cv2.destroyAllWindows()


def create_person_data(name):
    sub_data = name

    # Ensure the 'datasets' directory exists
    if not os.path.isdir(datasets):
        os.mkdir(datasets)

    # Create the subdirectory for the current person's data
    path = os.path.join(datasets, sub_data)
    if not os.path.isdir(path):
        os.mkdir(path)

    # Defining the size of images
    (width, height) = (130, 100)

    # Load Haar cascade
    face_cascade = cv2.CascadeClassifier(haar_file)
    if face_cascade.empty():
        print("Error: Unable to load Haar cascade file.")
        exit()

    # Initialize webcam
    webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not webcam.isOpened():
        print("Error: Could not access the webcam.")
        exit()

    # The program loops until it has 30 images of the face.
    count = 1
    while count <= 30:
        ret, im = webcam.read()
        if not ret or im is None:
            print("Error: Failed to capture frame from webcam.")
            break

        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
            face = gray[y:y + h, x:x + w]
            face_resize = cv2.resize(face, (width, height))
            cv2.imwrite(f'{path}/{count}.png', face_resize)
            count += 1

        cv2.imshow('OpenCV', im)
        key = cv2.waitKey(10)
        if key == 27:  # Exit on 'Esc' key
            break

    webcam.release()
    cv2.destroyAllWindows()

create_person_data("Saraj")