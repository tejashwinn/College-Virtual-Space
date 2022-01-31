import json
from PyQt5 import QtCore, QtGui, QtWidgets
from root_copy import Ui_MainWindow
from sql.fetch_classes_sql import Fetch_Classes_Cl
from compon.mini_components import Individual_Class_Button


def json_data():
    with open(r'C:\Users\tejas\Desktop\22-01-22\.qt_for_python\uic\settings.json') as settings_json_file:
        return json.load(settings_json_file)


def sign_up_switch(variable):
    variable.up_outer_frame.show()
    variable.in_outer_frame.hide()
    variable.main_class_frame.hide()
    variable.in_email_entry.setText("")
    variable.in_password_entry.setText("")


def sign_in_switch(variable):

    variable.in_outer_frame.show()
    variable.up_outer_frame.hide()
    variable.main_class_frame.hide()

    variable.up_name_entry.setText("")
    variable.up_username_entry.setText("")
    variable.up_email_entry.setText("")
    variable.up_password_entry.setText("")


def show_main_frame(variable):
    variable.main_class_frame.show()
    variable.all_classes_frame.show()
    variable.up_outer_frame.hide()
    variable.in_outer_frame.hide()
    variable.class_name_frame.hide()
    variable.posts_scroll_area.hide()


def show_posts_scroll_and_class_frame(variable):
    variable.all_classes_frame.hide()
    variable.class_name_frame.show()
    variable.posts_scroll_area.show()


def show_all_classes_frame(variable):
    variable.all_classes_frame.show()
    variable.class_name_frame.hide()
    variable.posts_scroll_area.hide()


if __name__ == "__main__":
    data = json_data()
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # switches
    ui.actionSignUp.triggered.connect(lambda: sign_up_switch(ui))
    ui.actionSignIn.triggered.connect(lambda: sign_in_switch(ui))
    ui.actionClasses.triggered.connect(lambda: show_main_frame(ui))

    # button actions
    ui.in_sign_up_button.clicked.connect(lambda: sign_up_switch(ui))
    ui.up_sign_in_button.clicked.connect(lambda: sign_in_switch(ui))

    # actions
    ui.posts_scroll_area.setHorizontalScrollBarPolicy(
        QtCore.Qt.ScrollBarAlwaysOff)
    ui.up_sign_up_button.clicked.connect(ui.sign_up_insert)

    for i in range(100):
        temp = ui.return_post_button(MainWindow, str(i))
        ui.verticalLayout.addWidget(temp)

    for i in data["classes_joined"]:
        temp = Individual_Class_Button(
            mainwindow=MainWindow, name=i["class_name"], description=i["class_description"], ui_te=ui, class_code=i["class_code"])
        ui.verticalLayout_5.addWidget(temp.child)

    Fetch_Classes_Cl()

    show_all_classes_frame(ui)
    MainWindow.show()
    sys.exit(app.exec_())
