# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\tejas\Desktop\22-01-22\assignments.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(563, 651)
        Form.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.assign_scroll_area = QtWidgets.QScrollArea(Form)
        self.assign_scroll_area.setMinimumSize(QtCore.QSize(539, 231))
        self.assign_scroll_area.setMaximumSize(QtCore.QSize(539, 231))
        self.assign_scroll_area.setStyleSheet("background: #FFFFFF;\n"
"border-radius: 8px;")
        self.assign_scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.assign_scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.assign_scroll_area.setWidgetResizable(True)
        self.assign_scroll_area.setObjectName("assign_scroll_area")
        self.assign_scroll_area_widget = QtWidgets.QWidget()
        self.assign_scroll_area_widget.setGeometry(QtCore.QRect(0, 0, 539, 323))
        self.assign_scroll_area_widget.setStyleSheet("text-align: center;\n"
"letter-spacing: 0.05em;\n"
"\n"
"color: #000000;\n"
"position: absolute;\n"
"width: 409px;\n"
"left: 12px;\n"
"top: 119px;\n"
"bottom: 9px;\n"
"\n"
"background: rgba(252, 202, 201, 0.01);\n"
"backdrop-filter: blur(4px);\n"
"/* Note: backdrop-filter has minimal browser support */\n"
"\n"
"border-radius: 10px;\n"
"")
        self.assign_scroll_area_widget.setObjectName("assign_scroll_area_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.assign_scroll_area_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.events_view_2 = QtWidgets.QFrame(self.assign_scroll_area_widget)
        self.events_view_2.setMinimumSize(QtCore.QSize(0, 70))
        self.events_view_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.events_view_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.events_view_2.setStyleSheet("#events_view_2{\n"
"position: absolute;\n"
"width: 370px;\n"
"height: 110px;\n"
"left: 7px;\n"
"top: 28px;\n"
"\n"
"background: rgba(0, 0, 0, 0.05);\n"
"border: 1px solid rgba(0, 0, 0, 0.3);\n"
"box-sizing: border-box;\n"
"border-radius: 10px}")
        self.events_view_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.events_view_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.events_view_2.setObjectName("events_view_2")
        self.label_8 = QtWidgets.QLabel(self.events_view_2)
        self.label_8.setGeometry(QtCore.QRect(10, 0, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_8.setStyleSheet("position: absolute;\n"
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
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.events_view_2)
        self.label_9.setGeometry(QtCore.QRect(10, 40, 441, 21))
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_9.setStyleSheet("position: absolute;\n"
"left: 20px;\n"
"right: 30px;\n"
"top: 10px;\n"
"bottom: 10px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 37px;\n"
"letter-spacing: 0.05em;\n"
"background: rgba(0, 0, 0, 0.01);\n"
"color: #000000;")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.events_view_2)
        self.events_view_5 = QtWidgets.QFrame(self.assign_scroll_area_widget)
        self.events_view_5.setMinimumSize(QtCore.QSize(0, 70))
        self.events_view_5.setMaximumSize(QtCore.QSize(16777215, 70))
        self.events_view_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.events_view_5.setStyleSheet("#events_view_2{\n"
"position: absolute;\n"
"width: 370px;\n"
"height: 110px;\n"
"left: 7px;\n"
"top: 28px;\n"
"\n"
"background: rgba(0, 0, 0, 0.05);\n"
"border: 1px solid rgba(0, 0, 0, 0.3);\n"
"box-sizing: border-box;\n"
"border-radius: 10px}")
        self.events_view_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.events_view_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.events_view_5.setObjectName("events_view_5")
        self.label_14 = QtWidgets.QLabel(self.events_view_5)
        self.label_14.setGeometry(QtCore.QRect(10, 0, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_14.setStyleSheet("position: absolute;\n"
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
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.events_view_5)
        self.label_15.setGeometry(QtCore.QRect(10, 40, 441, 21))
        self.label_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_15.setStyleSheet("position: absolute;\n"
"left: 20px;\n"
"right: 30px;\n"
"top: 10px;\n"
"bottom: 10px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 37px;\n"
"letter-spacing: 0.05em;\n"
"background: rgba(0, 0, 0, 0.01);\n"
"color: #000000;")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.events_view_5)
        self.events_view_6 = QtWidgets.QFrame(self.assign_scroll_area_widget)
        self.events_view_6.setMinimumSize(QtCore.QSize(0, 70))
        self.events_view_6.setMaximumSize(QtCore.QSize(16777215, 70))
        self.events_view_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.events_view_6.setStyleSheet("#events_view_3{\n"
"position: absolute;\n"
"width: 370px;\n"
"height: 110px;\n"
"left: 7px;\n"
"top: 28px;\n"
"\n"
"background: rgba(0, 0, 0, 0.05);\n"
"border: 1px solid rgba(0, 0, 0, 0.3);\n"
"box-sizing: border-box;\n"
"border-radius: 10px}")
        self.events_view_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.events_view_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.events_view_6.setObjectName("events_view_6")
        self.label_16 = QtWidgets.QLabel(self.events_view_6)
        self.label_16.setGeometry(QtCore.QRect(10, 0, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_16.setStyleSheet("position: absolute;\n"
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
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.events_view_6)
        self.label_17.setGeometry(QtCore.QRect(10, 40, 441, 21))
        self.label_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_17.setStyleSheet("position: absolute;\n"
"left: 20px;\n"
"right: 30px;\n"
"top: 10px;\n"
"bottom: 10px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 37px;\n"
"letter-spacing: 0.05em;\n"
"background: rgba(0, 0, 0, 0.01);\n"
"color: #000000;")
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_3.addWidget(self.events_view_6)
        self.events_view_3 = QtWidgets.QFrame(self.assign_scroll_area_widget)
        self.events_view_3.setMinimumSize(QtCore.QSize(0, 70))
        self.events_view_3.setMaximumSize(QtCore.QSize(16777215, 70))
        self.events_view_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.events_view_3.setStyleSheet("#events_view_3{\n"
"position: absolute;\n"
"width: 370px;\n"
"height: 110px;\n"
"left: 7px;\n"
"top: 28px;\n"
"\n"
"background: rgba(0, 0, 0, 0.05);\n"
"border: 1px solid rgba(0, 0, 0, 0.3);\n"
"box-sizing: border-box;\n"
"border-radius: 10px}")
        self.events_view_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.events_view_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.events_view_3.setObjectName("events_view_3")
        self.label_10 = QtWidgets.QLabel(self.events_view_3)
        self.label_10.setGeometry(QtCore.QRect(10, 0, 431, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_10.setStyleSheet("position: absolute;\n"
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
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.events_view_3)
        self.label_11.setGeometry(QtCore.QRect(10, 40, 441, 21))
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_11.setStyleSheet("position: absolute;\n"
"left: 20px;\n"
"right: 30px;\n"
"top: 10px;\n"
"bottom: 10px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 37px;\n"
"letter-spacing: 0.05em;\n"
"background: rgba(0, 0, 0, 0.01);\n"
"color: #000000;")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.events_view_3)
        self.assign_scroll_area.setWidget(self.assign_scroll_area_widget)
        self.gridLayout.addWidget(self.assign_scroll_area, 1, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setMinimumSize(QtCore.QSize(541, 351))
        self.frame_2.setMaximumSize(QtCore.QSize(541, 351))
        self.frame_2.setStyleSheet("#frame_2{/* Auto layout */\n"
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
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.post_heading_posts = QtWidgets.QLabel(self.frame_2)
        self.post_heading_posts.setGeometry(QtCore.QRect(20, 20, 511, 31))
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
        self.des = QtWidgets.QLabel(self.frame_2)
        self.des.setGeometry(QtCore.QRect(20, 90, 511, 131))
        self.des.setMaximumSize(QtCore.QSize(511, 16777215))
        self.des.setStyleSheet("background: rgba(196, 196, 196, 0.1);\n"
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
        self.des.setScaledContents(False)
        self.des.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.des.setWordWrap(True)
        self.des.setObjectName("des")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(20, 310, 111, 31))
        self.label.setStyleSheet("font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 30px;\n"
"/* identical to box height */\n"
"\n"
"letter-spacing: 0.05em;\n"
"text-transform: capitalize;\n"
"")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(412, 310, 121, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(152, 310, 251, 31))
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
"border: 2px solid #4F4F4F;\n"
"box-sizing: border-box;\n"
"border-radius: 7px;\n"
"\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 230, 511, 31))
        self.label_2.setStyleSheet("font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 30px;\n"
"/* identical to box height */\n"
"\n"
"letter-spacing: 0.05em;\n"
"text-transform: capitalize;\n"
"")
        self.label_2.setObjectName("label_2")
        self.submit_button_assignment = QtWidgets.QPushButton(self.frame_2)
        self.submit_button_assignment.setGeometry(QtCore.QRect(180, 260, 191, 31))
        self.submit_button_assignment.setStyleSheet("#submit_button_assignment{\n"
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
"#submit_button_assignment:pressed {\n"
"    border-style: inset;\n"
"    border: 1px solid  #4F4F4F;\n"
"color: #4F4F4F;\n"
"background: #FFFFFF;\n"
"}\n"
"/* Inside auto layout */\n"
"\n"
"")
        self.submit_button_assignment.setObjectName("submit_button_assignment")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 361, 16))
        self.label_3.setStyleSheet("font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 13px;\n"
"line-height: 30px;\n"
"/* identical to box height */\n"
"\n"
"letter-spacing: 0.05em;\n"
"text-transform: capitalize;\n"
"")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_8.setText(_translate("Form", "Comment"))
        self.label_9.setText(_translate("Form", "User"))
        self.label_14.setText(_translate("Form", "Comment"))
        self.label_15.setText(_translate("Form", "User"))
        self.label_16.setText(_translate("Form", "Comment"))
        self.label_17.setText(_translate("Form", "User"))
        self.label_10.setText(_translate("Form", "Comment"))
        self.label_11.setText(_translate("Form", "User"))
        self.post_heading_posts.setText(_translate("Form", "Assignment Heading"))
        self.des.setText(_translate("Form", "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec."))
        self.label.setText(_translate("Form", "Comments 🔽"))
        self.pushButton.setText(_translate("Form", "Add comment"))
        self.label_2.setText(_translate("Form", "Files: "))
        self.submit_button_assignment.setText(_translate("Form", "Submit"))
        self.label_3.setText(_translate("Form", "Last Date:"))
