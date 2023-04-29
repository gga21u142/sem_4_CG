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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QGraphicsView, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1231, 932)
        MainWindow.setMinimumSize(QSize(1231, 932))
        self.about_program = QAction(MainWindow)
        self.about_program.setObjectName(u"about_program")
        font = QFont()
        font.setPointSize(10)
        self.about_program.setFont(font)
        self.about_author = QAction(MainWindow)
        self.about_author.setObjectName(u"about_author")
        self.about_author.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_13 = QGridLayout(self.centralwidget)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.groupBox_14 = QGroupBox(self.centralwidget)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setMinimumSize(QSize(314, 888))
        self.groupBox_14.setMaximumSize(QSize(314, 888))
        self.groupBox_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.gridLayout_12 = QGridLayout(self.groupBox_14)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.groupBox_14)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(310, 190))
        self.groupBox.setMaximumSize(QSize(310, 190))
        self.groupBox.setFont(font)
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 30, 141, 71))
        self.groupBox_2.setMinimumSize(QSize(141, 71))
        self.groupBox_2.setMaximumSize(QSize(141, 71))
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBox_color_bg = QComboBox(self.groupBox_2)
        self.comboBox_color_bg.addItem("")
        self.comboBox_color_bg.addItem("")
        self.comboBox_color_bg.addItem("")
        self.comboBox_color_bg.addItem("")
        self.comboBox_color_bg.addItem("")
        self.comboBox_color_bg.addItem("")
        self.comboBox_color_bg.addItem("")
        self.comboBox_color_bg.setObjectName(u"comboBox_color_bg")
        self.comboBox_color_bg.setMinimumSize(QSize(100, 30))
        self.comboBox_color_bg.setMaximumSize(QSize(100, 30))
        font1 = QFont()
        font1.setPointSize(9)
        self.comboBox_color_bg.setFont(font1)

        self.gridLayout_2.addWidget(self.comboBox_color_bg, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(160, 30, 141, 71))
        self.groupBox_3.setMinimumSize(QSize(141, 71))
        self.groupBox_3.setMaximumSize(QSize(141, 71))
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.comboBox_color_figure = QComboBox(self.groupBox_3)
        self.comboBox_color_figure.addItem("")
        self.comboBox_color_figure.addItem("")
        self.comboBox_color_figure.addItem("")
        self.comboBox_color_figure.addItem("")
        self.comboBox_color_figure.addItem("")
        self.comboBox_color_figure.addItem("")
        self.comboBox_color_figure.addItem("")
        self.comboBox_color_figure.setObjectName(u"comboBox_color_figure")
        self.comboBox_color_figure.setMinimumSize(QSize(100, 30))
        self.comboBox_color_figure.setMaximumSize(QSize(100, 30))
        self.comboBox_color_figure.setFont(font1)

        self.gridLayout_3.addWidget(self.comboBox_color_figure, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 110, 291, 71))
        self.groupBox_5.setMinimumSize(QSize(291, 71))
        self.groupBox_5.setMaximumSize(QSize(291, 71))
        self.comboBox_alrorithm = QComboBox(self.groupBox_5)
        self.comboBox_alrorithm.addItem("")
        self.comboBox_alrorithm.addItem("")
        self.comboBox_alrorithm.addItem("")
        self.comboBox_alrorithm.addItem("")
        self.comboBox_alrorithm.addItem("")
        self.comboBox_alrorithm.setObjectName(u"comboBox_alrorithm")
        self.comboBox_alrorithm.setGeometry(QRect(20, 30, 251, 30))
        self.comboBox_alrorithm.setMinimumSize(QSize(251, 30))
        self.comboBox_alrorithm.setMaximumSize(QSize(251, 30))
        self.comboBox_alrorithm.setFont(font1)

        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_4 = QGroupBox(self.groupBox_14)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(310, 527))
        self.groupBox_4.setMaximumSize(QSize(310, 527))
        self.groupBox_4.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.groupBox_4)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(286, 486))
        self.tabWidget.setMaximumSize(QSize(286, 486))
        self.tab_circle = QWidget()
        self.tab_circle.setObjectName(u"tab_circle")
        self.gridLayout_4 = QGridLayout(self.tab_circle)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_8 = QGroupBox(self.tab_circle)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(258, 70))
        self.groupBox_8.setMaximumSize(QSize(258, 70))
        self.horizontalLayout = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_8)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(17, 29))
        self.label.setMaximumSize(QSize(17, 29))

        self.horizontalLayout.addWidget(self.label)

        self.doubleSpinBox_circle_centre_x = QDoubleSpinBox(self.groupBox_8)
        self.doubleSpinBox_circle_centre_x.setObjectName(u"doubleSpinBox_circle_centre_x")
        self.doubleSpinBox_circle_centre_x.setMinimumSize(QSize(90, 30))
        self.doubleSpinBox_circle_centre_x.setMaximumSize(QSize(90, 30))
        self.doubleSpinBox_circle_centre_x.setFont(font1)
        self.doubleSpinBox_circle_centre_x.setAccelerated(True)
        self.doubleSpinBox_circle_centre_x.setDecimals(3)
        self.doubleSpinBox_circle_centre_x.setMinimum(-999999.000000000000000)
        self.doubleSpinBox_circle_centre_x.setMaximum(99999999.000000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBox_circle_centre_x)

        self.label_2 = QLabel(self.groupBox_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(16, 29))
        self.label_2.setMaximumSize(QSize(16, 29))

        self.horizontalLayout.addWidget(self.label_2)

        self.doubleSpinBox_circle_centre_y = QDoubleSpinBox(self.groupBox_8)
        self.doubleSpinBox_circle_centre_y.setObjectName(u"doubleSpinBox_circle_centre_y")
        self.doubleSpinBox_circle_centre_y.setMinimumSize(QSize(90, 30))
        self.doubleSpinBox_circle_centre_y.setMaximumSize(QSize(90, 30))
        self.doubleSpinBox_circle_centre_y.setFont(font1)
        self.doubleSpinBox_circle_centre_y.setAccelerated(True)
        self.doubleSpinBox_circle_centre_y.setDecimals(3)
        self.doubleSpinBox_circle_centre_y.setMinimum(-999999.000000000000000)
        self.doubleSpinBox_circle_centre_y.setMaximum(99999999.000000000000000)

        self.horizontalLayout.addWidget(self.doubleSpinBox_circle_centre_y)


        self.gridLayout_4.addWidget(self.groupBox_8, 0, 0, 1, 2)

        self.groupBox_9 = QGroupBox(self.tab_circle)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMinimumSize(QSize(258, 70))
        self.groupBox_9.setMaximumSize(QSize(258, 70))
        self.gridLayout_5 = QGridLayout(self.groupBox_9)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_3 = QLabel(self.groupBox_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(17, 29))
        self.label_3.setMaximumSize(QSize(17, 29))

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.doubleSpinBox_circle_radius = QDoubleSpinBox(self.groupBox_9)
        self.doubleSpinBox_circle_radius.setObjectName(u"doubleSpinBox_circle_radius")
        self.doubleSpinBox_circle_radius.setMinimumSize(QSize(210, 30))
        self.doubleSpinBox_circle_radius.setMaximumSize(QSize(210, 30))
        self.doubleSpinBox_circle_radius.setFont(font1)
        self.doubleSpinBox_circle_radius.setAccelerated(True)
        self.doubleSpinBox_circle_radius.setDecimals(3)
        self.doubleSpinBox_circle_radius.setMaximum(99999999.000000000000000)

        self.gridLayout_5.addWidget(self.doubleSpinBox_circle_radius, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_9, 1, 0, 1, 2)

        self.groupBox_10 = QGroupBox(self.tab_circle)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(258, 243))
        self.groupBox_10.setMaximumSize(QSize(258, 243))
        self.gridLayout_8 = QGridLayout(self.groupBox_10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.checkBox_3 = QCheckBox(self.groupBox_10)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setMinimumSize(QSize(116, 20))
        self.checkBox_3.setMaximumSize(QSize(116, 20))
        self.checkBox_3.setFont(font1)

        self.gridLayout_8.addWidget(self.checkBox_3, 6, 0, 1, 1)

        self.doubleSpinBox_circle_end_radius = QDoubleSpinBox(self.groupBox_10)
        self.doubleSpinBox_circle_end_radius.setObjectName(u"doubleSpinBox_circle_end_radius")
        self.doubleSpinBox_circle_end_radius.setMinimumSize(QSize(111, 30))
        self.doubleSpinBox_circle_end_radius.setMaximumSize(QSize(111, 30))
        self.doubleSpinBox_circle_end_radius.setFont(font1)
        self.doubleSpinBox_circle_end_radius.setAccelerated(True)
        self.doubleSpinBox_circle_end_radius.setDecimals(3)
        self.doubleSpinBox_circle_end_radius.setMinimum(-999999.000000000000000)
        self.doubleSpinBox_circle_end_radius.setMaximum(99999999.000000000000000)

        self.gridLayout_8.addWidget(self.doubleSpinBox_circle_end_radius, 4, 1, 1, 1)

        self.checkBox_4 = QCheckBox(self.groupBox_10)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setMinimumSize(QSize(116, 20))
        self.checkBox_4.setMaximumSize(QSize(116, 20))
        self.checkBox_4.setFont(font1)

        self.gridLayout_8.addWidget(self.checkBox_4, 7, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox_10)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMinimumSize(QSize(116, 20))
        self.checkBox_2.setMaximumSize(QSize(116, 20))
        self.checkBox_2.setFont(font1)

        self.gridLayout_8.addWidget(self.checkBox_2, 4, 0, 1, 1)

        self.spinBox_circle_step = QSpinBox(self.groupBox_10)
        self.spinBox_circle_step.setObjectName(u"spinBox_circle_step")
        self.spinBox_circle_step.setMinimumSize(QSize(111, 30))
        self.spinBox_circle_step.setMaximumSize(QSize(111, 30))
        self.spinBox_circle_step.setFont(font1)
        self.spinBox_circle_step.setAccelerated(True)

        self.gridLayout_8.addWidget(self.spinBox_circle_step, 6, 1, 1, 1)

        self.doubleSpinBox_circle_start_radius = QDoubleSpinBox(self.groupBox_10)
        self.doubleSpinBox_circle_start_radius.setObjectName(u"doubleSpinBox_circle_start_radius")
        self.doubleSpinBox_circle_start_radius.setMinimumSize(QSize(111, 30))
        self.doubleSpinBox_circle_start_radius.setMaximumSize(QSize(111, 30))
        self.doubleSpinBox_circle_start_radius.setFont(font1)
        self.doubleSpinBox_circle_start_radius.setAccelerated(True)
        self.doubleSpinBox_circle_start_radius.setDecimals(3)
        self.doubleSpinBox_circle_start_radius.setMinimum(-999999.000000000000000)
        self.doubleSpinBox_circle_start_radius.setMaximum(99999999.000000000000000)

        self.gridLayout_8.addWidget(self.doubleSpinBox_circle_start_radius, 2, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(234, 17))
        self.label_4.setMaximumSize(QSize(234, 17))
        font2 = QFont()
        font2.setPointSize(9)
        font2.setUnderline(True)
        self.label_4.setFont(font2)

        self.gridLayout_8.addWidget(self.label_4, 0, 0, 1, 2)

        self.spinBox_circle_amount = QSpinBox(self.groupBox_10)
        self.spinBox_circle_amount.setObjectName(u"spinBox_circle_amount")
        self.spinBox_circle_amount.setMinimumSize(QSize(111, 30))
        self.spinBox_circle_amount.setMaximumSize(QSize(111, 30))
        self.spinBox_circle_amount.setFont(font1)
        self.spinBox_circle_amount.setAccelerated(True)

        self.gridLayout_8.addWidget(self.spinBox_circle_amount, 7, 1, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_10)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMinimumSize(QSize(116, 20))
        self.checkBox.setMaximumSize(QSize(116, 20))
        self.checkBox.setFont(font1)

        self.gridLayout_8.addWidget(self.checkBox, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_10, 2, 0, 1, 2)

        self.pushButton_circle_draw = QPushButton(self.tab_circle)
        self.pushButton_circle_draw.setObjectName(u"pushButton_circle_draw")
        self.pushButton_circle_draw.setMinimumSize(QSize(126, 30))
        self.pushButton_circle_draw.setMaximumSize(QSize(126, 30))
        self.pushButton_circle_draw.setFont(font1)

        self.gridLayout_4.addWidget(self.pushButton_circle_draw, 3, 0, 1, 1)

        self.pushButton_circle_spectre_draw = QPushButton(self.tab_circle)
        self.pushButton_circle_spectre_draw.setObjectName(u"pushButton_circle_spectre_draw")
        self.pushButton_circle_spectre_draw.setMinimumSize(QSize(125, 30))
        self.pushButton_circle_spectre_draw.setMaximumSize(QSize(125, 30))
        self.pushButton_circle_spectre_draw.setFont(font1)

        self.gridLayout_4.addWidget(self.pushButton_circle_spectre_draw, 3, 1, 1, 1)

        self.tabWidget.addTab(self.tab_circle, "")
        self.tab_ellipse = QWidget()
        self.tab_ellipse.setObjectName(u"tab_ellipse")
        self.gridLayout_11 = QGridLayout(self.tab_ellipse)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.groupBox_13 = QGroupBox(self.tab_ellipse)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setMinimumSize(QSize(258, 70))
        self.groupBox_13.setMaximumSize(QSize(258, 70))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.groupBox_13)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(17, 29))
        self.label_7.setMaximumSize(QSize(17, 29))

        self.horizontalLayout_2.addWidget(self.label_7)

        self.doubleSpinBox_ellipse_centre_x = QDoubleSpinBox(self.groupBox_13)
        self.doubleSpinBox_ellipse_centre_x.setObjectName(u"doubleSpinBox_ellipse_centre_x")
        self.doubleSpinBox_ellipse_centre_x.setMinimumSize(QSize(90, 30))
        self.doubleSpinBox_ellipse_centre_x.setMaximumSize(QSize(90, 30))
        self.doubleSpinBox_ellipse_centre_x.setFont(font1)
        self.doubleSpinBox_ellipse_centre_x.setAccelerated(True)
        self.doubleSpinBox_ellipse_centre_x.setDecimals(3)
        self.doubleSpinBox_ellipse_centre_x.setMinimum(-999999.000000000000000)
        self.doubleSpinBox_ellipse_centre_x.setMaximum(99999999.000000000000000)

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_ellipse_centre_x)

        self.label_8 = QLabel(self.groupBox_13)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(17, 29))
        self.label_8.setMaximumSize(QSize(17, 29))

        self.horizontalLayout_2.addWidget(self.label_8)

        self.doubleSpinBox_ellipse_centre_y = QDoubleSpinBox(self.groupBox_13)
        self.doubleSpinBox_ellipse_centre_y.setObjectName(u"doubleSpinBox_ellipse_centre_y")
        self.doubleSpinBox_ellipse_centre_y.setMinimumSize(QSize(90, 30))
        self.doubleSpinBox_ellipse_centre_y.setMaximumSize(QSize(90, 30))
        self.doubleSpinBox_ellipse_centre_y.setFont(font1)
        self.doubleSpinBox_ellipse_centre_y.setAccelerated(True)
        self.doubleSpinBox_ellipse_centre_y.setDecimals(3)
        self.doubleSpinBox_ellipse_centre_y.setMinimum(-999999.000000000000000)
        self.doubleSpinBox_ellipse_centre_y.setMaximum(99999999.000000000000000)

        self.horizontalLayout_2.addWidget(self.doubleSpinBox_ellipse_centre_y)


        self.gridLayout_11.addWidget(self.groupBox_13, 0, 0, 1, 2)

        self.groupBox_12 = QGroupBox(self.tab_ellipse)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setMinimumSize(QSize(258, 70))
        self.groupBox_12.setMaximumSize(QSize(258, 70))
        self.gridLayout_10 = QGridLayout(self.groupBox_12)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_6 = QLabel(self.groupBox_12)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(17, 29))
        self.label_6.setMaximumSize(QSize(17, 29))

        self.gridLayout_10.addWidget(self.label_6, 0, 0, 1, 1)

        self.doubleSpinBox_ellipse_radius_x = QDoubleSpinBox(self.groupBox_12)
        self.doubleSpinBox_ellipse_radius_x.setObjectName(u"doubleSpinBox_ellipse_radius_x")
        self.doubleSpinBox_ellipse_radius_x.setMinimumSize(QSize(90, 30))
        self.doubleSpinBox_ellipse_radius_x.setMaximumSize(QSize(90, 30))
        self.doubleSpinBox_ellipse_radius_x.setFont(font1)
        self.doubleSpinBox_ellipse_radius_x.setAccelerated(True)
        self.doubleSpinBox_ellipse_radius_x.setDecimals(3)
        self.doubleSpinBox_ellipse_radius_x.setMaximum(99999999.000000000000000)

        self.gridLayout_10.addWidget(self.doubleSpinBox_ellipse_radius_x, 0, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_12)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(21, 29))
        self.label_9.setMaximumSize(QSize(21, 29))

        self.gridLayout_10.addWidget(self.label_9, 0, 2, 1, 1)

        self.doubleSpinBox_ellipse_radius_y = QDoubleSpinBox(self.groupBox_12)
        self.doubleSpinBox_ellipse_radius_y.setObjectName(u"doubleSpinBox_ellipse_radius_y")
        self.doubleSpinBox_ellipse_radius_y.setMinimumSize(QSize(90, 30))
        self.doubleSpinBox_ellipse_radius_y.setMaximumSize(QSize(90, 30))
        self.doubleSpinBox_ellipse_radius_y.setFont(font1)
        self.doubleSpinBox_ellipse_radius_y.setAccelerated(True)
        self.doubleSpinBox_ellipse_radius_y.setDecimals(3)
        self.doubleSpinBox_ellipse_radius_y.setMaximum(99999999.000000000000000)

        self.gridLayout_10.addWidget(self.doubleSpinBox_ellipse_radius_y, 0, 3, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_12, 1, 0, 1, 2)

        self.groupBox_11 = QGroupBox(self.tab_ellipse)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setMinimumSize(QSize(258, 243))
        self.groupBox_11.setMaximumSize(QSize(258, 243))
        self.gridLayout_9 = QGridLayout(self.groupBox_11)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_5 = QLabel(self.groupBox_11)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(114, 30))
        self.label_5.setMaximumSize(QSize(114, 30))
        self.label_5.setFont(font1)

        self.gridLayout_9.addWidget(self.label_5, 0, 0, 1, 1)

        self.doubleSpinBox_ellipse_start_rx = QDoubleSpinBox(self.groupBox_11)
        self.doubleSpinBox_ellipse_start_rx.setObjectName(u"doubleSpinBox_ellipse_start_rx")
        self.doubleSpinBox_ellipse_start_rx.setMinimumSize(QSize(113, 30))
        self.doubleSpinBox_ellipse_start_rx.setMaximumSize(QSize(113, 30))
        self.doubleSpinBox_ellipse_start_rx.setFont(font1)
        self.doubleSpinBox_ellipse_start_rx.setAccelerated(True)
        self.doubleSpinBox_ellipse_start_rx.setDecimals(3)
        self.doubleSpinBox_ellipse_start_rx.setMinimum(-999999.000000000000000)
        self.doubleSpinBox_ellipse_start_rx.setMaximum(99999999.000000000000000)

        self.gridLayout_9.addWidget(self.doubleSpinBox_ellipse_start_rx, 0, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_11)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(114, 30))
        self.label_10.setMaximumSize(QSize(114, 30))
        self.label_10.setFont(font1)

        self.gridLayout_9.addWidget(self.label_10, 1, 0, 1, 1)

        self.doubleSpinBox_ellipse_start_ry = QDoubleSpinBox(self.groupBox_11)
        self.doubleSpinBox_ellipse_start_ry.setObjectName(u"doubleSpinBox_ellipse_start_ry")
        self.doubleSpinBox_ellipse_start_ry.setMinimumSize(QSize(113, 30))
        self.doubleSpinBox_ellipse_start_ry.setMaximumSize(QSize(113, 30))
        self.doubleSpinBox_ellipse_start_ry.setFont(font1)
        self.doubleSpinBox_ellipse_start_ry.setAccelerated(True)
        self.doubleSpinBox_ellipse_start_ry.setDecimals(3)
        self.doubleSpinBox_ellipse_start_ry.setMinimum(-999999.000000000000000)
        self.doubleSpinBox_ellipse_start_ry.setMaximum(99999999.000000000000000)

        self.gridLayout_9.addWidget(self.doubleSpinBox_ellipse_start_ry, 1, 1, 1, 1)

        self.radioButton_step_rx = QRadioButton(self.groupBox_11)
        self.radioButton_step_rx.setObjectName(u"radioButton_step_rx")
        self.radioButton_step_rx.setMinimumSize(QSize(114, 20))
        self.radioButton_step_rx.setMaximumSize(QSize(114, 20))
        self.radioButton_step_rx.setFont(font1)

        self.gridLayout_9.addWidget(self.radioButton_step_rx, 2, 0, 1, 1)

        self.doubleSpinBox_ellipse_step_rx = QDoubleSpinBox(self.groupBox_11)
        self.doubleSpinBox_ellipse_step_rx.setObjectName(u"doubleSpinBox_ellipse_step_rx")
        self.doubleSpinBox_ellipse_step_rx.setMinimumSize(QSize(113, 30))
        self.doubleSpinBox_ellipse_step_rx.setMaximumSize(QSize(113, 30))
        self.doubleSpinBox_ellipse_step_rx.setFont(font1)
        self.doubleSpinBox_ellipse_step_rx.setAccelerated(True)
        self.doubleSpinBox_ellipse_step_rx.setDecimals(3)
        self.doubleSpinBox_ellipse_step_rx.setMinimum(-999999.000000000000000)
        self.doubleSpinBox_ellipse_step_rx.setMaximum(99999999.000000000000000)

        self.gridLayout_9.addWidget(self.doubleSpinBox_ellipse_step_rx, 2, 1, 1, 1)

        self.radioButton_step_ry = QRadioButton(self.groupBox_11)
        self.radioButton_step_ry.setObjectName(u"radioButton_step_ry")
        self.radioButton_step_ry.setMinimumSize(QSize(114, 20))
        self.radioButton_step_ry.setMaximumSize(QSize(114, 20))
        self.radioButton_step_ry.setFont(font1)

        self.gridLayout_9.addWidget(self.radioButton_step_ry, 3, 0, 1, 1)

        self.doubleSpinBox_ellipse_step_ry = QDoubleSpinBox(self.groupBox_11)
        self.doubleSpinBox_ellipse_step_ry.setObjectName(u"doubleSpinBox_ellipse_step_ry")
        self.doubleSpinBox_ellipse_step_ry.setMinimumSize(QSize(113, 30))
        self.doubleSpinBox_ellipse_step_ry.setMaximumSize(QSize(113, 30))
        self.doubleSpinBox_ellipse_step_ry.setFont(font1)
        self.doubleSpinBox_ellipse_step_ry.setAccelerated(True)
        self.doubleSpinBox_ellipse_step_ry.setDecimals(3)
        self.doubleSpinBox_ellipse_step_ry.setMinimum(-999999.000000000000000)
        self.doubleSpinBox_ellipse_step_ry.setMaximum(99999999.000000000000000)

        self.gridLayout_9.addWidget(self.doubleSpinBox_ellipse_step_ry, 3, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox_11)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(114, 30))
        self.label_11.setMaximumSize(QSize(114, 30))
        self.label_11.setFont(font1)

        self.gridLayout_9.addWidget(self.label_11, 4, 0, 1, 1)

        self.spinBox_ellipse_amount = QSpinBox(self.groupBox_11)
        self.spinBox_ellipse_amount.setObjectName(u"spinBox_ellipse_amount")
        self.spinBox_ellipse_amount.setMinimumSize(QSize(113, 30))
        self.spinBox_ellipse_amount.setMaximumSize(QSize(113, 30))
        self.spinBox_ellipse_amount.setFont(font1)
        self.spinBox_ellipse_amount.setAccelerated(True)

        self.gridLayout_9.addWidget(self.spinBox_ellipse_amount, 4, 1, 1, 1)


        self.gridLayout_11.addWidget(self.groupBox_11, 2, 0, 1, 2)

        self.pushButton_ellipse_draw = QPushButton(self.tab_ellipse)
        self.pushButton_ellipse_draw.setObjectName(u"pushButton_ellipse_draw")
        self.pushButton_ellipse_draw.setMinimumSize(QSize(125, 30))
        self.pushButton_ellipse_draw.setMaximumSize(QSize(125, 30))
        self.pushButton_ellipse_draw.setFont(font1)

        self.gridLayout_11.addWidget(self.pushButton_ellipse_draw, 3, 0, 1, 1)

        self.pushButton_ellipse_spectre_draw = QPushButton(self.tab_ellipse)
        self.pushButton_ellipse_spectre_draw.setObjectName(u"pushButton_ellipse_spectre_draw")
        self.pushButton_ellipse_spectre_draw.setMinimumSize(QSize(125, 30))
        self.pushButton_ellipse_spectre_draw.setMaximumSize(QSize(125, 30))
        self.pushButton_ellipse_spectre_draw.setFont(font1)

        self.gridLayout_11.addWidget(self.pushButton_ellipse_spectre_draw, 3, 1, 1, 1)

        self.tabWidget.addTab(self.tab_ellipse, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox_7 = QGroupBox(self.groupBox_14)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(310, 73))
        self.groupBox_7.setMaximumSize(QSize(310, 73))
        self.groupBox_7.setFont(font)
        self.gridLayout_6 = QGridLayout(self.groupBox_7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pushButton_measure_circle = QPushButton(self.groupBox_7)
        self.pushButton_measure_circle.setObjectName(u"pushButton_measure_circle")
        self.pushButton_measure_circle.setMinimumSize(QSize(140, 30))
        self.pushButton_measure_circle.setMaximumSize(QSize(140, 30))
        self.pushButton_measure_circle.setFont(font1)

        self.gridLayout_6.addWidget(self.pushButton_measure_circle, 0, 0, 1, 1)

        self.pushButton_measure_ellipse = QPushButton(self.groupBox_7)
        self.pushButton_measure_ellipse.setObjectName(u"pushButton_measure_ellipse")
        self.pushButton_measure_ellipse.setMinimumSize(QSize(140, 30))
        self.pushButton_measure_ellipse.setMaximumSize(QSize(140, 30))
        self.pushButton_measure_ellipse.setFont(font1)

        self.gridLayout_6.addWidget(self.pushButton_measure_ellipse, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_7)

        self.groupBox_6 = QGroupBox(self.groupBox_14)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(310, 73))
        self.groupBox_6.setMaximumSize(QSize(310, 73))
        self.groupBox_6.setFont(font)
        self.gridLayout_7 = QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pushButto_undo = QPushButton(self.groupBox_6)
        self.pushButto_undo.setObjectName(u"pushButto_undo")
        self.pushButto_undo.setMinimumSize(QSize(140, 30))
        self.pushButto_undo.setMaximumSize(QSize(140, 30))
        self.pushButto_undo.setFont(font1)

        self.gridLayout_7.addWidget(self.pushButto_undo, 0, 0, 1, 1)

        self.pushButton_clear = QPushButton(self.groupBox_6)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setMinimumSize(QSize(140, 30))
        self.pushButton_clear.setMaximumSize(QSize(140, 30))
        self.pushButton_clear.setFont(font1)

        self.gridLayout_7.addWidget(self.pushButton_clear, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_6)


        self.gridLayout_12.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.groupBox_14, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(888, 888))
        self.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)

        self.gridLayout_13.addWidget(self.graphicsView, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1231, 25))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.about_program)
        self.menu.addAction(self.about_author)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u043d\u0430\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430. \u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u21164", None))
        self.about_program.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.about_author.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431 \u0430\u0432\u0442\u043e\u0440\u0435", None))
        self.groupBox_14.setTitle("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u044f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430", None))
        self.comboBox_color_bg.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u043b\u044b\u0439", None))
        self.comboBox_color_bg.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0427\u0435\u0440\u043d\u044b\u0439", None))
        self.comboBox_color_bg.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0430\u0441\u043d\u044b\u0439", None))
        self.comboBox_color_bg.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0417\u0435\u043b\u0435\u043d\u044b\u0439", None))
        self.comboBox_color_bg.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0438\u0439", None))
        self.comboBox_color_bg.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0416\u0435\u043b\u0442\u044b\u0439", None))
        self.comboBox_color_bg.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0420\u043e\u0437\u043e\u0432\u044b\u0439", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442 \u0444\u0438\u0433\u0443\u0440\u044b", None))
        self.comboBox_color_figure.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0427\u0435\u0440\u043d\u044b\u0439", None))
        self.comboBox_color_figure.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u043b\u044b\u0439", None))
        self.comboBox_color_figure.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0430\u0441\u043d\u044b\u0439", None))
        self.comboBox_color_figure.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0417\u0435\u043b\u0435\u043d\u044b\u0439", None))
        self.comboBox_color_figure.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0438\u0439", None))
        self.comboBox_color_figure.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0416\u0435\u043b\u0442\u044b\u0439", None))
        self.comboBox_color_figure.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0420\u043e\u0437\u043e\u0432\u044b\u0439", None))

        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u044f", None))
        self.comboBox_alrorithm.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u043e\u043d\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435", None))
        self.comboBox_alrorithm.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0443\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435", None))
        self.comboBox_alrorithm.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c \u0411\u0440\u0435\u0437\u0435\u043d\u0445\u0435\u043c\u0430", None))
        self.comboBox_alrorithm.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c \u0441\u0440\u0435\u0434\u043d\u0435\u0439 \u0442\u043e\u0447\u043a\u0438", None))
        self.comboBox_alrorithm.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0411\u0438\u0431\u043b\u0438\u043e\u0442\u0435\u0447\u043d\u0430\u044f \u0444\u0443\u043d\u043a\u0446\u0438\u044f", None))

        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u0435", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0442\u0440", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"R:", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u043f\u0435\u043a\u0442\u0440\u0430", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433 \u043f\u043e\u0441\u0442\u0440\u043e\u0435\u043d\u0438\u044f:", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u0444\u0438\u0433\u0443\u0440:", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d. \u0440\u0430\u0434\u0438\u0443\u0441:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 3 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u0430:", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447. \u0440\u0430\u0434\u0438\u0443\u0441:", None))
        self.pushButton_circle_draw.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0444\u0438\u0433\u0443\u0440\u0443", None))
        self.pushButton_circle_spectre_draw.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0441\u043f\u0435\u043a\u0442\u0440", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_circle), QCoreApplication.translate("MainWindow", u"\u041e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0442\u0440", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441\u044b", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Rx:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u" Ry:", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u043f\u0435\u043a\u0442\u0440\u0430", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447. Rx:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447. Ry:", None))
        self.radioButton_step_rx.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433 Rx:", None))
        self.radioButton_step_ry.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433 Ry:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b-\u0432\u043e \u0444\u0438\u0433\u0443\u0440:", None))
        self.pushButton_ellipse_draw.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0444\u0438\u0433\u0443\u0440\u0443", None))
        self.pushButton_ellipse_spectre_draw.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u0441\u043f\u0435\u043a\u0442\u0440", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_ellipse), QCoreApplication.translate("MainWindow", u"\u042d\u043b\u043b\u0438\u043f\u0441", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u0435 \u0432\u0440\u0435\u043c\u0435\u043d\u0438", None))
        self.pushButton_measure_circle.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u0438", None))
        self.pushButton_measure_ellipse.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043b\u043b\u0438\u043f\u0441\u0430", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u043d\u0432\u0430\u0441", None))
        self.pushButto_undo.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.pushButton_clear.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e", None))
    # retranslateUi

