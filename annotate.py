import pandas as pd
import sqlite3
import os

def cases_year():
    cases = dict()
    conn = sqlite3.connect(os.path.join(settings.PROCESSED_DIR, 'cadre.db'))
    df_y = pd.read_sql_query("select DISTINCT(YEAR) from claims;", conn)
    years = df_y["YEAR"].tolist()

    for year in years:
        df = pd.read_sql_query("select PRIMARY_CASE as CASE, YEAR, count(*) as COUNT from claims where YEAR={year} group by PRIMARY CASE, YEAR;".format(year=year), conn)
        cases[year] = df
    conn.close()
    return(cases)


def cluster(df):
    #sklearn k-means
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(df[['COUNT', 'M']])
    df['CLUSTER'] = kmeans.labels_
    return(df)


if __name__ == "__main__":
    df_cases = cases_year()
    target = dict()
    yrs = [k for k, v in df_cases.items()]
    origin = min(yrs)
    yrs = yrs[1:]
    for yr in yrs:
        target[yr] = df_cases[yr]

    col_m = ["PRIMARY_CASE", "YEAR", "COUNT", "M"]
    dfs = []
    for k, v in target.items():
        new_v = pd.merge(df_cases[origin], v, on='PRIMARY_CASE', how='right')
        new_v["M"] = (new_v["COUNT_y"] - new_v["COUNT_x"]) / (new_v["YEAR_y"] - new_v["YEAR_x"])
        new_v["YEAR"] = new_v["YEAR_y"]
        new_v["COUNT"] = new_v["COUNT_y"]
        few_cols = new_v[col_m]
        few_cols = few_cols.fillna(0)
        df_clust = cluster(few_cols)
        dfs.append(df_clust)
    clustered_cases = pd.concat(dfs, axis=0)
    clustered_cases.to_csv(os.path.join(settings.PROCESSED_DIR, 'clustered.csv'))