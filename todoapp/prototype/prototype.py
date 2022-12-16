import sqlite3

connection = sqlite3.connect("text_app.db")
cursor = connection.cursor()


def main():
    # Connection to Database

    # Creating Table:
    # Data is stored in tables. Tables have a set of columns and rows
    cursor.execute("CREATE TABLE IF NOT EXISTS text_app (text TEXT)")
    print("Welcome to our todo")
    print("What would you like to do?")
    print("add --> Add an item to our database")
    print("query --> look what's in the database")

    user_input = input("Enter command: ")
    if user_input == "query":
        query()

    if user_input == "add":
        user_input = input("Enter the text you would like to add: ")
        add(user_input)


def add(user_input):
    cursor.execute("INSERT INTO text_app (text) VALUES(?)", [user_input])
    connection.commit()
    print("Success")


def query():
    # Reading Data:
    rows = cursor.execute("SELECT text FROM text_app").fetchall()
    print(rows)
    if len(rows) == 0:
        print("Nothing in the database...please add")
    else:
        for row in rows:
            print(row)


if __name__ == "__main__":
    main()
