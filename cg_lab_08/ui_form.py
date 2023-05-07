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
        MainWindow.resize(1173, 907)
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
        self.groupBox_4.setMaximumSize(QSize(332, 80))
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
        self.groupBox_2.setMaximumSize(QSize(332, 16777215))
        self.gridLayout_8 = QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_8.addWidget(self.label_4, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.doubleSpinBox_line_x_b = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_line_x_b.setObjectName(u"doubleSpinBox_line_x_b")
        self.doubleSpinBox_line_x_b.setMinimum(-5000.000000000000000)
        self.doubleSpinBox_line_x_b.setMaximum(5000.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_line_x_b, 1, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(12, 16777215))

        self.gridLayout_4.addWidget(self.label_7, 3, 2, 1, 1)

        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(12, 16777215))

        self.gridLayout_4.addWidget(self.label_19, 1, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(12, 16777215))

        self.gridLayout_4.addWidget(self.label_6, 1, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 2)

        self.doubleSpinBox_line_x_e = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_line_x_e.setObjectName(u"doubleSpinBox_line_x_e")
        self.doubleSpinBox_line_x_e.setMinimum(-5000.000000000000000)
        self.doubleSpinBox_line_x_e.setMaximum(5000.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_line_x_e, 3, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 2, 0, 1, 2)

        self.doubleSpinBox_line_y_b = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_line_y_b.setObjectName(u"doubleSpinBox_line_y_b")
        self.doubleSpinBox_line_y_b.setMinimum(-5000.000000000000000)
        self.doubleSpinBox_line_y_b.setMaximum(5000.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_line_y_b, 1, 3, 1, 1)

        self.doubleSpinBox_line_y_e = QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_line_y_e.setObjectName(u"doubleSpinBox_line_y_e")
        self.doubleSpinBox_line_y_e.setMinimum(-5000.000000000000000)
        self.doubleSpinBox_line_y_e.setMaximum(5000.000000000000000)

        self.gridLayout_4.addWidget(self.doubleSpinBox_line_y_e, 3, 3, 1, 1)

        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 0))
        self.label_18.setMaximumSize(QSize(12, 16777215))

        self.gridLayout_4.addWidget(self.label_18, 3, 0, 1, 1)

        self.pushButton_line_add = QPushButton(self.groupBox_3)
        self.pushButton_line_add.setObjectName(u"pushButton_line_add")
        self.pushButton_line_add.setMinimumSize(QSize(0, 80))
        self.pushButton_line_add.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_4.addWidget(self.pushButton_line_add, 1, 5, 3, 1)


        self.gridLayout_8.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.tableWidget_lines = QTableWidget(self.groupBox_2)
        if (self.tableWidget_lines.columnCount() < 2):
            self.tableWidget_lines.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_lines.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_lines.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_lines.setObjectName(u"tableWidget_lines")
        self.tableWidget_lines.setMaximumSize(QSize(304, 16777215))
        font = QFont()
        font.setPointSize(7)
        font.setBold(False)
        self.tableWidget_lines.setFont(font)
        self.tableWidget_lines.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_lines.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_lines.setSelectionMode(QAbstractItemView.NoSelection)

        self.gridLayout_8.addWidget(self.tableWidget_lines, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(332, 16777215))
        self.gridLayout_6 = QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_cutter_connect = QPushButton(self.groupBox_5)
        self.pushButton_cutter_connect.setObjectName(u"pushButton_cutter_connect")

        self.gridLayout_6.addWidget(self.pushButton_cutter_connect, 3, 0, 1, 1)

        self.pushButton_cut = QPushButton(self.groupBox_5)
        self.pushButton_cut.setObjectName(u"pushButton_cut")

        self.gridLayout_6.addWidget(self.pushButton_cut, 3, 1, 1, 1)

        self.label_14 = QLabel(self.groupBox_5)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 0, 0, 1, 2)

        self.groupBox_6 = QGroupBox(self.groupBox_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.gridLayout_2 = QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_21 = QLabel(self.groupBox_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(12, 16777215))

        self.gridLayout_2.addWidget(self.label_21, 0, 0, 1, 1)

        self.doubleSpinBox_box_x_b = QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_box_x_b.setObjectName(u"doubleSpinBox_box_x_b")
        self.doubleSpinBox_box_x_b.setMinimum(-5000.000000000000000)
        self.doubleSpinBox_box_x_b.setMaximum(5000.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_box_x_b, 0, 1, 1, 1)

        self.doubleSpinBox_box_y_b = QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox_box_y_b.setObjectName(u"doubleSpinBox_box_y_b")
        self.doubleSpinBox_box_y_b.setMinimum(-5000.000000000000000)
        self.doubleSpinBox_box_y_b.setMaximum(5000.000000000000000)

        self.gridLayout_2.addWidget(self.doubleSpinBox_box_y_b, 0, 3, 1, 1)

        self.pushButton_box_add = QPushButton(self.groupBox_6)
        self.pushButton_box_add.setObjectName(u"pushButton_box_add")
        self.pushButton_box_add.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_box_add, 0, 4, 2, 1)

        self.label_16 = QLabel(self.groupBox_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(12, 16777215))

        self.gridLayout_2.addWidget(self.label_16, 0, 2, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox_6, 1, 0, 1, 2)

        self.tableWidget_cutter = QTableWidget(self.groupBox_5)
        if (self.tableWidget_cutter.columnCount() < 2):
            self.tableWidget_cutter.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_cutter.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_cutter.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.tableWidget_cutter.setObjectName(u"tableWidget_cutter")

        self.gridLayout_6.addWidget(self.tableWidget_cutter, 2, 0, 1, 2)


        self.gridLayout.addWidget(self.groupBox_5, 2, 1, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(332, 133))
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

        self.pushButton_color_line = QPushButton(self.groupBox)
        self.pushButton_color_line.setObjectName(u"pushButton_color_line")
        self.pushButton_color_line.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.pushButton_color_line, 2, 1, 1, 1)

        self.pushButton_color_cutted = QPushButton(self.groupBox)
        self.pushButton_color_cutted.setObjectName(u"pushButton_color_cutted")
        self.pushButton_color_cutted.setStyleSheet(u"background-color: rgb(0, 170, 0);")

        self.gridLayout_3.addWidget(self.pushButton_color_cutted, 3, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout.addWidget(self.graphicsView, 0, 2, 6, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1173, 21))
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u0430\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430. \u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u21168. \u041e\u0442\u0441\u0435\u043a\u0430\u0442\u0435\u043b\u044c", None))
        self.about_programm.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.about_author.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431 \u0430\u0432\u0442\u043e\u0440\u0435", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0432\u0430\u0441", None))
        self.pushButton_undo.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0440\u0435\u0437\u043a\u0438", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u043e\u0442\u0440\u0435\u0437\u043e\u043a \u0434\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u041b\u041a\u041c \u043f\u043e \u0445\u043e\u043b\u0441\u0442\u0443", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043e\u0442\u0440\u0435\u0437\u043e\u043a \u0441 \u043a\u043b\u0430\u0432\u0438\u0430\u0442\u0443\u0440\u044b:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043a\u0430 \u043d\u0430\u0447\u0430\u043b\u0430:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0447\u043a\u0430 \u043a\u043e\u043d\u0446\u0430:", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.pushButton_line_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        ___qtablewidgetitem = self.tableWidget_lines.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447. \u0442\u043e\u0447\u043a\u0430", None));
        ___qtablewidgetitem1 = self.tableWidget_lines.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d. \u0442\u043e\u0447\u043a\u0430", None));
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0435\u043a\u0430\u0442\u0435\u043b\u044c", None))
        self.pushButton_cutter_connect.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043c\u043a\u043d\u0443\u0442\u044c", None))
        self.pushButton_cut.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0435\u0447\u044c", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u0435\u043a\u0430\u0442\u0435\u043b\u044c \u043c\u0435\u043d\u044f\u0435\u0442\u0441\u044f \u043d\u0430\u0436\u0430\u0442\u0438\u0435\u043c \u041f\u041a\u041c \u043d\u0430 \u0445\u043e\u043b\u0441\u0442\u0435", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432\u0435\u0440\u0448\u0438\u043d\u0443 \u043e\u0442\u0441\u0435\u043a\u0430\u0442\u0435\u043b\u044f", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.pushButton_box_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        ___qtablewidgetitem2 = self.tableWidget_cutter.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem3 = self.tableWidget_cutter.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Y", None));
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0446\u0432\u0435\u0442\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u043e\u0442\u0441\u0435\u0447\u0435\u043d\u0438\u044f:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u043e\u0442\u0440\u0435\u0437\u043a\u043e\u0432:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430:", None))
        self.pushButton_color_bg.setText("")
        self.pushButton_color_line.setText("")
        self.pushButton_color_cutted.setText("")
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e", None))
    # retranslateUi

