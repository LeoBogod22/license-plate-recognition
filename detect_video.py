import cv2
import pafy
import numpy as np
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# To capture video from webcam.

url = "https://www.youtube.com/watch?v=iM_KMYulI_s"
video = pafy.new(url)
best = video.getbest(preftype="mp4")

captura = cv2.VideoCapture() #Youtube
captura.open(0)
while True:
    # Read the frame ret, frame = capt  _, img = cap.read()
    # Convert to grayscale
    _, img = captura.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

# Release the VideoCapture object

captura.release()
cv2.destroyAllWindows()
