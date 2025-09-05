import cv2
import os

# Start webcam
cap = cv2.VideoCapture(0)

# Number of images to collect
dataset_size = 500

# Create directory to store images
data_dir = "Data_Collection"
os.makedirs(data_dir, exist_ok=True)

# Ask user for their name
person_name = input("Enter your name: ").strip()
person_dir = os.path.join(data_dir, person_name)
os.makedirs(person_dir, exist_ok=True)

count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.putText(frame, "Press 'C' to start or 'Q' to quit", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Collection", frame)

    key = cv2.waitKey(1)

    if key == ord("c"):
        while count < dataset_size:
            ret, frame = cap.read()
            if not ret:
                break
            img_path = os.path.join(person_dir, f"{person_name}_{count}.jpg")
            cv2.imwrite(img_path, frame)
            count += 1
            cv2.imshow("Collection", frame)
            if cv2.waitKey(1) == ord("q"):
                break
        break

    if key == ord("q"):
        print("Collection stopped.")
        break

cap.release()
cv2.destroyAllWindows()
