# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edom.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_fgdc_attrdomv(object):
    def setupUi(self, fgdc_attrdomv):
        fgdc_attrdomv.setObjectName("fgdc_attrdomv")
        fgdc_attrdomv.resize(256, 100)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(fgdc_attrdomv.sizePolicy().hasHeightForWidth())
        fgdc_attrdomv.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(fgdc_attrdomv)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fgdc_edom = QtWidgets.QFrame(fgdc_attrdomv)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_edom.sizePolicy().hasHeightForWidth())
        self.fgdc_edom.setSizePolicy(sizePolicy)
        self.fgdc_edom.setFrameShape(QtWidgets.QFrame.Box)
        self.fgdc_edom.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fgdc_edom.setObjectName("fgdc_edom")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.fgdc_edom)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.fgdc_edom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fgdc_edomv = QtWidgets.QLineEdit(self.widget_3)
        self.fgdc_edomv.setText("")
        self.fgdc_edomv.setObjectName("fgdc_edomv")
        self.horizontalLayout_2.addWidget(self.fgdc_edomv)
        self.label_27 = QtWidgets.QLabel(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setMinimumSize(QtCore.QSize(15, 20))
        self.label_27.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setScaledContents(True)
        self.label_27.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_27.setIndent(0)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_2.addWidget(self.label_27)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.label_21 = QtWidgets.QLabel(self.fgdc_edom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QtCore.QSize(0, 0))
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_21.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_21.setIndent(0)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_2.addWidget(self.label_21)
        self.widget = QtWidgets.QWidget(self.fgdc_edom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.fgdc_edomvd = GrowingTextEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fgdc_edomvd.sizePolicy().hasHeightForWidth())
        self.fgdc_edomvd.setSizePolicy(sizePolicy)
        self.fgdc_edomvd.setMinimumSize(QtCore.QSize(0, 30))
        self.fgdc_edomvd.setObjectName("fgdc_edomvd")
        self.horizontalLayout_9.addWidget(self.fgdc_edomvd)
        self.label_25 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setMinimumSize(QtCore.QSize(15, 20))
        self.label_25.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_25.setFont(font)
        self.label_25.setScaledContents(True)
        self.label_25.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_25.setIndent(0)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_9.addWidget(self.label_25)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.fgdc_edom)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_22 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QtCore.QSize(0, 0))
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setIndent(0)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout.addWidget(self.label_22)
        self.fgdc_edomvds = QtWidgets.QLineEdit(self.widget_2)
        self.fgdc_edomvds.setObjectName("fgdc_edomvds")
        self.horizontalLayout.addWidget(self.fgdc_edomvds)
        self.label_26 = QtWidgets.QLabel(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMinimumSize(QtCore.QSize(15, 20))
        self.label_26.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_26.setFont(font)
        self.label_26.setScaledContents(True)
        self.label_26.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_26.setIndent(0)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout.addWidget(self.label_26)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.fgdc_edom)

        self.retranslateUi(fgdc_attrdomv)
        QtCore.QMetaObject.connectSlotsByName(fgdc_attrdomv)

    def retranslateUi(self, fgdc_attrdomv):
        _translate = QtCore.QCoreApplication.translate
        fgdc_attrdomv.setWindowTitle(_translate("fgdc_attrdomv", "Form"))
        self.label_27.setToolTip(_translate("fgdc_attrdomv", "Required"))
        self.label_27.setText(_translate("fgdc_attrdomv", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#55aaff;\">*</span></p></body></html>"))
        self.label_21.setText(_translate("fgdc_attrdomv", "Definition of this Value"))
        self.label_25.setToolTip(_translate("fgdc_attrdomv", "Required"))
        self.label_25.setText(_translate("fgdc_attrdomv", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#55aaff;\">*</span></p></body></html>"))
        self.label_22.setText(_translate("fgdc_attrdomv", "Definition Source"))
        self.fgdc_edomvds.setText(_translate("fgdc_attrdomv", "Producer defined"))
        self.label_26.setToolTip(_translate("fgdc_attrdomv", "Required"))
        self.label_26.setText(_translate("fgdc_attrdomv", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#55aaff;\">*</span></p></body></html>"))

from growingtextedit import GrowingTextEdit
