from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Avaible_components(object):
    def setupUi(self, Avaible_components):
        Avaible_components.setObjectName("Avaible_components")
        Avaible_components.resize(363, 328)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Avaible_components)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.component_type = QtWidgets.QLabel(Avaible_components)
        self.component_type.setMinimumSize(QtCore.QSize(0, 30))
        self.component_type.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.component_type.setFont(font)
        self.component_type.setObjectName("component_type")
        self.verticalLayout.addWidget(self.component_type)
        self.device = QtWidgets.QLabel(Avaible_components)
        self.device.setMinimumSize(QtCore.QSize(0, 30))
        self.device.setMaximumSize(QtCore.QSize(16777215, 30))
        self.device.setFont(font)
        self.device.setObjectName("device")
        self.verticalLayout.addWidget(self.device)
        self.label = QtWidgets.QLabel(Avaible_components)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.list_avaible_components = QtWidgets.QListWidget(Avaible_components)
        self.list_avaible_components.setFont(font)
        self.list_avaible_components.setObjectName("list_avaible_components")
        self.verticalLayout.addWidget(self.list_avaible_components)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Avaible_components)
        QtCore.QMetaObject.connectSlotsByName(Avaible_components)

    def retranslateUi(self, Avaible_components):
        _translate = QtCore.QCoreApplication.translate
        Avaible_components.setWindowTitle(_translate("Avaible_components", "Form"))
        self.component_type.setText(_translate("Avaible_components", "Тип компонента: Экран"))
        self.device.setText(_translate("Avaible_components", "Телефон:"))
        self.label.setText(_translate("Avaible_components", "Список доступных компонентов"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Avaible_components = QtWidgets.QWidget()
    ui = Ui_Avaible_components()
    ui.setupUi(Avaible_components)
    Avaible_components.show()
    sys.exit(app.exec_())
