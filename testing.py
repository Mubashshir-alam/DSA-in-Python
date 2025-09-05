import cv2
import dlib
import pickle
import numpy as np

# Load model and Dlib tools
model_dict = pickle.load(open("model.p", "rb"))
model = model_dict["model"]

detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
facerec = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Load label names
labels_dict = {name: name for name in os.listdir("Data_Collection")}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        shape = sp(gray, face)
        face_descriptor = facerec.compute_face_descriptor(frame, shape)
        face_data = np.array(face_descriptor).reshape(1, -1)

        prediction = model.predict(face_data)
        name = prediction[0]

        x1, y1, x2, y2 = face.left(), face.top(), face.right(), face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, name, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
