import cv2

class WebCam:
    def __init__(self,opt):

        cap = cv2.VideoCapture(opt)

        while(True):

            ret, frame = cap.read()
            image =frame.copy()

            img=cv2.putText(frame, 'Press q to capture image', (50, 50) , cv2.FONT_HERSHEY_SIMPLEX ,0.9, (255, 100, 100) , 1, cv2.LINE_AA)    
            cv2.imshow('frame',img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.imwrite("./output/out.jpg", image) 
                break
        cap.release()
        cv2.destroyAllWindows()       





# # web=WebCam(2)
# img= cv2.imread("./data/staff.jpg")
# face=Face(img,1)
# print(face.hasFace())
# print(face.numberOfFace())