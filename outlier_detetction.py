import pandas as pd
import sqlite3
import os
import settings
import numpy as np


def outlier(ls):
    q1, q3 = np.percentile(ls, [25, 75])
    iqr = q3 - q1
    lower_bound = q1 - (iqr * 1.5)
    upper_bound = q3 + (iqr * 1.5)
    return(ls > upper_bound)


if __name__ == '__main__':
    df = pd.read_csv(os.path.join(settings.PROCESSED_DIR, 'clustered.csv'), index_col=0)
    calv = df[df["CLUSTER"] != 0]
    grpd = calv.groupby('YEAR')
    yr_codes = dict()
    for name, grp in grpd:
        yr_codes[name] = list(grp["PRIMARY_CASE"])
    yr_codes_medical = dict()
    yr_codes_surgical = dict()
    for year, codes in yr_codes.items():
        codes_alp = []
        codes_int = []
        for code in codes:
            try:
                code = int(code)
                codes_int.append(code)
            except Exception:
                codes_alp.append(code)

        yr_codes_surgical[year] = codes_int
        yr_codes_medical[year] = codes_alp

    conn = sqlite3.connect(os.path.join(settings.PROCESSED_DIR, 'cadre.db'))
    outlier_hci_surgical = dict()
    for year, codes in yr_codes_surgical.items():
        codes_hci = dict()
        for code in codes:
            df_x = pd.read_sql_query("select INST_NAME, count(*) as COUNT from claims where YEAR={year} and PRIMARY_CASE={code} group by INST_NAME;".format(year=year, code=code), conn)
            out1 = outlier(df_x["COUNT"])
            out2 = list(df_x["INST_NAME"][out1])
            codes_hci[code] = out2
        outlier_hci_surgical[year] = codes_hci
    conn.close()

    conn = sqlite3.connect(os.path.join(settings.PROCESSED_DIR, 'cadre_db'))
    outlier_hci_medical = dict()
    for year, codes in yr_codes_medical.items():
        codes_hci = dict()
        for code in codes:
            df_x = pd.read_sql_query(
                "select INST_NAME, count(*) as COUNT from claims where YEAR={year} and PRIMARY_CASE='{code}' group by INST_NAME;".format(
                    year=year, code=code), conn)
            out1 = outlier(df_x["COUNT"])
            out2 = list(df_x["INST_NAME"][out1])
            codes_hci[code] = out2
        outlier_hci_medical[year] = codes_hci
    conn.close()

    df_medical = pd.DataFrame.from_dict(outlier_hci_surgical)
    df_surgical = pd.DataFrame.from_dict(outlier_hci_surgical)
    df_medical.reset_index(inplace=True)
    df_surgical.reset_index(inplace=True)
    df_medical["PRIMARY_CASE"] = df_medical["index"]
    df_surgical["PRIMARY_CASE"] = df_surgical["index"]
    df_medical.drop('index', axis=1, inplace=True)
    df_medical.drop('index', axis=1, inplace=True)
    df_medical.to_csv(os.path.join(settings.PROCESSED_DIR, '2015_2017_outliers_medical.csv'))
    df_surgical.to_csv(os.path.join(settings.PROCESSED_DIR, '2015_2017_outliers_surfical.csv'))






