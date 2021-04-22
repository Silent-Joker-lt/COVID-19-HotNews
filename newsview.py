# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataView.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow
import service
from PyQt5.QtCore import QUrl
from PyQt5 import QtWebEngineWidgets

class Ui_NewsView(QMainWindow):
    def __init__(self):
        super(Ui_NewsView, self).__init__()
        #self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setupUi(self)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(949, 530)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/png/image/j2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 31))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(70, 50, 200, 41))
        self.comboBox.setObjectName("comboBox")
        #self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        #self.comboBox_2.setGeometry(QtCore.QRect(190, 50, 170, 41))
        #self.comboBox_2.setObjectName("comboBox_2")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 100, 800, 800))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.frame = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.frame.setGeometry(QtCore.QRect(830, 100, 1070, 800))
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(380, 50, 51, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(480, 50, 400, 41))#480, 50, 231, 41
        self.label_2.setObjectName("label_2")

        list_0 = ["国内疫情热点新闻", "全球疫情热点新闻"]
        self.comboBox.addItems(list_0)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "疫情热点新闻查看模块"))
        self.label.setText(_translate("Dialog", "新闻查看"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.label_2.setText(_translate("Dialog", "待选择"))

        self.comboBox.currentIndexChanged.connect(self.getname)
        self.pushButton.clicked.connect(self.datashow)
        self.tableWidget.cellDoubleClicked.connect(self.htmlview)



    def getname(self):
        part = self.comboBox.currentText()
        self.label_2.setText("您选择的是："+part)
    def datashow(self):
        self.tableWidget.setRowCount(0)
        part = self.comboBox.currentText()
        if part == "国内疫情热点新闻":
            result = service.query2("select * from 国内新闻")
        else:
            result = service.query2("select * from 国外新闻")
        row = len(result)
        namelist = ['id','时间', '事件简述', '事件地址', '事件来源']
        self.tableWidget.setRowCount(row)
        self.tableWidget.setColumnCount(len(namelist))
        self.tableWidget.setHorizontalHeaderLabels(namelist)
        for i in range(row):
            for j in range(self.tableWidget.columnCount()):
                data = QtWidgets.QTableWidgetItem(str(result[i][j]))
                self.tableWidget.setItem(i,j,data)
        self.tableWidget.verticalHeader().setVisible(False)
    def htmlview(self):
        a = self.tableWidget.currentColumn()
        b = self.tableWidget.currentRow()
        url = self.tableWidget.item(b,a).text()
        self.frame.load(QUrl(url))



# import sys
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_NewsView()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())