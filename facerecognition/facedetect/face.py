import cv2
import face_recognition
import numpy as np




cap = cv2.VideoCapture(0)

diva_image = face_recognition.load_image_file("C:/Users/DELL/OneDrive/Documents/divvv.jpg")
diva_face_encoding = face_recognition.face_encodings(diva_image)[0]


known_face_encodings = [
    diva_face_encoding
     
]
known_face_names = [
    
    "Divya Lalwani"
    
]


while True:
    
    _, img = cap.read()



    rgb_frame = img[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)

    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)  


   
    for (top, right, bottom, left) , face_encoding  in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings,face_encoding)

        name = "Random Person"

        if True in matches:
             first_match_index = matches.index(True)
             name = known_face_names[first_match_index]

        cv2.rectangle(img, (left, bottom - 35), (right, bottom), (255,0,255),cv2.FILLED)
        
        font=cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img,name,(left + 8,bottom - 8),font, 1.2,(255,0,0), 1)
        if(name != "Random Person"):
            print(name, "is here ")

    
    cv2.imshow('open camera detector', img)

    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
   
    
        

cap.release()
cv2.destroyAllWindows()


