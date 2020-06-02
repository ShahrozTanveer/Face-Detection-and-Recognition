import cv2
import numpy as np


class Face:
    def __init__(self,img,flag):
        net = cv2.dnn.readNet("./yolo-coco/face.weights", "./yolo-coco/face.cfg")
        classes = list()
        f= open("./yolo-coco/face.names", "r")#read .names file
        for line in f.readlines():#loop each line in file
            classes.append(line.strip())
        layer_names = net.getLayerNames()#get layes names
        layer=list()#init layes list
        for i in net.getUnconnectedOutLayers():
            layer.append(layer_names[i[0] - 1])
        colors = np.random.uniform(0, 255, size=(len(classes), 3))
        # img = cv2.resize(img, None, fx=0.2, fy=0.2)

        height, width,_ = img.shape
        if height >1500 or width >1500:
            img = cv2.resize(img, None, fx=0.2, fy=0.2)
            height, width,_ = img.shape



        blobObject = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blobObject)
        outputs = net.forward(layer)#get next layer
        class_ids = list()
        confidences = list()
        boxes = list()
        for out in outputs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.8:#tresh >0.5

                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    # get points for rectangle
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)
        self.dec = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)#number of dectected objects in frame
        if flag == 1:
            for i in range(len(boxes)):
                if i in self.dec:
                    x, y, w, h = boxes[i]
                    label = str(classes[class_ids[i]])#get label
                    color = colors[0]#each classs has specific color defined above
                    cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)#create rectangle
                    # cv2.putText(img, label, (10,50), cv2.FONT_ITALIC, 2, color, 3)

            cv2.imshow("Image", img)




            cv2.waitKey(0)
            cv2.destroyAllWindows()        

    def hasFace(self):
        return len(self.dec)>0

    def numberOfFace(self):
        return len(self.dec)



# img= cv2.imread("./data/staff.jpg")
# face=Face(img,1)
# print(face.hasFace())
# print(face.numberOfFace())




