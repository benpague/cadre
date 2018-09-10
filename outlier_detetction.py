import  pandas as pd
import os

def outliers(ls):
    q1, q3 = np.percentile(ls, [25, 75])
    iqr = q3 - q1
    lower_bound = q1 - (iqr * 1.5)
    upper_bound = q3 + (iqr * 1.5)
    return(ls > upper_bound)

def