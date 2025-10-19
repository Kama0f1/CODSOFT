import cv2
import face_recognition
import os

face_models_path = r"E:\Projects\Codsoft\Internship\tasks\task-5\face models"

known_faces = []
known_names = []

for filename in os.listdir(face_models_path):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(face_models_path, filename)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)
        if encoding:
            known_faces.append(encoding[0])
            known_names.append(os.path.splitext(filename)[0])
            
        if len(encoding) == 0:
            print(f"No face found in {filename}")
            continue
            
cam = cv2.VideoCapture(0)

frame_count = 0
while True:
    ret, frame = cam.read()
    if not ret:
        break
    frame_count += 1
    if frame_count % 5 != 0:  # Process every 5th frame
        continue
    
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    faces = face_recognition.face_locations(rgb_frame)
    encodings = face_recognition.face_encodings(rgb_frame, faces)
    
    for (top, right, bottom, left), face_encoding in zip(faces, encodings):
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.6)
        name = "Unknown"
        
        if True in match:
            index = match.index(True)
            name = known_names[index]
            
        
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10)
                    , cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    cv2.imshow("Face Recognition", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()