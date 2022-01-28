# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\tejas\Desktop\22-01-22\create_posts.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_create_posts_form(object):
    def setupUi(self, create_posts_form):
        create_posts_form.setObjectName("create_posts_form")
        create_posts_form.resize(563, 524)
        create_posts_form.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(create_posts_form)
        self.gridLayout.setObjectName("gridLayout")
        self.create_posts_frame = QtWidgets.QFrame(create_posts_form)
        self.create_posts_frame.setMinimumSize(QtCore.QSize(541, 502))
        self.create_posts_frame.setMaximumSize(QtCore.QSize(541, 502))
        self.create_posts_frame.setStyleSheet("#create_posts_frame{/* Auto layout */\n"
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
        self.create_posts_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.create_posts_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.create_posts_frame.setObjectName("create_posts_frame")
        self.post_heading_posts = QtWidgets.QLabel(self.create_posts_frame)
        self.post_heading_posts.setGeometry(QtCore.QRect(20, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.post_heading_posts.setFont(font)
        self.post_heading_posts.setStyleSheet("position: absolute;\n"
"width: 233px;\n"
"height: 60px;\n"
"left: 92px;\n"
"top: 48px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 30px;\n"
"line-height: 60px;\n"
"/* identical to box height */\n"
"\n"
"letter-spacing: 0.05em;\n"
"text-decoration-line: underline;\n"
"text-transform: capitalize;\n"
"\n"
"color: #000000;\n"
"")
        self.post_heading_posts.setObjectName("post_heading_posts")
        self.description_label_posts = QtWidgets.QLabel(self.create_posts_frame)
        self.description_label_posts.setGeometry(QtCore.QRect(30, 170, 111, 41))
        self.description_label_posts.setStyleSheet("font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 30px;\n"
"/* identical to box height */\n"
"\n"
"letter-spacing: 0.05em;\n"
"text-transform: capitalize;\n"
"")
        self.description_label_posts.setObjectName("description_label_posts")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.create_posts_frame)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 210, 511, 131))
        self.plainTextEdit.setStyleSheet("background: rgba(196, 196, 196, 0.1);\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 30px;\n"
"/* identical to box height */\n"
"\n"
"letter-spacing: 0.05em;\n"
"text-transform: capitalize;\n"
"\n"
"color: #000000;")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.create_posts_frame)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(20, 110, 511, 41))
        self.plainTextEdit_2.setStyleSheet("background: rgba(196, 196, 196, 0.1);\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 30px;\n"
"/* identical to box height */\n"
"\n"
"letter-spacing: 0.05em;\n"
"text-transform: capitalize;\n"
"\n"
"color: #000000;")
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_4 = QtWidgets.QLabel(self.create_posts_frame)
        self.label_4.setGeometry(QtCore.QRect(30, 70, 81, 41))
        self.label_4.setStyleSheet("font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 30px;\n"
"/* identical to box height */\n"
"\n"
"letter-spacing: 0.05em;\n"
"text-transform: capitalize;\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.create_posts_frame)
        self.label_5.setGeometry(QtCore.QRect(20, 370, 511, 41))
        self.label_5.setStyleSheet("font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 30px;\n"
"/* identical to box height */\n"
"\n"
"letter-spacing: 0.05em;\n"
"text-transform: capitalize;\n"
"")
        self.label_5.setObjectName("label_5")
        self.add_files_button_posts = QtWidgets.QPushButton(self.create_posts_frame)
        self.add_files_button_posts.setGeometry(QtCore.QRect(160, 440, 221, 40))
        self.add_files_button_posts.setStyleSheet("\n"
"*{\n"
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
":pressed {\n"
"    border-style: inset;\n"
"    border: 1px solid  #4F4F4F;\n"
"color: #4F4F4F;\n"
"background: #FFFFFF;\n"
"}\n"
"/* Inside auto layout */\n"
"\n"
"")
        self.add_files_button_posts.setObjectName("add_files_button_posts")
        self.close_button_create_posts = QtWidgets.QPushButton(self.create_posts_frame)
        self.close_button_create_posts.setGeometry(QtCore.QRect(490, 10, 40, 40))
        self.close_button_create_posts.setStyleSheet("*{border-radius:0px;}\n"
":pressed{\n"
"    border: 3px solid  #FF0000;\n"
"boder:10px;\n"
"border-radius: 8px;\n"
"}")
        self.close_button_create_posts.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/x-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button_create_posts.setIcon(icon)
        self.close_button_create_posts.setIconSize(QtCore.QSize(40, 40))
        self.close_button_create_posts.setObjectName("close_button_create_posts")
        self.gridLayout.addWidget(self.create_posts_frame, 0, 0, 1, 1)

        self.retranslateUi(create_posts_form)
        QtCore.QMetaObject.connectSlotsByName(create_posts_form)

    def retranslateUi(self, create_posts_form):
        _translate = QtCore.QCoreApplication.translate
        create_posts_form.setWindowTitle(_translate("create_posts_form", "Form"))
        self.post_heading_posts.setText(_translate("create_posts_form", "Create Post"))
        self.description_label_posts.setText(_translate("create_posts_form", "Description"))
        self.label_4.setText(_translate("create_posts_form", "Heading"))
        self.label_5.setText(_translate("create_posts_form", "File Name: "))
        self.add_files_button_posts.setText(_translate("create_posts_form", "Add Files"))
