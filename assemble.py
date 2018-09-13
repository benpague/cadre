import os
import sqlite3
import pandas as pd
import settings
import dateutil

cols = ["SERIES","MONTH","YEAR","INST_NAME","PRIMARY_CASE","SECONDARY_CASE","PATAGE","PATSEX","CLASS_DEF"]

# concatenate data files in csv or xls(x) format to a dataframe
def concatenate():
    files = os.listdir(settings.DATA_DIR)
    full = []
    for f in files:
        if f.endswith('csv'):
            dat = pd.read_csv(os.path.join(settings.DATA_DIR, f), index_col=False, encoding='latin1')
            full.append(dat)
        else:
            dat = pd.read_excel(os.path.join(settings.DATA_DIR, f), index_col=False)
            full.append(dat)

    full_data = pd.concat(full, axis=0, sort=False)
    return(full_data)


# deduplicate concatenated data
def dedup(df):
    df_dedup = df.drop_duplicates(subset=['SERIES'], keep='last')
    return(df_dedup)

def year(x):
    from dateutil.parser import parse
    x = str(x)
    dat = parse(x)
    return(dat.year)

def month(x):
    from dateutil.parser import parse
    x = str(x)
    dat = parse(x)
    return(dat.month)


# create the sqlite db
def db_unlock(db_file):
    conn = sqlite3.connect(os.path.join(settings.PROCESSED_DIR, db_file))
    conn.commit()
    conn.close()


# populate the sqlite db
def create_table(df, db):
    conn = sqlite3.connect(os.path.join(settings.PROCESSED_DIR, db))
    df.to_sql('claims', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    df_con = concatenate()
    df_cadr = dedup(df_con)
    df_cadr["MONTH"]= df_cadr["DATE_ADM"].map(lambda x: month(x))
    df_cadr["YEAR"] = df_cadr["DATE_ADM"].map(lambda x: year(x))
    df_cadr = df_cadr[cols]
    db_unlock('cadre.db')
    create_table(df_cadr, 'cadre.db')

