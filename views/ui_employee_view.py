from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Employee_view(object):
    def setupUi(self, Employee_view, employee):
        self.employee_id = employee.id
        Employee_view.setObjectName("Form")
        Employee_view.resize(446, 233)
        self.verticalLayout = QtWidgets.QVBoxLayout(Employee_view)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(20, -1, 20, -1)
        self.formLayout.setHorizontalSpacing(20)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.label_name = QtWidgets.QLabel(Employee_view)
        self.label_name.setMinimumSize(QtCore.QSize(65, 25))
        self.label_name.setMaximumSize(QtCore.QSize(65, 0))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_name)
        self.label_login = QtWidgets.QLabel(Employee_view)
        self.label_login.setMinimumSize(QtCore.QSize(65, 25))
        self.label_login.setMaximumSize(QtCore.QSize(65, 0))
        self.label_login.setFont(font)
        self.label_login.setObjectName("label_login")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_login)
        self.employee_name = QtWidgets.QLineEdit(Employee_view)
        self.employee_name.setMinimumSize(QtCore.QSize(0, 25))
        self.employee_name.setMaximumSize(QtCore.QSize(16777215, 25))
        self.employee_name.setFont(font)
        self.employee_name.setObjectName("employee_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.employee_name)
        self.employee_login = QtWidgets.QLineEdit(Employee_view)
        self.employee_login.setMinimumSize(QtCore.QSize(0, 25))
        self.employee_login.setMaximumSize(QtCore.QSize(16777215, 25))
        self.employee_login.setFont(font)
        self.employee_login.setObjectName("employee_login")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.employee_login)
        self.label_experience = QtWidgets.QLabel(Employee_view)
        self.label_experience.setMinimumSize(QtCore.QSize(65, 25))
        self.label_experience.setMaximumSize(QtCore.QSize(65, 0))
        self.label_experience.setFont(font)
        self.label_experience.setObjectName("label_experience")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_experience)
        self.employee_experience = QtWidgets.QSpinBox(Employee_view)
        self.employee_experience.setMinimumSize(QtCore.QSize(0, 25))
        self.employee_experience.setMaximumSize(QtCore.QSize(16777215, 25))
        self.employee_experience.setFont(font)
        self.employee_experience.setMinimum(1)
        self.employee_experience.setMaximum(50)
        self.employee_experience.setObjectName("employee_experience")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.employee_experience)
        self.label_password = QtWidgets.QLabel(Employee_view)
        self.label_password.setMinimumSize(QtCore.QSize(65, 25))
        self.label_password.setMaximumSize(QtCore.QSize(65, 0))
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_password)
        self.employee_password = QtWidgets.QLineEdit(Employee_view)
        self.employee_password.setMinimumSize(QtCore.QSize(0, 25))
        self.employee_password.setMaximumSize(QtCore.QSize(16777215, 25))
        self.employee_password.setFont(font)
        self.employee_password.setObjectName("employee_password")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.employee_password)
        self.label_phone = QtWidgets.QLabel(Employee_view)
        self.label_phone.setMinimumSize(QtCore.QSize(65, 25))
        self.label_phone.setMaximumSize(QtCore.QSize(65, 0))
        self.label_phone.setFont(font)
        self.label_phone.setObjectName("label_phone")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_phone)
        self.employee_phone = QtWidgets.QLineEdit(Employee_view)
        self.employee_phone.setMinimumSize(QtCore.QSize(0, 25))
        self.employee_phone.setMaximumSize(QtCore.QSize(16777215, 25))
        self.employee_phone.setFont(font)
        self.employee_phone.setObjectName("employee_phone")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.employee_phone)
        self.label_role = QtWidgets.QLabel(Employee_view)
        self.label_role.setMinimumSize(QtCore.QSize(65, 25))
        self.label_role.setMaximumSize(QtCore.QSize(65, 0))
        self.label_role.setFont(font)
        self.label_role.setObjectName("label_role")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_role)
        self.employee_role = QtWidgets.QComboBox(Employee_view)
        self.employee_role.setMinimumSize(QtCore.QSize(0, 25))
        self.employee_role.setMaximumSize(QtCore.QSize(16777215, 25))
        self.employee_role.setFont(font)
        self.employee_role.setObjectName("employee_role")
        self.employee_role.addItem("")
        self.employee_role.addItem("")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.employee_role)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(30, -1, 30, -1)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.change_data = QtWidgets.QPushButton(Employee_view)
        self.change_data.setMinimumSize(QtCore.QSize(0, 30))
        self.change_data.setMaximumSize(QtCore.QSize(16777215, 30))
        self.change_data.setFont(font)
        self.change_data.setObjectName("change_data")
        self.horizontalLayout.addWidget(self.change_data)
        self.delete_employee = QtWidgets.QPushButton(Employee_view)
        self.delete_employee.setMinimumSize(QtCore.QSize(0, 30))
        self.delete_employee.setMaximumSize(QtCore.QSize(16777215, 30))
        self.delete_employee.setFont(font)
        self.delete_employee.setObjectName("delete_employee")
        self.horizontalLayout.addWidget(self.delete_employee)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Employee_view)
        QtCore.QMetaObject.connectSlotsByName(Employee_view)
        self.setup_employee(employee)

    def retranslateUi(self, Employee_view):
        _translate = QtCore.QCoreApplication.translate
        Employee_view.setWindowTitle(_translate("Form", "Form"))
        self.label_name.setText(_translate("Form", "Имя"))
        self.label_login.setText(_translate("Form", "Логин"))
        self.label_experience.setText(_translate("Form", "Опыт"))
        self.label_password.setText(_translate("Form", "Пароль"))
        self.label_phone.setText(_translate("Form", "Телефон"))
        self.label_role.setText(_translate("Form", "Роль"))
        self.employee_role.setItemText(0, _translate("Form", "Менеджер"))
        self.employee_role.setItemText(1, _translate("Form", "Техник"))
        self.change_data.setText(_translate("Form", "Изменить"))
        self.delete_employee.setText(_translate("Form", "Удалить"))

    def setup_employee(self, employee):
        self.employee_name.setText(employee.name)
        self.employee_login.setText(employee.login)
        self.employee_password.setText(employee.password)
        self.employee_phone.setText(employee.phone)
        self.employee_experience.setValue(employee.experience)