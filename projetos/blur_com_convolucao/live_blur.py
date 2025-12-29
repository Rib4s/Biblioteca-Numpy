import cv2
import numpy as np
import scipy
import scipy.ndimage
from scipy import signal
from scipy.signal.windows import gaussian



PATH_XML = 'haarcascade_frontalface_default.xml'

def generate_kernel(kernlen=5, std=5):

    generate_kernel1d = gaussian(kernlen, std=std).reshape(kernlen, 1)
    generate_kernel2d = np.outer(generate_kernel1d, generate_kernel1d)

    return generate_kernel2d

video_capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + PATH_XML)

kernel = generate_kernel(kernlen=31, std=30)

kernel_tile = np.tile(kernel, (3, 1, 1))
kernel_sum = kernel.sum()
kernel = kernel / kernel_sum

while True:
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for x, y, w, h in faces:  
        frame[y:y+h, x:x+w] = scipy.ndimage.convolve(frame[y:y+h, x:x+w], np.atleast_3d(kernel), mode='nearest') # 1ª opção
        #frame[y:y+h, x:x+w] = cv2.GaussianBlur(frame[y:y+h, x:x+w], (25, 25), sigmaX=20, sigmaY=20) # 2ª opção
    
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()