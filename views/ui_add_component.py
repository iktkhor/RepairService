# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_component.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Add_component(object):
    def setupUi(self, Add_component):
        Add_component.setObjectName("Add_component")
        Add_component.resize(800, 370)
        Add_component.setMinimumSize(QtCore.QSize(800, 370))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Add_component)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(Add_component)
        self.label_5.setMinimumSize(QtCore.QSize(0, 30))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(15)
        self.formLayout.setVerticalSpacing(18)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Add_component)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.component_name = QtWidgets.QLineEdit(Add_component)
        self.component_name.setMinimumSize(QtCore.QSize(0, 30))
        self.component_name.setFont(font)
        self.component_name.setObjectName("component_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.component_name)
        self.label_3 = QtWidgets.QLabel(Add_component)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.component_type = QtWidgets.QComboBox(Add_component)
        self.component_type.setMinimumSize(QtCore.QSize(0, 30))
        self.component_type.setFont(font)
        self.component_type.setObjectName("component_type")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.component_type)
        self.label_device = QtWidgets.QLabel(Add_component)
        self.label_device.setMinimumSize(QtCore.QSize(70, 30))
        self.label_device.setMaximumSize(QtCore.QSize(70, 30))
        self.label_device.setFont(font)
        self.label_device.setObjectName("label_device")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_device)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.device_company = QtWidgets.QComboBox(Add_component)
        self.device_company.setMinimumSize(QtCore.QSize(0, 30))
        self.device_company.setMaximumSize(QtCore.QSize(16777215, 30))
        self.device_company.setFont(font)
        self.device_company.setObjectName("device_company")
        self.horizontalLayout_4.addWidget(self.device_company)
        self.device_name = QtWidgets.QComboBox(Add_component)
        self.device_name.setMinimumSize(QtCore.QSize(0, 30))
        self.device_name.setMaximumSize(QtCore.QSize(16777215, 30))
        self.device_name.setFont(font)
        self.device_name.setObjectName("device_name")
        self.horizontalLayout_4.addWidget(self.device_name)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_2 = QtWidgets.QLabel(Add_component)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.component_supplier = QtWidgets.QComboBox(Add_component)
        self.component_supplier.setMinimumSize(QtCore.QSize(0, 30))
        self.component_supplier.setFont(font)
        self.component_supplier.setObjectName("component_supplier")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.component_supplier)
        self.label_4 = QtWidgets.QLabel(Add_component)
        self.label_4.setMinimumSize(QtCore.QSize(0, 30))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.component_cost = QtWidgets.QLineEdit(Add_component)
        self.component_cost.setMinimumSize(QtCore.QSize(0, 30))
        self.component_cost.setFont(font)
        self.component_cost.setObjectName("component_cost")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.component_cost)
        self.label_8 = QtWidgets.QLabel(Add_component)
        self.label_8.setMinimumSize(QtCore.QSize(0, 30))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.component_quantity = QtWidgets.QSpinBox(Add_component)
        self.component_quantity.setMinimumSize(QtCore.QSize(0, 30))
        self.component_quantity.setMaximumSize(QtCore.QSize(16777215, 30))
        self.component_quantity.setFont(font)
        self.component_quantity.setObjectName("component_quantity")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.component_quantity)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.add_component = QtWidgets.QPushButton(Add_component)
        self.add_component.setMinimumSize(QtCore.QSize(0, 30))
        self.add_component.setFont(font)
        self.add_component.setObjectName("add_component")
        self.verticalLayout_2.addWidget(self.add_component)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(Add_component)
        self.label_6.setMinimumSize(QtCore.QSize(0, 30))
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(Add_component)
        self.label_7.setMinimumSize(QtCore.QSize(0, 30))
        self.label_7.setMaximumSize(QtCore.QSize(120, 16777215))
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.list_component_type = QtWidgets.QComboBox(Add_component)
        self.list_component_type.setMinimumSize(QtCore.QSize(0, 30))
        self.list_component_type.setFont(font)
        self.list_component_type.setObjectName("list_component_type")
        self.horizontalLayout_2.addWidget(self.list_component_type)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.list_components = QtWidgets.QListWidget(Add_component)
        self.list_components.setObjectName("list_components")
        self.verticalLayout.addWidget(self.list_components)
        self.refresh_list = QtWidgets.QPushButton(Add_component)
        self.refresh_list.setMinimumSize(QtCore.QSize(0, 30))
        self.refresh_list.setMaximumSize(QtCore.QSize(16777215, 30))
        self.refresh_list.setFont(font)
        self.refresh_list.setObjectName("refresh_list")
        self.verticalLayout.addWidget(self.refresh_list)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Add_component)
        QtCore.QMetaObject.connectSlotsByName(Add_component)

    def retranslateUi(self, Add_component):
        _translate = QtCore.QCoreApplication.translate
        Add_component.setWindowTitle(_translate("Add_component", "Form"))
        self.label_5.setText(_translate("Add_component", "Введить данные нового компонента"))
        self.label.setText(_translate("Add_component", "Название компонента:"))
        self.label_3.setText(_translate("Add_component", "Тип компонента:"))
        self.label_device.setText(_translate("Add_component", "Устройство:"))
        self.label_2.setText(_translate("Add_component", "Поставщик:"))
        self.label_4.setText(_translate("Add_component", "Стоимость:"))
        self.label_8.setText(_translate("Add_component", "Количество"))
        self.add_component.setText(_translate("Add_component", "Добавить компонент"))
        self.label_6.setText(_translate("Add_component", "Список компонентов"))
        self.label_7.setText(_translate("Add_component", "Тип компонента"))
        self.refresh_list.setText(_translate("Add_component", "Обновить список"))