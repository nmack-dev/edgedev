#!/usr/bin/env python

import sys
import requests
import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):

    # This must initialize the size of the qt canvas
    def __init__(self, parent=None, width=5, height=4, dpi = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Generates the window and PyQt widget
        self.canvas = MplCanvas(self, width=10.24, height=7.68, dpi=100)
        self.setCentralWidget(self.canvas)

        # Makes a call to the alpha vantage api given a stock ticker
        self.stock_ticker = 'AAPL'
        self.interval = 1
        self.api_key = '4N8Y14A6Z02I26VB'
        self.get_url = 'https://www.alphavantage.co/query?' \
                       'function=TIME_SERIES_INTRADAY&symbol=%s' \
                       '&interval=%smin&apikey=%s' \
                       % (self.stock_ticker, self.interval, self.api_key)

        self.data = None
        self.stock_data = None
        self.data_dict = None
        self.stock_data_dict = None
        self.values = None

        self.get_stock_data()

        self.xdata = range(100)
        self.ydata = self.values
        self.canvas.axes.plot(self.xdata, self.ydata, 'r')
        self.canvas.draw()
        self.show()

        # Setup a timer to trigger the redraw by calling update_plot
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

        self.timeout = 0

    def get_stock_data(self):
        self.data = requests.get(self.get_url)
        self.stock_data = self.data.json()

        self.data_dict = self.stock_data['Time Series (%smin)' % (self.interval)]
        self.stock_data_dict = {}

        for key in self.data_dict:
            temp = self.data_dict[key]['4. close']
            self.stock_data_dict[key] = temp

        self.values = []

        for item in list(self.stock_data_dict.values()):
            self.values.append(float(item))

    def update_plot(self):
        self.timeout = self.timeout + 1

        file = open('placeholder.txt', 'r+')
        words = [word.strip() for line in file.readlines() for word in line.split(',') if word.strip()]

        if (words):
            if ((words[0] is not self.stock_ticker) & (words[1] is not self.interval)):
                self.stock_ticker = words[0]
                self.interval = words[1]
                self.get_url = 'https://www.alphavantage.co/query?' \
                            'function=TIME_SERIES_INTRADAY&symbol=%s' \
                            '&interval=%smin&apikey=%s' \
                            % (self.stock_ticker, self.interval, self.api_key)
                file.truncate(0)
                self.get_stock_data()

        elif (self.timeout == (60 * self.interval)):
            self.get_stock_data()

        self.canvas.axes.cla()
        self.canvas.axes.plot(range(100), self.values, 'r')
        self.canvas.draw()

        file.close()

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
