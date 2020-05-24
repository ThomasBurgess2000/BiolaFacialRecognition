import face_recognition
import pickle
import os

all_face_encodings={}

directory = os.fsencode("PATH")

i=0
for file in os.listdir(directory):
    filename=os.fsdecode(file)
    img1=face_recognition.load_image_file("PATH"+filename)
    name=filename[:-4]
    print (name)
    if len(face_recognition.face_encodings(img1)) > 0:
        all_face_encodings[name]=face_recognition.face_encodings(img1)[0]

with open ('dataset_faces.dat', 'wb') as f:
    pickle.dump(all_face_encodings, f)

k=input("press close to exit")