from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex
from PyQt5.QtCore import pyqtSignal
from data_provider import SQLiteDatabaseProvider


class ResultTableModel(QAbstractTableModel):
    fetched = pyqtSignal(list)

    def __init__(self, items=[], headers=[]):
        super().__init__()
        self.items = items
        self.headers = headers
        self.db_provider = SQLiteDatabaseProvider()

    def execute_query(self, connection_string, query):
        self.connection_string, self.query = connection_string, query
        self.clear()
        items = self.db_provider.execute(connection_string, query)
        self.headers = self.db_provider.headers
        self.items += items
        self.emit_data_changed()
        self.fetched.emit(self.items)

    def fetchMore(self, index):
        if self.db_provider:
            items = self.db_provider.fetch_next(
                self.connection_string, self.query)
            self.items += items
            self.emit_data_changed()
            self.fetched.emit(self.items)

    def canFetchMore(self, index):
        if self.db_provider:
            return self.db_provider.there_is_any_record
        return False

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole and self.headers:
            return self.headers[section]
        return QAbstractTableModel.headerData(self, section, orientation, role)

    def rowCount(self, parent):
        return len(self.items)

    def columnCount(self, parent):
        if self.items:
            return len(self.items[0])
        if self.headers:
            return len(self.headers)
        return 0

    def data(self, index, role):
        if role == Qt.DisplayRole:
            row = self.items[index.row()]
            return row[index.column()]

    def clear(self):
        self.items = []
        self.headers = []

    def close(self):
        if self.db_provider:
            self.db_provider.close()

    def emit_data_changed(self):
        self.beginResetModel()
        self.endResetModel()
