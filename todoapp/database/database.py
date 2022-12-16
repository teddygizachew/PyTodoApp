import sqlite3

from todoapp.database.MetaSingleton import MetaSingleton


class SQLiteDatabase(metaclass=MetaSingleton):
    connection = None
    db_name = "todoapp.db"

    def __init__(self):
        self.cur = None
        self.connection = None
        self.db_name = SQLiteDatabase.db_name
        self.todoapp = "todoapp"

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect(self.db_name)
            self.cur = self.connection.cursor()

        return self.cur

    def close(self):
        self.connection.close()

    def create_table(self):
        # generate the query string
        query = 'CREATE TABLE IF NOT EXISTS todoapp (todoID INTEGER PRIMARY KEY, date date, startTime timestamp, endTime timestamp, task TEXT, tag TEXT, completion int DEFAULT 0)'
        # execute the query
        self.cur.execute(query)

    def insert(self, date, startTime, endTime, task, tag):
        # execute the query

        query = 'INSERT INTO todoapp (date, startTime, endTime, task, tag) VALUES (?, ?, ?, ?, ?)'
        # execute the query
        self.cur.execute(query, [date, startTime, endTime, task, tag])
        self.connection.commit()
        print(f"Successfully inserted '{task}'!")

    def query(self, tag_name=""):
        # generate the query string
        query = f"SELECT todoID, STRFTIME('%m/%d/%Y', date), startTime, endTime, task, tag, completion FROM {self.todoapp}"

        # add condition if provided
        if tag_name == "ALL":
            self.cur.execute(query)
        elif tag_name == "TAGS":
            column_query = f"SELECT tag FROM {self.todoapp}"
            self.cur.execute(column_query)
        else:
            query += f" WHERE tag = ?"
            self.cur.execute(query, (tag_name,))
        # execute the query and return the result
        # self.cur.execute(query)
        # self.cur.execute("SELECT * FROM todoapp WHERE tag =?", (tag_name,))
        return self.cur.fetchall()

    def update(self, row, value):
        # generate the query string
        # if value == "complete" or value == "done":
        #     value = 1
        # execute the query
        self.cur.execute("UPDATE todoapp SET task = ? WHERE todoID = ?", (value, row))
        self.connection.commit()

    def delete(self, condition=""):
        # generate the query string
        query = f"DELETE FROM todoapp"
        query += f" WHERE tag=?"
        self.cur.execute(query, (condition,))
        print(f"Successfully deleted {condition}!")
        # execute the query
        self.connection.commit()

    def drop(self):
        # generate the query string
        query = f"DROP TABLE IF EXISTS todoapp"

        # add condition if provided
        self.cur.execute(query)
        self.connection.commit()
        print("Successfully deleted all data!")

    def complete(self, todo_ID):
        # generate the query string
        self.cur.execute("UPDATE todoapp SET completion = ? WHERE todoID = ?", (1, todo_ID))
        self.connection.commit()

        print("Successfully completed to-do!")

