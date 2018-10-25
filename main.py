
import sys
from data_provider import DbConnectionError, QueryExecutionError

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import Qt

from window import Ui_MainWindow
from model import ResultTableModel


class MainWindow(QMainWindow, Ui_MainWindow):

    createSql = 'select * from customer'
    selectSql = 'select * from users'

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.executeBtn.clicked.connect(self.executeQuery)
        self.openBtn.clicked.connect(self.openFile)
        self.resultTable.verticalHeader().hide()
        self.queryTextEdit.setText(self.createSql)
        self.connectionStringLineEdit.setText(':memory:')
        self.outputTextView.setReadOnly(True)

    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self,
            'Open database',
            '',
            'SQLite database files (*.db *.sqlite *.db3 *.sqlite3)',
            options=options)
        if fileName:
            self.connectionStringLineEdit.setText(fileName)

    def fetched(self, items):
        self.rowCountLabel.setText('\nFetched: %s' % str(len(items)))

    def executeQuery(self):
        con_string = str(self.connectionStringLineEdit.text())
        query = str(self.queryTextEdit.toPlainText())

        if self.resultTable.model():
            self.resultTable.model().clear()
        else:
            self.resultTable.setModel(ResultTableModel())
            self.resultTable.model().fetched.connect(self.fetched)

        model = self.resultTable.model()
        try:
            model.execute_query(con_string, query)
            self.outputTextView.append('\n%s\nSuccess.\n' % (query))

        except DbConnectionError as ce:
            self.outputTextView.append(
                '\n%s\nConnection error: %s\n' % (query, ce)
            )
        except QueryExecutionError as ee:
            self.outputTextView.append(
                '\n%s\nExecution error: %s\n' % (query, ee)
            )
        except Exception as e:
            self.outputTextView.append(
                '\n%s\nUndefined error: %s\n' % (query, e)
            )
        self.outputTextView.ensureCursorVisible()

    def closeEvent(self, event):
        self.resultTable.model().close()
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
