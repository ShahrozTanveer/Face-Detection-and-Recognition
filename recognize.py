import face_recognition
# import cv2
# import numpy as np
import os




# os.path.splitext(


class Recognition:
    def __init__(self):
        self.faceNames=list()
        self.knownFaces=list()
        self.loadData()


    def loadData(self):

        for file in os.listdir('./data/'):
            self.faceNames.append(os.path.splitext(file)[0])
            print("./data/"+file)
            image=face_recognition.load_image_file("./data/"+file)
            faceEncoding = face_recognition.face_encodings(image)[0]
            self.knownFaces.append(faceEncoding)
        print(self.faceNames)



rec= Recognition()

# biden_image = face_recognition.load_image_file("./data/me.jpg")
# biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
# known_face_encodings = [
#     biden_face_encoding,
# ]
# known_face_names = [
#     "Sharoz",
# ]
