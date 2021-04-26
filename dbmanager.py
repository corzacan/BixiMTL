import sqlite3 as sl


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sl.connect(db_file)
    except sl.Error as e:
        print(e)

    return conn

