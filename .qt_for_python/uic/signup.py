# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\tejas\Desktop\22-01-22\signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(491, 746)
        Form.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.outer = QtWidgets.QFrame(Form)
        self.outer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.outer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outer.setObjectName("outer")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.outer)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.outer)
        self.frame.setMaximumSize(QtCore.QSize(445, 700))
        self.frame.setStyleSheet("#frame{/* Auto layout */\n"
"\n"
"display: flex;\n"
"flex-direction: column;\n"
"align-items: flex-start;\n"
"padding: 40px 25px;\n"
"\n"
"position: absolute;\n"
"width: 593px;\n"
"height: 594px;\n"
"left: calc(50% - 593px/2 - 0.5px);\n"
"top: 243px;\n"
"\n"
"/* White */\n"
"\n"
"background: #FFFFFF;\n"
"/* Grey / Dark */\n"
"\n"
"border: 1px solid #D1D1D1;\n"
"box-sizing: border-box;\n"
"border-radius: 8px;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.signup = QtWidgets.QLabel(self.frame)
        self.signup.setGeometry(QtCore.QRect(10, 10, 81, 30))
        self.signup.setStyleSheet("position: absolute;\n"
"left: 20px;\n"
"right: 30px;\n"
"top: 10px;\n"
"bottom: 10px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 20px;\n"
"line-height: 37px;\n"
"letter-spacing: 0.05em;\n"
"background: rgba(0, 0, 0, 0.01);\n"
"color: #000000;")
        self.signup.setObjectName("signup")
        self.des = QtWidgets.QLabel(self.frame)
        self.des.setGeometry(QtCore.QRect(10, 40, 261, 41))
        self.des.setStyleSheet("position: absolute;\n"
"left: 0%;\n"
"right: 12.33%;\n"
"top: 15%;\n"
"bottom: 14.17%;\n"
"\n"
"font-family: poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 17px;\n"
"\n"
"/* Dark / Medium */\n"
"\n"
"color: #4F4F4F;")
        self.des.setObjectName("des")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 90, 445, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 5, 141, 21))
        font = QtGui.QFont()
        font.setFamily("poppins")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("position: absolute;\n"
"left: 0%;\n"
"right: 12.33%;\n"
"top: 15%;\n"
"bottom: 14.17%;\n"
"\n"
"font-family: poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 17px;\n"
"\n"
"/* Dark / Medium */\n"
"\n"
"color: #4F4F4F;")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 425, 40))
        self.lineEdit.setStyleSheet("position: static;\n"
"width: 535px;\n"
"height: 53px;\n"
"left: 0px;\n"
"top: 0px;\n"
"\n"
"/* White */\n"
"\n"
"background: #FFFFFF;\n"
"/* Dark / Medium */\n"
"\n"
"border: 1px solid #4F4F4F;\n"
"box-sizing: border-box;\n"
"border-radius: 7px;\n"
"\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 180, 445, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(20, 5, 141, 21))
        self.label_2.setStyleSheet("position: absolute;\n"
"left: 0%;\n"
"right: 12.33%;\n"
"top: 15%;\n"
"bottom: 14.17%;\n"
"\n"
"font-family: poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 17px;\n"
"\n"
"/* Dark / Medium */\n"
"\n"
"color: #4F4F4F;")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 30, 425, 40))
        self.lineEdit_2.setStyleSheet("position: static;\n"
"width: 535px;\n"
"height: 53px;\n"
"left: 0px;\n"
"top: 0px;\n"
"\n"
"/* White */\n"
"\n"
"background: #FFFFFF;\n"
"/* Dark / Medium */\n"
"\n"
"border: 1px solid #4F4F4F;\n"
"box-sizing: border-box;\n"
"border-radius: 7px;\n"
"\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(0, 270, 445, 80))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(20, 0, 425, 21))
        self.label_3.setStyleSheet("position: absolute;\n"
"left: 0%;\n"
"right: 12.33%;\n"
"top: 15%;\n"
"bottom: 14.17%;\n"
"\n"
"font-family: poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 17px;\n"
"\n"
"/* Dark / Medium */\n"
"\n"
"color: #4F4F4F;")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 30, 425, 40))
        self.lineEdit_3.setStyleSheet("position: static;\n"
"width: 535px;\n"
"height: 53px;\n"
"left: 0px;\n"
"top: 0px;\n"
"\n"
"/* White */\n"
"\n"
"background: #FFFFFF;\n"
"/* Dark / Medium */\n"
"\n"
"border: 1px solid #4F4F4F;\n"
"box-sizing: border-box;\n"
"border-radius: 7px;\n"
"\n"
"")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setGeometry(QtCore.QRect(0, 350, 445, 80))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(20, 5, 141, 21))
        self.label_4.setStyleSheet("position: absolute;\n"
"left: 0%;\n"
"right: 12.33%;\n"
"top: 15%;\n"
"bottom: 14.17%;\n"
"\n"
"font-family: poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 17px;\n"
"\n"
"/* Dark / Medium */\n"
"\n"
"color: #4F4F4F;")
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 30, 425, 40))
        self.lineEdit_4.setStyleSheet("position: static;\n"
"width: 535px;\n"
"height: 53px;\n"
"left: 0px;\n"
"top: 0px;\n"
"\n"
"/* White */\n"
"\n"
"background: #FFFFFF;\n"
"/* Dark / Medium */\n"
"\n"
"border: 1px solid #4F4F4F;\n"
"box-sizing: border-box;\n"
"border-radius: 7px;\n"
"\n"
"")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.war = QtWidgets.QLabel(self.frame)
        self.war.setGeometry(QtCore.QRect(0, 520, 441, 41))
        self.war.setStyleSheet("position: absolute;\n"
"left: 0%;\n"
"right: 12.33%;\n"
"top: 15%;\n"
"bottom: 14.17%;\n"
"\n"
"font-family: poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 17px;\n"
"\n"
"/* Dark / Medium */\n"
"\n"
"color: #FF0000;")
        self.war.setAlignment(QtCore.Qt.AlignCenter)
        self.war.setObjectName("war")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setGeometry(QtCore.QRect(0, 440, 445, 80))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setGeometry(QtCore.QRect(20, 5, 141, 21))
        self.label_6.setStyleSheet("position: absolute;\n"
"left: 0%;\n"
"right: 12.33%;\n"
"top: 15%;\n"
"bottom: 14.17%;\n"
"\n"
"font-family: poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"line-height: 17px;\n"
"\n"
"/* Dark / Medium */\n"
"\n"
"color: #4F4F4F;")
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_6.setGeometry(QtCore.QRect(10, 30, 425, 40))
        self.lineEdit_6.setStyleSheet("position: static;\n"
"width: 535px;\n"
"height: 53px;\n"
"left: 0px;\n"
"top: 0px;\n"
"\n"
"/* White */\n"
"\n"
"background: #FFFFFF;\n"
"/* Dark / Medium */\n"
"\n"
"border: 2px solid #4F4F4F;\n"
"box-sizing: border-box;\n"
"border-radius: 7px;\n"
"\n"
"")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.sign_up_button = QtWidgets.QPushButton(self.frame)
        self.sign_up_button.setGeometry(QtCore.QRect(10, 570, 421, 41))
        self.sign_up_button.setStyleSheet("\n"
"#sign_up_button{\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 14px;\n"
"line-height: 17px;\n"
"/* identical to box height */\n"
"\n"
"align-items: center;\n"
"\n"
"/* Grey / Light */\n"
"\n"
"color: white;\n"
"background: #4F4F4F;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"#sign_up_button:pressed {\n"
"    border-style: inset;\n"
"    border: 1px solid  #4F4F4F;\n"
"color: #4F4F4F;\n"
"background: #FFFFFF;\n"
"}\n"
"/* Inside auto layout */\n"
"\n"
"")
        self.sign_up_button.setObjectName("sign_up_button")
        self.sign_in_button = QtWidgets.QPushButton(self.frame)
        self.sign_in_button.setGeometry(QtCore.QRect(10, 640, 421, 41))
        self.sign_in_button.setStyleSheet("\n"
"#sign_in_button{\n"
"font-family: Inter;\n"
"font-style: normal;\n"
"font-weight: 500;\n"
"font-size: 14px;\n"
"line-height: 17px;\n"
"/* identical to box height */\n"
"\n"
"align-items: center;\n"
"\n"
"/* Grey / Light */\n"
"\n"
"\n"
"    border-style: inset;\n"
"    border: 1px solid  #4F4F4F;\n"
"color: #4F4F4F;\n"
"background: #FFFFFF;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"#sign_in_button:pressed {\n"
"    border-style: inset;\n"
"    color: white;\n"
"background: #4F4F4F;\n"
"border-radius: 8px;\n"
"}\n"
"/* Inside auto layout */\n"
"\n"
"")
        self.sign_in_button.setObjectName("sign_in_button")
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.outer, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.signup.setText(_translate("Form", "Sign Up"))
        self.des.setText(_translate("Form", "Please enter your details to continue."))
        self.label.setText(_translate("Form", "Name"))
        self.label_2.setText(_translate("Form", "Username"))
        self.label_3.setText(_translate("Form", "Email Id"))
        self.label_4.setText(_translate("Form", "Password"))
        self.war.setText(_translate("Form", "All fields are manadatory"))
        self.label_6.setText(_translate("Form", "Confirm Password"))
        self.sign_up_button.setText(_translate("Form", "Sign Up"))
        self.sign_in_button.setText(_translate("Form", "Already a user? Sign In"))
