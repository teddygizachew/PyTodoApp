import sqlite3


class SQLiteDatabase(object):
    db_name = "todoapp.db"

    def __init__(self):
        self.cur = None
        self.connection = None
        self.db_name = SQLiteDatabase.db_name
        self.todoapp = "todoapp"

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cur = self.connection.cursor()

    def close(self):
        self.connection.close()

    def create_table(self):
        # generate the query string
        # execute the query
        query = 'CREATE TABLE IF NOT EXISTS todoapp (todoID INTEGER PRIMARY KEY, date date, startTime timestamp, endTime timestamp, task TEXT, tag TEXT)'
        self.cur.execute(query)

    def insert(self, date, startTime, endTime, task, tag):
        # execute the query
        default_completion = 0
        query = 'INSERT INTO todoapp (date, startTime, endTime, task, tag) VALUES (?, ?, ?, ?, ?)'
        self.cur.execute(query, [date, startTime, endTime, task, tag])
        self.connection.commit()
        print(f"Successfully inserted '{task}'!")

    def query(self, tag_name=""):
        # generate the query string
        query = f"SELECT todoID, STRFTIME('%m/%d/%Y', date), startTime, endTime, task, tag FROM {self.todoapp}"

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
        if value == "complete" or value == "done":
            value = 1
        query = f"UPDATE {self.todoapp} SET completion = {value} WHERE todoID = {row}"
        print("ASSAAS")
        # execute the query
        self.cur.execute(query)
        self.connection.commit()

    def delete(self, item_type="tag", condition=""):
        # generate the query string
        query = f"DROP TABLE IF EXISTS todoapp"

        # add condition if provided
        if condition == "ALL":
            self.cur.execute(query)
            print("Successfully deleted all data!")
            self.connection.commit()

        elif item_type == "tag":
            query = f"DELETE FROM todoapp"
            query += f" WHERE tag=?"
            self.cur.execute(query, (condition,))
            print(f"Successfully deleted {condition}!")
        # execute the query
        self.connection.commit()
