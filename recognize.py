import face_recognition as fr
import cv2
import numpy as np
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
            image=fr.load_image_file("./data/"+file)
            faceEncoding = fr.face_encodings(image)[0]
            self.knownFaces.append(faceEncoding)

        print("")
        print(self.faceNames)

    def recognizeImage(self,img_path):
        img=cv2.imread(img_path)
        frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
        rgb_frame = frame[:, :, ::-1]#BRG to RGB
        facesInFrame = fr.face_locations(rgb_frame)
        faceEnc = fr.face_encodings(rgb_frame, facesInFrame)
        face_names = []
        for face_encoding in faceEnc:
            matches = fr.compare_faces(self.knownFaces, face_encoding)
            face_distances = fr.face_distance(self.knownFaces, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = self.faceNames[best_match_index]
            else:
                return "-1"
            face_names.append(name)
  
        retname=""
        for (top, right, bottom, left), name in zip(facesInFrame, face_names):
            top = top * 4
            right = right * 4
            bottom =  bottom *4
            left = left * 4

            cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(img, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
            retname = name

        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return retname

    def recognizeLive(self,opt):
        cap = cv2.VideoCapture(opt)
        process_this_frame=True
        while True:
            ret, img = cap.read()
            frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
            rgb_frame = frame[:, :, ::-1]#BRG to RGB
            facesInFrame = fr.face_locations(rgb_frame)
            if process_this_frame:
                faceEnc = fr.face_encodings(rgb_frame, facesInFrame)
                face_names = []
                for face_encoding in faceEnc:
                    matches = fr.compare_faces(self.knownFaces, face_encoding)
                    face_distances = fr.face_distance(self.knownFaces, face_encoding)
                    best_match_index = np.argmin(face_distances)

                    if matches[best_match_index]:
                        name = self.faceNames[best_match_index]
                    else:
                        print("unknown face")
                        name="unknown"
                    face_names.append(name)
            process_this_frame = not process_this_frame

            retname=""
            for (top, right, bottom, left), name in zip(facesInFrame, face_names):
                top = top * 4
                right = right * 4
                bottom =  bottom *4
                left = left * 4

                cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)

                cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(img, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
                retname = name

            cv2.imshow('img', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def recognizeLogin(self,opt):
        counter = 0
        found=0
        retname="-1"
        cap = cv2.VideoCapture(opt)
        process_this_frame=True
        while True:
            counter +=1
            ret, img = cap.read()
            frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
            rgb_frame = frame[:, :, ::-1]#BRG to RGB
            facesInFrame = fr.face_locations(rgb_frame)
            if process_this_frame:
                faceEnc = fr.face_encodings(rgb_frame, facesInFrame)
                face_names = []
                for face_encoding in faceEnc:
                    matches = fr.compare_faces(self.knownFaces, face_encoding)
                    face_distances = fr.face_distance(self.knownFaces, face_encoding)
                    best_match_index = np.argmin(face_distances)

                    if matches[best_match_index]:
                        name = self.faceNames[best_match_index]
                        found +=1
                    
                    else:
                        # print("unknown face")
                        name="unknown"
                    face_names.append(name)
            process_this_frame = not process_this_frame
            if found >5:
                retname=name
                break
            
            for (top, right, bottom, left), name in zip(facesInFrame, face_names):
                top = top * 4
                right = right * 4
                bottom =  bottom *4
                left = left * 4

                cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)

                cv2.rectangle(img, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(img, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
                

            cv2.imshow('img', img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if counter>100:

                break
        cap.release()
        cv2.destroyAllWindows()
        return retname








# rec= Recognition()
# # print(rec.recognizeImage("./testData/charles.jpg"))
# # print(rec.recognizeImage("./testData/tstMAx.jpg"))
# rec.recognizeLive(2)
