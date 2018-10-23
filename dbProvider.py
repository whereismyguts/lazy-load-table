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


class SQLiteLayer:

    def __init__(self):
        self.connection_string = ""
        self.connection = None

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def validate_and_connect(self, cs):

        if self.connection_string != cs:
            if cs == ":memory:" or os.path.isfile(cs):
                self.close_connection()
                self.connection_string = cs
                self.connection = sqlite3.connect(cs)
                return

            raise DbConnectionError("Connection string is not valid.")

    def execute_query(self, connection_string, query):
        self.validate_and_connect(connection_string)

        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()

            result = []
            self.count = 0
            there_is_any_record = True
            while there_is_any_record:
                row = cursor.fetchone()
                if row:
                    result.append(row)
                    self.count += 1
                    if self.count > 100000:
                        there_is_any_record = False
                else:
                    there_is_any_record = False

            headers = []
            if cursor.description:
                    headers = [col[0] for col in cursor.description]
            if result:
                return result, headers
            return [], headers

        except (sqlite3.OperationalError,
                sqlite3.Warning,
                sqlite3.DatabaseError) as e:
                    raise QueryExecutionError(str(e), e)

    def close(self):
        if self.connection:
            self.connection.close()
