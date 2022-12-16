from todoapp.database.database import SQLiteDatabase
import argparse
from tabulate import tabulate
import re
import datetime


class Todo:
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
        parser.add_argument("--delete", type=str, nargs='+')
        parser.add_argument("--record", type=str, nargs='+')
        args = parser.parse_args()

        if args.record:
            date = args.record[0]
            start_time = args.record[1]
            end_time = args.record[2]
            task = args.record[3]
            tag = re.sub(r'[\W_]', '', args.record[4]).upper()
            current_date_time = datetime.datetime.now()

            if date == "today":
                date = current_date_time
            self.db.insert(
                date=current_date_time,
                startTime=start_time,
                endTime=end_time,
                task=task,
                tag=tag
            )
        if args.query:
            if args.query == "tags":
                rows = self.db.query(tag_name=args.query.upper())
                print(tabulate([[
                    row[0],
                ] for row in rows],
                    headers=["Tags"]))
            else:
                rows = self.db.query(tag_name=args.query.upper())
                print(tabulate([[
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                ] for row in rows],
                    headers=["#", "Date", "StartTime", "EndTime", "Task", "Tag"]))
        if args.delete:
            item_type = args.delete[0]
            condition = args.delete[1].upper()
            self.db.delete(item_type=item_type, condition=condition)

        if args.update:
            print(f"row={args.update[0]}, value={args.update[1]}")
            self.db.update(row=args.update[0], value=args.update[1])
