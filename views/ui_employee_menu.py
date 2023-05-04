from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Employee_menu(object):
    def setupUi(self, Employee_menu):
        Employee_menu.setObjectName("Employee_menu")
        Employee_menu.resize(500, 450)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Employee_menu)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Employee_menu)
        self.tabWidget.setObjectName("tabWidget")
        # self.tab = QtWidgets.QWidget()
        # self.tab.setObjectName("tab")
        # self.tabWidget.addTab(self.tab, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Employee_menu)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Employee_menu)

    def retranslateUi(self, Employee_menu):
        _translate = QtCore.QCoreApplication.translate
        Employee_menu.setWindowTitle(_translate("Employee_menu", "Employee_menu"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Employee_menu", "Tab 1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Employee_menu = QtWidgets.QWidget()
    ui = Ui_Employee_menu()
    ui.setupUi(Employee_menu)
    Employee_menu.show()
    sys.exit(app.exec_())
