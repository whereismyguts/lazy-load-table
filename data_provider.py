import sqlite3
import os.path


class QueryExecutionError(Exception):
    def __init__(self, message, *errors):
        super().__init__(message)
        self.errors = errors


class DbConnectionError(Exception):
    def __init__(self, message, *errors):
        super().__init__(message)
        self.errors = errors


class SQLiteDatabaseProvider:

    def __init__(self):
        self.connection_string = ""
        self.connection = None
        self.cursor = None
        self.there_is_any_record = True
        self.headers = []

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def validate_and_connect(self, cs):
        if self.connection_string != cs:
            if cs == ":memory:" or os.path.isfile(cs):
                self.headers = []
                self.close_connection()
                self.connection_string = cs
                self.connection = sqlite3.connect(cs)
                return
            raise DbConnectionError("Connection string is not valid.")

    def exception_aware(func):
        def result(*args):
            try:
                return func(*args)
            except (
                    sqlite3.OperationalError,
                    sqlite3.Warning,
                    sqlite3.DatabaseError) as e:
                raise QueryExecutionError(str(e), e)
        return result

    @exception_aware
    def execute(self, connection_string, query):
        self.there_is_any_record = True
        self.validate_and_connect(connection_string)
        self.cursor = self.connection.cursor()
        self.cursor.execute(query)
        self.connection.commit()
        return self.fetch_next(connection_string, query)

    @exception_aware
    def fetch_next(self, connection_string, query):
        result = []
        if not self.connection:
            return result
        while self.there_is_any_record:
            row = self.cursor.fetchone()
            if row:
                result.append(row)
                if len(result) >= 10000:
                    break
            else:
                self.there_is_any_record = False

        if self.cursor.description:
            self.headers = [col[0] for col in self.cursor.description]

        return result

    def close(self):
        if self.connection:
            self.connection.close()
