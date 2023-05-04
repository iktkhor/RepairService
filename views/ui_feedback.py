from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Feedback(object):
    def setupUi(self, Feedback):
        Feedback.setObjectName("Feedback")
        Feedback.resize(343, 121)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Feedback)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.photo = QtWidgets.QLabel(Feedback)
        self.photo.setMinimumSize(QtCore.QSize(40, 40))
        self.photo.setMaximumSize(QtCore.QSize(40, 40))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../photos/default.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.photo.setObjectName("photo")
        self.horizontalLayout_4.addWidget(self.photo)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.client_name_label = QtWidgets.QLabel(Feedback)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.client_name_label.sizePolicy().hasHeightForWidth())
        self.client_name_label.setSizePolicy(sizePolicy)
        self.client_name_label.setMaximumSize(QtCore.QSize(140, 30))
        self.client_name_label.setObjectName("client_name_label")
        self.verticalLayout_3.addWidget(self.client_name_label)
        self.feedback_value_label = QtWidgets.QLabel(Feedback)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feedback_value_label.sizePolicy().hasHeightForWidth())
        self.feedback_value_label.setSizePolicy(sizePolicy)
        self.feedback_value_label.setMaximumSize(QtCore.QSize(140, 30))
        self.feedback_value_label.setObjectName("feedback_value_label")
        self.verticalLayout_3.addWidget(self.feedback_value_label)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.date_label = QtWidgets.QLabel(Feedback)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_label.sizePolicy().hasHeightForWidth())
        self.date_label.setSizePolicy(sizePolicy)
        self.date_label.setMaximumSize(QtCore.QSize(65575, 30))
        self.date_label.setAlignment(QtCore.Qt.AlignCenter)
        self.date_label.setObjectName("date_label")
        self.horizontalLayout_4.addWidget(self.date_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.feedback_text = QtWidgets.QLabel(Feedback)
        self.feedback_text.setWordWrap(True)
        self.feedback_text.setObjectName("feedback_text")
        self.verticalLayout_2.addWidget(self.feedback_text)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Feedback)
        QtCore.QMetaObject.connectSlotsByName(Feedback)

    def retranslateUi(self, Feedback):
        _translate = QtCore.QCoreApplication.translate
        Feedback.setWindowTitle(_translate("Feedback", "Form"))
        self.client_name_label.setText(_translate("Feedback", "Никитос Чулкос"))
        self.feedback_value_label.setText(_translate("Feedback", "Оценка: 4.5 / 5"))
        self.date_label.setText(_translate("Feedback", "08.04.2023"))
        self.feedback_text.setText(_translate("Feedback", "Бля кайф пушка вообще"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Feedback = QtWidgets.QWidget()
    ui = Ui_Feedback()
    ui.setupUi(Feedback)
    Feedback.show()
    sys.exit(app.exec_())
