# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\tejas\Desktop\22-01-22\root.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1081, 663)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(0, 0, 1081, 601))
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
        self.class_name_label_dynamic = QtWidgets.QLabel(self.class_name_frame)
        self.class_name_label_dynamic.setGeometry(QtCore.QRect(10, 0, 521, 51))
        self.class_name_label_dynamic.setStyleSheet("#class_name_label{\n"
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
        self.class_name_label_dynamic.setObjectName("class_name_label_dynamic")
        self.class_description_label_dynamic = QtWidgets.QLabel(self.class_name_frame)
        self.class_description_label_dynamic.setGeometry(QtCore.QRect(10, 40, 521, 51))
        self.class_description_label_dynamic.setStyleSheet("#class_description_label{\n"
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
        self.class_description_label_dynamic.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.class_description_label_dynamic.setObjectName("class_description_label_dynamic")
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
        self.static_events = QtWidgets.QLabel(self.main_frame)
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
        self.events_scroll_area.setWidget(self.events_scroll_area_widget)
        self.static_assignment = QtWidgets.QLabel(self.main_frame)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1081, 26))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setObjectName("menubar")
        self.menuUser = QtWidgets.QMenu(self.menubar)
        self.menuUser.setObjectName("menuUser")
        self.menuViews = QtWidgets.QMenu(self.menubar)
        self.menuViews.setObjectName("menuViews")
        self.menuClass_Admin = QtWidgets.QMenu(self.menubar)
        self.menuClass_Admin.setObjectName("menuClass_Admin")
        self.menuClub = QtWidgets.QMenu(self.menubar)
        self.menuClub.setObjectName("menuClub")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSignup = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/user-plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSignup.setIcon(icon)
        self.actionSignup.setObjectName("actionSignup")
        self.actionLogin = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLogin.setIcon(icon1)
        self.actionLogin.setObjectName("actionLogin")
        self.actionLog_Out = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLog_Out.setIcon(icon2)
        self.actionLog_Out.setObjectName("actionLog_Out")
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
        self.actionCreate_Post = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/plus-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreate_Post.setIcon(icon6)
        self.actionCreate_Post.setObjectName("actionCreate_Post")
        self.actionCreate_Assignment = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/file-plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreate_Assignment.setIcon(icon7)
        self.actionCreate_Assignment.setObjectName("actionCreate_Assignment")
        self.actionView_Assignment = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/eye.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionView_Assignment.setIcon(icon8)
        self.actionView_Assignment.setObjectName("actionView_Assignment")
        self.actionView_Classes = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/trello.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionView_Classes.setIcon(icon9)
        self.actionView_Classes.setObjectName("actionView_Classes")
        self.actionEvents_2 = QtWidgets.QAction(MainWindow)
        self.actionEvents_2.setObjectName("actionEvents_2")
        self.actionClubs = QtWidgets.QAction(MainWindow)
        self.actionClubs.setObjectName("actionClubs")
        self.menuUser.addAction(self.actionSignup)
        self.menuUser.addSeparator()
        self.menuUser.addAction(self.actionLogin)
        self.menuUser.addSeparator()
        self.menuUser.addAction(self.actionLog_Out)
        self.menuUser.addSeparator()
        self.menuViews.addAction(self.actionClasses)
        self.menuViews.addSeparator()
        self.menuViews.addAction(self.actionEvents)
        self.menuViews.addSeparator()
        self.menuViews.addAction(self.actionAssignments)
        self.menuClass_Admin.addAction(self.actionCreate_Post)
        self.menuClass_Admin.addAction(self.actionCreate_Assignment)
        self.menuClass_Admin.addAction(self.actionView_Assignment)
        self.menuClass_Admin.addAction(self.actionView_Classes)
        self.menuClub.addAction(self.actionEvents_2)
        self.menuClub.addAction(self.actionClubs)
        self.menubar.addAction(self.menuUser.menuAction())
        self.menubar.addAction(self.menuViews.menuAction())
        self.menubar.addAction(self.menuClass_Admin.menuAction())
        self.menubar.addAction(self.menuClub.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.class_name_label_dynamic.setText(_translate("MainWindow", "Class Name"))
        self.class_description_label_dynamic.setText(_translate("MainWindow", "Class description"))
        self.static_events.setText(_translate("MainWindow", "Events"))
        self.static_assignment.setText(_translate("MainWindow", "Assignments"))
        self.menuUser.setTitle(_translate("MainWindow", "User"))
        self.menuViews.setTitle(_translate("MainWindow", "Views"))
        self.menuClass_Admin.setTitle(_translate("MainWindow", "Class Admin"))
        self.menuClub.setTitle(_translate("MainWindow", "Club"))
        self.actionSignup.setText(_translate("MainWindow", "Sign Up"))
        self.actionLogin.setText(_translate("MainWindow", "Log In"))
        self.actionLog_Out.setText(_translate("MainWindow", "Log Out"))
        self.actionClasses.setText(_translate("MainWindow", "Classes"))
        self.actionEvents.setText(_translate("MainWindow", "Events"))
        self.actionAssignments.setText(_translate("MainWindow", "Assignments"))
        self.actionCreate_Post.setText(_translate("MainWindow", "Create Post"))
        self.actionCreate_Assignment.setText(_translate("MainWindow", "Create Assignment"))
        self.actionView_Assignment.setText(_translate("MainWindow", "View Assignment"))
        self.actionView_Classes.setText(_translate("MainWindow", "View Classes"))
        self.actionEvents_2.setText(_translate("MainWindow", "Events"))
        self.actionClubs.setText(_translate("MainWindow", "Clubs"))
