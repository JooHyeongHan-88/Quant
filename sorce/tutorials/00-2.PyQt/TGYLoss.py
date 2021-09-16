import sys
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self._setup_ui()

    def _setup_ui(self):
        self.setGeometry(800, 200, 800, 400)
        self.setWindowTitle("TGYLoss1.0")

        layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        right_layout = QVBoxLayout()
        layout_source = QVBoxLayout()
        layout_date = QVBoxLayout()
        layout_open_s5k = QHBoxLayout()
        layout_open_s5s = QHBoxLayout()
        layout_open_scrap = QHBoxLayout()
        layout_open_wip = QHBoxLayout()
        layout_year = QHBoxLayout()
        layout_week = QHBoxLayout()

        box_source = QGroupBox("소스 파일")
        box_date = QGroupBox("연도/주차 설정")

        label_s5k = QLabel("상판 TYPE 전환 (S5K)", self)
        label_s5s = QLabel("하판 TYPE 전환 (S5S)", self)
        label_scrap = QLabel("Scrap", self)
        label_wip = QLabel("FAB 재공", self)
        label_year = QLabel("연도: ", self)
        label_week = QLabel("주차: ", self)

        self.dir_s5k = QLabel()
        self.dir_s5s = QLabel()
        self.dir_scrap = QLabel()
        self.dir_wip = QLabel()

        button_s5k = QPushButton("Open")
        button_s5k.clicked.connect(self._open_s5k_clicked)
        button_s5s = QPushButton("Open")
        button_s5s.clicked.connect(self._open_s5s_clicked)
        button_scrap = QPushButton("Open")
        button_scrap.clicked.connect(self._open_scrap_clicked)
        button_wip = QPushButton("Open")
        button_wip.clicked.connect(self._open_wip_clicked)
        button_run = QPushButton("RUN")
        button_run.clicked.connect(self._run_main_program)

        self.spin_box_year = QSpinBox(self)
        self.spin_box_year.setMinimum(2021)
        self.spin_box_year.setMaximum(2040)

        self.spin_box_week = QSpinBox(self)
        self.spin_box_week.setMinimum(1)
        self.spin_box_week.setMaximum(53)
        
        layout_open_s5k.addWidget(label_s5k)
        layout_open_s5k.addWidget(button_s5k)
        layout_open_s5s.addWidget(label_s5s)
        layout_open_s5s.addWidget(button_s5s)
        layout_open_scrap.addWidget(label_scrap)
        layout_open_scrap.addWidget(button_scrap)
        layout_open_wip.addWidget(label_wip)
        layout_open_wip.addWidget(button_wip)

        layout_source.addLayout(layout_open_s5k)
        layout_source.addWidget(self.dir_s5k)
        layout_source.addLayout(layout_open_s5s)
        layout_source.addWidget(self.dir_s5s)
        layout_source.addLayout(layout_open_scrap)
        layout_source.addWidget(self.dir_scrap)
        layout_source.addLayout(layout_open_wip)
        layout_source.addWidget(self.dir_wip)

        box_source.setLayout(layout_source)

        left_layout.addWidget(box_source)

        layout_year.addWidget(label_year)
        layout_year.addWidget(self.spin_box_year)

        layout_week.addWidget(label_week)
        layout_week.addWidget(self.spin_box_week)

        layout_date.addLayout(layout_year)
        layout_date.addLayout(layout_week)

        box_date.setLayout(layout_date)

        right_layout.addWidget(box_date)
        right_layout.addWidget(button_run)
        

        ###### check #######
        self.check = QLabel()
        right_layout.addWidget(self.check)
        #################


        layout.addLayout(left_layout)
        layout.addLayout(right_layout)

        self.setLayout(layout)

    def _open_s5k_clicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.dir_s5k.setText(fname[0])

    def _open_s5s_clicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.dir_s5s.setText(fname[0])

    def _open_scrap_clicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.dir_scrap.setText(fname[0])

    def _open_wip_clicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.dir_wip.setText(fname[0])

    def _run_main_program(self):
        date_year = self.spin_box_year.value()
        date_week = self.spin_box_week.value()
        msg = '연도: %d / 주차: %d' % (date_year, date_week)
        self.check.setText(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()