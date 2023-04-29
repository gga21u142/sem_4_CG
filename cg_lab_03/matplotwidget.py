
# Виджет матплотлиба для канвы

import matplotlib

from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT 
from matplotlib.figure import Figure

class MatplotlibWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.axis = self.figure.add_subplot(1, 1, 1)

        self.colors_line = {"Черный":(0, 0, 0, 1), "Белый":(1, 1, 1, 1), "Красный":(1, 0, 0, 1), "Зеленый":(0, 1, 0, 1), "Синий":(0, 0, 1, 1), "Желтый":(1, 1, 0, 1), "Фиолетовый":(0.5, 0, 0.5, 1), "Розовый":(1, 0, 1, 1), "Оранжевый":(1, 0.5, 0, 1)}
        self.colors_bg = {"Черный":(0, 0, 0, 0.5), "Белый":(1, 1, 1, 1), "Красный":(1, 0, 0, 0.5), "Зеленый":(0, 1, 0, 0.5), "Синий":(0, 0, 1, 0.5), "Желтый":(1, 1, 0, 0.5), "Фиолетовый":(0.5, 0, 0.5, 0.5), "Розовый":(1, 0, 1, 0.5), "Оранжевый":(1, 0.5, 0, 0.5)}
        
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        
        self.layout_vertical = QtWidgets.QVBoxLayout(self)
        self.layout_vertical.addWidget(self.canvas) 
        self.layout_vertical.addWidget(self.toolbar)
        self.figure.tight_layout()
