from Arguments import RecordFunction, QueryFunction, DeleteFunction, UpdateFunction, CompleteFunction
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
        parser.add_argument("--complete", type=str, nargs='+')
        args = parser.parse_args()

        if args.record:
            function = RecordFunction(
                db=self.db,
                argument=args.record
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

        if args.complete:
            function = CompleteFunction(
                db=self.db,
                argument=args.complete
            )
            function.render()
