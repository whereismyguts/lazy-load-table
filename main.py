import sqlite3
import sys

from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow

from window import UiMainWindow


class QueryResultTableModel(QAbstractTableModel):
    def __init__(self, items):
        super(QueryResultTableModel, self).__init__()
        self.items = items

    def rowCount(self, parent):
        return len(self.items)

    def columnCount(self, parent):
        return len(self.items[0])

    def data(self, index, role):
        if role == Qt.DisplayRole:
            row = self.items[index.row()]
            return row[index.column()]        


class MainWindow(QMainWindow, UiMainWindow):
    
    connection = None
    connection_string = ""
    createSql = "CREATE TABLE users (id integer, name text, address text)"
    selectSql = "select * from users"

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        UiMainWindow.__init__(self)
        self.setupUi(self)

        self.executeBtn.clicked.connect(self.executeQuery)
        self.resultTable.horizontalHeader().hide()
        self.resultTable.verticalHeader().hide()
        self.queryTextEdit.setText(self.createSql)
        self.connectionStringLineEdit.setText(":memory:")
        self.outputTextView.setReadOnly(True)


    def executeQuery(self):
        con_string = str(self.connectionStringLineEdit.text())
        if self.connection_string != con_string and self.connection:
            self.connection.close()
            self.connection = None

        if not self.connection:    
            self.connection = sqlite3.connect(con_string)
            self.connection_string = con_string

        cursor = self.connection.cursor()
        try:
            query = str(self.queryTextEdit.toPlainText())
            cursor.execute(query)
            self.connection.commit()
            result = cursor.fetchall()
            if result:
                self.resultTable.setModel(QueryResultTableModel(result))
            else:
                self.outputTextView.append( "\n%s\nSuccess.\n" % query)                                
                
        except (sqlite3.OperationalError, sqlite3.Warning) as e:
            self.outputTextView.append( "\n%s\nError: %s\n" % (query, e))

    def closeEvent(self, event):
        if self.connection:
            self.connection.close()
        event.accept()

def app_main(args):
    app = QApplication(sys.argv)
    view = MainWindow()
    view.show()
    return app.exec_()

if __name__ == '__main__':
    sys.exit(app_main(sys.argv))
