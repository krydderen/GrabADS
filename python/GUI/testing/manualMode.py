# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'grabynvIPC.ui'
##
## Created by: Qt User Interface Compiler version 6.0.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class manualModeWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"manualModeWindow")
        MainWindow.resize(870, 635)
        MainWindow.setMinimumSize(QSize(870, 635))
        MainWindow.setMaximumSize(QSize(870, 635))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(81, 39, 77);\n"
"color: rgb(252, 124, 44);\n"
"border-color: rgb(0, 0, 0);")
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
        self.zeroButton = QPushButton(self.horizontalLayoutWidget_2)
        self.zeroButton.setObjectName(u"zeroButton")
        self.zeroButton.setMinimumSize(QSize(80, 50))
        self.zeroButton.setMaximumSize(QSize(80, 50))
        font = QFont()
        font.setPointSize(10)
        self.zeroButton.setFont(font)
        self.zeroButton.setAutoDefault(False)
        self.zeroButton.setFlat(False)

        self.mainFunctionLayout.addWidget(self.zeroButton)

        self.stopButton = QPushButton(self.horizontalLayoutWidget_2)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setMinimumSize(QSize(80, 50))
        self.stopButton.setMaximumSize(QSize(80, 50))
        self.stopButton.setFont(font)
        self.stopButton.setAutoDefault(False)
        self.stopButton.setFlat(False)

        self.mainFunctionLayout.addWidget(self.stopButton)

        self.resetButton = QPushButton(self.horizontalLayoutWidget_2)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setMinimumSize(QSize(80, 50))
        self.resetButton.setMaximumSize(QSize(80, 50))
        self.resetButton.setFont(font)
        self.resetButton.setAutoDefault(False)
        self.resetButton.setFlat(False)

        self.mainFunctionLayout.addWidget(self.resetButton)

        self.disableButton = QPushButton(self.horizontalLayoutWidget_2)
        self.disableButton.setObjectName(u"disableButton")
        self.disableButton.setMinimumSize(QSize(80, 50))
        self.disableButton.setMaximumSize(QSize(80, 50))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setKerning(True)
        self.disableButton.setFont(font1)
        self.disableButton.setAutoDefault(False)
        self.disableButton.setFlat(False)

        self.mainFunctionLayout.addWidget(self.disableButton)

        self.menuButton = QPushButton(self.horizontalLayoutWidget_2)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setMinimumSize(QSize(80, 50))
        self.menuButton.setMaximumSize(QSize(80, 50))
        self.menuButton.setFont(font1)
        self.menuButton.setAutoDefault(False)
        self.menuButton.setFlat(False)

        self.mainFunctionLayout.addWidget(self.menuButton)


        self.functionsLayout.addWidget(self.mainFunctionGroup)

        self.axisFunctionsGroup = QGroupBox(self.horizontalLayoutWidget)
        self.axisFunctionsGroup.setObjectName(u"axisFunctionsGroup")
        self.axisFunctionsGroup.setMinimumSize(QSize(500, 490))
        self.axisFunctionsGroup.setMaximumSize(QSize(500, 490))
        self.axis1Group = QGroupBox(self.axisFunctionsGroup)
        self.axis1Group.setObjectName(u"axis1Group")
        self.axis1Group.setEnabled(False)
        self.axis1Group.setGeometry(QRect(10, 20, 231, 131))
        self.incrementAxis1 = QPushButton(self.axis1Group)
        self.incrementAxis1.setObjectName(u"incrementAxis1")
        self.incrementAxis1.setGeometry(QRect(20, 30, 91, 41))
        font2 = QFont()
        font2.setPointSize(16)
        self.incrementAxis1.setFont(font2)
        self.decrementAxis1 = QPushButton(self.axis1Group)
        self.decrementAxis1.setObjectName(u"decrementAxis1")
        self.decrementAxis1.setGeometry(QRect(20, 80, 91, 41))
        self.decrementAxis1.setFont(font2)
        self.zeroAxis1 = QPushButton(self.axis1Group)
        self.zeroAxis1.setObjectName(u"zeroAxis1")
        self.zeroAxis1.setGeometry(QRect(120, 80, 91, 41))
        self.zeroAxis1.setFont(font)
        self.axis2Group = QGroupBox(self.axisFunctionsGroup)
        self.axis2Group.setObjectName(u"axis2Group")
        self.axis2Group.setEnabled(False)
        self.axis2Group.setGeometry(QRect(10, 170, 231, 131))
        self.incrementAxis2 = QPushButton(self.axis2Group)
        self.incrementAxis2.setObjectName(u"incrementAxis2")
        self.incrementAxis2.setGeometry(QRect(20, 30, 91, 41))
        self.incrementAxis2.setFont(font2)
        self.decrementAxis2 = QPushButton(self.axis2Group)
        self.decrementAxis2.setObjectName(u"decrementAxis2")
        self.decrementAxis2.setGeometry(QRect(20, 80, 91, 41))
        self.decrementAxis2.setFont(font2)
        self.zeroAxis2 = QPushButton(self.axis2Group)
        self.zeroAxis2.setObjectName(u"zeroAxis2")
        self.zeroAxis2.setGeometry(QRect(120, 80, 91, 41))
        self.zeroAxis2.setFont(font)
        self.axis3Group = QGroupBox(self.axisFunctionsGroup)
        self.axis3Group.setObjectName(u"axis3Group")
        self.axis3Group.setEnabled(False)
        self.axis3Group.setGeometry(QRect(10, 320, 231, 131))
        self.incrementAxis3 = QPushButton(self.axis3Group)
        self.incrementAxis3.setObjectName(u"incrementAxis3")
        self.incrementAxis3.setGeometry(QRect(20, 30, 91, 41))
        self.incrementAxis3.setFont(font2)
        self.decrementAxis3 = QPushButton(self.axis3Group)
        self.decrementAxis3.setObjectName(u"decrementAxis3")
        self.decrementAxis3.setGeometry(QRect(20, 80, 91, 41))
        self.decrementAxis3.setFont(font2)
        self.zeroAxis3 = QPushButton(self.axis3Group)
        self.zeroAxis3.setObjectName(u"zeroAxis3")
        self.zeroAxis3.setGeometry(QRect(120, 80, 91, 41))
        self.zeroAxis3.setFont(font)
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
        self.zeroAxis4 = QPushButton(self.axis4Group)
        self.zeroAxis4.setObjectName(u"zeroAxis4")
        self.zeroAxis4.setGeometry(QRect(120, 80, 91, 41))
        self.zeroAxis4.setFont(font)
        self.axisEnableGroup = QGroupBox(self.axisFunctionsGroup)
        self.axisEnableGroup.setObjectName(u"axisEnableGroup")
        self.axisEnableGroup.setGeometry(QRect(250, 170, 231, 281))
        self.horizontalAxisEnableCheckBox = QCheckBox(self.axisEnableGroup)
        self.horizontalAxisEnableCheckBox.setObjectName(u"horizontalAxisEnableCheckBox")
        self.horizontalAxisEnableCheckBox.setGeometry(QRect(20, 30, 191, 41))
        self.rotationalAxisEnableCheckBox = QCheckBox(self.axisEnableGroup)
        self.rotationalAxisEnableCheckBox.setObjectName(u"rotationalAxisEnableCheckBox")
        self.rotationalAxisEnableCheckBox.setGeometry(QRect(20, 80, 191, 41))
        self.snakeAxisCheckBox = QCheckBox(self.axisEnableGroup)
        self.snakeAxisCheckBox.setObjectName(u"snakeAxisCheckBox")
        self.snakeAxisCheckBox.setEnabled(False)
        self.snakeAxisCheckBox.setGeometry(QRect(20, 180, 191, 41))
        self.verticalAxisEnableCheckBox = QCheckBox(self.axisEnableGroup)
        self.verticalAxisEnableCheckBox.setObjectName(u"verticalAxisEnableCheckBox")
        self.verticalAxisEnableCheckBox.setGeometry(QRect(20, 130, 191, 41))

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
        self.powerOnRadioButton = QRadioButton(self.verticalLayoutWidget_3)
        self.powerOnRadioButton.setObjectName(u"powerOnRadioButton")
        self.powerOnRadioButton.setFont(font)

        self.statusLayout.addWidget(self.powerOnRadioButton)

        self.connectedRadioButton = QRadioButton(self.verticalLayoutWidget_3)
        self.connectedRadioButton.setObjectName(u"connectedRadioButton")
        self.connectedRadioButton.setFont(font)

        self.statusLayout.addWidget(self.connectedRadioButton)

        self.enabledRadioButton = QRadioButton(self.verticalLayoutWidget_3)
        self.enabledRadioButton.setObjectName(u"enabledRadioButton")
        self.enabledRadioButton.setFont(font)

        self.statusLayout.addWidget(self.enabledRadioButton)

        self.readyForOperationRadioButton = QRadioButton(self.verticalLayoutWidget_3)
        self.readyForOperationRadioButton.setObjectName(u"readyForOperationRadioButton")
        self.readyForOperationRadioButton.setFont(font)

        self.statusLayout.addWidget(self.readyForOperationRadioButton)

        self.movingRadioButton = QRadioButton(self.verticalLayoutWidget_3)
        self.movingRadioButton.setObjectName(u"movingRadioButton")
        self.movingRadioButton.setFont(font)

        self.statusLayout.addWidget(self.movingRadioButton)

        self.stoppedRadioButton = QRadioButton(self.verticalLayoutWidget_3)
        self.stoppedRadioButton.setObjectName(u"stoppedRadioButton")
        self.stoppedRadioButton.setFont(font)

        self.statusLayout.addWidget(self.stoppedRadioButton)

        self.errorRadioButton = QRadioButton(self.verticalLayoutWidget_3)
        self.errorRadioButton.setObjectName(u"errorRadioButton")
        self.errorRadioButton.setFont(font)

        self.statusLayout.addWidget(self.errorRadioButton)


        self.verticalLayout.addWidget(self.statusGroup)


        self.mainHorizontalLayout.addWidget(self.verticalGroupBox)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.horizontalAxisEnableCheckBox.toggled.connect(self.axis1Group.setEnabled)
        self.rotationalAxisEnableCheckBox.toggled.connect(self.axis2Group.setEnabled)
        self.verticalAxisEnableCheckBox.toggled.connect(self.axis3Group.setEnabled)
        self.snakeAxisCheckBox.toggled.connect(self.axis4Group.setEnabled)
        self.disableButton.clicked.connect(self.horizontalAxisEnableCheckBox.setChecked)
        self.disableButton.clicked.connect(self.rotationalAxisEnableCheckBox.setChecked)
        self.disableButton.clicked.connect(self.verticalAxisEnableCheckBox.setChecked)
        self.disableButton.clicked.connect(self.snakeAxisCheckBox.setChecked)
        self.stopButton.clicked.connect(self.stoppedRadioButton.toggle)

        self.zeroButton.setDefault(False)
        self.stopButton.setDefault(False)
        self.resetButton.setDefault(False)
        self.disableButton.setDefault(False)
        self.menuButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Grab2.0", None))
        self.mainFunctionGroup.setTitle(QCoreApplication.translate("MainWindow", u"Main Functions", None))
        self.zeroButton.setText(QCoreApplication.translate("MainWindow", u"Zero", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.disableButton.setText(QCoreApplication.translate("MainWindow", u"Disable", None))
        self.menuButton.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.axisFunctionsGroup.setTitle(QCoreApplication.translate("MainWindow", u"Axis Functions", None))
        self.axis1Group.setTitle(QCoreApplication.translate("MainWindow", u"Axis 1", None))
        self.incrementAxis1.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.decrementAxis1.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.zeroAxis1.setText(QCoreApplication.translate("MainWindow", u"Zero", None))
        self.axis2Group.setTitle(QCoreApplication.translate("MainWindow", u"Axis 2", None))
        self.incrementAxis2.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.decrementAxis2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.zeroAxis2.setText(QCoreApplication.translate("MainWindow", u"Zero", None))
        self.axis3Group.setTitle(QCoreApplication.translate("MainWindow", u"Axis 3", None))
        self.incrementAxis3.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.decrementAxis3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.zeroAxis3.setText(QCoreApplication.translate("MainWindow", u"Zero", None))
        self.axis4Group.setTitle(QCoreApplication.translate("MainWindow", u"Axis 4", None))
        self.incrementAxis4.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.decrementAxis4.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.zeroAxis4.setText(QCoreApplication.translate("MainWindow", u"Zero", None))
        self.axisEnableGroup.setTitle(QCoreApplication.translate("MainWindow", u"Enable Axis", None))
        self.horizontalAxisEnableCheckBox.setText(QCoreApplication.translate("MainWindow", u"Horizontal Axis", None))
        self.rotationalAxisEnableCheckBox.setText(QCoreApplication.translate("MainWindow", u"Rotational Axis", None))
        self.snakeAxisCheckBox.setText(QCoreApplication.translate("MainWindow", u"Snake Axis", None))
        self.verticalAxisEnableCheckBox.setText(QCoreApplication.translate("MainWindow", u"Vertical Axis", None))
        self.statusGroup.setTitle(QCoreApplication.translate("MainWindow", u"Status", None))
        self.powerOnRadioButton.setText(QCoreApplication.translate("MainWindow", u"Power On", None))
        self.connectedRadioButton.setText(QCoreApplication.translate("MainWindow", u"Connected", None))
        self.enabledRadioButton.setText(QCoreApplication.translate("MainWindow", u"Enabled", None))
        self.readyForOperationRadioButton.setText(QCoreApplication.translate("MainWindow", u"Ready for operation", None))
        self.movingRadioButton.setText(QCoreApplication.translate("MainWindow", u"Moving", None))
        self.stoppedRadioButton.setText(QCoreApplication.translate("MainWindow", u"Stopped", None))
        self.errorRadioButton.setText(QCoreApplication.translate("MainWindow", u"Error", None))
    # retranslateUi

if __name__ == "__main__":
    import sys, os, qdarkstyle
    sys.path.append(os.path.abspath("python/ADS"))
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = manualModeWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())