from PyQt5 import QtCore, QtGui, QtWidgets


class Indi_marks(object):


    def return_object(self):
        self.o = self.username_form

    def setupUi(self, Form, di):
        # print(di)
        self.di = di
        self.username_form = QtWidgets.QFrame()
        self.username_form.setGeometry(QtCore.QRect(10, 70, 451, 150))
        self.username_form.setMinimumSize(QtCore.QSize(0, 150))
        self.username_form.setMaximumSize(QtCore.QSize(99999, 150))
        self.username_form.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.username_form.setStyleSheet("*{\n"
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
        self.username_form.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.username_form.setFrameShadow(QtWidgets.QFrame.Raised)
        self.username_form.setObjectName("username_form")
        self.dynamic_name_label = QtWidgets.QLabel(self.username_form)
        self.dynamic_name_label.setGeometry(QtCore.QRect(10, 0, 431, 61))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dynamic_name_label.setFont(font)
        self.dynamic_name_label.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dynamic_name_label.setStyleSheet("position: absolute;\n"
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
                                              "color: #000000;\n"
                                              "border:0px;\n"
                                              "")
        self.dynamic_name_label.setWordWrap(True)
        self.dynamic_name_label.setObjectName("dynamic_name_label")
        self.dynamic_sub_date = QtWidgets.QLabel(self.username_form)
        self.dynamic_sub_date.setGeometry(QtCore.QRect(10, 60, 181, 21))
        self.dynamic_sub_date.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dynamic_sub_date.setStyleSheet("position: absolute;\n"
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
        self.dynamic_sub_date.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.dynamic_sub_date.setObjectName("dynamic_sub_date")
        self.download_file_button = QtWidgets.QPushButton(self.username_form)
        self.download_file_button.setGeometry(QtCore.QRect(320, 110, 121, 28))
        self.download_file_button.setStyleSheet("*{\n"
                                                "font-family: Inter;\n"
                                                "font-style: normal;\n"
                                                "font-weight: 500;\n"
                                                "font-size: 14px;\n"
                                                "line-height: 17px;\n"
                                                "align-items: center;\n"
                                                "border-style: inset;\n"
                                                "border: 1px solid  #4F4F4F;\n"
                                                "color: #4F4F4F;\n"
                                                "background: #FFFFFF;\n"
                                                "border-radius:10px;\n"
                                                "}\n"
                                                "\n"
                                                ":pressed {\n"
                                                "border-style: inset;\n"
                                                "color: white;\n"
                                                "background: #4F4F4F;\n"
                                                "border-radius: 8px;\n"
                                                "}\n"
                                                "\n"
                                                "\n"
                                                "")
        self.download_file_button.setObjectName("download_file_button")
        self.static_marks = QtWidgets.QLabel(self.username_form)
        self.static_marks.setGeometry(QtCore.QRect(10, 110, 71, 30))
        self.static_marks.setStyleSheet("position: absolute;\n"
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
                                        "color: #000000;\n"
                                        "border:0px;\n"
                                        "")
        self.static_marks.setObjectName("static_marks")
        self.marks_entry = QtWidgets.QLineEdit(self.username_form)
        self.marks_entry.setGeometry(QtCore.QRect(90, 110, 113, 30))
        self.marks_entry.setStyleSheet("position: static;\n"
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
        self.marks_entry.setObjectName("marks_entry")
        self.submit_file_button = QtWidgets.QPushButton(self.username_form)
        self.submit_file_button.setGeometry(QtCore.QRect(220, 110, 93, 30))
        self.submit_file_button.setStyleSheet("*{\n"
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
        self.submit_file_button.setObjectName("submit_file_button")
        self.dynamic_file_name_label = QtWidgets.QLabel(self.username_form)
        self.dynamic_file_name_label.setGeometry(
            QtCore.QRect(200, 60, 241, 21))
        self.dynamic_file_name_label.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dynamic_file_name_label.setStyleSheet("position: absolute;\n"
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
        self.dynamic_file_name_label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.dynamic_file_name_label.setObjectName(self.di["as_file_name"])
        self.dynamic_name_label.setText(self.di["as_user"])
        self.dynamic_sub_date.setText(self.di[""])
        self.download_file_button.setText(self.di[""])
        self.static_marks.setText(self.di[""])
        self.submit_file_button.setText(self.di[""])
        self.dynamic_file_name_label.setText(self.di[""])
        self.return_object()
