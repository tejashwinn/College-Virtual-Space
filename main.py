# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1079, 658)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.heading_frame = QtWidgets.QFrame(self.centralwidget)
        self.heading_frame.setGeometry(QtCore.QRect(10, 10, 1061, 41))
        self.heading_frame.setStyleSheet("position: absolute;\n"
"width: 1895px;\n"
"height: 81px;\n"
"left: 12px;\n"
"top: 15px;\n"
"\n"
"border-radius: 10px;")
        self.heading_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.heading_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.heading_frame.setObjectName("heading_frame")
        self.label_2 = QtWidgets.QLabel(self.heading_frame)
        self.label_2.setGeometry(QtCore.QRect(0, 5, 1061, 31))
        self.label_2.setStyleSheet("position: absolute;\n"
"width: 572px;\n"
"height: 48px;\n"
"left: 680px;\n"
"top: 6px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 35px;\n"
"line-height: 61px;\n"
"text-align: center;\n"
"letter-spacing: 0.07em;\n"
"text-transform: uppercase;\n"
"\n"
"text-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(-1, 49, 1081, 611))
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.class_name_frame = QtWidgets.QFrame(self.main_frame)
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
        self.class_name_label = QtWidgets.QLabel(self.class_name_frame)
        self.class_name_label.setGeometry(QtCore.QRect(10, 0, 521, 51))
        self.class_name_label.setStyleSheet("#class_name_label{\n"
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
"font-size: 25px;\n"
"line-height: 61px;\n"
"letter-spacing: 0.05em;\n"
"\n"
"color: #FFFFFF;\n"
"\n"
"}")
        self.class_name_label.setObjectName("class_name_label")
        self.class_description_label = QtWidgets.QLabel(self.class_name_frame)
        self.class_description_label.setGeometry(QtCore.QRect(10, 40, 521, 51))
        self.class_description_label.setStyleSheet("#class_description_label{\n"
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
"\n"
"}")
        self.class_description_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.class_description_label.setObjectName("class_description_label")
        self.posts_scroll_area = QtWidgets.QScrollArea(self.main_frame)
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
        self.posts_scroll_area_widget.setGeometry(QtCore.QRect(0, 0, 520, 885))
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
        self.post_button = QtWidgets.QPushButton(self.posts_scroll_area_widget)
        self.post_button.setMaximumSize(QtCore.QSize(495, 80))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        self.post_button.setFont(font)
        self.post_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.post_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.post_button.setStyleSheet("position: absolute;\n"
"width: 1000px;\n"
"height: 148px;\n"
"left: calc(50% - 1000px/2 + 2px);\n"
"top: calc(50% - 148px/2 + 249px);\n"
"\n"
"background: #FFFFFF;\n"
"border: 2px solid #000000;\n"
"box-sizing: border-box;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 10px;\n"
"")
        self.post_button.setObjectName("post_button")
        self.verticalLayout.addWidget(self.post_button)
        self.post_button_2 = QtWidgets.QPushButton(self.posts_scroll_area_widget)
        self.post_button_2.setMaximumSize(QtCore.QSize(495, 80))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        self.post_button_2.setFont(font)
        self.post_button_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.post_button_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.post_button_2.setStyleSheet("position: absolute;\n"
"width: 1000px;\n"
"height: 148px;\n"
"left: calc(50% - 1000px/2 + 2px);\n"
"top: calc(50% - 148px/2 + 249px);\n"
"\n"
"background: #FFFFFF;\n"
"border: 2px solid #000000;\n"
"box-sizing: border-box;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 10px;\n"
"")
        self.post_button_2.setObjectName("post_button_2")
        self.verticalLayout.addWidget(self.post_button_2)
        self.post_button_4 = QtWidgets.QPushButton(self.posts_scroll_area_widget)
        self.post_button_4.setMaximumSize(QtCore.QSize(495, 80))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        self.post_button_4.setFont(font)
        self.post_button_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.post_button_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.post_button_4.setStyleSheet("position: absolute;\n"
"width: 1000px;\n"
"height: 148px;\n"
"left: calc(50% - 1000px/2 + 2px);\n"
"top: calc(50% - 148px/2 + 249px);\n"
"\n"
"background: #FFFFFF;\n"
"border: 2px solid #000000;\n"
"box-sizing: border-box;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 10px;\n"
"")
        self.post_button_4.setObjectName("post_button_4")
        self.verticalLayout.addWidget(self.post_button_4)
        self.post_button_5 = QtWidgets.QPushButton(self.posts_scroll_area_widget)
        self.post_button_5.setMaximumSize(QtCore.QSize(495, 80))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        self.post_button_5.setFont(font)
        self.post_button_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.post_button_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.post_button_5.setStyleSheet("position: absolute;\n"
"width: 1000px;\n"
"height: 148px;\n"
"left: calc(50% - 1000px/2 + 2px);\n"
"top: calc(50% - 148px/2 + 249px);\n"
"\n"
"background: #FFFFFF;\n"
"border: 2px solid #000000;\n"
"box-sizing: border-box;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 10px;\n"
"")
        self.post_button_5.setObjectName("post_button_5")
        self.verticalLayout.addWidget(self.post_button_5)
        self.post_button_6 = QtWidgets.QPushButton(self.posts_scroll_area_widget)
        self.post_button_6.setMaximumSize(QtCore.QSize(495, 80))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        self.post_button_6.setFont(font)
        self.post_button_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.post_button_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.post_button_6.setStyleSheet("position: absolute;\n"
"width: 1000px;\n"
"height: 148px;\n"
"left: calc(50% - 1000px/2 + 2px);\n"
"top: calc(50% - 148px/2 + 249px);\n"
"\n"
"background: #FFFFFF;\n"
"border: 2px solid #000000;\n"
"box-sizing: border-box;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 10px;\n"
"")
        self.post_button_6.setObjectName("post_button_6")
        self.verticalLayout.addWidget(self.post_button_6)
        self.post_button_3 = QtWidgets.QPushButton(self.posts_scroll_area_widget)
        self.post_button_3.setMaximumSize(QtCore.QSize(495, 80))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        self.post_button_3.setFont(font)
        self.post_button_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.post_button_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.post_button_3.setStyleSheet("position: absolute;\n"
"width: 1000px;\n"
"height: 148px;\n"
"left: calc(50% - 1000px/2 + 2px);\n"
"top: calc(50% - 148px/2 + 249px);\n"
"\n"
"background: #FFFFFF;\n"
"border: 2px solid #000000;\n"
"box-sizing: border-box;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 10px;\n"
"")
        self.post_button_3.setObjectName("post_button_3")
        self.verticalLayout.addWidget(self.post_button_3)
        self.post_button_10 = QtWidgets.QPushButton(self.posts_scroll_area_widget)
        self.post_button_10.setMaximumSize(QtCore.QSize(495, 80))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        self.post_button_10.setFont(font)
        self.post_button_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.post_button_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.post_button_10.setStyleSheet("position: absolute;\n"
"width: 1000px;\n"
"height: 148px;\n"
"left: calc(50% - 1000px/2 + 2px);\n"
"top: calc(50% - 148px/2 + 249px);\n"
"\n"
"background: #FFFFFF;\n"
"border: 2px solid #000000;\n"
"box-sizing: border-box;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 10px;\n"
"")
        self.post_button_10.setObjectName("post_button_10")
        self.verticalLayout.addWidget(self.post_button_10)
        self.post_button_9 = QtWidgets.QPushButton(self.posts_scroll_area_widget)
        self.post_button_9.setMaximumSize(QtCore.QSize(495, 80))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        self.post_button_9.setFont(font)
        self.post_button_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.post_button_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.post_button_9.setStyleSheet("position: absolute;\n"
"width: 1000px;\n"
"height: 148px;\n"
"left: calc(50% - 1000px/2 + 2px);\n"
"top: calc(50% - 148px/2 + 249px);\n"
"\n"
"background: #FFFFFF;\n"
"border: 2px solid #000000;\n"
"box-sizing: border-box;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 10px;\n"
"")
        self.post_button_9.setObjectName("post_button_9")
        self.verticalLayout.addWidget(self.post_button_9)
        self.post_button_8 = QtWidgets.QPushButton(self.posts_scroll_area_widget)
        self.post_button_8.setMaximumSize(QtCore.QSize(495, 80))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        self.post_button_8.setFont(font)
        self.post_button_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.post_button_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.post_button_8.setStyleSheet("position: absolute;\n"
"width: 1000px;\n"
"height: 148px;\n"
"left: calc(50% - 1000px/2 + 2px);\n"
"top: calc(50% - 148px/2 + 249px);\n"
"\n"
"background: #FFFFFF;\n"
"border: 2px solid #000000;\n"
"box-sizing: border-box;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 10px;\n"
"")
        self.post_button_8.setObjectName("post_button_8")
        self.verticalLayout.addWidget(self.post_button_8)
        self.post_button_7 = QtWidgets.QPushButton(self.posts_scroll_area_widget)
        self.post_button_7.setMaximumSize(QtCore.QSize(495, 80))
        font = QtGui.QFont()
        font.setFamily("Poppins Medium")
        font.setPointSize(14)
        self.post_button_7.setFont(font)
        self.post_button_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.post_button_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.post_button_7.setStyleSheet("position: absolute;\n"
"width: 1000px;\n"
"height: 148px;\n"
"left: calc(50% - 1000px/2 + 2px);\n"
"top: calc(50% - 148px/2 + 249px);\n"
"\n"
"background: #FFFFFF;\n"
"border: 2px solid #000000;\n"
"box-sizing: border-box;\n"
"box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);\n"
"border-radius: 10px;\n"
"")
        self.post_button_7.setObjectName("post_button_7")
        self.verticalLayout.addWidget(self.post_button_7)
        self.posts_scroll_area.setWidget(self.posts_scroll_area_widget)
        self.label_4 = QtWidgets.QLabel(self.main_frame)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 251, 51))
        self.label_4.setStyleSheet("position: absolute;\n"
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
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.events_scroll_area = QtWidgets.QScrollArea(self.main_frame)
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
        self.events_view = QtWidgets.QFrame(self.events_scroll_area_widget)
        self.events_view.setMaximumSize(QtCore.QSize(16777215, 70))
        self.events_view.setStyleSheet("#events_view{\n"
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
        self.events_view.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.events_view.setFrameShadow(QtWidgets.QFrame.Raised)
        self.events_view.setObjectName("events_view")
        self.label_6 = QtWidgets.QLabel(self.events_view)
        self.label_6.setGeometry(QtCore.QRect(10, 0, 211, 41))
        self.label_6.setStyleSheet("position: absolute;\n"
"left: 20px;\n"
"right: 30px;\n"
"top: 10px;\n"
"bottom: 10px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;\n"
"line-height: 37px;\n"
"letter-spacing: 0.05em;\n"
"background: rgba(0, 0, 0, 0.01);\n"
"color: #000000;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.events_view)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 211, 41))
        self.label_7.setStyleSheet("position: absolute;\n"
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
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.events_view)
        self.events_scroll_area.setWidget(self.events_scroll_area_widget)
        self.label_5 = QtWidgets.QLabel(self.main_frame)
        self.label_5.setGeometry(QtCore.QRect(820, 20, 251, 51))
        self.label_5.setStyleSheet("position: absolute;\n"
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
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.assign_scroll_area = QtWidgets.QScrollArea(self.main_frame)
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
        self.assign_scroll_area_widget.setGeometry(QtCore.QRect(0, 0, 251, 554))
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
        self.events_view_4 = QtWidgets.QFrame(self.assign_scroll_area_widget)
        self.events_view_4.setMinimumSize(QtCore.QSize(229, 70))
        self.events_view_4.setMaximumSize(QtCore.QSize(229, 70))
        self.events_view_4.setStyleSheet("#events_view_4{\n"
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
        self.events_view_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.events_view_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.events_view_4.setObjectName("events_view_4")
        self.label_18 = QtWidgets.QLabel(self.events_view_4)
        self.label_18.setGeometry(QtCore.QRect(10, 0, 211, 41))
        self.label_18.setStyleSheet("position: absolute;\n"
"left: 20px;\n"
"right: 30px;\n"
"top: 10px;\n"
"bottom: 10px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;\n"
"line-height: 37px;\n"
"letter-spacing: 0.05em;\n"
"background: rgba(0, 0, 0, 0.01);\n"
"color: #000000;")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.events_view_4)
        self.label_19.setGeometry(QtCore.QRect(10, 40, 211, 21))
        self.label_19.setStyleSheet("position: absolute;\n"
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
        self.label_19.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_3.addWidget(self.events_view_4)
        self.events_view_2 = QtWidgets.QFrame(self.assign_scroll_area_widget)
        self.events_view_2.setMinimumSize(QtCore.QSize(229, 70))
        self.events_view_2.setMaximumSize(QtCore.QSize(229, 70))
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
        self.label_12 = QtWidgets.QLabel(self.events_view_2)
        self.label_12.setGeometry(QtCore.QRect(10, 0, 211, 41))
        self.label_12.setStyleSheet("position: absolute;\n"
"left: 20px;\n"
"right: 30px;\n"
"top: 10px;\n"
"bottom: 10px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;\n"
"line-height: 37px;\n"
"letter-spacing: 0.05em;\n"
"background: rgba(0, 0, 0, 0.01);\n"
"color: #000000;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.events_view_2)
        self.label_13.setGeometry(QtCore.QRect(10, 40, 211, 21))
        self.label_13.setStyleSheet("position: absolute;\n"
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
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.events_view_2)
        self.events_view_8 = QtWidgets.QFrame(self.assign_scroll_area_widget)
        self.events_view_8.setMinimumSize(QtCore.QSize(229, 70))
        self.events_view_8.setMaximumSize(QtCore.QSize(229, 70))
        self.events_view_8.setStyleSheet("#events_view_8{\n"
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
        self.events_view_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.events_view_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.events_view_8.setObjectName("events_view_8")
        self.label_34 = QtWidgets.QLabel(self.events_view_8)
        self.label_34.setGeometry(QtCore.QRect(10, 0, 211, 41))
        self.label_34.setStyleSheet("position: absolute;\n"
"left: 20px;\n"
"right: 30px;\n"
"top: 10px;\n"
"bottom: 10px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;\n"
"line-height: 37px;\n"
"letter-spacing: 0.05em;\n"
"background: rgba(0, 0, 0, 0.01);\n"
"color: #000000;")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.events_view_8)
        self.label_35.setGeometry(QtCore.QRect(10, 40, 211, 21))
        self.label_35.setStyleSheet("position: absolute;\n"
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
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_3.addWidget(self.events_view_8)
        self.events_view_5 = QtWidgets.QFrame(self.assign_scroll_area_widget)
        self.events_view_5.setMinimumSize(QtCore.QSize(229, 70))
        self.events_view_5.setMaximumSize(QtCore.QSize(229, 70))
        self.events_view_5.setStyleSheet("#events_view_5{\n"
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
        self.label_20 = QtWidgets.QLabel(self.events_view_5)
        self.label_20.setGeometry(QtCore.QRect(10, 0, 211, 41))
        self.label_20.setStyleSheet("position: absolute;\n"
"left: 20px;\n"
"right: 30px;\n"
"top: 10px;\n"
"bottom: 10px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;\n"
"line-height: 37px;\n"
"letter-spacing: 0.05em;\n"
"background: rgba(0, 0, 0, 0.01);\n"
"color: #000000;")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.events_view_5)
        self.label_21.setGeometry(QtCore.QRect(10, 40, 211, 21))
        self.label_21.setStyleSheet("position: absolute;\n"
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
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_3.addWidget(self.events_view_5)
        self.events_view_3 = QtWidgets.QFrame(self.assign_scroll_area_widget)
        self.events_view_3.setMinimumSize(QtCore.QSize(229, 70))
        self.events_view_3.setMaximumSize(QtCore.QSize(229, 70))
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
        self.label_14 = QtWidgets.QLabel(self.events_view_3)
        self.label_14.setGeometry(QtCore.QRect(10, 0, 211, 41))
        self.label_14.setStyleSheet("position: absolute;\n"
"left: 20px;\n"
"right: 30px;\n"
"top: 10px;\n"
"bottom: 10px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;\n"
"line-height: 37px;\n"
"letter-spacing: 0.05em;\n"
"background: rgba(0, 0, 0, 0.01);\n"
"color: #000000;")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.events_view_3)
        self.label_15.setGeometry(QtCore.QRect(10, 40, 211, 21))
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
        self.verticalLayout_3.addWidget(self.events_view_3)
        self.events_view_7 = QtWidgets.QFrame(self.assign_scroll_area_widget)
        self.events_view_7.setMinimumSize(QtCore.QSize(229, 70))
        self.events_view_7.setMaximumSize(QtCore.QSize(229, 70))
        self.events_view_7.setStyleSheet("#events_view_7\n"
"{\n"
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
        self.events_view_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.events_view_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.events_view_7.setObjectName("events_view_7")
        self.label_26 = QtWidgets.QLabel(self.events_view_7)
        self.label_26.setGeometry(QtCore.QRect(10, 0, 211, 41))
        self.label_26.setStyleSheet("position: absolute;\n"
"left: 20px;\n"
"right: 30px;\n"
"top: 10px;\n"
"bottom: 10px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;\n"
"line-height: 37px;\n"
"letter-spacing: 0.05em;\n"
"background: rgba(0, 0, 0, 0.01);\n"
"color: #000000;")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.events_view_7)
        self.label_27.setGeometry(QtCore.QRect(10, 40, 211, 21))
        self.label_27.setStyleSheet("position: absolute;\n"
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
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_3.addWidget(self.events_view_7)
        self.events_view_6 = QtWidgets.QFrame(self.assign_scroll_area_widget)
        self.events_view_6.setMinimumSize(QtCore.QSize(229, 70))
        self.events_view_6.setMaximumSize(QtCore.QSize(229, 70))
        self.events_view_6.setStyleSheet("#events_view_6\n"
"{\n"
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
        self.label_22 = QtWidgets.QLabel(self.events_view_6)
        self.label_22.setGeometry(QtCore.QRect(10, 0, 211, 41))
        self.label_22.setStyleSheet("position: absolute;\n"
"left: 20px;\n"
"right: 30px;\n"
"top: 10px;\n"
"bottom: 10px;\n"
"\n"
"font-family: Poppins;\n"
"font-style: normal;\n"
"font-weight: normal;\n"
"font-size: 25px;\n"
"line-height: 37px;\n"
"letter-spacing: 0.05em;\n"
"background: rgba(0, 0, 0, 0.01);\n"
"color: #000000;")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.events_view_6)
        self.label_23.setGeometry(QtCore.QRect(10, 40, 211, 21))
        self.label_23.setStyleSheet("position: absolute;\n"
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
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_3.addWidget(self.events_view_6)
        self.assign_scroll_area.setWidget(self.assign_scroll_area_widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "College Virtual Space"))
        self.class_name_label.setText(_translate("MainWindow", "Class Name"))
        self.class_description_label.setText(_translate("MainWindow", "Class description"))
        self.post_button.setText(_translate("MainWindow", "Text Label"))
        self.post_button_2.setText(_translate("MainWindow", "Text Label"))
        self.post_button_4.setText(_translate("MainWindow", "Text Label"))
        self.post_button_5.setText(_translate("MainWindow", "Text Label"))
        self.post_button_6.setText(_translate("MainWindow", "Text Label"))
        self.post_button_3.setText(_translate("MainWindow", "Text Label"))
        self.post_button_10.setText(_translate("MainWindow", "Text Label"))
        self.post_button_9.setText(_translate("MainWindow", "Text Label"))
        self.post_button_8.setText(_translate("MainWindow", "Text Label"))
        self.post_button_7.setText(_translate("MainWindow", "Text Label"))
        self.label_4.setText(_translate("MainWindow", "Events"))
        self.label_6.setText(_translate("MainWindow", "Name"))
        self.label_7.setText(_translate("MainWindow", "Time"))
        self.label_5.setText(_translate("MainWindow", "Assignments"))
        self.label_18.setText(_translate("MainWindow", "Name"))
        self.label_19.setText(_translate("MainWindow", "Time"))
        self.label_12.setText(_translate("MainWindow", "Name"))
        self.label_13.setText(_translate("MainWindow", "Time"))
        self.label_34.setText(_translate("MainWindow", "Name"))
        self.label_35.setText(_translate("MainWindow", "Time"))
        self.label_20.setText(_translate("MainWindow", "Name"))
        self.label_21.setText(_translate("MainWindow", "Time"))
        self.label_14.setText(_translate("MainWindow", "Name"))
        self.label_15.setText(_translate("MainWindow", "Time"))
        self.label_26.setText(_translate("MainWindow", "Name"))
        self.label_27.setText(_translate("MainWindow", "Time"))
        self.label_22.setText(_translate("MainWindow", "Name"))
        self.label_23.setText(_translate("MainWindow", "Time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
