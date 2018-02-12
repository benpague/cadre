import os
import settings
import pandas as pd
import sqlite3
import csv
import settings
from dateutil.parser import parse

def year(x):
    date = parse(x)
    return(date.year)

def month(x):
    date = parse(x)
    return(date.month)


def unlock_db(db_filename):
    '''Replace db_filename with the name of SQLite3 db'''
    conn = sqlite3.connect(db_filename)
    conn.commit()
    conn.close()

def create_table():
    df = pd.read_csv(os.path.join(settings.DATA_DIR,"claims.csv"))
    df["YEAR"] = df["DATE_ADM"].map(lambda x: year(x))
    df["MONTH"] = df["DATE_ADM"].map(lambda x: month(x))
    unlock_db(os.path.join(settings.PROCESSED_DIR,"claims.db"))
    df.to_sql(os.path.join(settings.PROCESSED_DIR, 'claims'), conn, if_exists='replace',index=False)

if __name__ == "__main__":
    create_table()

