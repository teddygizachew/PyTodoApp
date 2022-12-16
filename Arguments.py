import datetime

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
        self.db = SQLiteDatabase()

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


class InsertFunction(Argument):
    def __init__(self, db, date, startTime, endTime, task, tag):
        self.db = db
        self.date = date
        self.start_time = startTime
        self.end_time = endTime
        self.task = task
        self.tag = tag
        self.current_date_time = datetime.datetime.now()
        self.db = SQLiteDatabase()

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
