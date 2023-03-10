import datetime
from tabulate import tabulate
from todoapp.Utils.Days import Day
import re


# Interfaces
class Argument(object):
    def render(self): pass


class RecordFunction(Argument):
    def __init__(self, db, argument):
        self.db = db
        self.date = argument[0]
        self.start_time = argument[1]
        self.end_time = argument[2]
        self.task = argument[3]
        self.tag = argument[4]
        self.current_date_time = datetime.datetime.now()

    def render(self):
        if self.date == Day.Today.name:
            self.date = self.current_date_time
        self.db.insert(
            date=self.current_date_time,
            startTime=self.start_time,
            endTime=self.end_time,
            task=self.task,
            tag=re.sub(r'[\W_]', '', self.tag).upper()
        )


class QueryFunction(Argument):
    def __init__(self, db, mode):
        self.db = db
        self.mode = mode

    def render(self):
        rows = self.db.query(tag_name=self.mode.upper())
        if self.mode == "tags":
            self.print_tags(rows)
        else:
            self.print_info(rows)

    def print_tags(self, rows):
        print(tabulate([[
            row[0],
        ] for row in rows],
            headers=["Tags"]))

    def print_info(self, rows):
        print(tabulate([[
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            "Not Completed" if row[6] == 0 else "Done"
        ] for row in rows],
            headers=["#", "Date", "StartTime", "EndTime", "Task", "Tag", "Status"]))


class DeleteFunction(Argument):
    def __init__(self, db, argument):
        self.db = db
        self.argument = argument

    def render(self):
        if self.argument[0].upper() == "ALL":
            self.db.drop()
        else:
            self.db.delete(condition=self.argument[1].upper())


class UpdateFunction(Argument):
    def __init__(self, db, argument):
        self.db = db
        self.argument = argument

    def render(self):
        self.db.update(row=self.argument[0], value=self.argument[1])


class CompleteFunction(Argument):
    def __init__(self, db, argument):
        self.db = db
        self.argument = argument

    def render(self):
        self.db.complete(todo_ID=self.argument[0])
