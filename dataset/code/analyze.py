import pandas as pd
import numpy as np
def summary(filename):
    '''filename should be a pandas dataframe'''
    print("Description",filename.describe())
    print('*'*100)
    print("Information",filename.info())
    print('*'*100)
    print("Data-Types", filename.dtypes)

def col_check(filename, col):
    ''''''
    if not filename[col].isnull().values.sum():
        pass
    else:
        print("Null count {0} in column {1}".format(filename[col].isnull().values.sum(), col))


def col_desc(filename, col):
    return filename[col].describe()


def col_replace(filename, col, v=None):
    ''' Pass parameters according to required datatype
        # example: - filename[col].replace(np.nan/string/random value, value)
    '''
    return filename[col].replace(np.nan, v)


def col_fillna(filename, col, v=None):
    return filename[col].fillna(v, inplace=True)
