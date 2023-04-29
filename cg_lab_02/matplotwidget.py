
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
        
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        
        self.layout_vertical = QtWidgets.QVBoxLayout(self)
        self.layout_vertical.addWidget(self.canvas) 
        self.layout_vertical.addWidget(self.toolbar)
        self.figure.tight_layout()
