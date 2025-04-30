import cv2
import face_recognition
import os
import numpy as np
import base64
from io import BytesIO
from PIL import Image

# === STEP 1: Load known faces ===
known_face_encodings = []
known_face_names = []

for filename in os.listdir("image"):
    path = os.path.join("image", filename)
    img = face_recognition.load_image_file(path)
    encodings = face_recognition.face_encodings(img)

    if encodings:
        known_face_encodings.append(encodings[0])
        name = os.path.splitext(filename)[0]
        known_face_names.append(name)
    else:
        print(f" No face found in {filename}")

# === Function for use in Flask (web app) ===
def recognize_face_from_base64(base64_string):
    try:
        img_data = base64.b64decode(base64_string.split(',')[-1])
        pil_image = Image.open(BytesIO(img_data)).convert('RGB')
        img = np.array(pil_image)

        small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        recognized_names = []

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            if True in matches:
                match_index = matches.index(True)
                name = known_face_names[match_index]
            recognized_names.append(name)

        return recognized_names

    except Exception as e:
        print(f"Error during recognition: {e}")
        return []

# === Optional: Run from terminal like before ===
if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            if True in matches:
                match_index = matches.index(True)
                name = known_face_names[match_index]

            top *= 4; right *= 4; bottom *= 4; left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
