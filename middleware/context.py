
import os

# This is a bad place for this import
import pymysql

def get_db_info():
    """
    This is crappy code.

    :return: A dictionary with connect info for MySQL
    """
    db_host = os.environ.get("DBHOST", None)
    db_user = os.environ.get("DBUSER", None)
    db_password = os.environ.get("DBPASSWORD", None)

    if db_host is not None:
        db_info = {
            "host": "thesequels.cx5yyazvwywf.us-east-2.rds.amazonaws.com",
            "user": "admin",
            "password": "password",
            "cursorclass": pymysql.cursors.DictCursor
        }
    else:
        db_info = {
            "host": "thesequels.cx5yyazvwywf.us-east-2.rds.amazonaws.com",
            "user": "admin",
            "password": "password",
            "cursorclass": pymysql.cursors.DictCursor
        }

    return db_info
