from database import SQLiteDatabase
import datetime


class TestClass:
    def setup_class(self):
        self.db = SQLiteDatabase()
        self.db.connect()
        self.db.create_table()
        print("setup_class called once for the class")

    def teardown_class(self):
        # Close connection
        self.db.connection.close()
        print("teardown_class called once for the class")

    def setup_module(module):
        """ setup any state specific to the execution of the given module."""

    def teardown_module(module):
        """ teardown any state that was previously setup with a setup_module
        method.
        """

    def test_sqlite3_database_connection(self):
        # Setup database connection
        self.db.connect()
        # conn = sqlite3.connect('test.db')

        # Check if connection is successful
        assert self.db.connection is not None

    def test_insert_from_database(self):
        current_date_time = datetime.datetime.now()
        date = current_date_time
        start_time = "1AM"
        end_time = "2AM"
        task = "task"
        tag = "pytest"
        query = 'INSERT INTO todoapp (date, startTime, endTime, task, tag) VALUES (?, ?, ?, ?, ?)'

        assert self.db.cur.execute(query, [date, start_time, end_time, task, tag]) is not None
