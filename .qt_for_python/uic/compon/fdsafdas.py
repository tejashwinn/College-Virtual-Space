# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\tejas\Desktop\22-01-22\posts.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# from imp import load_compiled
from PyQt5 import QtCore, QtGui, QtWidgets
import json


class Ui_posts_form(object):

    def return_comment(self, user1, comment1, p=""):
        # print(12)
        if p == "":
            p=self.p_f
        
        comment_view_frame = QtWidgets.QFrame(p)
        comment_view_frame.setGeometry(QtCore.QRect(410, 430, 461, 70))
        comment_view_frame.setMinimumSize(QtCore.QSize(0, 70))
        comment_view_frame.setMaximumSize(QtCore.QSize(520, 70))
        # comment_view_frame.setCursor(
        #     QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        comment_view_frame.setStyleSheet("*{\n"
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
        comment_view_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        comment_view_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        comment_view_frame.setObjectName("comment_view_frame")
        comment = QtWidgets.QLabel(comment_view_frame)
        comment.setGeometry(QtCore.QRect(10, 0, 441, 40))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        comment.setFont(font)
        comment.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        comment.setStyleSheet("position: absolute;\n"
                              "left: 20px;\n"
                              "right: 30px;\n"
                              "top: 10px;\n"
                              "bottom: 10px;\n"
                              "\n"
                              "font-family: Poppins;\n"
                              "font-style: normal;\n"
                              "font-weight: normal;\n"
                              "font-size: 15\n"
                              "px;\n"
                              "line-height: 37px;\n"
                              "letter-spacing: 0.05em;\n"
                              "background: rgba(0, 0, 0, 0.01);\n"
                              "color: #000000;\n"
                              "border:0px;")
        comment.setObjectName("comment")
        user = QtWidgets.QLabel(comment_view_frame)
        user.setGeometry(QtCore.QRect(10, 40, 441, 21))
        user.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        user.setStyleSheet("position: absolute;\n"
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
                           "color: #000000;\n"
                           "border:0px;")
        user.setAlignment(QtCore.Qt.AlignLeading |
                          QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        user.setObjectName("user")
        comment.setText(comment1)
        user.setText(user1)
        return comment_view_frame

    def load_comment(self):
        def clearLayout(layout):
            if layout is not None:
                while layout.count():
                    child = layout.takeAt(0)
                    if child.widget() is not None:
                        child.widget().deleteLater()
                    elif child.layout() is not None:
                        clearLayout(child.layout())
        clearLayout(self.verticalLayout_39)
        if self.te1.existing_comments != []:
            for i in self.te1.existing_comments:
                self.verticalLayout_39.addWidget(
                    self.return_comment(user1=i["user"], comment1=i["comment"]))

            self.verticalLayout_39.addItem(QtWidgets.QSpacerItem(
                20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

    def add_comment(self):
        def json_data():
            with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
                return json.load(settings_json_file)

        data = json_data()
        from compon.add_insert_comment import Comments
        self.te1 = Comments(user=str(data["log"]["username"]),
                            post=data["post_selected"], comment=self.lineEdit.text())
        # print(self.lineEdit.text())
        self.te1.insert()
        self.load_comment()

    def setupUi(self, posts_form):
        self.p_f = posts_form
        posts_form.setObjectName("posts_form")
        posts_form.resize(563, 611)
        posts_form.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(posts_form)
        self.gridLayout.setObjectName("gridLayout")
        self.post_posts_scroll_area = QtWidgets.QScrollArea(posts_form)
        self.post_posts_scroll_area.setMinimumSize(QtCore.QSize(541, 290))
        self.post_posts_scroll_area.setMaximumSize(QtCore.QSize(541, 291))
        self.post_posts_scroll_area.setStyleSheet("background: #FFFFFF;\n"
                                                  "border-radius: 8px;")
        self.post_posts_scroll_area.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.post_posts_scroll_area.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.post_posts_scroll_area.setWidgetResizable(True)
        self.post_posts_scroll_area.setObjectName("post_posts_scroll_area")
        self.post_posts_scroll_area_widget = QtWidgets.QWidget()
        self.post_posts_scroll_area_widget.setGeometry(
            QtCore.QRect(0, 0, 541, 291))
        self.post_posts_scroll_area_widget.setStyleSheet("text-align: center;\n"
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
        self.post_posts_scroll_area_widget.setObjectName(
            "post_posts_scroll_area_widget")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(
            self.post_posts_scroll_area_widget)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.post_posts_scroll_area.setWidget(
            self.post_posts_scroll_area_widget)
        self.gridLayout.addWidget(self.post_posts_scroll_area, 1, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(posts_form)
        self.frame_2.setMinimumSize(QtCore.QSize(541, 291))
        self.frame_2.setMaximumSize(QtCore.QSize(541, 291))
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
        self.dynamic_posts_heading_label = QtWidgets.QLabel(self.frame_2)
        self.dynamic_posts_heading_label.setGeometry(
            QtCore.QRect(20, 30, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dynamic_posts_heading_label.setFont(font)
        self.dynamic_posts_heading_label.setStyleSheet("position: absolute;\n"
                                                       "width: 233px;\n"
                                                       "height: 60px;\n"
                                                       "left: 92px;\n"
                                                       "top: 48px;\n"
                                                       "\n"
                                                       "font-family: Poppins;\n"
                                                       "font-style: normal;\n"
                                                       "font-weight: normal;\n"
                                                       "font-size: 25px;\n"
                                                       "line-height: 60px;\n"
                                                       "/* identical to box height */\n"
                                                       "\n"
                                                       "letter-spacing: 0.05em;\n"
                                                       "text-decoration-line: underline;\n"
                                                       "text-transform: capitalize;\n"
                                                       "\n"
                                                       "color: #000000;\n"
                                                       "")
        self.dynamic_posts_heading_label.setObjectName(
            "dynamic_posts_heading_label")
        self.dynamic_posts_description_label = QtWidgets.QLabel(self.frame_2)
        self.dynamic_posts_description_label.setGeometry(
            QtCore.QRect(20, 70, 511, 131))
        self.dynamic_posts_description_label.setMaximumSize(
            QtCore.QSize(511, 16777215))
        self.dynamic_posts_description_label.setStyleSheet("background: rgba(196, 196, 196, 0.1);\n"
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
        self.dynamic_posts_description_label.setScaledContents(False)
        self.dynamic_posts_description_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.dynamic_posts_description_label.setWordWrap(True)
        self.dynamic_posts_description_label.setObjectName(
            "dynamic_posts_description_label")
        self.static_comments_label = QtWidgets.QLabel(self.frame_2)
        self.static_comments_label.setGeometry(QtCore.QRect(20, 250, 111, 31))
        self.static_comments_label.setStyleSheet("font-family: Poppins;\n"
                                                 "font-style: normal;\n"
                                                 "font-weight: normal;\n"
                                                 "font-size: 15px;\n"
                                                 "line-height: 30px;\n"
                                                 "/* identical to box height */\n"
                                                 "\n"
                                                 "letter-spacing: 0.05em;\n"
                                                 "text-transform: capitalize;\n"
                                                 "")
        self.static_comments_label.setObjectName("static_comments_label")
        self.button_add_comment = QtWidgets.QPushButton(self.frame_2)
        self.button_add_comment.setGeometry(QtCore.QRect(410, 250, 121, 31))
        self.button_add_comment.setStyleSheet("*{\n"
                                              "font-family: Inter;\n"
                                              "font-style: normal;\n"
                                              "font-weight: 500;\n"
                                              "font-size: 12px;\n"
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
                                              "border-radius:7px;\n"
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_add_comment.setIcon(icon)
        self.button_add_comment.setObjectName("button_add_comment")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(150, 250, 251, 31))
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
                                    "\n"
                                    "\n"
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
                                    " \n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 210, 401, 31))
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
        self.button_file_download = QtWidgets.QPushButton(self.frame_2)
        self.button_file_download.setGeometry(QtCore.QRect(440, 210, 93, 28))
        self.button_file_download.setStyleSheet("*{\n"
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
        self.button_file_download.setObjectName("button_file_download")
        self.dynamic_time_label = QtWidgets.QLabel(self.frame_2)
        self.dynamic_time_label.setGeometry(QtCore.QRect(10, 10, 201, 16))
        self.dynamic_time_label.setStyleSheet("font-family: Poppins;\n"
                                              "font-style: normal;\n"
                                              "font-weight: normal;\n"
                                              "font-size: 13px;\n"
                                              "line-height: 30px;\n"
                                              "/* identical to box height */\n"
                                              "\n"
                                              "letter-spacing: 0.05em;\n"
                                              "text-transform: capitalize;\n"
                                              "")
        self.dynamic_time_label.setObjectName("dynamic_time_label")
        self.close_button_posts = QtWidgets.QPushButton(self.frame_2)
        self.close_button_posts.setGeometry(QtCore.QRect(489, 10, 35, 35))
        self.close_button_posts.setStyleSheet("*{border-radius:0px;}\n"
                                              ":pressed{\n"
                                              "    border: 3px solid  #FF0000;\n"
                                              "boder:10px;\n"
                                              "border-radius: 8px;\n"
                                              "}")
        self.close_button_posts.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "c:\\Users\\tejas\\Desktop\\22-01-22\\assests/icons/x-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button_posts.setIcon(icon1)
        self.close_button_posts.setIconSize(QtCore.QSize(40, 40))
        self.close_button_posts.setObjectName("close_button_posts")
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        ###
        self.button_add_comment.clicked.connect(self.add_comment)
        ###
        self.retranslateUi(posts_form)

        def json_data():
            with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
                return json.load(settings_json_file)

        data = json_data()
        from compon.add_insert_comment import Comments

        self.te1 = Comments(user=str(data["log"]["username"]),
                            post=data["post_selected"], comment="")

        self.load_comment()
        print(0)
        QtCore.QMetaObject.connectSlotsByName(posts_form)

    def retranslateUi(self, posts_form):
        _translate = QtCore.QCoreApplication.translate
        posts_form.setWindowTitle(_translate("posts_form", "Form"))
        self.dynamic_posts_heading_label.setText(
            _translate("posts_form", "Post Heading"))
        self.dynamic_posts_description_label.setText(_translate(
            "posts_form", "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec."))
        self.static_comments_label.setText(
            _translate("posts_form", "Comments 🔽"))
        self.button_add_comment.setText(
            _translate("posts_form", "Add Comment"))
        self.label_2.setText(_translate("posts_form", "Files: "))
        self.button_file_download.setText(_translate("posts_form", "Download"))
        self.dynamic_time_label.setText(_translate("posts_form", "Time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    create_posts_form = QtWidgets.QWidget()
    ui = Ui_posts_form()
    ui.setupUi(create_posts_form)
    create_posts_form.show()
    sys.exit(app.exec_())
