#!/usr/bin/python3
"""
Script to connect to a MySQL server and retrieve states
from the hbtn_0e_0_usa database that start with 'N'.

Usage:
    ./1-filter_states.py username password database

Arguments:
    username (str): MySQL username.
    password (str): MySQL password.
    database (str): MySQL database name.

The script connects to the MySQL server running on localhost
at port 3306 and executes a query to select states whose names
start with 'N'. The results are displayed in ascending order
based on the states' id.

Note:
    This script requires the MySQLdb module.

Example:
    ./1-filter_states.py root root hbtn_0e_0_usa
"""

import MySQLdb
import sys


def filter_states(username, password, database):
    """
    Connect to the MySQL server and retrieve states starting with 'N'.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): MySQL database name.

    Returns:
        None

    Prints:
        Results of the query in the format (id, name).
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    filter_states(username, password, database)
