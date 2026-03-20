import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'ImagesAttendance'
images = []
classNames = []

attendance_cache = {}

print(f"Loading database...")

if not os.path.exists(path):
    os.makedirs(path)
    print(f"Folder '{path}' tidak ditemukan. Membuat folder baru...")

myList = [f for f in os.listdir(path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

print(f"Siap mendeteksi: {classNames}")

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        try:
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        except IndexError:
            pass
    return encodeList

def markAttendance(name):
    now = datetime.now()
    current_date = now.strftime('%d-%m-%Y')
    current_hour = now.strftime('%H')

    session_key = f"{current_date}_{current_hour}"
    
    if attendance_cache.get(name) == session_key:
        return 

    attendance_cache[name] = session_key

    filename = 'Absensi.csv'
    
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write('Name,Time,Date\n')
            
    with open(filename, 'a') as f:
        dtString = now.strftime('%H:%M:%S')
        f.write(f'{name},{dtString},{current_date}\n')
        print(f"[DATA MASUK] {name} berhasil absen pada jam {current_hour}:00")

encodeListKnown = findEncodings(images)
print('Kamera dimulai...')

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

process_this_frame = True 
face_locations = []
face_names = []

while True:
    success, img = cap.read()
    if not success: 
        print("Gagal membaca kamera.")
        break

    if process_this_frame:
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(imgS)
        face_encodings = face_recognition.face_encodings(imgS, face_locations)

        face_names = []
        for encodeFace in face_encodings:

            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)

            if faceDis[matchIndex] < 0.50:
                name = classNames[matchIndex].upper()
                markAttendance(name)
            else:
                name = "Unknown"
            
            face_names.append(name)

    process_this_frame = not process_this_frame

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)

        cv2.rectangle(img, (left, top), (right, bottom), color, 2)
        cv2.rectangle(img, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
        
        font = cv2.FONT_HERSHEY_DUPLEX
        fontScale = 0.8
        thickness = 1
        (text_w, text_h), _ = cv2.getTextSize(name, font, fontScale, thickness)
        box_width = right - left
        text_x = left + (box_width - text_w) // 2
        text_y = bottom - 6

        cv2.putText(img, name, (text_x, text_y), font, fontScale, (255, 255, 255), thickness)

    cv2.imshow('Sistem Absensi Aman', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
