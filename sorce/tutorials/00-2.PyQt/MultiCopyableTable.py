import sys
import io
import csv
import pandas as pd
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtCore import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        data = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['c1', 'c2', 'c3'], index=['r1', 'r2', 'r3'])
        self.table_win = TableWindow(data)

        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("TEST")

        layout = QVBoxLayout()
        label = QLabel("Data Table", self)
        button = QPushButton("Show")
        button.clicked.connect(self._open_table)
 
        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)

    def _open_table(self):
        self.table_win.show()


class TableWindow(QWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self._setup_ui()

    def _setup_ui(self):
        self.setWindowTitle("TEST")

        layout = QVBoxLayout()
        label = QLabel("Data Table", self)
        self.table = MultiCopyableTable()
 
        self.table.set_data(self.data)
        layout.addWidget(label)
        layout.addWidget(self.table)
        self.setLayout(layout)


class MultiCopyableTable(QTableWidget):
    def __init__(self):
        super().__init__()
        
    def set_data(self, df):

        cols = list(df)
        rows = list(df.index)

        ncols = len(cols)
        nrows = len(rows)

        for i in range(nrows):
            for j in range(ncols):
                self.setItem(i, j, QTableWidgetItem(str(df.iat[i, j])))

        self.setHorizontalHeaderLabels(cols)
        self.setVerticalHeaderLabels(rows)
        self.setColumnCount(ncols)
        self.setRowCount(nrows)
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def keyPressEvent(self, ev):
        if (ev.key() == Qt.Key_C) and (ev.modifiers() & Qt.ControlModifier): 
            self._copy_selection()

    def _copy_selection(self):
        selection = self.selectedIndexes()
        if selection:
            rows = sorted(index.row() for index in selection)
            cols = sorted(index.column() for index in selection)
            nrows = rows[-1] - rows[0] + 1
            ncols = cols[-1] - cols[0] + 1
            table = [[''] * ncols for _ in range(nrows)]
            for index in selection:
                row = index.row() - rows[0]
                column = index.column() - cols[0]
                table[row][column] = index.data()
            stream = io.StringIO()
            csv.writer(stream).writerows(table)
            QApplication.clipboard().setText(stream.getvalue())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec()