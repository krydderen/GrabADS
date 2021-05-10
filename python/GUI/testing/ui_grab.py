# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'grabcGoVID.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(870, 635)
        MainWindow.setMinimumSize(QSize(870, 635))
        MainWindow.setMaximumSize(QSize(870, 635))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 851, 601))
        self.mainHorizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.mainHorizontalLayout.setObjectName(u"mainHorizontalLayout")
        self.mainHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.functionsLayout = QVBoxLayout()
        self.functionsLayout.setSpacing(6)
        self.functionsLayout.setObjectName(u"functionsLayout")
        self.functionsLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.mainFunctionGroup = QGroupBox(self.horizontalLayoutWidget)
        self.mainFunctionGroup.setObjectName(u"mainFunctionGroup")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFunctionGroup.sizePolicy().hasHeightForWidth())
        self.mainFunctionGroup.setSizePolicy(sizePolicy)
        self.mainFunctionGroup.setMaximumSize(QSize(500, 100))
        self.mainFunctionGroup.setAutoFillBackground(False)
        self.mainFunctionGroup.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.mainFunctionGroup.setFlat(False)
        self.mainFunctionGroup.setCheckable(False)
        self.horizontalLayoutWidget_2 = QWidget(self.mainFunctionGroup)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 20, 481, 61))
        self.mainFunctionLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.mainFunctionLayout.setObjectName(u"mainFunctionLayout")
        self.mainFunctionLayout.setContentsMargins(0, 0, 0, 0)
        
        self.homeButton = QPushButton(self.horizontalLayoutWidget_2)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setMinimumSize(QSize(80, 50))
        self.homeButton.setMaximumSize(QSize(80, 50))
        font = QFont()
        font.setPointSize(10)
        self.homeButton.setFont(font)
        self.homeButton.setAutoDefault(False)
        self.homeButton.setFlat(False)

        self.mainFunctionLayout.addWidget(self.homeButton)

        self.stopButton = QPushButton(self.horizontalLayoutWidget_2)
        self.stopButton.clicked.connect(lambda: grab.stopAllAxis())
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setMinimumSize(QSize(80, 50))
        self.stopButton.setMaximumSize(QSize(80, 50))
        self.stopButton.setFont(font)
        self.stopButton.setAutoDefault(False)
        self.stopButton.setFlat(False)

        self.mainFunctionLayout.addWidget(self.stopButton)

        self.resetButton = QPushButton(self.horizontalLayoutWidget_2)
        self.resetButton.clicked.connect(lambda: grab.resetAllAxis())
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setMinimumSize(QSize(80, 50))
        self.resetButton.setMaximumSize(QSize(80, 50))
        self.resetButton.setFont(font)
        self.resetButton.setAutoDefault(False)
        self.resetButton.setFlat(False)

        self.mainFunctionLayout.addWidget(self.resetButton)

        self.setButton = QPushButton(self.horizontalLayoutWidget_2)
        self.setButton.setObjectName(u"setButton")
        self.setButton.setMinimumSize(QSize(80, 50))
        self.setButton.setMaximumSize(QSize(80, 50))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        self.setButton.setFont(font1)
        self.setButton.setAutoDefault(False)
        self.setButton.setFlat(False)

        self.mainFunctionLayout.addWidget(self.setButton)


        self.functionsLayout.addWidget(self.mainFunctionGroup)

        self.axisFunctionsGroup = QGroupBox(self.horizontalLayoutWidget)
        self.axisFunctionsGroup.setObjectName(u"axisFunctionsGroup")
        self.axisFunctionsGroup.setMinimumSize(QSize(500, 490))
        self.axisFunctionsGroup.setMaximumSize(QSize(500, 490))
        self.axis1Group = QGroupBox(self.axisFunctionsGroup)
        self.axis1Group.setObjectName(u"axis1Group")
        self.axis1Group.setGeometry(QRect(10, 20, 231, 131))
        
        self.incrementAxis1 = QPushButton(self.axis1Group)
        self.incrementAxis1.setObjectName(u"incrementAxis1")
        self.incrementAxis1.pressed.connect(lambda: grab.startExtendSnake())
        self.incrementAxis1.released.connect(lambda: grab.stopExtendSnake())
        self.incrementAxis1.setGeometry(QRect(20, 30, 91, 41))
        font2 = QFont()
        font2.setPointSize(16)
        self.incrementAxis1.setFont(font2)
        
        self.decrementAxis1 = QPushButton(self.axis1Group)
        self.decrementAxis1.setObjectName(u"decrementAxis1")
        self.decrementAxis1.setGeometry(QRect(20, 80, 91, 41))
        self.decrementAxis1.setFont(font2)
        
        self.homeAxis1 = QPushButton(self.axis1Group)
        self.homeAxis1.setObjectName(u"homeAxis1")
        self.homeAxis1.setGeometry(QRect(120, 80, 91, 41))
        self.homeAxis1.setFont(font)
        
        self.goToAxis1 = QLineEdit(self.axis1Group)
        self.goToAxis1.setObjectName(u"goToAxis1")
        self.goToAxis1.setGeometry(QRect(120, 30, 91, 41))
        self.goToAxis1.setFont(font)
        self.goToAxis1.setContextMenuPolicy(Qt.CustomContextMenu)
        self.goToAxis1.setMaxLength(100)
        self.goToAxis1.setAlignment(Qt.AlignCenter)
        self.goToAxis1.setClearButtonEnabled(False)
        
        self.axis2Group = QGroupBox(self.axisFunctionsGroup)
        self.axis2Group.setObjectName(u"axis2Group")
        self.axis2Group.setGeometry(QRect(10, 170, 231, 131))
        
        self.incrementAxis2 = QPushButton(self.axis2Group)
        self.incrementAxis2.setObjectName(u"incrementAxis2")
        self.incrementAxis2.setGeometry(QRect(20, 30, 91, 41))
        self.incrementAxis2.setFont(font2)
        
        self.decrementAxis2 = QPushButton(self.axis2Group)
        self.decrementAxis2.setObjectName(u"decrementAxis2")
        self.decrementAxis2.setGeometry(QRect(20, 80, 91, 41))
        self.decrementAxis2.setFont(font2)
        
        self.homeAxis2 = QPushButton(self.axis2Group)
        self.homeAxis2.setObjectName(u"homeAxis2")
        self.homeAxis2.setGeometry(QRect(120, 80, 91, 41))
        self.homeAxis2.setFont(font)
        
        self.goToAxis2 = QLineEdit(self.axis2Group)
        self.goToAxis2.setObjectName(u"goToAxis2")
        self.goToAxis2.setGeometry(QRect(120, 30, 91, 41))
        self.goToAxis2.setFont(font)
        self.goToAxis2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.goToAxis2.setMaxLength(100)
        self.goToAxis2.setAlignment(Qt.AlignCenter)
        self.goToAxis2.setClearButtonEnabled(False)
        
        self.axis3Group = QGroupBox(self.axisFunctionsGroup)
        self.axis3Group.setObjectName(u"axis3Group")
        self.axis3Group.setGeometry(QRect(10, 320, 231, 131))
        
        self.incrementAxis3 = QPushButton(self.axis3Group)
        self.incrementAxis3.setObjectName(u"incrementAxis3")
        self.incrementAxis3.setGeometry(QRect(20, 30, 91, 41))
        self.incrementAxis3.setFont(font2)
        
        self.decrementAxis3 = QPushButton(self.axis3Group)
        self.decrementAxis3.setObjectName(u"decrementAxis3")
        self.decrementAxis3.setGeometry(QRect(20, 80, 91, 41))
        self.decrementAxis3.setFont(font2)
        
        self.homeAxis3 = QPushButton(self.axis3Group)
        self.homeAxis3.setObjectName(u"homeAxis3")
        self.homeAxis3.setGeometry(QRect(120, 80, 91, 41))
        self.homeAxis3.setFont(font)
        
        self.goToAxis3 = QLineEdit(self.axis3Group)
        self.goToAxis3.setObjectName(u"goToAxis3")
        self.goToAxis3.setGeometry(QRect(120, 30, 91, 41))
        self.goToAxis3.setFont(font)
        self.goToAxis3.setContextMenuPolicy(Qt.CustomContextMenu)
        self.goToAxis3.setMaxLength(100)
        self.goToAxis3.setAlignment(Qt.AlignCenter)
        self.goToAxis3.setClearButtonEnabled(False)
        
        self.axis4Group = QGroupBox(self.axisFunctionsGroup)
        self.axis4Group.setObjectName(u"axis4Group")
        self.axis4Group.setEnabled(False)
        self.axis4Group.setGeometry(QRect(250, 20, 231, 131))
        
        self.incrementAxis4 = QPushButton(self.axis4Group)
        self.incrementAxis4.setObjectName(u"incrementAxis4")
        self.incrementAxis4.setGeometry(QRect(20, 30, 91, 41))
        self.incrementAxis4.setFont(font2)
        
        self.decrementAxis4 = QPushButton(self.axis4Group)
        self.decrementAxis4.setObjectName(u"decrementAxis4")
        self.decrementAxis4.setGeometry(QRect(20, 80, 91, 41))
        self.decrementAxis4.setFont(font2)
        
        self.homeAxis4 = QPushButton(self.axis4Group)
        self.homeAxis4.setObjectName(u"homeAxis4")
        self.homeAxis4.setGeometry(QRect(120, 80, 91, 41))
        self.homeAxis4.setFont(font)
        
        self.goToAxis4 = QLineEdit(self.axis4Group)
        self.goToAxis4.setObjectName(u"goToAxis4")
        self.goToAxis4.setGeometry(QRect(120, 30, 91, 41))
        self.goToAxis4.setFont(font)
        self.goToAxis4.setContextMenuPolicy(Qt.CustomContextMenu)
        self.goToAxis4.setMaxLength(100)
        self.goToAxis4.setAlignment(Qt.AlignCenter)
        self.goToAxis4.setClearButtonEnabled(False)

        self.functionsLayout.addWidget(self.axisFunctionsGroup)


        self.mainHorizontalLayout.addLayout(self.functionsLayout)

        self.verticalGroupBox = QGroupBox(self.horizontalLayoutWidget)
        self.verticalGroupBox.setObjectName(u"verticalGroupBox")
        self.verticalGroupBox.setMinimumSize(QSize(200, 393))
        self.verticalGroupBox.setMaximumSize(QSize(200, 16777215))
        self.verticalGroupBox.setFlat(False)
        self.verticalLayout = QVBoxLayout(self.verticalGroupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.statusGroup = QGroupBox(self.verticalGroupBox)
        self.statusGroup.setObjectName(u"statusGroup")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.statusGroup.sizePolicy().hasHeightForWidth())
        self.statusGroup.setSizePolicy(sizePolicy1)
        self.statusGroup.setMaximumSize(QSize(415, 597))
        self.verticalLayoutWidget_3 = QWidget(self.statusGroup)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(20, 20, 161, 221))
        self.statusLayout = QVBoxLayout(self.verticalLayoutWidget_3)
        self.statusLayout.setObjectName(u"statusLayout")
        self.statusLayout.setContentsMargins(0, 0, 0, 0)
        self.powerOn = QRadioButton(self.verticalLayoutWidget_3)
        self.powerOn.setObjectName(u"powerOn")
        self.powerOn.setFont(font)

        self.statusLayout.addWidget(self.powerOn)

        self.enabled = QRadioButton(self.verticalLayoutWidget_3)
        self.enabled.setObjectName(u"enabled")
        self.enabled.setFont(font)

        self.statusLayout.addWidget(self.enabled)

        self.readyForOperation = QRadioButton(self.verticalLayoutWidget_3)
        self.readyForOperation.setObjectName(u"readyForOperation")
        self.readyForOperation.setFont(font)

        self.statusLayout.addWidget(self.readyForOperation)

        self.moving = QRadioButton(self.verticalLayoutWidget_3)
        self.moving.setObjectName(u"moving")
        self.moving.setFont(font)

        self.statusLayout.addWidget(self.moving)

        self.stopped = QRadioButton(self.verticalLayoutWidget_3)
        self.stopped.setObjectName(u"stopped")
        self.stopped.setFont(font)

        self.statusLayout.addWidget(self.stopped)

        self.error = QRadioButton(self.verticalLayoutWidget_3)
        self.error.setObjectName(u"error")
        self.error.setFont(font)

        self.statusLayout.addWidget(self.error)


        self.verticalLayout.addWidget(self.statusGroup)


        self.mainHorizontalLayout.addWidget(self.verticalGroupBox)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.homeButton.setDefault(False)
        self.stopButton.setDefault(False)
        self.resetButton.setDefault(False)
        self.setButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Grab2.0", None))
        self.mainFunctionGroup.setTitle(QCoreApplication.translate("MainWindow", u"Main Functions", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.setButton.setText(QCoreApplication.translate("MainWindow", u"Set", None))
        self.axisFunctionsGroup.setTitle(QCoreApplication.translate("MainWindow", u"Axis Functions", None))
        self.axis1Group.setTitle(QCoreApplication.translate("MainWindow", u"Axis 1", None))
        self.incrementAxis1.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.decrementAxis1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.homeAxis1.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.goToAxis1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Go to value", None))
        self.axis2Group.setTitle(QCoreApplication.translate("MainWindow", u"Axis 2", None))
        self.incrementAxis2.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.decrementAxis2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.homeAxis2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.goToAxis2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Go to value", None))
        self.axis3Group.setTitle(QCoreApplication.translate("MainWindow", u"Axis 3", None))
        self.incrementAxis3.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.decrementAxis3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.homeAxis3.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.goToAxis3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Go to value", None))
        self.axis4Group.setTitle(QCoreApplication.translate("MainWindow", u"Axis 4", None))
        self.incrementAxis4.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.decrementAxis4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.homeAxis4.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.goToAxis4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Go to value", None))
        self.statusGroup.setTitle(QCoreApplication.translate("MainWindow", u"Status", None))
        self.powerOn.setText(QCoreApplication.translate("MainWindow", u"Power On", None))
        self.enabled.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.readyForOperation.setText(QCoreApplication.translate("MainWindow", u"Ready for operation", None))
        self.moving.setText(QCoreApplication.translate("MainWindow", u"Moving", None))
        self.stopped.setText(QCoreApplication.translate("MainWindow", u"Stopped", None))
        self.error.setText(QCoreApplication.translate("MainWindow", u"Error", None))
    # retranslateUi
    
if __name__ == "__main__":
    import sys, os, qdarkstyle
    sys.path.append(os.path.abspath("python/ADS"))
    
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow.show()
    sys.exit(app.exec_())
