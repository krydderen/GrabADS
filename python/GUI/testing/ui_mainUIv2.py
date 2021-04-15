# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUIv2DISQce.ui'
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
        MainWindow.resize(602, 695)
        palette = QPalette()
        brush = QBrush(QColor(252, 124, 44, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(81, 39, 77, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(227, 227, 227, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(160, 160, 160, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush5 = QBrush(QColor(105, 105, 105, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush5)
        brush6 = QBrush(QColor(0, 120, 215, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush6)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush2)
        brush7 = QBrush(QColor(0, 0, 255, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Link, brush7)
        brush8 = QBrush(QColor(255, 0, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush8)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush9 = QBrush(QColor(0, 0, 0, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.NoRole, brush9)
        brush10 = QBrush(QColor(255, 255, 220, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush5)
        brush11 = QBrush(QColor(240, 240, 240, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush11)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush8)
        brush12 = QBrush(QColor(245, 245, 245, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush12)
        brush13 = QBrush(QColor(0, 0, 0, 255))
        brush13.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.NoRole, brush13)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush12)
        brush14 = QBrush(QColor(0, 0, 0, 255))
        brush14.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.NoRole, brush14)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet(u"background-color: rgb(81, 39, 77);\n"
"color: rgb(252, 124, 44);\n"
"border-color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.titleTextLabel = QLabel(self.centralwidget)
        self.titleTextLabel.setObjectName(u"titleTextLabel")
        font = QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        self.titleTextLabel.setFont(font)
        self.titleTextLabel.setLayoutDirection(Qt.LeftToRight)
        self.titleTextLabel.setAutoFillBackground(False)
        self.titleTextLabel.setFrameShadow(QFrame.Plain)
        self.titleTextLabel.setTextFormat(Qt.AutoText)
        self.titleTextLabel.setScaledContents(False)
        self.titleTextLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.titleTextLabel)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.connectButton = QPushButton(self.centralwidget)
        self.connectButton.setObjectName(u"connectButton")
        self.connectButton.setMinimumSize(QSize(185, 60))
        self.connectButton.setMaximumSize(QSize(185, 16777215))
        font1 = QFont()
        font1.setPointSize(18)
        self.connectButton.setFont(font1)
        self.connectButton.setStyleSheet(u"background-color: rgb(73, 35, 69);\n"
"selection-color: rgb(255, 255, 255);")
        self.connectButton.setCheckable(True)
        self.connectButton.setChecked(False)
        self.connectButton.setFlat(False)

        self.verticalLayout.addWidget(self.connectButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.homingButton = QPushButton(self.centralwidget)
        self.homingButton.setObjectName(u"homingButton")
        self.homingButton.setMinimumSize(QSize(185, 60))
        self.homingButton.setMaximumSize(QSize(185, 16777215))
        self.homingButton.setFont(font1)
        self.homingButton.setStyleSheet(u"background-color: rgb(73, 35, 69);")
        self.homingButton.setCheckable(True)

        self.verticalLayout.addWidget(self.homingButton, 0, Qt.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.manualButton = QPushButton(self.centralwidget)
        self.manualButton.setObjectName(u"manualButton")
        self.manualButton.setMinimumSize(QSize(185, 60))
        self.manualButton.setMaximumSize(QSize(185, 16777215))
        self.manualButton.setFont(font1)
        self.manualButton.setStyleSheet(u"background-color: rgb(73, 35, 69);")

        self.verticalLayout.addWidget(self.manualButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.setPosButton = QPushButton(self.centralwidget)
        self.setPosButton.setObjectName(u"setPosButton")
        self.setPosButton.setEnabled(False)
        self.setPosButton.setMinimumSize(QSize(185, 60))
        self.setPosButton.setMaximumSize(QSize(185, 16777215))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush15 = QBrush(QColor(73, 35, 69, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush15)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        brush16 = QBrush(QColor(0, 0, 0, 255))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush16)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        brush17 = QBrush(QColor(50, 30, 48, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush17)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush18 = QBrush(QColor(0, 0, 0, 255))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.setPosButton.setPalette(palette1)
        self.setPosButton.setFont(font1)
        self.setPosButton.setStyleSheet(u"background-color: rgb(73, 35, 69);")

        self.verticalLayout.addWidget(self.setPosButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.pickBoxButton = QPushButton(self.centralwidget)
        self.pickBoxButton.setObjectName(u"pickBoxButton")
        self.pickBoxButton.setMinimumSize(QSize(185, 60))
        self.pickBoxButton.setMaximumSize(QSize(185, 16777215))
        self.pickBoxButton.setFont(font1)
        self.pickBoxButton.setStyleSheet(u"background-color: rgb(73, 35, 69);")
        self.pickBoxButton.setCheckable(True)
        self.pickBoxButton.setAutoDefault(False)

        self.verticalLayout.addWidget(self.pickBoxButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalWidget = QWidget(self.centralwidget)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_12)

        self.stateGroupBox = QGroupBox(self.horizontalWidget)
        self.stateGroupBox.setObjectName(u"stateGroupBox")
        self.stateGroupBox.setEnabled(True)
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(False)
        self.stateGroupBox.setFont(font2)
        self.stateGroupBox.setAutoFillBackground(False)
        self.stateGroupBox.setStyleSheet(u"selection-color: rgb(6, 255, 35);")
        self.stateGroupBox.setFlat(False)
        self.stateGroupBox.setCheckable(False)
        self.horizontalLayout_4 = QHBoxLayout(self.stateGroupBox)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.connectedRadioButton = QRadioButton(self.stateGroupBox)
        self.connectedRadioButton.setObjectName(u"connectedRadioButton")
        self.connectedRadioButton.setFont(font1)
        self.connectedRadioButton.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.connectedRadioButton)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_11)

        self.homingRadioButton = QRadioButton(self.stateGroupBox)
        self.homingRadioButton.setObjectName(u"homingRadioButton")
        font3 = QFont()
        font3.setPointSize(19)
        self.homingRadioButton.setFont(font3)
        self.homingRadioButton.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.homingRadioButton)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_10)

        self.pickboxRadioButton = QRadioButton(self.stateGroupBox)
        self.pickboxRadioButton.setObjectName(u"pickboxRadioButton")
        self.pickboxRadioButton.setFont(font1)
        self.pickboxRadioButton.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.pickboxRadioButton)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_9)

        self.errorRadioButton = QRadioButton(self.stateGroupBox)
        self.errorRadioButton.setObjectName(u"errorRadioButton")
        self.errorRadioButton.setMinimumSize(QSize(0, 0))
        self.errorRadioButton.setSizeIncrement(QSize(0, 0))
        self.errorRadioButton.setBaseSize(QSize(0, 0))
        self.errorRadioButton.setFont(font1)
        self.errorRadioButton.setMouseTracking(False)
        self.errorRadioButton.setIconSize(QSize(18, 18))
        self.errorRadioButton.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.errorRadioButton)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer_8)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addWidget(self.stateGroupBox)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_13)

        self.emergencyStopButton = QPushButton(self.horizontalWidget)
        self.emergencyStopButton.setObjectName(u"emergencyStopButton")
        self.emergencyStopButton.setMinimumSize(QSize(185, 185))
        self.emergencyStopButton.setMaximumSize(QSize(207, 16777215))
        font4 = QFont()
        font4.setPointSize(41)
        font4.setBold(True)
        font4.setUnderline(True)
        self.emergencyStopButton.setFont(font4)
        self.emergencyStopButton.setStyleSheet(u"background-color: rgb(73, 35, 69);")
        self.emergencyStopButton.setCheckable(True)

        self.verticalLayout_2.addWidget(self.emergencyStopButton)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_14)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_2.addWidget(self.horizontalWidget)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.connectButton, self.homingButton)
        QWidget.setTabOrder(self.homingButton, self.manualButton)
        QWidget.setTabOrder(self.manualButton, self.setPosButton)
        QWidget.setTabOrder(self.setPosButton, self.pickBoxButton)

        self.retranslateUi(MainWindow)
        self.connectButton.toggled.connect(self.connectCom)
        self.homingButton.toggled.connect(self.homing)
        self.pickBoxButton.toggled.connect(self.pickboxRadioButton.setChecked)
        self.manualButton.clicked.connect(self.menuToManual)
        self.pickBoxButton.clicked.connect(lambda : grab.newPickBox())

        self.pickBoxButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    
    def menuToManual(self):
        MainWindow.hide()
        grab.manualMode()
        ManualWindow.show()
    
    def connectCom(self):        
        if self.connectButton.isChecked():
            print('connected')
        #     grab.open()
            self.connectedRadioButton.setChecked(True)
        
        elif not self.connectButton.isChecked():
            print('disconnected')
        #     grab.close()
            self.connectedRadioButton.setChecked(False)
            
    def homing(self):
        
        logging.info('homing')
        self.homingRadioButton.setChecked(True)
        # grab.startHoming()
        self.homingButton.setStyleSheet("QPushButton{background-color: #58D68D;}")
        logging.info('done')
        self.homingRadioButton.setChecked(False)
        logging.info('is false')
        self.homingButton.setChecked(False)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleTextLabel.setText(QCoreApplication.translate("MainWindow", u"GRAB 2.0", None))
        self.connectButton.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.homingButton.setText(QCoreApplication.translate("MainWindow", u"Homing", None))
        self.manualButton.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.setPosButton.setText(QCoreApplication.translate("MainWindow", u"Set Position", None))
        self.pickBoxButton.setText(QCoreApplication.translate("MainWindow", u"Pick BOX", None))
        self.stateGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"States", None))
        self.connectedRadioButton.setText(QCoreApplication.translate("MainWindow", u"Connected", None))
        self.homingRadioButton.setText(QCoreApplication.translate("MainWindow", u"Homing", None))
        self.pickboxRadioButton.setText(QCoreApplication.translate("MainWindow", u"Picking Box", None))
        self.errorRadioButton.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.emergencyStopButton.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
    # retranslateUi



if __name__ == "__main__":
    import sys, os, qdarkstyle, time
    sys.path.append(os.path.abspath("python/ADS"))
    
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
#     app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    MainWindow.show()
    sys.exit(app.exec_())
