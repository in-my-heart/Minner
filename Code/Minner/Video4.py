# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Video4.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VideoWidget4(object):
    def setupUi(self, VideoWidget4):
        VideoWidget4.setObjectName("VideoWidget4")
        VideoWidget4.resize(979, 463)
        self.gridLayout = QtWidgets.QGridLayout(VideoWidget4)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widgetView = QtWidgets.QWidget(VideoWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetView.sizePolicy().hasHeightForWidth())
        self.widgetView.setSizePolicy(sizePolicy)
        self.widgetView.setMinimumSize(QtCore.QSize(0, 400))
        self.widgetView.setObjectName("widgetView")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widgetView)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_0 = QtWidgets.QLabel(self.widgetView)
        self.label_0.setMaximumSize(QtCore.QSize(400, 200))
        self.label_0.setStyleSheet("")
        self.label_0.setText("")
        self.label_0.setObjectName("label_0")
        self.gridLayout_2.addWidget(self.label_0, 0, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.widgetView)
        self.label_1.setMaximumSize(QtCore.QSize(400, 200))
        self.label_1.setStyleSheet("")
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.gridLayout_2.addWidget(self.label_1, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widgetView)
        self.label_2.setMaximumSize(QtCore.QSize(400, 200))
        self.label_2.setStyleSheet("")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widgetView)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(400, 200))
        self.label_3.setStyleSheet("")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.widgetView, 0, 0, 1, 1)

        self.retranslateUi(VideoWidget4)
        QtCore.QMetaObject.connectSlotsByName(VideoWidget4)

    def retranslateUi(self, VideoWidget4):
        _translate = QtCore.QCoreApplication.translate
        VideoWidget4.setWindowTitle(_translate("VideoWidget4", "Form"))
