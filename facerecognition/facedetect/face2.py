from PIL import Image, ImageDraw
import face_recognition
import cv2
import numpy as np

# Load a sample picture and learn how to recognize it.


divya_image = face_recognition.load_image_file("C:/Users/DELL/OneDrive/Documents/divvv.jpg")
divya_face_encoding = face_recognition.face_encodings(divya_image) [0]

karan_image = face_recognition.load_image_file("C:/Users/DELL/Downloads/karan.jpeg")
karan_face_encoding = face_recognition.face_encodings(karan_image) [0]

mummy_image = face_recognition.load_image_file("C:/Users/DELL/Downloads/mummy.jpeg")
mummy_face_encoding = face_recognition.face_encodings(mummy_image) [0]

papa_image = face_recognition.load_image_file("C:/Users/DELL/Downloads/papa.jpeg")
papa_face_encoding = face_recognition.face_encodings(papa_image) [0]

mahak_image = face_recognition.load_image_file("C:/Users/DELL/Downloads/mahak.jpeg")
mahak_face_encoding = face_recognition.face_encodings(mahak_image) [0]


# Create arrays of known face encodings and their names
known_face_encodings = [divya_face_encoding , karan_face_encoding,mummy_face_encoding,papa_face_encoding,mahak_face_encoding]
known_face_names = ["Divya","Karan","Muskan","Ashok","Mahak"]

# Load an image with an unknown face
image = face_recognition.load_image_file("C:/Users/DELL/OneDrive/Pictures/fam.jpeg")

# Find all the faces and face encodings in the unknown image
face_locations = face_recognition.face_locations(image)
face_encodings = face_recognition.face_encodings(image, face_locations)


pil_image = Image.fromarray(image)
draw = ImageDraw.Draw(pil_image)

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "UNKNOWN"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(0,0,255))

    # Draw a label with a name below the face
    text_width, text_height = draw.textsize(name)
   
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0 ,0, 255), outline=(255,255,255))
    
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))
    
    

# Remove the drawing library from memory as per the Pillow docs
del draw

pil_image.show()

