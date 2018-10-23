
import sys

from dbProvider import SQLiteLayer
from dbProvider import DbConnectionError, QueryExecutionError

from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from window import Ui_MainWindow


class ResultTableModel(QAbstractTableModel):
    def __init__(self, items, headers):
        super(ResultTableModel, self).__init__()
        self.items = items
        self.headers = headers

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.headers[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def rowCount(self, parent):
        return len(self.items)

    def columnCount(self, parent):
        if self.items:
            return len(self.items[0])
        if self.headers:
            return len(self.headers)
        return QAbstractTableModel.columnCount(self, parent)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            row = self.items[index.row()]
            return row[index.column()]
        return QAbstractTableModel.data(self, index, role)    


class MainWindow(QMainWindow, Ui_MainWindow):

    createSql = "select * from customer"
    selectSql = "select * from users"

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.executeBtn.clicked.connect(self.executeQuery)
        self.openBtn.clicked.connect(self.openFile)
        self.resultTable.verticalHeader().hide()
        self.queryTextEdit.setText(self.createSql)
        self.connectionStringLineEdit.setText(":memory:")
        self.outputTextView.setReadOnly(True)
        self.db_layer = SQLiteLayer()

    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self,
            "Open database",
            "",
            "SQLite database files (*.db *.sqlite *.db3 *.sqlite3)",
            options=options)
        if fileName:
            self.connectionStringLineEdit.setText(fileName)

    def executeQuery(self):
        con_string = str(self.connectionStringLineEdit.text())
        query = str(self.queryTextEdit.toPlainText())
        try:
            result, headers = self.db_layer.execute_query(con_string, query)
            self.resultTable.setModel(ResultTableModel(result, headers))
            self.outputTextView.append("\n%s\nSuccess.\n" % (query))

        except DbConnectionError as ce:
            self.outputTextView.append(
                "\n%s\nConnection error: %s\n" % (query, ce)
            )
        except QueryExecutionError as ee:
            self.outputTextView.append(
                "\n%s\nExecution error: %s\n" % (query, ee)
            )
        self.outputTextView.ensureCursorVisible()

    def closeEvent(self, event):
        self.db_layer.close()
        event.accept()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F5:
            self.executeQuery()


def app_main(args):
    app = QApplication(sys.argv)
    view = MainWindow()
    view.show()
    return app.exec_()

if __name__ == '__main__':
    sys.exit(app_main(sys.argv))
