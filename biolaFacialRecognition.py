import face_recognition
import pickle
import numpy as np
import re

#Initial variables
goAgain="z"
with open ('dataset_faces.dat', 'rb') as f:
        all_face_encodings=pickle.load(f)
face_names=list(all_face_encodings.keys())
face_encodings=np.array(list(all_face_encodings.values()))

#compareFace function
def compareFace():
    filename=input("Please enter the filename of the file with the unknown face, stored in the 'Unknowns' folder (e.g. face3.jpg): ")
    unknown_image=face_recognition.load_image_file("PATH"+filename)
    unknown_face=face_recognition.face_encodings(unknown_image)

    toleranceVal=0.61
    
    matches="foo"

    #Increases strictness until there is only one result left
    while (len(matches)>1):
        toleranceVal=toleranceVal-0.01
        result=face_recognition.compare_faces(face_encodings,unknown_face,tolerance=toleranceVal)
        names_with_result=list(zip(face_names,result))
        matches=[item for item in names_with_result if True in item]

    if len(matches)<1:
        print ("NO MATCH FOUND.")
    else:
        prettyMatch=str(matches[0][0])
        capMatch=prettyMatch.upper()
        print ("\n********************")
        print ("Match found: "+capMatch)
        print ("********************\n")
    goAgain=input("Would you like to analyze another photo? (y/n) ")
    print ("\n")
    if goAgain=="y":
        compareFace()

#MAIN

print ("BIOLA FACE FINDER\n")
print ("Given an unknown face, this program will search the Biola database and return any match it finds.\n")

compareFace()
