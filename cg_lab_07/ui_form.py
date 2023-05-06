# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDoubleSpinBox, QGraphicsView,
    QGridLayout, QGroupBox, QHeaderView, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1004, 785)
        self.about_programm = QAction(MainWindow)
        self.about_programm.setObjectName(u"about_programm")
        self.about_author = QAction(MainWindow)
        self.about_author.setObjectName(u"about_author")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(276, 71))
        self.groupBox_4.setMaximumSize(QSize(276, 71))
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_undo = QPushButton(self.groupBox_4)
        self.pushButton_undo.setObjectName(u"pushButton_undo")

        self.gridLayout_5.addWidget(self.pushButton_undo, 0, 0, 1, 1)

        self.pushButton_clear = QPushButton(self.groupBox_4)
        self.pushButton_clear.setObjectName(u"pushButton_clear")

        self.gridLayout_5.addWidget(self.pushButton_clear, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 4, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(276, 297))
        self.groupBox_2.setMaximumSize(QSize(276, 16777215))
        self.gridLayout_8 = QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_8.addWidget(self.label_4, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 2)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(12, 16777215))

        self.gridLayout_4.addWidget(self.label_6, 1, 2, 1, 1)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setMinimum(-5000.000000000000000)
        self.doubleSpinBox_3.setMaximum(5000.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_3, 3, 1, 1, 1)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 0))
        self.label_18.setMaximumSize(QSize(12, 16777215))

        self.gridLayout_4.addWidget(self.label_18, 3, 0, 1, 1)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")
        self.doubleSpinBox_4.setMinimum(-5000.000000000000000)
        self.doubleSpinBox_4.setMaximum(5000.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_4, 3, 3, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMinimum(-5000.000000000000000)
        self.doubleSpinBox.setMaximum(5000.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox, 1, 1, 1, 1)

        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(12, 16777215))

        self.gridLayout_4.addWidget(self.label_19, 1, 0, 1, 1)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")
        self.doubleSpinBox_2.setMinimum(-5000.000000000000000)
        self.doubleSpinBox_2.setMaximum(5000.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_2, 1, 3, 1, 1)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 2)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(12, 16777215))

        self.gridLayout_4.addWidget(self.label_7, 3, 2, 1, 1)

        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 80))
        self.pushButton.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_4.addWidget(self.pushButton, 1, 4, 3, 1)


        self.gridLayout_8.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.tableWidget_ribs = QTableWidget(self.groupBox_2)
        if (self.tableWidget_ribs.columnCount() < 2):
            self.tableWidget_ribs.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_ribs.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_ribs.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_ribs.setObjectName(u"tableWidget_ribs")
        font = QFont()
        font.setPointSize(7)
        font.setBold(False)
        self.tableWidget_ribs.setFont(font)
        self.tableWidget_ribs.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_ribs.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_ribs.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_ribs.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_ribs.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_8.addWidget(self.tableWidget_ribs, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(276, 220))
        self.gridLayout_9 = QGridLayout(self.groupBox_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_14 = QLabel(self.groupBox_5)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_9.addWidget(self.label_14, 0, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_2 = QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.doubleSpinBox_5 = QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setMinimum(-5000.000000000000000)
        self.doubleSpinBox_5.setMaximum(5000.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_5, 1, 1, 1, 1)

        self.label_22 = QLabel(self.groupBox_6)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_2.addWidget(self.label_22, 0, 0, 1, 4)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")
        self.doubleSpinBox_7.setMinimum(-5000.000000000000000)
        self.doubleSpinBox_7.setMaximum(5000.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_7, 1, 3, 1, 1)

        self.doubleSpinBox_8 = QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")
        self.doubleSpinBox_8.setMinimum(-5000.000000000000000)
        self.doubleSpinBox_8.setMaximum(5000.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_8, 3, 3, 1, 1)

        self.label_20 = QLabel(self.groupBox_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 0))
        self.label_20.setMaximumSize(QSize(12, 16777215))

        self.gridLayout_2.addWidget(self.label_20, 3, 0, 1, 1)

        self.label_21 = QLabel(self.groupBox_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(12, 16777215))

        self.gridLayout_2.addWidget(self.label_21, 1, 0, 1, 1)

        self.label_15 = QLabel(self.groupBox_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(12, 16777215))

        self.gridLayout_2.addWidget(self.label_15, 3, 2, 1, 1)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        self.doubleSpinBox_6.setMinimum(-5000.000000000000000)
        self.doubleSpinBox_6.setMaximum(5000.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_6, 3, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(12, 16777215))

        self.gridLayout_2.addWidget(self.label_16, 1, 2, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 80))
        self.pushButton_2.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_2, 1, 4, 3, 1)

        self.label_23 = QLabel(self.groupBox_6)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_2.addWidget(self.label_23, 2, 0, 1, 4)


        self.gridLayout_9.addWidget(self.groupBox_6, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_5, 2, 1, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(276, 133))
        self.groupBox.setMaximumSize(QSize(276, 133))
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_color_bg = QPushButton(self.groupBox)
        self.pushButton_color_bg.setObjectName(u"pushButton_color_bg")
        self.pushButton_color_bg.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_3.addWidget(self.pushButton_color_bg, 0, 1, 1, 1)

        self.pushButton_color_rib = QPushButton(self.groupBox)
        self.pushButton_color_rib.setObjectName(u"pushButton_color_rib")
        self.pushButton_color_rib.setStyleSheet(u"background-color: rgb(170, 0, 0);")

        self.gridLayout_3.addWidget(self.pushButton_color_rib, 2, 1, 1, 1)

        self.pushButton_color_fill = QPushButton(self.groupBox)
        self.pushButton_color_fill.setObjectName(u"pushButton_color_fill")
        self.pushButton_color_fill.setStyleSheet(u"background-color: rgb(0, 170, 0);")

        self.gridLayout_3.addWidget(self.pushButton_color_fill, 3, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 0, 2, 6, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1004, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.about_programm)
        self.menu.addAction(self.about_author)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u0430\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430. \u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u21167. \u041e\u0442\u0441\u0435\u043a\u0430\u0442\u0435\u043b\u044c", None))
        self.about_programm.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.about_author.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431 \u0430\u0432\u0442\u043e\u0440\u0435", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0432\u0430\u0441", None))
        self.pushButton_undo.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0440\u0435\u0437\u043a\u0438", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u043e\u0442\u0440\u0435\u0437\u043e\u043a \u0434\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u041b\u041a\u041c \u043f\u043e \u0445\u043e\u043b\u0441\u0442\u0443", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0442\u0440\u0435\u0437\u043e\u043a \u0441 \u043a\u043b\u0430\u0432\u0438\u0430\u0442\u0443\u0440\u044b:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043a\u0430 \u043d\u0430\u0447\u0430\u043b\u0430:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043a\u0430 \u043a\u043e\u043d\u0446\u0430:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        ___qtablewidgetitem = self.tableWidget_ribs.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447. \u0442\u043e\u0447\u043a\u0430", None));
        ___qtablewidgetitem1 = self.tableWidget_ribs.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d. \u0442\u043e\u0447\u043a\u0430", None));
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0435\u043a\u0430\u0442\u0435\u043b\u044c", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0435\u043a\u0430\u0442\u0435\u043b\u044c \u043c\u0435\u043d\u044f\u0435\u0442\u0441\u044f \u0443\u0434\u0435\u0440\u0436. \u041f\u041a\u041c \u043d\u0430 \u0445\u043e\u043b\u0441\u0442\u0435", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043e\u0442\u0441\u0435\u043a\u0430\u0442\u0435\u043b\u044c \u0441 \u043a\u043b\u0430\u0432\u0438\u0430\u0442\u0443\u0440\u044b:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0435\u0432\u0430\u044f \u0432\u0435\u0440\u0445\u043d\u044f\u044f \u0442\u043e\u0447\u043a\u0430:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u0430\u044f \u043d\u0438\u0436\u043d\u044f\u044f \u0442\u043e\u0447\u043a\u0430:", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0446\u0432\u0435\u0442\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u043e\u0442\u0441\u0435\u0447\u0435\u043d\u0438\u044f:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u043e\u0442\u0440\u0435\u0437\u043a\u043e\u0432:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430:", None))
        self.pushButton_color_bg.setText("")
        self.pushButton_color_rib.setText("")
        self.pushButton_color_fill.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e", None))
    # retranslateUi

