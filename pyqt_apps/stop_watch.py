from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Stopwatch(QWidget):
    def __init__(self, name, counter_value, parent=None):
        super().__init__(parent)
        self.count = 0
        self.flag = False
        self.counter_value = counter_value

        layout = QGridLayout()
        layout.setVerticalSpacing(2)
        layout.setContentsMargins(2, 2, 2, 2)

        name_label = QLabel(name, self)
        name_label.setFont(QFont('Arial', 16))
        name_label.setAlignment(Qt.AlignLeft)
        name_label.setFixedHeight(20)
        layout.addWidget(name_label, 0, 0, 1, 1)

        self.name_count_label = QLabel(str(self.counter_value), self)
        self.name_count_label.setFont(QFont('Arial', 16))
        self.name_count_label.setAlignment((Qt.AlignRight))
        self.name_count_label.setFixedHeight(20)
        layout.addWidget(self.name_count_label, 0, 1, 1, 1)

        self.label = QLabel("0.0", self)
        self.label.setStyleSheet("border : 2px solid black;")
        self.label.setFont(QFont('Arial', 16))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFixedHeight(30)
        layout.addWidget(self.label, 1, 0, 1, 2)

        start = QPushButton("Start", self)
        start.pressed.connect(self.start)
        layout.addWidget(start, 2, 0, 1, 1)

        pause = QPushButton("Pause", self)
        pause.pressed.connect(self.pause)
        layout.addWidget(pause, 2, 1, 1, 1)

        reset = QPushButton("Reset", self)
        reset.pressed.connect(self.reset)
        layout.addWidget(reset, 3, 0, 1, 2)
        reset.setContentsMargins(0, 0, 0, 0)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(100)

        self.setLayout(layout)

    def showTime(self):
        if self.flag:
            self.count += 1

        seconds = self.count // 10
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        text = f"{hours:02}:{minutes:02}:{seconds:02}"
        self.label.setText(text)

    def start(self):
        self.flag = True

        self.update_counter_value()

    def pause(self):
        self.flag = False

    def reset(self):
        self.flag = False
        self.count = 0
        self.label.setText("00:00:00")
        self.flag = True

        self.update_counter_value()

    def update_counter_value(self):
        self.counter_value += 1
        self.name_count_label.setText(str(self.counter_value))


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mohan Stopwatches")
        self.setGeometry(100, 100, 200, 800)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        main_layout = QGridLayout()
        main_layout.setVerticalSpacing(5)
        main_layout.setContentsMargins(5,5,5,5)
        #main_layout.setVerticalSpacing(0)

        self.stopwatches = {}
        counter_value = 0
        names = ["9-WS", "6-LB", "6-SB", "5-W", "4-R", "4-F", "8-T", "7-W"]
        for i, name in enumerate(names):
            stopwatch = Stopwatch(name, counter_value, self)
            row = i // 2
            col = i % 2
            main_layout.addWidget(stopwatch, row, col)
            self.stopwatches[name] = stopwatch

        print(self.stopwatches)

        short_break_button = QPushButton("Short Break", self)
        short_break_button.clicked.connect(self.reset_short_break_timers)
        main_layout.addWidget(short_break_button)

        long_break_button = QPushButton("Long Break", self)
        long_break_button.clicked.connect(self.reset_long_break_timers)
        main_layout.addWidget(long_break_button)

        start_all_button = QPushButton("Start ALL", self)
        start_all_button.clicked.connect(self.start_all_timers)
        main_layout.addWidget(start_all_button)

        reset_all_button = QPushButton("Reset ALL", self)
        reset_all_button.clicked.connect(self.reset_all_timers)
        main_layout.addWidget(reset_all_button)

        rrr_button = QPushButton("RRR", self)
        rrr_button.clicked.connect(self.rrr_timers)
        main_layout.addWidget(rrr_button)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.show()

    def reset_short_break_timers(self):
        timers_to_reset = ["9-WS", "6-SB"]
        for timer in timers_to_reset:
            if timer in self.stopwatches.keys():
                #print(timer)
                self.stopwatches[timer].reset()

    def reset_long_break_timers(self):
        timers_to_reset = ["9-WS", "6-SB", "6-LB"]
        for timer in timers_to_reset:
            if timer in self.stopwatches.keys():
                #print(timer)
                self.stopwatches[timer].reset()

    def start_all_timers(self):
        for _ in self.stopwatches.keys():
            self.stopwatches[_].start()

    def reset_all_timers(self):
        for _ in self.stopwatches.keys():
            self.stopwatches[_].reset()

    def rrr_timers(self):
        timers_to_reset = ["9-WS", "6-SB", "4-R"]
        for timer in timers_to_reset:
            if timer in self.stopwatches.keys():
                # print(timer)
                self.stopwatches[timer].reset()


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())