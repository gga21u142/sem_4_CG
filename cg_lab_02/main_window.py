
# Основной модуль программы, содержит весь основной фунционал программы

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton
from ui_window import Ui_MainWindow
from figure import Figure
from matplotwidget import MatplotlibWidget
from my_logging import Logging
from copy import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.figure = Figure()
        self.logs = Logging()
        self.condition = deepcopy(self.figure.dots)

        self.canvas_height = 0
        self.canvas_width = 0
        self.canvas_init()

        # нажатия внопок и ивенты
        self.about_author.triggered.connect(self.info_author)
        self.about_proramm.triggered.connect(self.info_task)

        self.pushButton_clear.clicked.connect(self.btn_download_figure)
        self.pushButton_move.clicked.connect(self.btn_move_figure)
        self.pushButton_rotate.clicked.connect(self.btn_rotate_figure)
        self.pushButton_scale.clicked.connect(self.btn_scale_figure)
        self.pushButton_undo.clicked.connect(self.btn_undo_log)
        self.pushButton_autoscale.clicked.connect(self.btn_autoscale_canvas)

        self.resized.connect(self.resize_canvas)
        

    # Служебная информация м функции для управления логом
    def info_author(self):
        info_author = QMessageBox()
        info_author.setWindowTitle("Об авторе")
        info_author.setText("\tСтудент ИУ7-44Б\t\n\tГареев Г. А.\t")
        info_author.setDefaultButton(QMessageBox.Ok)

        info_author.exec_()
    
    def info_task(self):
        info_task = QMessageBox()
        info_task.setWindowTitle("Условие задачи")
        info_task.setText("Реализация базовых преобразований над фигурой в плоскости. Фигура задана вариантом, в данном случае гитара. Для взаимодейтсвия с фигурой доступны: перемещение, масштабирование и поворот отн-но заданной точки.")
        info_task.setDefaultButton(QMessageBox.Ok)

        info_task.exec_()

    def closeEvent(self, event):
        msg = QMessageBox(self)
        msg.setWindowTitle("Выход")
        msg.setIcon(QMessageBox.Question)
        msg.setText("Вы действительно хотите выйти ?")

        buttonAceptar  = msg.addButton("Да", QMessageBox.YesRole)    
        buttonCancelar = msg.addButton("Нет", QMessageBox.RejectRole) 
        msg.setDefaultButton(buttonAceptar)
        msg.exec_()

        if msg.clickedButton() == buttonAceptar:
            event.accept()
        elif msg.clickedButton() == buttonCancelar:
            event.ignore()

    def show_warning_fail_download(self):
        error = QMessageBox()
        error.setWindowTitle("Ошибка!")
        error.setText("Невозможно загрузить фигуру из файла!")
        error.setDefaultButton(QMessageBox.Ok)
        error.setIcon(QMessageBox.Warning)
        error.exec_()
    
    def show_warning_figure_nexist(self):
        error = QMessageBox()
        error.setWindowTitle("Ошибка!")
        error.setText("Фигура не задана!")
        error.setDefaultButton(QMessageBox.Ok)
        error.setIcon(QMessageBox.Warning)
        error.exec_()
    
    def show_warning_scale_zero(self):
        error = QMessageBox()
        error.setWindowTitle("Ошибка!")
        error.setText("Коэффициент масштабирования должен быть больше нуля!")
        error.setDefaultButton(QMessageBox.Ok)
        error.setIcon(QMessageBox.Warning)
        error.exec_()

    def update_condition(self):
        self.condition = deepcopy(self.figure.dots)
    
    
    # Функции кнопок интерфейса
    def btn_undo_log(self):
        if self.logs.get_log_len() > 1:
            self.figure.dots = self.logs.undo_log()
            self.update_condition()
            self.canvas_refresh(False, self.matplotlib_widget.axis.get_xlim(), self.matplotlib_widget.axis.get_ylim())
        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка!")
            error.setText("Нельзя отменить прошлое действие!")
            error.setDefaultButton(QMessageBox.Ok)
            error.setIcon(QMessageBox.Warning)
            error.exec_()
        
    def btn_move_figure(self):
        if (self.figure.get_dots_count() > 0):
            move_x = self.doubleSpinBox_move_x.value()
            move_y = self.doubleSpinBox_move_y.value()
            self.figure.figure_move(move_x, move_y)
            self.canvas_refresh(False, self.matplotlib_widget.axis.get_xlim(), self.matplotlib_widget.axis.get_ylim())
        else:
            self.show_warning_figure_nexist()

    def btn_rotate_figure(self):
        if (self.figure.get_dots_count() > 0):
            degree = self.doubleSpinBox_rotate_x.value()
            centre = (self.doubleSpinBox_centre_x.value(), self.doubleSpinBox_centre_y.value())
            self.figure.figure_rotate(centre, degree)
            self.canvas_refresh(False, self.matplotlib_widget.axis.get_xlim(), self.matplotlib_widget.axis.get_ylim())
        else:
            self.show_warning_figure_nexist()

    def btn_scale_figure(self):
        if (self.figure.get_dots_count() > 0):
            coeff_x = self.doubleSpinBox_scale_x.value()
            coeff_y = self.doubleSpinBox_scale_y.value()
            centre = (self.doubleSpinBox_centre_x.value(), self.doubleSpinBox_centre_y.value())
            if (self.figure.figure_scale(centre, coeff_x, coeff_y) != 0):
                self.show_warning_scale_zero()
            else:
                self.canvas_refresh(False, self.matplotlib_widget.axis.get_xlim(), self.matplotlib_widget.axis.get_ylim())
        else:
            self.show_warning_figure_nexist()

    def btn_download_figure(self):
        file = "guitar_copy.txt"
        if self.figure.figure_download_from_file(file) != 0:
            self.show_warning_fail_download()
        
        self.canvas_refresh(False, self.matplotlib_widget.axis.get_xlim(), self.matplotlib_widget.axis.get_ylim())
    
    def btn_autoscale_canvas(self):
        self.canvas_refresh(True, [-150, 150], [-110, 110])


    # Функции начальной настройки канвы и функции для ее использования
    def canvas_init(self):
        self.matplotlib_widget = MatplotlibWidget()
        self.gridLayout.addWidget(self.matplotlib_widget, 1, 0, 1, 2)
        self.canvas_height = self.matplotlib_widget.frameGeometry().height()
        self.canvas_width = self.matplotlib_widget.frameGeometry().width()
        
        self.canvas_refresh(False, [-150, 150], [-110, 110])  
 
    def canvas_refresh(self, bool, x, y):
        self.matplotlib_widget.axis.clear()

        self.update_condition()
        self.logs.update_log(list(self.condition))

        self.canvas_default(bool, x, y)
        self.canvas_draw_figure()
        self.canvas_draw_centre()

    def canvas_default(self, bool, x, y):
        self.matplotlib_widget.axis.set_aspect("auto", 'box')
        self.matplotlib_widget.axis.set_xlim(x[0], x[1])
        self.matplotlib_widget.axis.set_ylim(y[0], y[1])
        if bool:
            self.matplotlib_widget.axis.autoscale(True)
        self.matplotlib_widget.axis.grid()

    def canvas_draw_centre(self):
        centre_x = self.doubleSpinBox_centre_x.value()
        centre_y = self.doubleSpinBox_centre_y.value()

        self.draw_point([centre_x, centre_y], 'g')
        self.matplotlib_widget.figure.canvas.draw()
                
    def canvas_draw_figure(self):
        if self.figure.get_dots_count():
            for i in range(self.figure.get_dots_count()):
                self.draw_point(self.figure.dots[i], 'r')

            for i in range(self.figure.get_connections_count()):
                connection = self.figure.connections[i]
                dot_1 = self.figure.dots[connection[0]]
                dot_2 = self.figure.dots[connection[1]]
                # print(connection)
                self.draw_connection(dot_1, dot_2, 'b')
            
        self.matplotlib_widget.figure.canvas.draw()

    def draw_point(self, Coords, color):
        if not (Coords[0] is None or Coords[1] is None):
            self.matplotlib_widget.axis.plot(Coords[0], Coords[1], color + 'o', markersize = 5)

    def draw_connection(self, dot_1, dot_2, color):
        if not (dot_1 is None or dot_2 is None):
            # print(dot_1, dot_2)
            self.matplotlib_widget.axis.plot([dot_1[0], dot_2[0]], [dot_1[1], dot_2[1]], c = color)

    # Доп функции
    def resize_canvas(self):
        self.resize_y_axis()
        self.resize_x_axis()

    def resizeEvent(self, event):
        self.resized.emit()
        return super(MainWindow, self).resizeEvent(event)
    
    def resize_y_axis(self):
        ylim = list(self.matplotlib_widget.axis.get_ylim())
        range_y = abs(ylim[1] - ylim[0])
        height = self.matplotlib_widget.frameGeometry().height()
        coef = self.canvas_height / range_y
        delta = (height - self.canvas_height) / 2
        self.matplotlib_widget.axis.set_ylim(ylim[0] - (delta / coef), ylim[1] + (delta / coef))
        self.canvas_height = height

    def resize_x_axis(self):
        xlim = list(self.matplotlib_widget.axis.get_xlim())
        range_x = abs(xlim[1] - xlim[0])
        width = self.matplotlib_widget.frameGeometry().width()
        coef = self.canvas_width / range_x
        delta = (width - self.canvas_width) / 2
        self.matplotlib_widget.axis.set_xlim((xlim[0] - (delta / coef)), (xlim[1] + (delta / coef)))
        self.canvas_width = width

