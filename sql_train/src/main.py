import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from queries.core import insert_data, return_sql_version, create_tables

if __name__ == "__main__":
    # return_sql_version()
    create_tables()
    insert_data()
