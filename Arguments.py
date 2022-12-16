import datetime

from tabulate import tabulate

from todoapp.Utils.Days import Day
from todoapp.database.database import SQLiteDatabase
import re


# Interfaces
class Argument(object):
    def render(self): pass


class RecordFunction(Argument):
    def __init__(self, db, date, startTime, endTime, task, tag):
        self.db = db
        self.date = date
        self.start_time = startTime
        self.end_time = endTime
        self.task = task
        self.tag = tag
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
        if self.mode == "tags":
            rows = self.db.query(tag_name=self.mode.upper())
            self.print_tags(rows)
        else:
            rows = self.db.query(tag_name=self.mode.upper())
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
        ] for row in rows],
            headers=["#", "Date", "StartTime", "EndTime", "Task", "Tag"]))
