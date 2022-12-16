import sqlite3
import pytest


class TestTodoApp:

    @pytest.fixture
    def setup(self):
        connection = sqlite3.connect(':memory:')
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE items
            (date text, trans text, symbol text, qty real, price real)''')
        sample_data = [
            ('2021-09-12', 'Take', 'Coin', 1000, 45.0)
        ]
        cursor.executemany('INSERT INTO items VALUES(?, ?, ?, ?, ?)', sample_data)
        yield connection

    def test_connection(self, setup):
        cursor = setup
        assert len(list(cursor.execute('SELECT * FROM items'))) == 1
