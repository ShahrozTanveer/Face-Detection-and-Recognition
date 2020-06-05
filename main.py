from PyQt5 import QtCore, QtGui, QtWidgets
from recognize import Recognition
from webcam import WebCam
from face import Face
import cv2
from shutil import copyfile
class Window2(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow2")
        MainWindow.resize(800, 600)
        self.filePath=""
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.nameInput.setGeometry(QtCore.QRect(180, 220, 200, 25))
        self.nameInput.setObjectName("nameInput")
        self.nameInput.setPlaceholderText("Enter Name!") 
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel.setGeometry(QtCore.QRect(430, 220, 241, 17))
        self.resultLabel.setObjectName("resultLabel")
        self.resultLabel.setVisible(False)
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(180, 40, 451, 81))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(430, 260, 211, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("-----------------------")
        self.comboBox.addItem("Internal WebCam")
        self.comboBox.addItem("External WebCam")
        self.comboBox.addItem("Select Image")
        self.comboBox.currentIndexChanged.connect(self.comboChanged)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 260, 181, 21))
        self.label.setObjectName("label")
        self.browse_btn = QtWidgets.QPushButton(self.centralwidget)
        self.browse_btn.setGeometry(QtCore.QRect(190, 320, 151, 25))
        self.browse_btn.setObjectName("browse_btn")
        self.browse_btn.setText("Browse Image")
        self.browse_btn.setVisible(False)
        self.browse_btn.clicked.connect(self.getFile)
        

        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(680, 260, 89, 25))
        self.start_btn.setObjectName("start_btn")
        self.start_btn.clicked.connect(self.start_clicked)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.w=MainWindow
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow2", "MainWindow2"))
        self.label2.setText(_translate("MainWindow2", "Face Detection and Recognition"))
        self.resultLabel.setText(_translate("MainWindow2", "Result"))

        
        self.label.setText(_translate("MainWindow2", "Select Input Source"))
       
        self.start_btn.setText(_translate("MainWindow2", "Start"))
    def comboChanged(self):
        text = str(self.comboBox.currentText())
        print("changed",text)
        self.browse_btn.setVisible(False)
        if text =="Select Image":
            print("true")
            #TODO

            
            self.browse_btn.setVisible(True)


        else:
            
            self.resultLabel.setVisible(False)
           


    def getFile(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget,'Select image','.','Image Files (*.jpg *.jpeg)')
        # print(fileName[0])
        if len(fileName) >0:
            print(fileName[0])
            self.filePath=fileName[0]

        
    def start_clicked(self):
        text = str(self.comboBox.currentText())
        name=self.nameInput.text()
        print(name)
        if name =="":
            print("no")
            QtWidgets.QMessageBox.critical(self.centralwidget, "Error",'Please Enter Name')
        else:
            if text =="-----------------------":
                # self.resultLabel.setText("Please Select Input Source^")
                
                # self.resultLabel.setVisible(True)
                QtWidgets.QMessageBox.critical(self.centralwidget, "Error",'Please Select Input Source')

            if text == "Select Image":
                if self.filePath == "":
                    QtWidgets.QMessageBox.critical(self.centralwidget, "Error",'Please Select Image')
                else:
                    img = cv2.imread(self.filePath)
                    face = Face(img,1)
                    if face.hasFace():
                        if face.numberOfFace()  == 1:
                            src=self.filePath
                            dst="./data/"+name+".jpg"
                            copyfile(src, dst)
                            QtWidgets.QMessageBox.information(self.centralwidget, "Success",'Face successfully added')
                            # QtWidgets.qApp.quit()
                            # self.w.close()
                        else:
                            QtWidgets.QMessageBox.critical(self.centralwidget, "Error",'Image contains '+str(face.numberOfFace())+" faces. It sholud only have one face" )

                    else:
                        QtWidgets.QMessageBox.critical(self.centralwidget, "Error","Image has no face" )

            else:
                inputScr=0
                if text =="External WebCam":
                    inputScr = 2
                
                webcam=WebCam(inputScr)
                img = cv2.imread("./output/out.jpg")
                face = Face(img,1)
                if face.hasFace():


                    print("image has face")
                    src="./output/out.jpg"
                    dst="./data/"+name+".jpg"
                    copyfile(src, dst)
                    QtWidgets.QMessageBox.information(self.centralwidget, "Success",'Face successfully added')

                else:
                    QtWidgets.QMessageBox.critical(self.centralwidget, "Error",'Image has no face')






class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.filePath=""
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 40, 451, 81))
        font = QtGui.QFont()
        font.setFamily("Fira Code")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(260, 260, 121, 61))
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(self.login_clicked)
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(420, 260, 121, 61))
        self.add_btn.setObjectName("add_btn")
        self.add_btn.clicked.connect(self.add_clicked)

        self.live_btn= QtWidgets.QPushButton(self.centralwidget)
        self.live_btn.setGeometry(QtCore.QRect(260, 350, 121, 61))
        self.live_btn.setObjectName("live_btn")
        self.live_btn.clicked.connect(self.live_clicked)

        self.image_btn= QtWidgets.QPushButton(self.centralwidget)
        self.image_btn.setGeometry(QtCore.QRect(420, 350, 121, 61))
        self.image_btn.setObjectName("image_btn")
        self.image_btn.clicked.connect(self.testImage)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Face Detection and Recognition"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.add_btn.setText(_translate("MainWindow", "Add"))
        self.live_btn.setText(_translate("MainWindow", "Live!"))
        self.image_btn.setText(_translate("MainWindow", "Test By Image"))

    def add_clicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Window2()
        self.ui.setupUi(self.window)
        
        self.window.show()

    def live_clicked(self):
        buttonReply = QtWidgets.QMessageBox.question(self.centralwidget, 'Live Feed!', "Do you like use external web cam?", QtWidgets.QMessageBox.Yes , QtWidgets.QMessageBox.No)
        if buttonReply == QtWidgets.QMessageBox.Yes:
            rec = Recognition()
            rec.recognizeLive(2)
        else:
            rec = Recognition()
            rec.recognizeLive(0)
        # pass
    def getFile(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self.centralwidget,'Select image','.','Image Files (*.jpg *.jpeg *.png)')
        # print(fileName[0])
        if len(fileName) >0:
            print(fileName[0])
            self.filePath=fileName[0]
    def testImage(self):
        self.getFile()
        if self.filePath == "":
                    QtWidgets.QMessageBox.critical(self.centralwidget, "Error",'Please Select Image')
        else:
            img = cv2.imread(self.filePath)
            face = Face(img,1)
            if face.hasFace():
                if face.numberOfFace()   >0:
                    src=self.filePath
                    print("ok")
                    rec= Recognition()
                    rec.recognizeImage(self.filePath) 
                    # if rec.recognizeImage(self.filePath) == "-1":
                    #     QtWidgets.QMessageBox.information(self.centralwidget, "Not Found",'Unknown Face!')


                # else:
                #     QtWidgets.QMessageBox.critical(self.centralwidget, "Error",'Image contains '+str(face.numberOfFace())+" faces. It sholud only have one face" )

            else:
                QtWidgets.QMessageBox.critical(self.centralwidget, "Error","Image has no face" )


    def login_clicked(self):
        buttonReply = QtWidgets.QMessageBox.question(self.centralwidget, 'Live Feed!', "Do you like use external web cam?", QtWidgets.QMessageBox.Yes , QtWidgets.QMessageBox.No)
        rec = Recognition()
        name=""
        if buttonReply == QtWidgets.QMessageBox.Yes:
            print("here")
            name = rec.recognizeLogin(2)
        else:
            name = rec.recognizeLogin(0)
        if name == "-1":
            QtWidgets.QMessageBox.critical(self.centralwidget, "Error",'Login Failed')
        else:
            QtWidgets.QMessageBox.information(self.centralwidget, "Success",'Login successfully!\n Welcome '+str(name))


        


    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
