# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\tejas\Desktop\22-01-22\root_copy.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1094, 658)
        MainWindow.setMinimumSize(QtCore.QSize(1094, 658))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(1081, 607))
        self.centralwidget.setObjectName("centralwidget")
        self.up_outer_frame = QtWidgets.QFrame(self.centralwidget)
        self.up_outer_frame.setGeometry(QtCore.QRect(11, 11, 1081, 601))
        self.up_outer_frame.setMinimumSize(QtCore.QSize(1081, 601))
        self.up_outer_frame.setMaximumSize(QtCore.QSize(1081, 601))
        self.up_outer_frame.setStyleSheet("background:white;")
        self.up_outer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.up_outer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.up_outer_frame.setObjectName("up_outer_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.up_outer_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.up_inner_frame = QtWidgets.QFrame(self.up_outer_frame)
        self.up_inner_frame.setMaximumSize(QtCore.QSize(445, 650))
        self.up_inner_frame.setStyleSheet("#up_inner_frame{/* Auto layout */\n"
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
        self.up_inner_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.up_inner_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.up_inner_frame.setObjectName("up_inner_frame")
        self.up_heading_label = QtWidgets.QLabel(self.up_inner_frame)
        self.up_heading_label.setGeometry(QtCore.QRect(10, 0, 81, 30))
        self.up_heading_label.setStyleSheet("position: absolute;\n"
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
        self.up_heading_label.setObjectName("up_heading_label")
        self.up_name_frame = QtWidgets.QFrame(self.up_inner_frame)
        self.up_name_frame.setGeometry(QtCore.QRect(1, 60, 443, 80))
        self.up_name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.up_name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.up_name_frame.setObjectName("up_name_frame")
        self.up_name_label = QtWidgets.QLabel(self.up_name_frame)
        self.up_name_label.setGeometry(QtCore.QRect(20, 5, 141, 21))
        font = QtGui.QFont()
        font.setFamily("poppins")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.up_name_label.setFont(font)
        self.up_name_label.setStyleSheet("position: absolute;\n"
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
        self.up_name_label.setObjectName("up_name_label")
        self.up_name_entry = QtWidgets.QLineEdit(self.up_name_frame)
        self.up_name_entry.setGeometry(QtCore.QRect(10, 30, 425, 40))
        self.up_name_entry.setStyleSheet("position: static;\n"
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
"font-family: poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"\n"
"")
        self.up_name_entry.setText("")
        self.up_name_entry.setObjectName("up_name_entry")
        self.username_frame = QtWidgets.QFrame(self.up_inner_frame)
        self.username_frame.setEnabled(True)
        self.username_frame.setGeometry(QtCore.QRect(1, 140, 443, 80))
        self.username_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.username_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.username_frame.setObjectName("username_frame")
        self.up_username_label = QtWidgets.QLabel(self.username_frame)
        self.up_username_label.setGeometry(QtCore.QRect(20, 5, 141, 21))
        self.up_username_label.setStyleSheet("position: absolute;\n"
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
        self.up_username_label.setObjectName("up_username_label")
        self.up_username_entry = QtWidgets.QLineEdit(self.username_frame)
        self.up_username_entry.setGeometry(QtCore.QRect(10, 30, 425, 40))
        self.up_username_entry.setStyleSheet("position: static;\n"
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
"font-family: poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"\n"
"")
        self.up_username_entry.setObjectName("up_username_entry")
        self.up_email_frame = QtWidgets.QFrame(self.up_inner_frame)
        self.up_email_frame.setGeometry(QtCore.QRect(1, 220, 443, 80))
        self.up_email_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.up_email_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.up_email_frame.setObjectName("up_email_frame")
        self.up_email_label = QtWidgets.QLabel(self.up_email_frame)
        self.up_email_label.setGeometry(QtCore.QRect(20, 0, 411, 31))
        self.up_email_label.setStyleSheet("position: absolute;\n"
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
        self.up_email_label.setObjectName("up_email_label")
        self.up_email_entry = QtWidgets.QLineEdit(self.up_email_frame)
        self.up_email_entry.setGeometry(QtCore.QRect(10, 30, 425, 40))
        self.up_email_entry.setStyleSheet("font-family: poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"position: static;\n"
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
        self.up_email_entry.setObjectName("up_email_entry")
        self.up_password_frame = QtWidgets.QFrame(self.up_inner_frame)
        self.up_password_frame.setGeometry(QtCore.QRect(1, 300, 443, 80))
        self.up_password_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.up_password_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.up_password_frame.setObjectName("up_password_frame")
        self.up_password_label = QtWidgets.QLabel(self.up_password_frame)
        self.up_password_label.setGeometry(QtCore.QRect(20, 5, 141, 21))
        self.up_password_label.setStyleSheet("position: absolute;\n"
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
        self.up_password_label.setObjectName("up_password_label")
        self.up_password_entry = QtWidgets.QLineEdit(self.up_password_frame)
        self.up_password_entry.setGeometry(QtCore.QRect(10, 30, 425, 40))
        self.up_password_entry.setStyleSheet("\n"
"font-family: poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"position: static;\n"
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
        self.up_password_entry.setObjectName("up_password_entry")
        self.up_warning_label = QtWidgets.QLabel(self.up_inner_frame)
        self.up_warning_label.setGeometry(QtCore.QRect(10, 35, 421, 21))
        self.up_warning_label.setStyleSheet("position: absolute;\n"
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
        self.up_warning_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.up_warning_label.setObjectName("up_warning_label")
        self.up_confirm_password_frame = QtWidgets.QFrame(self.up_inner_frame)
        self.up_confirm_password_frame.setGeometry(QtCore.QRect(1, 380, 443, 80))
        self.up_confirm_password_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.up_confirm_password_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.up_confirm_password_frame.setObjectName("up_confirm_password_frame")
        self.up_confirm_password_label = QtWidgets.QLabel(self.up_confirm_password_frame)
        self.up_confirm_password_label.setGeometry(QtCore.QRect(20, 5, 141, 21))
        self.up_confirm_password_label.setStyleSheet("position: absolute;\n"
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
        self.up_confirm_password_label.setObjectName("up_confirm_password_label")
        self.up_confirm_password_entry = QtWidgets.QLineEdit(self.up_confirm_password_frame)
        self.up_confirm_password_entry.setGeometry(QtCore.QRect(10, 30, 425, 40))
        self.up_confirm_password_entry.setStyleSheet("font-family: poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 14px;\n"
"position: static;\n"
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
        self.up_confirm_password_entry.setObjectName("up_confirm_password_entry")
        self.up_sign_up_button = QtWidgets.QPushButton(self.up_inner_frame)
        self.up_sign_up_button.setGeometry(QtCore.QRect(10, 470, 425, 40))
        self.up_sign_up_button.setStyleSheet("\n"
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
        self.up_sign_up_button.setObjectName("up_sign_up_button")
        self.up_sign_in_button = QtWidgets.QPushButton(self.up_inner_frame)
        self.up_sign_in_button.setGeometry(QtCore.QRect(10, 520, 425, 40))
        self.up_sign_in_button.setStyleSheet("\n"
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
"\n"
"    border-style: inset;\n"
"    border: 1px solid  #4F4F4F;\n"
"color: #4F4F4F;\n"
"background: #FFFFFF;\n"
"border-radius:10px;\n"
"}\n"
"\n"
":pressed {\n"
"    border-style: inset;\n"
"    color: white;\n"
"background: #4F4F4F;\n"
"border-radius: 8px;\n"
"}\n"
"/* Inside auto layout */\n"
"\n"
"")
        self.up_sign_in_button.setObjectName("up_sign_in_button")
        self.gridLayout_2.addWidget(self.up_inner_frame, 0, 0, 1, 1)
        self.in_outer_frame = QtWidgets.QFrame(self.centralwidget)
        self.in_outer_frame.setGeometry(QtCore.QRect(10, 10, 1081, 601))
        self.in_outer_frame.setMinimumSize(QtCore.QSize(1081, 601))
        self.in_outer_frame.setMaximumSize(QtCore.QSize(1081, 601))
        self.in_outer_frame.setStyleSheet("background:white;")
        self.in_outer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.in_outer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.in_outer_frame.setObjectName("in_outer_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.in_outer_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.in_inner_frame = QtWidgets.QFrame(self.in_outer_frame)
        self.in_inner_frame.setMinimumSize(QtCore.QSize(460, 410))
        self.in_inner_frame.setMaximumSize(QtCore.QSize(460, 410))
        self.in_inner_frame.setStyleSheet("#in_inner_frame{/* Auto layout */\n"
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
        self.in_inner_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.in_inner_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.in_inner_frame.setObjectName("in_inner_frame")
        self.static_in_heading = QtWidgets.QLabel(self.in_inner_frame)
        self.static_in_heading.setGeometry(QtCore.QRect(10, 10, 81, 30))
        self.static_in_heading.setStyleSheet("position: absolute;\n"
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
        self.static_in_heading.setObjectName("static_in_heading")
        self.in_email_frame = QtWidgets.QFrame(self.in_inner_frame)
        self.in_email_frame.setGeometry(QtCore.QRect(1, 80, 457, 80))
        self.in_email_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.in_email_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.in_email_frame.setObjectName("in_email_frame")
        self.in_email_label = QtWidgets.QLabel(self.in_email_frame)
        self.in_email_label.setGeometry(QtCore.QRect(20, 0, 425, 31))
        self.in_email_label.setStyleSheet("position: absolute;\n"
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
        self.in_email_label.setObjectName("in_email_label")
        self.in_email_entry = QtWidgets.QLineEdit(self.in_email_frame)
        self.in_email_entry.setGeometry(QtCore.QRect(15, 30, 430, 40))
        self.in_email_entry.setStyleSheet("position: static;\n"
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
        self.in_email_entry.setObjectName("in_email_entry")
        self.in_password_frame = QtWidgets.QFrame(self.in_inner_frame)
        self.in_password_frame.setGeometry(QtCore.QRect(1, 180, 457, 80))
        self.in_password_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.in_password_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.in_password_frame.setObjectName("in_password_frame")
        self.in_password_label = QtWidgets.QLabel(self.in_password_frame)
        self.in_password_label.setGeometry(QtCore.QRect(20, 5, 141, 21))
        self.in_password_label.setStyleSheet("position: absolute;\n"
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
        self.in_password_label.setObjectName("in_password_label")
        self.in_password_entry = QtWidgets.QLineEdit(self.in_password_frame)
        self.in_password_entry.setGeometry(QtCore.QRect(15, 30, 430, 40))
        self.in_password_entry.setStyleSheet("position: static;\n"
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
        self.in_password_entry.setObjectName("in_password_entry")
        self.in_sign_in_button = QtWidgets.QPushButton(self.in_inner_frame)
        self.in_sign_in_button.setGeometry(QtCore.QRect(15, 290, 430, 40))
        self.in_sign_in_button.setStyleSheet("\n"
"*{font-family: Inter;\n"
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
":pressed {\n"
"    border-style: inset;\n"
"    border: 1px solid  #4F4F4F;\n"
"color: #4F4F4F;\n"
"background: #FFFFFF;\n"
"}\n"
"/* Inside auto layout */\n"
"\n"
"")
        self.in_sign_in_button.setObjectName("in_sign_in_button")
        self.in_sign_up_button = QtWidgets.QPushButton(self.in_inner_frame)
        self.in_sign_up_button.setGeometry(QtCore.QRect(15, 350, 430, 40))
        self.in_sign_up_button.setStyleSheet("\n"
"*{font-family: Inter;\n"
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
":pressed {\n"
"    border-style: inset;\n"
"    color: white;\n"
"background: #4F4F4F;\n"
"border-radius: 8px;\n"
"}\n"
"/* Inside auto layout */\n"
"\n"
"")
        self.in_sign_up_button.setObjectName("in_sign_up_button")
        self.in_warning_label = QtWidgets.QLabel(self.in_inner_frame)
        self.in_warning_label.setGeometry(QtCore.QRect(10, 40, 421, 41))
        self.in_warning_label.setStyleSheet("position: absolute;\n"
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
        self.in_warning_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.in_warning_label.setObjectName("in_warning_label")
        self.gridLayout_3.addWidget(self.in_inner_frame, 0, 0, 1, 1)
        self.main_class_framework = QtWidgets.QFrame(self.centralwidget)
        self.main_class_framework.setGeometry(QtCore.QRect(0, 0, 1081, 601))
        self.main_class_framework.setStyleSheet("background:white;")
        self.main_class_framework.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_class_framework.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_class_framework.setObjectName("main_class_framework")
        self.class_name_frame = QtWidgets.QFrame(self.main_class_framework)
        self.class_name_frame.setGeometry(QtCore.QRect(269, 20, 541, 101))
        self.class_name_frame.setStyleSheet("#class_name_frame{position: absolute;\n"
"left: 435px;\n"
"right: 429px;\n"
"top: 119px;\n"
"bottom: 756px;\n"
"\n"
"background: rgba(118, 158, 161, 0.4);\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 10px;}")
        self.class_name_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.class_name_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.class_name_frame.setObjectName("class_name_frame")
        self.class_name_label_dynamic = QtWidgets.QLabel(self.class_name_frame)
        self.class_name_label_dynamic.setGeometry(QtCore.QRect(10, 0, 521, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.class_name_label_dynamic.setFont(font)
        self.class_name_label_dynamic.setStyleSheet("#class_name_label_dynamic{\n"
"/* ADA */\n"
"\n"
"\n"
"position: absolute;\n"
"width: 266px;\n"
"height: 61px;\n"
"left: 26px;\n"
"top: 21px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: bold;\n"
"font-size: 25px;\n"
"line-height: 61px;\n"
"letter-spacing: 0.05em;\n"
"\n"
"color: #FFFFFF;\n"
"background:rgba(118, 158, 161, 0.01);\n"
"}")
        self.class_name_label_dynamic.setObjectName("class_name_label_dynamic")
        self.class_description_label_dynamic = QtWidgets.QLabel(self.class_name_frame)
        self.class_description_label_dynamic.setGeometry(QtCore.QRect(10, 40, 521, 51))
        self.class_description_label_dynamic.setStyleSheet("#class_description_label_dynamic\n"
"{\n"
"/* ADA */\n"
"\n"
"\n"
"position: absolute;\n"
"width: 266px;\n"
"height: 61px;\n"
"left: 26px;\n"
"top: 21px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 15px;\n"
"line-height: 61px;\n"
"letter-spacing: 0.05em;\n"
"\n"
"color: #000000;\n"
"background:rgba(118, 158, 161, 0.01);\n"
"\n"
"\n"
"}")
        self.class_description_label_dynamic.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.class_description_label_dynamic.setWordWrap(True)
        self.class_description_label_dynamic.setObjectName("class_description_label_dynamic")
        self.posts_scroll_area = QtWidgets.QScrollArea(self.main_class_framework)
        self.posts_scroll_area.setGeometry(QtCore.QRect(269, 129, 541, 471))
        self.posts_scroll_area.setStyleSheet("#posts_scroll_area{\n"
"width: 1056px;\n"
"height: 710px;\n"
"left: 438px;\n"
"top: 343px;\n"
"\n"
"background: #FFFFFF;\n"
"mix-blend-mode: hard-light;\n"
"border-radius: 10px;}")
        self.posts_scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.posts_scroll_area.setWidgetResizable(True)
        self.posts_scroll_area.setObjectName("posts_scroll_area")
        self.posts_scroll_area_widget = QtWidgets.QWidget()
        self.posts_scroll_area_widget.setGeometry(QtCore.QRect(0, 0, 520, 471))
        self.posts_scroll_area_widget.setStyleSheet("#posts_scroll_area_widget{\n"
"\n"
"width: 1056px;\n"
"height: 710px;\n"
"left: 438px;\n"
"top: 343px;\n"
"\n"
"background: #FFFFFF;\n"
"mix-blend-mode: hard-light;\n"
"border-radius: 10px;}")
        self.posts_scroll_area_widget.setObjectName("posts_scroll_area_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.posts_scroll_area_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.posts_scroll_area.setWidget(self.posts_scroll_area_widget)
        self.static_events = QtWidgets.QLabel(self.main_class_framework)
        self.static_events.setGeometry(QtCore.QRect(10, 20, 251, 51))
        self.static_events.setStyleSheet("position: absolute;\n"
"width: 143px;\n"
"height: 62px;\n"
"left: 133px;\n"
"top: 44px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;\n"
"line-height: 61px;\n"
"/* identical to box height */\n"
"\n"
"text-align: center;\n"
"letter-spacing: 0.05em;\n"
"\n"
"color: #000000;\n"
"position: absolute;\n"
"width: 409px;\n"
"left: 12px;\n"
"top: 119px;\n"
"bottom: 9px;\n"
"\n"
"background: rgba(209, 233, 215, 0.6);\n"
"backdrop-filter: blur(4px);\n"
"/* Note: backdrop-filter has minimal browser support */\n"
"\n"
"border-radius: 10px;\n"
"")
        self.static_events.setAlignment(QtCore.Qt.AlignCenter)
        self.static_events.setObjectName("static_events")
        self.events_scroll_area = QtWidgets.QScrollArea(self.main_class_framework)
        self.events_scroll_area.setGeometry(QtCore.QRect(10, 80, 251, 521))
        self.events_scroll_area.setStyleSheet("#events_scroll_area{\n"
"text-align: center;\n"
"letter-spacing: 0.05em;\n"
"\n"
"color: #000000;\n"
"position: absolute;\n"
"width: 409px;\n"
"left: 12px;\n"
"top: 119px;\n"
"bottom: 9px;\n"
"\n"
"background: rgba(209, 233, 215, 0.6);\n"
"backdrop-filter: blur(4px);\n"
"/* Note: backdrop-filter has minimal browser support */\n"
"\n"
"border-radius: 10;\n"
"}")
        self.events_scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.events_scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.events_scroll_area.setWidgetResizable(True)
        self.events_scroll_area.setObjectName("events_scroll_area")
        self.events_scroll_area_widget = QtWidgets.QWidget()
        self.events_scroll_area_widget.setGeometry(QtCore.QRect(0, 0, 251, 521))
        self.events_scroll_area_widget.setStyleSheet("text-align: center;\n"
"letter-spacing: 0.05em;\n"
"\n"
"color: #000000;\n"
"position: absolute;\n"
"width: 409px;\n"
"left: 12px;\n"
"top: 119px;\n"
"bottom: 9px;\n"
"\n"
"background: rgba(209, 233, 215, 0.01);\n"
"backdrop-filter: blur(4px);\n"
"/* Note: backdrop-filter has minimal browser support */\n"
"\n"
"border-radius: 10px;\n"
"")
        self.events_scroll_area_widget.setObjectName("events_scroll_area_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.events_scroll_area_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.events_scroll_area.setWidget(self.events_scroll_area_widget)
        self.static_assignment = QtWidgets.QLabel(self.main_class_framework)
        self.static_assignment.setGeometry(QtCore.QRect(820, 20, 251, 51))
        self.static_assignment.setStyleSheet("position: absolute;\n"
"width: 143px;\n"
"height: 62px;\n"
"left: 133px;\n"
"top: 44px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;\n"
"line-height: 61px;\n"
"/* identical to box height */\n"
"\n"
"text-align: center;\n"
"letter-spacing: 0.05em;\n"
"\n"
"color: #000000;\n"
"position: absolute;\n"
"width: 409px;\n"
"left: 12px;\n"
"top: 119px;\n"
"bottom: 9px;\n"
"\n"
"background: rgba(252, 202, 201, 0.6);\n"
"backdrop-filter: blur(4px);\n"
"/* Note: backdrop-filter has minimal browser support */\n"
"\n"
"border-radius: 10px;\n"
"")
        self.static_assignment.setAlignment(QtCore.Qt.AlignCenter)
        self.static_assignment.setObjectName("static_assignment")
        self.assign_scroll_area = QtWidgets.QScrollArea(self.main_class_framework)
        self.assign_scroll_area.setGeometry(QtCore.QRect(820, 80, 251, 521))
        self.assign_scroll_area.setStyleSheet("#assign_scroll_area{\n"
"text-align: center;\n"
"letter-spacing: 0.05em;\n"
"\n"
"color: #000000;\n"
"position: absolute;\n"
"width: 409px;\n"
"left: 12px;\n"
"top: 119px;\n"
"bottom: 9px;\n"
"\n"
"background:rgba(252, 202, 201, 0.6);\n"
"backdrop-filter: blur(4px);\n"
"/* Note: backdrop-filter has minimal browser support */\n"
"\n"
"border-radius: 10;\n"
"}")
        self.assign_scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.assign_scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.assign_scroll_area.setWidgetResizable(True)
        self.assign_scroll_area.setObjectName("assign_scroll_area")
        self.assign_scroll_area_widget = QtWidgets.QWidget()
        self.assign_scroll_area_widget.setGeometry(QtCore.QRect(0, 0, 251, 521))
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
        self.assign_scroll_area.setWidget(self.assign_scroll_area_widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1094, 26))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setObjectName("menubar")
        self.menuUser = QtWidgets.QMenu(self.menubar)
        self.menuUser.setObjectName("menuUser")
        self.menuViews = QtWidgets.QMenu(self.menubar)
        self.menuViews.setObjectName("menuViews")
        self.menuAdmin = QtWidgets.QMenu(self.menubar)
        self.menuAdmin.setObjectName("menuAdmin")
        self.menuClub = QtWidgets.QMenu(self.menubar)
        self.menuClub.setObjectName("menuClub")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSignUp = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/user-plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSignUp.setIcon(icon)
        self.actionSignUp.setObjectName("actionSignUp")
        self.actionSignIn = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSignIn.setIcon(icon1)
        self.actionSignIn.setObjectName("actionSignIn")
        self.actionLogOut = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLogOut.setIcon(icon2)
        self.actionLogOut.setObjectName("actionLogOut")
        self.actionClasses = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/users.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClasses.setIcon(icon3)
        self.actionClasses.setObjectName("actionClasses")
        self.actionEvents = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/calendar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEvents.setIcon(icon4)
        self.actionEvents.setObjectName("actionEvents")
        self.actionAssignments = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/tag.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAssignments.setIcon(icon5)
        self.actionAssignments.setObjectName("actionAssignments")
        self.actionCreatePost = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/plus-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreatePost.setIcon(icon6)
        self.actionCreatePost.setObjectName("actionCreatePost")
        self.actionCreateAssignment = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/file-plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreateAssignment.setIcon(icon7)
        self.actionCreateAssignment.setObjectName("actionCreateAssignment")
        self.actionViewAssignment = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/eye.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionViewAssignment.setIcon(icon8)
        self.actionViewAssignment.setObjectName("actionViewAssignment")
        self.actionViewClasses = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/trello.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionViewClasses.setIcon(icon9)
        self.actionViewClasses.setObjectName("actionViewClasses")
        self.actionEvents_2 = QtWidgets.QAction(MainWindow)
        self.actionEvents_2.setObjectName("actionEvents_2")
        self.actionClubs = QtWidgets.QAction(MainWindow)
        self.actionClubs.setObjectName("actionClubs")
        self.menuUser.addAction(self.actionSignUp)
        self.menuUser.addSeparator()
        self.menuUser.addAction(self.actionSignIn)
        self.menuUser.addSeparator()
        self.menuUser.addAction(self.actionLogOut)
        self.menuUser.addSeparator()
        self.menuViews.addAction(self.actionClasses)
        self.menuViews.addSeparator()
        self.menuViews.addAction(self.actionEvents)
        self.menuViews.addSeparator()
        self.menuViews.addAction(self.actionAssignments)
        self.menuAdmin.addAction(self.actionCreatePost)
        self.menuAdmin.addAction(self.actionCreateAssignment)
        self.menuAdmin.addAction(self.actionViewAssignment)
        self.menuAdmin.addAction(self.actionViewClasses)
        self.menuClub.addAction(self.actionEvents_2)
        self.menuClub.addAction(self.actionClubs)
        self.menubar.addAction(self.menuUser.menuAction())
        self.menubar.addAction(self.menuViews.menuAction())
        self.menubar.addAction(self.menuAdmin.menuAction())
        self.menubar.addAction(self.menuClub.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.up_heading_label.setText(_translate("MainWindow", "Sign Up"))
        self.up_name_label.setText(_translate("MainWindow", "Name"))
        self.up_username_label.setText(_translate("MainWindow", "Username"))
        self.up_email_label.setText(_translate("MainWindow", "Email Id"))
        self.up_password_label.setText(_translate("MainWindow", "Password"))
        self.up_warning_label.setText(_translate("MainWindow", "Please enter your details to continue."))
        self.up_confirm_password_label.setText(_translate("MainWindow", "Confirm Password"))
        self.up_sign_up_button.setText(_translate("MainWindow", "Sign Up"))
        self.up_sign_in_button.setText(_translate("MainWindow", "Already a user? Sign In"))
        self.static_in_heading.setText(_translate("MainWindow", "Sign In"))
        self.in_email_label.setText(_translate("MainWindow", "Email Id"))
        self.in_password_label.setText(_translate("MainWindow", "Password"))
        self.in_sign_in_button.setText(_translate("MainWindow", "Sign In"))
        self.in_sign_up_button.setText(_translate("MainWindow", "New user? Sign Up"))
        self.in_warning_label.setText(_translate("MainWindow", "Please enter your details to continue."))
        self.class_name_label_dynamic.setText(_translate("MainWindow", "Class Name"))
        self.class_description_label_dynamic.setText(_translate("MainWindow", "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec."))
        self.static_events.setText(_translate("MainWindow", "Events"))
        self.static_assignment.setText(_translate("MainWindow", "Assignments"))
        self.menuUser.setTitle(_translate("MainWindow", "User"))
        self.menuViews.setTitle(_translate("MainWindow", "Views"))
        self.menuAdmin.setTitle(_translate("MainWindow", "Admin"))
        self.menuClub.setTitle(_translate("MainWindow", "Club"))
        self.actionSignUp.setText(_translate("MainWindow", "Sign Up"))
        self.actionSignIn.setText(_translate("MainWindow", "Log In"))
        self.actionLogOut.setText(_translate("MainWindow", "Log Out"))
        self.actionClasses.setText(_translate("MainWindow", "Classes"))
        self.actionEvents.setText(_translate("MainWindow", "Events"))
        self.actionAssignments.setText(_translate("MainWindow", "Assignments"))
        self.actionCreatePost.setText(_translate("MainWindow", "Create Post"))
        self.actionCreateAssignment.setText(_translate("MainWindow", "Create Assignment"))
        self.actionViewAssignment.setText(_translate("MainWindow", "View Assignment"))
        self.actionViewClasses.setText(_translate("MainWindow", "View Classes"))
        self.actionEvents_2.setText(_translate("MainWindow", "Events"))
        self.actionClubs.setText(_translate("MainWindow", "Clubs"))
