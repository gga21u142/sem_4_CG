# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(983, 630)
        MainWindow.setMinimumSize(QtCore.QSize(983, 630))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.groupBox_main = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_main.setMinimumSize(QtCore.QSize(379, 575))
        self.groupBox_main.setMaximumSize(QtCore.QSize(379, 575))
        font = QtGui.QFont()
        font.setKerning(True)
        self.groupBox_main.setFont(font)
        self.groupBox_main.setTitle("")
        self.groupBox_main.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.groupBox_main.setObjectName("groupBox_main")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_main)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_settings = QtWidgets.QGroupBox(self.groupBox_main)
        self.groupBox_settings.setMinimumSize(QtCore.QSize(355, 170))
        self.groupBox_settings.setMaximumSize(QtCore.QSize(355, 170))
        self.groupBox_settings.setObjectName("groupBox_settings")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_settings)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox_color_line = QtWidgets.QGroupBox(self.groupBox_settings)
        self.groupBox_color_line.setMinimumSize(QtCore.QSize(160, 60))
        self.groupBox_color_line.setMaximumSize(QtCore.QSize(160, 60))
        self.groupBox_color_line.setObjectName("groupBox_color_line")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_color_line)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.comboBox_color_line = QtWidgets.QComboBox(self.groupBox_color_line)
        self.comboBox_color_line.setMinimumSize(QtCore.QSize(118, 22))
        self.comboBox_color_line.setMaximumSize(QtCore.QSize(118, 22))
        self.comboBox_color_line.setObjectName("comboBox_color_line")
        self.comboBox_color_line.addItem("")
        self.comboBox_color_line.addItem("")
        self.comboBox_color_line.addItem("")
        self.comboBox_color_line.addItem("")
        self.comboBox_color_line.addItem("")
        self.comboBox_color_line.addItem("")
        self.comboBox_color_line.addItem("")
        self.comboBox_color_line.addItem("")
        self.comboBox_color_line.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_color_line, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_color_line, 0, 0, 1, 1)
        self.groupBox_color_bg = QtWidgets.QGroupBox(self.groupBox_settings)
        self.groupBox_color_bg.setMinimumSize(QtCore.QSize(160, 60))
        self.groupBox_color_bg.setMaximumSize(QtCore.QSize(160, 60))
        self.groupBox_color_bg.setObjectName("groupBox_color_bg")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_color_bg)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.comboBox_color_bg = QtWidgets.QComboBox(self.groupBox_color_bg)
        self.comboBox_color_bg.setMinimumSize(QtCore.QSize(118, 22))
        self.comboBox_color_bg.setMaximumSize(QtCore.QSize(118, 22))
        self.comboBox_color_bg.setObjectName("comboBox_color_bg")
        self.comboBox_color_bg.addItem("")
        self.comboBox_color_bg.addItem("")
        self.comboBox_color_bg.addItem("")
        self.comboBox_color_bg.addItem("")
        self.comboBox_color_bg.addItem("")
        self.comboBox_color_bg.addItem("")
        self.comboBox_color_bg.addItem("")
        self.comboBox_color_bg.addItem("")
        self.comboBox_color_bg.addItem("")
        self.gridLayout_6.addWidget(self.comboBox_color_bg, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_color_bg, 0, 1, 1, 1)
        self.groupBox_method = QtWidgets.QGroupBox(self.groupBox_settings)
        self.groupBox_method.setMinimumSize(QtCore.QSize(326, 60))
        self.groupBox_method.setMaximumSize(QtCore.QSize(326, 60))
        self.groupBox_method.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_method.setFlat(False)
        self.groupBox_method.setObjectName("groupBox_method")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_method)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.comboBox_method = QtWidgets.QComboBox(self.groupBox_method)
        self.comboBox_method.setMinimumSize(QtCore.QSize(246, 22))
        self.comboBox_method.setMaximumSize(QtCore.QSize(246, 22))
        self.comboBox_method.setObjectName("comboBox_method")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.gridLayout_7.addWidget(self.comboBox_method, 0, 1, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_method, 1, 0, 1, 2, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.gridLayout_2.addWidget(self.groupBox_settings, 0, 0, 1, 4)
        self.groupBox_compare = QtWidgets.QGroupBox(self.groupBox_main)
        self.groupBox_compare.setMinimumSize(QtCore.QSize(355, 68))
        self.groupBox_compare.setMaximumSize(QtCore.QSize(355, 68))
        self.groupBox_compare.setObjectName("groupBox_compare")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_compare)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_time = QtWidgets.QPushButton(self.groupBox_compare)
        self.pushButton_time.setMinimumSize(QtCore.QSize(162, 28))
        self.pushButton_time.setMaximumSize(QtCore.QSize(162, 28))
        self.pushButton_time.setObjectName("pushButton_time")
        self.horizontalLayout.addWidget(self.pushButton_time)
        self.pushButton_stairs = QtWidgets.QPushButton(self.groupBox_compare)
        self.pushButton_stairs.setMinimumSize(QtCore.QSize(162, 28))
        self.pushButton_stairs.setMaximumSize(QtCore.QSize(162, 28))
        self.pushButton_stairs.setObjectName("pushButton_stairs")
        self.horizontalLayout.addWidget(self.pushButton_stairs)
        self.gridLayout_2.addWidget(self.groupBox_compare, 3, 0, 1, 1)
        self.groupBox_draw = QtWidgets.QGroupBox(self.groupBox_main)
        self.groupBox_draw.setMinimumSize(QtCore.QSize(355, 224))
        self.groupBox_draw.setMaximumSize(QtCore.QSize(355, 224))
        self.groupBox_draw.setObjectName("groupBox_draw")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.groupBox_draw)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox_draw_line = QtWidgets.QGroupBox(self.groupBox_draw)
        self.groupBox_draw_line.setObjectName("groupBox_draw_line")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_draw_line)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.doubleSpinBox_ye = QtWidgets.QDoubleSpinBox(self.groupBox_draw_line)
        self.doubleSpinBox_ye.setMinimumSize(QtCore.QSize(100, 22))
        self.doubleSpinBox_ye.setMaximumSize(QtCore.QSize(100, 22))
        self.doubleSpinBox_ye.setDecimals(3)
        self.doubleSpinBox_ye.setMinimum(-99999.0)
        self.doubleSpinBox_ye.setMaximum(99999.0)
        self.doubleSpinBox_ye.setObjectName("doubleSpinBox_ye")
        self.gridLayout_3.addWidget(self.doubleSpinBox_ye, 6, 1, 1, 1)
        self.label_rotate_ys = QtWidgets.QLabel(self.groupBox_draw_line)
        self.label_rotate_ys.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_rotate_ys.setObjectName("label_rotate_ys")
        self.gridLayout_3.addWidget(self.label_rotate_ys, 2, 0, 1, 1)
        self.doubleSpinBox_xe = QtWidgets.QDoubleSpinBox(self.groupBox_draw_line)
        self.doubleSpinBox_xe.setMinimumSize(QtCore.QSize(100, 22))
        self.doubleSpinBox_xe.setMaximumSize(QtCore.QSize(100, 22))
        self.doubleSpinBox_xe.setDecimals(3)
        self.doubleSpinBox_xe.setMinimum(-99999.0)
        self.doubleSpinBox_xe.setMaximum(99999.0)
        self.doubleSpinBox_xe.setObjectName("doubleSpinBox_xe")
        self.gridLayout_3.addWidget(self.doubleSpinBox_xe, 4, 1, 1, 1)
        self.doubleSpinBox_ys = QtWidgets.QDoubleSpinBox(self.groupBox_draw_line)
        self.doubleSpinBox_ys.setMinimumSize(QtCore.QSize(100, 22))
        self.doubleSpinBox_ys.setMaximumSize(QtCore.QSize(100, 22))
        self.doubleSpinBox_ys.setDecimals(3)
        self.doubleSpinBox_ys.setMinimum(-99999.0)
        self.doubleSpinBox_ys.setMaximum(99999.0)
        self.doubleSpinBox_ys.setObjectName("doubleSpinBox_ys")
        self.gridLayout_3.addWidget(self.doubleSpinBox_ys, 2, 1, 1, 1)
        self.label_rotate_xe = QtWidgets.QLabel(self.groupBox_draw_line)
        self.label_rotate_xe.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_rotate_xe.setObjectName("label_rotate_xe")
        self.gridLayout_3.addWidget(self.label_rotate_xe, 4, 0, 1, 1)
        self.doubleSpinBox_xs = QtWidgets.QDoubleSpinBox(self.groupBox_draw_line)
        self.doubleSpinBox_xs.setMinimumSize(QtCore.QSize(100, 22))
        self.doubleSpinBox_xs.setMaximumSize(QtCore.QSize(100, 22))
        self.doubleSpinBox_xs.setDecimals(3)
        self.doubleSpinBox_xs.setMinimum(-99999.0)
        self.doubleSpinBox_xs.setMaximum(99999.0)
        self.doubleSpinBox_xs.setObjectName("doubleSpinBox_xs")
        self.gridLayout_3.addWidget(self.doubleSpinBox_xs, 0, 1, 1, 1)
        self.pushButton_draw_line = QtWidgets.QPushButton(self.groupBox_draw_line)
        self.pushButton_draw_line.setObjectName("pushButton_draw_line")
        self.gridLayout_3.addWidget(self.pushButton_draw_line, 7, 0, 1, 2)
        self.label_rotate_xs = QtWidgets.QLabel(self.groupBox_draw_line)
        self.label_rotate_xs.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_rotate_xs.setObjectName("label_rotate_xs")
        self.gridLayout_3.addWidget(self.label_rotate_xs, 0, 0, 1, 1)
        self.label_rotate_ye = QtWidgets.QLabel(self.groupBox_draw_line)
        self.label_rotate_ye.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_rotate_ye.setObjectName("label_rotate_ye")
        self.gridLayout_3.addWidget(self.label_rotate_ye, 6, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_draw_line, 1, 0, 1, 1)
        self.groupBox_draw_spectre = QtWidgets.QGroupBox(self.groupBox_draw)
        self.groupBox_draw_spectre.setObjectName("groupBox_draw_spectre")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_draw_spectre)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.doubleSpinBox_spectre_lenght = QtWidgets.QDoubleSpinBox(self.groupBox_draw_spectre)
        self.doubleSpinBox_spectre_lenght.setMinimumSize(QtCore.QSize(100, 22))
        self.doubleSpinBox_spectre_lenght.setMaximumSize(QtCore.QSize(100, 22))
        self.doubleSpinBox_spectre_lenght.setDecimals(3)
        self.doubleSpinBox_spectre_lenght.setMinimum(-99999.0)
        self.doubleSpinBox_spectre_lenght.setMaximum(99999.0)
        self.doubleSpinBox_spectre_lenght.setObjectName("doubleSpinBox_spectre_lenght")
        self.gridLayout_4.addWidget(self.doubleSpinBox_spectre_lenght, 4, 1, 1, 1)
        self.label_rotate_spectre_lenght = QtWidgets.QLabel(self.groupBox_draw_spectre)
        self.label_rotate_spectre_lenght.setObjectName("label_rotate_spectre_lenght")
        self.gridLayout_4.addWidget(self.label_rotate_spectre_lenght, 4, 0, 1, 1)
        self.pushButton_draw_spectre = QtWidgets.QPushButton(self.groupBox_draw_spectre)
        self.pushButton_draw_spectre.setObjectName("pushButton_draw_spectre")
        self.gridLayout_4.addWidget(self.pushButton_draw_spectre, 7, 0, 1, 2)
        self.label_rotate_spectre_degree = QtWidgets.QLabel(self.groupBox_draw_spectre)
        self.label_rotate_spectre_degree.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_rotate_spectre_degree.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_rotate_spectre_degree.setObjectName("label_rotate_spectre_degree")
        self.gridLayout_4.addWidget(self.label_rotate_spectre_degree, 6, 0, 1, 1)
        self.doubleSpinBox_spectre_degree = QtWidgets.QDoubleSpinBox(self.groupBox_draw_spectre)
        self.doubleSpinBox_spectre_degree.setMinimumSize(QtCore.QSize(100, 22))
        self.doubleSpinBox_spectre_degree.setMaximumSize(QtCore.QSize(100, 22))
        self.doubleSpinBox_spectre_degree.setDecimals(3)
        self.doubleSpinBox_spectre_degree.setMinimum(-99999.0)
        self.doubleSpinBox_spectre_degree.setMaximum(99999.0)
        self.doubleSpinBox_spectre_degree.setObjectName("doubleSpinBox_spectre_degree")
        self.gridLayout_4.addWidget(self.doubleSpinBox_spectre_degree, 6, 1, 1, 1)
        self.doubleSpinBox_yc = QtWidgets.QDoubleSpinBox(self.groupBox_draw_spectre)
        self.doubleSpinBox_yc.setMinimumSize(QtCore.QSize(100, 22))
        self.doubleSpinBox_yc.setMaximumSize(QtCore.QSize(100, 22))
        self.doubleSpinBox_yc.setDecimals(3)
        self.doubleSpinBox_yc.setMinimum(-99999.0)
        self.doubleSpinBox_yc.setMaximum(99999.0)
        self.doubleSpinBox_yc.setObjectName("doubleSpinBox_yc")
        self.gridLayout_4.addWidget(self.doubleSpinBox_yc, 3, 1, 1, 1)
        self.doubleSpinBox_xc = QtWidgets.QDoubleSpinBox(self.groupBox_draw_spectre)
        self.doubleSpinBox_xc.setMinimumSize(QtCore.QSize(100, 22))
        self.doubleSpinBox_xc.setMaximumSize(QtCore.QSize(100, 22))
        self.doubleSpinBox_xc.setDecimals(3)
        self.doubleSpinBox_xc.setMinimum(-99999.0)
        self.doubleSpinBox_xc.setMaximum(99999.0)
        self.doubleSpinBox_xc.setObjectName("doubleSpinBox_xc")
        self.gridLayout_4.addWidget(self.doubleSpinBox_xc, 0, 1, 1, 1)
        self.label_rotate_yc = QtWidgets.QLabel(self.groupBox_draw_spectre)
        self.label_rotate_yc.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_rotate_yc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_rotate_yc.setObjectName("label_rotate_yc")
        self.gridLayout_4.addWidget(self.label_rotate_yc, 3, 0, 1, 1)
        self.label_rotate_xc = QtWidgets.QLabel(self.groupBox_draw_spectre)
        self.label_rotate_xc.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_rotate_xc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_rotate_xc.setObjectName("label_rotate_xc")
        self.gridLayout_4.addWidget(self.label_rotate_xc, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_draw_spectre, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_draw, 2, 0, 1, 1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_canvas = QtWidgets.QGroupBox(self.groupBox_main)
        self.groupBox_canvas.setMinimumSize(QtCore.QSize(355, 68))
        self.groupBox_canvas.setMaximumSize(QtCore.QSize(355, 68))
        self.groupBox_canvas.setObjectName("groupBox_canvas")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_canvas)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.pushButton_clear = QtWidgets.QPushButton(self.groupBox_canvas)
        self.pushButton_clear.setMinimumSize(QtCore.QSize(162, 28))
        self.pushButton_clear.setMaximumSize(QtCore.QSize(162, 28))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.gridLayout_10.addWidget(self.pushButton_clear, 0, 0, 1, 1)
        self.pushButton_undo = QtWidgets.QPushButton(self.groupBox_canvas)
        self.pushButton_undo.setMinimumSize(QtCore.QSize(162, 28))
        self.pushButton_undo.setMaximumSize(QtCore.QSize(162, 28))
        self.pushButton_undo.setObjectName("pushButton_undo")
        self.gridLayout_10.addWidget(self.pushButton_undo, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_canvas, 4, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox_main, 1, 0, 1, 1)
        # self.canvas_widget = QtWidgets.QWidget(self.centralwidget)
        # self.canvas_widget.setMinimumSize(QtCore.QSize(575, 582))
        # self.canvas_widget.setObjectName("canvas_widget")
        # self.gridLayout.addWidget(self.canvas_widget, 1, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 983, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.about_programm = QtWidgets.QAction(MainWindow)
        self.about_programm.setObjectName("about_programm")
        self.about_author = QtWidgets.QAction(MainWindow)
        self.about_author.setObjectName("about_author")
        self.menu.addAction(self.about_programm)
        self.menu.addAction(self.about_author)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Компьютерная графика. Лабораторная работа 3"))
        self.groupBox_settings.setTitle(_translate("MainWindow", "Настройки"))
        self.groupBox_color_line.setTitle(_translate("MainWindow", "Цвет линий"))
        self.comboBox_color_line.setItemText(0, _translate("MainWindow", "Черный"))
        self.comboBox_color_line.setItemText(1, _translate("MainWindow", "Белый"))
        self.comboBox_color_line.setItemText(2, _translate("MainWindow", "Красный"))
        self.comboBox_color_line.setItemText(3, _translate("MainWindow", "Зеленый"))
        self.comboBox_color_line.setItemText(4, _translate("MainWindow", "Синий"))
        self.comboBox_color_line.setItemText(5, _translate("MainWindow", "Желтый"))
        self.comboBox_color_line.setItemText(6, _translate("MainWindow", "Фиолетовый"))
        self.comboBox_color_line.setItemText(7, _translate("MainWindow", "Розовый"))
        self.comboBox_color_line.setItemText(8, _translate("MainWindow", "Оранжевый"))
        self.groupBox_color_bg.setTitle(_translate("MainWindow", "Цвет фона"))
        self.comboBox_color_bg.setItemText(0, _translate("MainWindow", "Белый"))
        self.comboBox_color_bg.setItemText(1, _translate("MainWindow", "Черный"))
        self.comboBox_color_bg.setItemText(2, _translate("MainWindow", "Красный"))
        self.comboBox_color_bg.setItemText(3, _translate("MainWindow", "Зеленый"))
        self.comboBox_color_bg.setItemText(4, _translate("MainWindow", "Синий"))
        self.comboBox_color_bg.setItemText(5, _translate("MainWindow", "Желтый"))
        self.comboBox_color_bg.setItemText(6, _translate("MainWindow", "Фиолетовый"))
        self.comboBox_color_bg.setItemText(7, _translate("MainWindow", "Розовый"))
        self.comboBox_color_bg.setItemText(8, _translate("MainWindow", "Оранжевый"))
        self.groupBox_method.setTitle(_translate("MainWindow", "Метод построения"))
        self.comboBox_method.setItemText(0, _translate("MainWindow", "Библиотечная функция"))
        self.comboBox_method.setItemText(1, _translate("MainWindow", "ЦДА"))
        self.comboBox_method.setItemText(2, _translate("MainWindow", "Брезенхем (веществ.)"))
        self.comboBox_method.setItemText(3, _translate("MainWindow", "Брезенхем (целые)"))
        self.comboBox_method.setItemText(4, _translate("MainWindow", "Брезенхем (с устр. ступенчатости)"))
        self.comboBox_method.setItemText(5, _translate("MainWindow", "Ву"))
        self.groupBox_compare.setTitle(_translate("MainWindow", "Сравнение"))
        self.pushButton_time.setText(_translate("MainWindow", "Время"))
        self.pushButton_stairs.setText(_translate("MainWindow", "Ступенчатость"))
        self.groupBox_draw.setTitle(_translate("MainWindow", "Построение"))
        self.groupBox_draw_line.setTitle(_translate("MainWindow", "Отрезок"))
        self.label_rotate_ys.setText(_translate("MainWindow", "Ys:"))
        self.label_rotate_xe.setText(_translate("MainWindow", "Xe:"))
        self.pushButton_draw_line.setText(_translate("MainWindow", "Построить"))
        self.label_rotate_xs.setText(_translate("MainWindow", "Xs:"))
        self.label_rotate_ye.setText(_translate("MainWindow", "Ye:"))
        self.groupBox_draw_spectre.setTitle(_translate("MainWindow", "Спектр"))
        self.label_rotate_spectre_lenght.setText(_translate("MainWindow", "Длина:"))
        self.pushButton_draw_spectre.setText(_translate("MainWindow", "Построить"))
        self.label_rotate_spectre_degree.setText(_translate("MainWindow", "Угол:"))
        self.label_rotate_yc.setText(_translate("MainWindow", "Yс:"))
        self.label_rotate_xc.setText(_translate("MainWindow", "Xс:"))
        self.groupBox_canvas.setTitle(_translate("MainWindow", "Канвас"))
        self.pushButton_clear.setText(_translate("MainWindow", "Очистить"))
        self.pushButton_undo.setText(_translate("MainWindow", "Отменить действие"))
        self.menu.setTitle(_translate("MainWindow", "Инфо"))
        self.about_programm.setText(_translate("MainWindow", "О программе"))
        self.about_author.setText(_translate("MainWindow", "Об авторе"))