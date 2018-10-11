# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class UiMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(724, 496)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.queryTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.queryTextEdit.setObjectName("queryTextEdit")
        self.verticalLayout.addWidget(self.queryTextEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.connectionStringLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.connectionStringLineEdit.setObjectName("connectionStringLineEdit")
        self.horizontalLayout.addWidget(self.connectionStringLineEdit)
        self.executeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.executeBtn.setObjectName("executeBtn")
        self.horizontalLayout.addWidget(self.executeBtn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.resultTable = QtWidgets.QTableView(self.centralwidget)
        self.resultTable.setMinimumSize(QtCore.QSize(400, 0))
        self.resultTable.setObjectName("resultTable")
        self.horizontalLayout_2.addWidget(self.resultTable)
        self.outputTextView = QtWidgets.QTextEdit(self.centralwidget)
        self.outputTextView.setObjectName("outputTextView")
        self.horizontalLayout_2.addWidget(self.outputTextView)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 724, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Connection string"))
        self.executeBtn.setText(_translate("MainWindow", "Execute"))
