
# Основной модуль программы, содержит весь основной фунционал программы

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QPushButton
from ui_window import Ui_MainWindow
from matplotwidget import MatplotlibWidget
from my_logging import Logging
from copy import *
import time
import matplotlib.pyplot as plt
from math import cos, sin, radians, fabs, floor

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.logs = Logging()
        self.condition = list()
        self.update_condition()

        self.canvas_bg_color = (1, 1, 1, 1)
        self.canvas_line_color = (0, 0, 0, 1)
        
        self.canvas_height = 0
        self.canvas_width = 0
        self.canvas_init()

        # нажатия внопок и ивенты
        self.about_author.triggered.connect(self.info_author)
        self.about_programm.triggered.connect(self.info_task)

        self.pushButton_undo.clicked.connect(self.btn_undo_log)
        self.pushButton_draw_line.clicked.connect(self.btn_draw_line)
        self.pushButton_draw_spectre.clicked.connect(self.btn_draw_spectre)
        self.pushButton_time.clicked.connect(self.btn_mesure_time)
        self.pushButton_stairs.clicked.connect(self.btn_mesure_stairs)
        self.pushButton_clear.clicked.connect(self.btn_clear_canvas)

        self.comboBox_color_bg.activated[str].connect(self.change_bg_color)
        self.comboBox_color_line.activated[str].connect(self.change_line_color)

        self.resized.connect(self.resize_canvas)
        


    # Служебная информация и функции для управления логом
    def info_author(self):
        info_author = QMessageBox()
        info_author.setWindowTitle("Об авторе")
        info_author.setText("\tСтудент ИУ7-44Б\t\n\tГареев Г. А.\t")
        info_author.setDefaultButton(QMessageBox.Ok)
        info_author.setIcon(QMessageBox.Information) 

        info_author.exec_()
    
    def info_task(self):
        info_task = QMessageBox()
        info_task.setWindowTitle("Условие задачи")
        info_task.setText("Реализация построения отрезков и спектров различными алгоритмами: ЦДА, Брезенхема, Ву и функцией стандартной библиотеки. Сравнение временных характеристик и исследование ступенчатости различных алгоритмов.")
        info_task.setDefaultButton(QMessageBox.Ok)
        info_task.setIcon(QMessageBox.Information) 

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

    def show_warning_wrong_line(self):
        error = QMessageBox()
        error.setWindowTitle("Ошибка!")
        error.setText("Точки начала и конца отрезка не должны совпадать!")
        error.setDefaultButton(QMessageBox.Ok)
        error.setIcon(QMessageBox.Warning)
        error.exec_()
    
    def show_warning_spectre_nexist(self):
        error = QMessageBox()
        error.setWindowTitle("Ошибка!")
        error.setText("Угол и длина спектра не должны быть равны нулю!")
        error.setDefaultButton(QMessageBox.Ok)
        error.setIcon(QMessageBox.Warning)
        error.exec_()
    
    def show_info_time_measure(self):
        msg = QMessageBox()
        msg.setWindowTitle("О процессе замера времени")
        msg.setText("Замеры времени проводятся для процесса построения спектра с заданными в основном окне настройками, убедитесь, что вы задали верные настройки. Следует помнить, что маленькие углы и большая длина сказываются на времени выполнения замера.\nВыполнить замер?")
        buttonAceptar  = msg.addButton("Да", QMessageBox.YesRole)    
        buttonCancelar = msg.addButton("Нет", QMessageBox.RejectRole) 
        msg.setIcon(QMessageBox.Information) 
        msg.setDefaultButton(buttonAceptar)
        msg.exec_()

        if msg.clickedButton() == buttonAceptar:
            Xc = self.doubleSpinBox_xc.value()
            Yc = self.doubleSpinBox_yc.value()
            lenght = self.doubleSpinBox_spectre_lenght.value()
            degree = self.doubleSpinBox_spectre_degree.value()
            self.measure_exec_time([Xc, Yc], lenght, degree)

    def show_info_step_measure(self):
        msg = QMessageBox()
        msg.setWindowTitle("О процессе замера ступенчатости")
        msg.setText("Исследование ступенчатости имспользует процесс построения отрезков фиксированной длины (указывается в поле 'Длина' для построения спектра) с увеличивающимся углом наклона (от 0 до 90). Стоит помнить, что большая длина сказываются на времени выполнения замера.\nВыполнить замер?")
        buttonAceptar  = msg.addButton("Да", QMessageBox.YesRole)    
        buttonCancelar = msg.addButton("Нет", QMessageBox.RejectRole) 
        msg.setIcon(QMessageBox.Information) 
        msg.setDefaultButton(buttonAceptar)
        msg.exec_()

        if msg.clickedButton() == buttonAceptar:
            lenght = self.doubleSpinBox_spectre_lenght.value()
            self.measure_stepping(lenght)

    def update_condition(self, command = None):
        if command:
            self.condition.append(command)
        self.logs.update_log(self.condition)



    # Функции кнопок интерфейса  
    def btn_undo_log(self):
        if self.logs.get_log_len() > 1:
            self.canvas_default()
            self.condition = deepcopy(self.logs.undo_log())
            for command in self.condition:
                print(f"eval {command}")
                eval(command)
            self.update_condition()

        else:
            error = QMessageBox()
            error.setWindowTitle("Ошибка!")
            error.setText("Нельзя отменить прошлое действие!")
            error.setDefaultButton(QMessageBox.Ok)
            error.setIcon(QMessageBox.Warning)
            error.exec_()
    
    def btn_draw_line(self):
        Xs = self.doubleSpinBox_xs.value()
        Ys = self.doubleSpinBox_ys.value()
        Xe = self.doubleSpinBox_xe.value()
        Ye = self.doubleSpinBox_ye.value()
        method = self.comboBox_method.currentText()
        method_ind = self.comboBox_method.currentIndex()
        print(f"Draw line on points: ({Xs}, {Ys}) and ({Xe}, {Ye}) with method {method} (ind {method_ind})")
        self.draw_line_hub([Xs, Ys], [Xe, Ye], method_ind, self.canvas_line_color)

    def btn_draw_spectre(self):
        Xc = self.doubleSpinBox_xc.value()
        Yc = self.doubleSpinBox_yc.value()
        lenght = self.doubleSpinBox_spectre_lenght.value()
        degree = self.doubleSpinBox_spectre_degree.value()
        method = self.comboBox_method.currentText()
        method_ind = self.comboBox_method.currentIndex()
        print(f"Draw spectre on centre ({Xc}, {Yc}), lenght {lenght}, degree {degree} with method {method} (ind {method_ind})")
        self.draw_spectre_hub([Xc, Yc], lenght, degree, method_ind, self.canvas_line_color)
    
    def btn_mesure_time(self):
        self.show_info_time_measure()
    
    def btn_mesure_stairs(self):
        self.show_info_step_measure()
        
    def btn_clear_canvas(self):
        if len(self.condition)  != 0:
            self.condition.clear()
            self.update_condition()
            self.canvas_default()

    def change_bg_color(self, text):
        print("Bg color changed on " + text)
        print(self.matplotlib_widget.colors_bg[text])
        self.canvas_bg_color = (self.matplotlib_widget.colors_bg[text])
        self.canvas_refresh()

    def change_line_color(self, text):
        print("Line color changed on " + text)
        print(self.matplotlib_widget.colors_line[text])
        self.canvas_line_color = (self.matplotlib_widget.colors_line[text])
        


    # Функции начальной настройки канвы и функции для ее использования
    def canvas_init(self):
        self.matplotlib_widget = MatplotlibWidget()
        self.gridLayout.addWidget(self.matplotlib_widget, 1, 1, 2, 1)
        self.canvas_default()
      
    def canvas_refresh(self):
        # self.update_condition()
        # self.logs.update_log(list(self.condition))
        self.matplotlib_widget.axis.set_facecolor(self.canvas_bg_color)
        self.matplotlib_widget.axis.figure.canvas.draw()

    def canvas_default(self, autoscale = False):
        self.canvas_height = self.matplotlib_widget.frameGeometry().height()
        self.canvas_width = self.matplotlib_widget.frameGeometry().width()
        self.matplotlib_widget.axis.clear()
        self.matplotlib_widget.axis.set_xlim(-300, 300)
        self.matplotlib_widget.axis.set_ylim(-300, 300)
        if autoscale:
            self.matplotlib_widget.axis.autoscale(True)
        self.matplotlib_widget.axis.grid()
        self.canvas_refresh()

    def draw_line_hub(self, dot_s, dot_e, method_ind, color, silent = False, silent_draw = False):
        if dot_s == dot_e:
            self.show_warning_wrong_line()
        else:
            steps = 0
            if method_ind == 0:
                self.line_draw_stand(dot_s, dot_e, color)
            elif method_ind == 1:
                steps = self.line_draw_dda(dot_s, dot_e, color, silent_draw)
            elif method_ind == 2:
                steps = self.line_draw_bresenham_float(dot_s, dot_e, color, silent_draw)
            elif method_ind == 3:
                steps = self.line_draw_bresenham_int(dot_s, dot_e, color, silent_draw)
            elif method_ind == 4:
                steps = self.line_draw_bresenham_aas(dot_s, dot_e, color, silent_draw)
            elif method_ind == 5:
                steps = self.line_draw_wu(dot_s, dot_e, color, silent_draw)
            else:
                print("gg")
                return
            if not silent:
                self.update_condition(f"self.draw_line_hub({dot_s}, {dot_e}, {method_ind}, {color}, True)")
            self.canvas_refresh()

            return steps

    def draw_spectre_hub(self, centre, lenght, degree, method_ind, color, silent = False, silent_draw = False):
        if degree == 0 or lenght == 0:
            self.show_warning_spectre_nexist()
        else:
            if method_ind == 0:
                self.spectre_draw_stand(centre, lenght, degree, color)
            elif method_ind == 1:
                self.spectre_draw_dda(centre, lenght, degree, color, silent_draw)
            elif method_ind == 2:
                self.spectre_draw_bresenham_float(centre, lenght, degree, color, silent_draw)
            elif method_ind == 3:
                self.spectre_draw_bresenham_int(centre, lenght, degree, color, silent_draw)
            elif method_ind == 4:
                self.spectre_draw_bresenham_aas(centre, lenght, degree, color, silent_draw)
            elif method_ind == 5:
                self.spectre_draw_bresenham_wu(centre, lenght, degree, color, silent_draw)
            else:
                print("gg")
                return
            if not silent:
                self.update_condition(f"self.draw_spectre_hub({centre}, {lenght}, {degree}, {method_ind}, {color}, True)")
            self.canvas_refresh()



    # Функции отрисовки линий
    def line_draw_stand(self, dot_s, dot_e, color):
        if dot_s != dot_e:
            self.matplotlib_widget.axis.plot([dot_s[0], dot_e[0]], [dot_s[1], dot_e[1]], c=color)

    def line_draw_dda(self, dot_s, dot_e, color, silent = False):
        dx = dot_e[0] - dot_s[0]
        dy = dot_e[1] - dot_s[1]

        l = abs(dx) if abs(dx) >= abs(dy) else abs(dy)
        
        dx /= l
        dy /= l

        x_sign = self.sign(dx)
        y_sign = self.sign(dy)

        x = dot_s[0] + 0.5 * x_sign
        y = dot_s[1] + 0.5 * y_sign
        if not silent:
            self.matplotlib_widget.axis.plot(round(x), round(y), 'o', c=color, markersize = 1)

        steps = 0

        i = 1
        while i <= l:
            x_buf = x
            y_buf = y

            x += dx
            y += dy
            if not silent:
                self.matplotlib_widget.axis.plot(round(x), round(y), 'o', c=color, markersize = 1)

            if round(x_buf) != round(x) and round(y_buf) != round(y):
                steps += 1

            i += 1

        return steps
        
    def line_draw_bresenham_float(self, dot_s, dot_e, color, silent = False):
        dx = dot_e[0] - dot_s[0]
        dy = dot_e[1] - dot_s[1]

        x_sign = self.sign(dx)
        y_sign = self.sign(dy)

        dx = abs(dx)
        dy = abs(dy)

        exchange = 0
        if dy > dx:
            dx, dy = dy, dx
            exchange = 1
            

        e = dy / dx - 0.5
        x, y = dot_s

        x_buf = x
        y_buf = y
        steps = 0

        i = 0
        while i <= dx:
            if not silent:
                self.matplotlib_widget.axis.plot(floor(x), floor(y), 'o', c=color, markersize = 1)

            if e >= 0:
                if exchange:
                    x += x_sign
                else:
                    y += y_sign

                e -= 1

            if exchange:
                y += y_sign
            else:
                x += x_sign
            
            e += dy / dx
            i += 1

            if x_buf != x and y_buf != y:
                steps += 1

                x_buf = x
                y_buf = y

        return steps

    def line_draw_bresenham_int(self, dot_s, dot_e, color, silent = False):
        dx = dot_e[0] - dot_s[0]
        dy = dot_e[1] - dot_s[1]

        x_sign = self.sign(dx)
        y_sign = self.sign(dy)

        dx = abs(dx)
        dy = abs(dy)

        exchange = 0
        if dy > dx:
            dx, dy = dy, dx
            exchange = 1           

        e = 2 * dy - dx
        x, y = dot_s

        x_buf = x
        y_buf = y
        steps = 0

        i = 0
        while i <= dx:
            if not silent:
                self.matplotlib_widget.axis.plot(floor(x), floor(y), 'o', c=color, markersize = 1)

            if e >= 0:
                if exchange == 1:
                    x += x_sign
                else:
                    y += y_sign

                e -= 2 * dx

            if exchange == 1:
                y += y_sign
            else:
                x += x_sign
            
            e += 2 * dy
            i += 1

            if x_buf != x and y_buf != y:
                steps += 1

                x_buf = x
                y_buf = y

        return steps

    def line_draw_bresenham_aas(self, dot_s, dot_e, color, silent = False):
        dx = dot_e[0] - dot_s[0]
        dy = dot_e[1] - dot_s[1]

        x_sign = self.sign(dx)
        y_sign = self.sign(dy)

        dx = abs(dx)
        dy = abs(dy)

        exchange = 0
        if dy > dx:
            dx, dy = dy, dx
            exchange = 1
            

        m = dy / dx
        w = 1 - m
        e = 0.5

        x, y = dot_s

        x_buf = x
        y_buf = y
        steps = 0

        i = 0
        while i <= dx:
            if not silent:
                color_n = list(deepcopy(color))
                color_n[3] = e
                self.matplotlib_widget.axis.plot(floor(x), floor(y), 'o', c=color_n, markersize = 1)

            if e < w:
                if exchange == 0:
                    x += x_sign
                else:
                    y += y_sign

                e += m

            else:
                x += x_sign
                y += y_sign
                e -= w

            i += 1

            if x_buf != x and y_buf != y:
                steps += 1

                x_buf = x
                y_buf = y

        return steps

    def line_draw_wu(self, dot_s, dot_e, color, silent = False):
        x1, y1 = dot_s
        x2, y2 = dot_e

        dx = x2 - x1
        dy = y2 - y1

        m = 1
        step = 1

        steps = 0

        if abs(dy) >= abs(dx):
            m = dx / dy    
            m1 = m

            if y1 > y2:
                step *= -1
                m1 *= -1

            bord = round(y2) - 1 if dy < dx else round(y2) + 1

            for y in range(round(y1), bord, step):
                d1 = x1 - floor(x1)
                d2 = 1 - d1

                if not silent:
                    color_1 = list(deepcopy(color))
                    color_1[3] = 1 - fabs(d2)
                    color_2 = list(deepcopy(color))
                    color_2[3] = 1 - fabs(d1)

                    self.matplotlib_widget.axis.plot(floor(x1) + 1, y, 'o', c=color_1, markersize = 1)
                    self.matplotlib_widget.axis.plot(floor(x1), y, 'o', c=color_2, markersize = 1)

                if y < round(y2) and floor(x1) != floor(x1 + m):
                    steps += 1

                x1 += m1

        else:
            m = dy / dx
            m1 = m

            if x1 > x2:
                step *= -1
                m1 *= -1

            bord = round(x2) - 1 if dy > dx else round(x2) + 1

            for x in range(round(x1), bord, step):
                d1 = y1 - floor(y1)
                d2 = 1 - d1

                if not silent:
                    color_1 = list(deepcopy(color))
                    color_1[3] = 1 - fabs(d2)
                    color_2 = list(deepcopy(color))
                    color_2[3] = 1 - fabs(d1)

                    self.matplotlib_widget.axis.plot(x, floor(y1) + 1, 'o', c=color_1, markersize = 1)
                    self.matplotlib_widget.axis.plot(x, floor(y1), 'o', c=color_2, markersize = 1)

                if x < round(x2) and round(y1) != round(y1 + m):
                    steps += 1

                y1 += m1

        return steps
    


    # Функции отрисовки спектра
    def spectre_draw_stand(self, centre, lenght, degree, color):
        dot_end = deepcopy(centre)
        dot_end[1] += lenght
        cur_degree = 0
        while abs(cur_degree) < 360:
            self.line_draw_stand(centre, dot_end, color)
            cur_degree += degree
            self.point_rotate(dot_end, centre, degree)
    
    def spectre_draw_dda(self, centre, lenght, degree, color, silent_draw = False):
        dot_end = deepcopy(centre)
        dot_end[1] += lenght
        cur_degree = 0
        while abs(cur_degree) < 360:
            self.line_draw_dda(centre, dot_end, color, silent_draw)
            cur_degree += degree
            self.point_rotate(dot_end, centre, degree)
    
    def spectre_draw_bresenham_float(self, centre, lenght, degree, color, silent_draw = False):
        dot_end = deepcopy(centre)
        dot_end[1] += lenght
        cur_degree = 0
        while abs(cur_degree) < 360:
            self.line_draw_bresenham_float(centre, dot_end, color, silent_draw)
            cur_degree += degree
            self.point_rotate(dot_end, centre, degree)
    
    def spectre_draw_bresenham_int(self, centre, lenght, degree, color, silent_draw = False):
        dot_end = deepcopy(centre)
        dot_end[1] += lenght
        cur_degree = 0
        while abs(cur_degree) < 360:
            self.line_draw_bresenham_int(centre, dot_end, color, silent_draw)
            cur_degree += degree
            self.point_rotate(dot_end, centre, degree)
    
    def spectre_draw_bresenham_aas(self, centre, lenght, degree, color, silent_draw = False):
        dot_end = deepcopy(centre)
        dot_end[1] += lenght
        cur_degree = 0
        while abs(cur_degree) < 360:
            self.line_draw_bresenham_aas(centre, dot_end, color, silent_draw)
            cur_degree += degree
            self.point_rotate(dot_end, centre, degree)
    
    def spectre_draw_bresenham_wu(self, centre, lenght, degree, color, silent_draw = False):
        dot_end = deepcopy(centre)
        dot_end[1] += lenght
        cur_degree = 0
        while abs(cur_degree) < 360:
            self.line_draw_wu(centre, dot_end, color, silent_draw)
            cur_degree += degree
            self.point_rotate(dot_end, centre, degree)
    


    # Функции замера
    def measure_exec_time(self, centre, lenght, degree):
        if degree == 0 or lenght == 0:
            self.show_warning_spectre_nexist()
            return

        measure_time = list()
        methods_list = ["Ф-я библиотеки", "ЦДА", "Бр-м вещ.", "Бр-м целочисл.", "Бр-м с устр. ступ.", "Ву"]

        for i in range(6):
            time_start = time.time_ns()
            for j in range(3):
                self.draw_spectre_hub(centre, lenght, degree, i, self.canvas_line_color, True, False)
            time_end = time.time_ns()
            self.canvas_default()
            measure_time.append((time_end - time_start) / 3 / 1000)

        plt.figure(figsize = (12, 6))
        plt.title(f"Время отрисовки спектров длиной {lenght} и углом {degree} разными алгоритмами.")

        positions = [i for i in range(6)]

        plt.xticks(positions, methods_list)
        plt.ylabel("Время, мкс")

        plt.bar(positions, measure_time, align = "center", alpha = 1)

        plt.show()

    def measure_stepping(self, lenght):
        if lenght == 0:
            self.show_warning_wrong_line()
            return

        stepping_measure = [list() for i in range(5)]
        degrees = [i for i in range(91)]

        methods_list = ["ЦДА", "Бр-м вещ.", "Бр-м целочисл.", "Бр-м с устр. ступ.", "Ву"]

        centre = [0, 0]
        for i in range(1, 6):
            dot_e = [0, lenght]
            for j in range(46):
                steps = self.draw_line_hub(centre, dot_e, i, self.canvas_line_color, True, True)
                self.point_rotate(dot_e, centre, 1)
                stepping_measure[i - 1].append(steps)
                print(f"\r{j} с {methods_list[i - 1]}", end = '')
            self.canvas_default()

        for method in stepping_measure:
            leng = len(method)
            for i in range(1, leng):
                method.append(method[leng - 1 - i])


        plt.figure(figsize = (12, 6))
        plt.title(f"Исследование ступенчатости отрезков длиной {lenght} при разных углах наклона.")

        
        plt.ylabel("Кол-во 'ступенек'")
        plt.xlabel("Угол наклона отрезка")

        plt.plot(degrees, stepping_measure[0], linestyle = '-', label = methods_list[0])
        plt.plot(degrees, stepping_measure[1], linestyle = '--', label = methods_list[1])
        plt.plot(degrees, stepping_measure[2], linestyle = ':', label = methods_list[2])
        plt.plot(degrees, stepping_measure[3], linestyle = '-.', label = methods_list[3])
        plt.plot(degrees, stepping_measure[4], linestyle = (0, (3, 3, 1, 3, 1, 3)), label = methods_list[4])

        plt.legend()
        plt.xticks([i for i in range(0, 91, 5)])
        plt.show()

    # Доп функции
    def point_rotate(self, dot, centre, degree):
        degree_ = radians(degree)
        cos_ = cos(degree_)
        sin_ = sin(degree_)

        new_x = centre[0] + (dot[0] - centre[0]) * cos_ + (dot[1] - centre[1]) * sin_
        new_y = centre[1] + (dot[1] - centre[1]) * cos_ - (dot[0] - centre[0]) * sin_
        dot[0], dot[1] = new_x, new_y

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
    
    def sign(self, x):
        if x == 0:
            return 0
        return 1 if x > 0 else -1