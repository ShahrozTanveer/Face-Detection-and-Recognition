from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import  QMainWindow
from webcam import WebCam
from face import Face
import cv2
class Window2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow2")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        self.fileName_label = QtWidgets.QLabel(self.centralwidget)
        self.fileName_label.setGeometry(QtCore.QRect(430, 320, 141, 21))
        self.fileName_label.setObjectName("fileName_label")
        self.fileName_label.setText("file name")
        self.fileName_label.setVisible(False)
        self.fileName_label.resize(200, 25)

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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow2", "MainWindow2"))
        self.label2.setText(_translate("MainWindow", "Face Detection and Recognition"))

        # self.comboBox.setItemText(0, _translate("MainWindow2", "-----------------------"))
        # self.comboBox.setItemText(1, _translate("MainWindow2", "Internal WebCam"))
        # self.comboBox.setItemText(2, _translate("MainWindow2", "External WebCam"))
        # self.comboBox.setItemText(3, _translate("MainWindow2", "Select Image"))
        self.label.setText(_translate("MainWindow2", "Select Input Source"))
        # self.browse_btn.setText(_translate("MainWindow2", "Browse Image"))
        # self.fileName_label.setText(_translate("MainWindow2", "file name"))
        self.start_btn.setText(_translate("MainWindow2", "Start"))
    def comboChanged(self):
        text = str(self.comboBox.currentText())
        print("changed",text)
        if text =="Select Image":
            print("true")
            #TODO
            self.fileName_label.setText("file name")
            self.browse_btn.setVisible(True)

            self.fileName_label.setVisible(True)
        else:
            self.browse_btn.setVisible(False)

            self.fileName_label.setVisible(False)            
            
    def start_clicked(self):
        text = str(self.comboBox.currentText())
        if text =="-----------------------":
            self.fileName_label.setText("Please Select Input Source^")
            
            self.fileName_label.setVisible(True)


        else:
            inputScr=0
            if text =="External WebCam":
                inputScr = 2
            
            webcam=WebCam(inputScr)
            img = cv2.imread("./data/me.jpg")
            face = Face(img,1)
            print(face.hasFace())




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
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
        self.add_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_btn.setGeometry(QtCore.QRect(420, 260, 121, 61))
        self.add_btn.setObjectName("add_btn")
        self.add_btn.clicked.connect(self.add_clicked)
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

    def add_clicked(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Window2()
        self.ui.setupUi(self.window)
        
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())