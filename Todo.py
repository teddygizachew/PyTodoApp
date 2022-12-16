from Arguments import RecordFunction, QueryFunction, DeleteFunction, UpdateFunction
from todoapp.database.database import SQLiteDatabase
import argparse


class TodoApp:
    def __init__(self):
        self.db = SQLiteDatabase()
        self.db.connect()
        self.db.create_table()

    def start(self):
        # create an instance of the SQLiteDB class
        # connect to the database file

        parser = argparse.ArgumentParser(description="Todo App")
        parser.add_argument("--query", type=str)
        parser.add_argument("--update", type=str, nargs='+')
        parser.add_argument("--remove", type=str, nargs='+')
        parser.add_argument("--record", type=str, nargs='+')
        args = parser.parse_args()

        if args.record:
            function = RecordFunction(
                db=self.db,
                date=args.record[0],
                startTime=args.record[1],
                endTime=args.record[2],
                task=args.record[3],
                tag=args.record[4]
            )
            function.render()

        if args.query:
            function = QueryFunction(db=self.db, mode=args.query)
            function.render()

        if args.remove:
            function = DeleteFunction(
                db=self.db,
                argument=args.remove
            )
            function.render()

        if args.update:
            function = UpdateFunction(
                db=self.db,
                argument=args.update
            )
            function.render()
