# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 591)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.queryTextEdit = QtWidgets.QTextEdit(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.queryTextEdit.setFont(font)
        self.queryTextEdit.setObjectName("queryTextEdit")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.resultTable = QtWidgets.QTableView(self.splitter)
        self.resultTable.setMinimumSize(QtCore.QSize(600, 0))
        self.resultTable.setObjectName("resultTable")
        self.outputTextView = QtWidgets.QTextEdit(self.splitter)
        self.outputTextView.setMaximumSize(QtCore.QSize(255, 16777215))
        self.outputTextView.setObjectName("outputTextView")
        self.verticalLayout.addWidget(self.splitter)
        self.widget = QtWidgets.QWidget(self.layoutWidget)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 26))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.connectionStringLineEdit = QtWidgets.QLineEdit(self.widget)
        self.connectionStringLineEdit.setMinimumSize(QtCore.QSize(400, 0))
        self.connectionStringLineEdit.setObjectName("connectionStringLineEdit")
        self.horizontalLayout.addWidget(self.connectionStringLineEdit)
        self.openBtn = QtWidgets.QPushButton(self.widget)
        self.openBtn.setObjectName("openBtn")
        self.horizontalLayout.addWidget(self.openBtn)
        self.executeBtn = QtWidgets.QPushButton(self.widget)
        self.executeBtn.setObjectName("executeBtn")
        self.horizontalLayout.addWidget(self.executeBtn)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.rowCountLabel = QtWidgets.QLabel(self.widget)
        self.rowCountLabel.setObjectName("rowCountLabel")
        self.horizontalLayout.addWidget(self.rowCountLabel)
        self.verticalLayout.addWidget(self.widget)
        self.horizontalLayout_2.addWidget(self.splitter_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Connection string"))
        self.openBtn.setText(_translate("MainWindow", "..."))
        self.executeBtn.setText(_translate("MainWindow", "Execute(F5)"))
        self.rowCountLabel.setText(_translate("MainWindow", " "))
