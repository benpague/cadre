import os
import settings
import pandas as pd
import sqlite3
import csv

def unlock_db(db_filename):
    '''Replace db_filename with the name of SQLite3 db'''
    conn = sqlite3.connect(db_filename)
    conn.commit()
    conn.close()

def concatenate(prefix="CLAIMS"):
    files = os.listdir(settings.DATA_DIR)
    full = []
    for f in files:
        if not f.startswith(prefix):
            continue

        data = pd.read_csv(os.path.join(settings.DATA_DIR, f),index_col=False)
        full.append(data)


    df = pd.concat(full, axis=0)


    df.to_csv(os.path.join(settings.PROCESSED_DIR))