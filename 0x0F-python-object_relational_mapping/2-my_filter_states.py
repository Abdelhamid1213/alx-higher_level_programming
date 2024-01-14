#!/usr/bin/python3
"""
Script to connect to a MySQL server and display values
in the states table of hbtn_0e_0_usa where name matches
the provided argument.

Usage:
    ./2-my_filter_states.py username password database state_name

Arguments:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): MySQL database name.
    state_name (str): Name of the state to search for.

The script connects to the MySQL server running on localhost
at port 3306, constructs an SQL query with the user input, and
executes the query. The results are displayed in ascending order
based on the states' id.

Note:
    This script requires the MySQLdb module.

Example:
    ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
"""

import MySQLdb
import sys


def filter_states(username, password, database, state_name):
    """
    Connect to the MySQL server and display values
    in the states table where name matches the argument.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.
        state_name (str): Name of the state to search for.

    Returns:
        None

    Prints:
        Results of the query in the format (id, name).
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}' \
        ORDER BY id ASC".format(state_name)

    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1], \
        sys.argv[2], sys.argv[3], sys.argv[4]

    filter_states(username, password, database, state_name)
