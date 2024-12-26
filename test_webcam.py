# import cv2
# from threading import Timer

# def pic():
#     global name
#     cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#     retval, frame = cam.read()
#     if retval != True:
#         print("Can't read frame")
#     cv2.imwrite('img' + str(name) + '.png', frame)
#     name = name + 1

# if __name__ == '__main__':
#     name = 1
#     time = 0

#     while time != 4:
#         t = Timer(1, pic)
#         t.start()
#         t.join()
#         time=time+1

import cv2

# Open webcam
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # DirectShow backend for Windows


if not cam.isOpened():
    print("Error: Webcam not accessible.")
    exit()

while True:
    ret, frame = cam.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    cv2.imshow("Webcam Test", frame)
    if cv2.waitKey(10) == 27:  # Press 'Esc' to exit
        break

cam.release()
cv2.destroyAllWindows()
