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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGraphicsView, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QSpinBox, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(903, 789)
        self.about_programm = QAction(MainWindow)
        self.about_programm.setObjectName(u"about_programm")
        self.about_author = QAction(MainWindow)
        self.about_author.setObjectName(u"about_author")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(295, 140))
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(295, 16777215))

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

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(295, 80))
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
        self.groupBox_2.setMaximumSize(QSize(295, 16777215))
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 4)

        self.spinBox_add_x = QSpinBox(self.groupBox_2)
        self.spinBox_add_x.setObjectName(u"spinBox_add_x")
        self.spinBox_add_x.setMinimum(-100000)
        self.spinBox_add_x.setMaximum(100000)

        self.gridLayout_2.addWidget(self.spinBox_add_x, 1, 1, 1, 1)

        self.spinBox_add_y = QSpinBox(self.groupBox_2)
        self.spinBox_add_y.setObjectName(u"spinBox_add_y")
        self.spinBox_add_y.setMinimum(-100000)
        self.spinBox_add_y.setMaximum(100000)

        self.gridLayout_2.addWidget(self.spinBox_add_y, 1, 3, 1, 1)

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
        self.tableWidget_ribs.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_ribs.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_ribs.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_ribs.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.gridLayout_2.addWidget(self.tableWidget_ribs, 2, 0, 1, 5)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(19, 29))

        self.gridLayout_2.addWidget(self.label_6, 1, 2, 1, 1)

        self.pushButton_dot_add = QPushButton(self.groupBox_2)
        self.pushButton_dot_add.setObjectName(u"pushButton_dot_add")
        self.pushButton_dot_add.setMaximumSize(QSize(29, 29))

        self.gridLayout_2.addWidget(self.pushButton_dot_add, 1, 4, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(19, 29))

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.pushButton_autoconnect = QPushButton(self.groupBox_2)
        self.pushButton_autoconnect.setObjectName(u"pushButton_autoconnect")

        self.gridLayout_2.addWidget(self.pushButton_autoconnect, 3, 0, 1, 3)


        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(295, 143))
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.spinBox_delay = QSpinBox(self.groupBox_3)
        self.spinBox_delay.setObjectName(u"spinBox_delay")
        self.spinBox_delay.setMaximum(10000)

        self.gridLayout_4.addWidget(self.spinBox_delay, 0, 1, 1, 1)

        self.pushButton_fill = QPushButton(self.groupBox_3)
        self.pushButton_fill.setObjectName(u"pushButton_fill")

        self.gridLayout_4.addWidget(self.pushButton_fill, 2, 0, 1, 2)

        self.radioButton_delay = QRadioButton(self.groupBox_3)
        self.radioButton_delay.setObjectName(u"radioButton_delay")

        self.gridLayout_4.addWidget(self.radioButton_delay, 0, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_fill_time = QLabel(self.groupBox_3)
        self.label_fill_time.setObjectName(u"label_fill_time")

        self.gridLayout_4.addWidget(self.label_fill_time, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 2, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 1, 1, 1)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 0, 2, 6, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 903, 25))
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.about_programm.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.about_author.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431 \u0430\u0432\u0442\u043e\u0440\u0435", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0446\u0432\u0435\u0442\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0437\u0430\u043b\u0438\u0432\u043a\u0438:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0440\u0435\u0431\u0440\u0430:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430:", None))
        self.pushButton_color_bg.setText("")
        self.pushButton_color_rib.setText("")
        self.pushButton_color_fill.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0432\u0430\u0441", None))
        self.pushButton_undo.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043a\u0438 \u0440\u0435\u0431\u0435\u0440", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u043e\u0447\u043a\u0443:", None))
        ___qtablewidgetitem = self.tableWidget_ribs.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem1 = self.tableWidget_ribs.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Y", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.pushButton_dot_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.pushButton_autoconnect.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u043a\u043d\u0443\u0442\u044c", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u0430\u0441\u043a\u0430", None))
        self.pushButton_fill.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u0430\u0441\u0438\u0442\u044c", None))
        self.radioButton_delay.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430 \u0437\u0430\u043b\u0438\u0432\u043a\u0438 (\u043c\u0441)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u043a\u0440\u0430\u0441\u043a\u0438 (\u0441\u0435\u043a):", None))
        self.label_fill_time.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e", None))
    # retranslateUi

