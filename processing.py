import dlib
import cv2
import os
import pickle
import numpy as np

# Load Dlib's face detector and shape predictor
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

data_dir = "Data_Collection"
data = []
labels = []

for person in os.listdir(data_dir):
    person_path = os.path.join(data_dir, person)
    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = detector(gray)
        for face in faces:
            shape = sp(gray, face)
            face_descriptor = facerec.compute_face_descriptor(img, shape)
            data.append(np.array(face_descriptor))
            labels.append(person)

# Save data and labels
with open("data.pickle", "wb") as f:
    pickle.dump({"data": data, "labels": labels}, f)
