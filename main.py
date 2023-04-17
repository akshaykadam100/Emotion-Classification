import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# Generating class names
class_names = os.listdir(os.path.join(os.getcwd(), "data", "train"))
class_names.sort()

# Generating path of models
cnn_model_path = os.path.join(os.getcwd(), "modelling", "model.h5")
haarcascade_frontalface_path = os.path.join(os.getcwd(), "modelling", "haarcascade_frontalface_default.xml")

# Loading pretrained models
new_model = load_model(cnn_model_path)
face_detector = cv2.CascadeClassifier(haarcascade_frontalface_path)

video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()

    detections = face_detector.detectMultiScale(frame, minSize=(100, 100), minNeighbors=5)
    for (x, y, w, h) in detections:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        small_img = frame[y:y + h, x:x + w]
        cropped_img = cv2.resize(small_img, (48, 48), interpolation=cv2.INTER_AREA)

        predict_list_ = new_model.predict(np.expand_dims(cropped_img, axis=0), verbose=0).tolist()[0]
        index = predict_list_.index(max(predict_list_))
        str_ = f"{class_names[index].capitalize()}: {round(predict_list_[index] * 100, 2)} %"
        cv2.putText(frame, str_, (x+2, y+h-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
