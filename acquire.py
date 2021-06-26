#Z0096


# import standard libraries
import pandas as pd
import numpy as np

# import file checker
from os.path import isfile

# import connect function for database
from env import get_connection


#################### Acquire Data ####################


def get_sql(query, db_name, use_csv=True):
    '''

    Takes SQL query and database name as `string` and runs through
    pandas read_sql function, using get_connection from env.py.
    Requires Codeup database login credentials.

    use_csv=True will use data from existing CSV file if one exists,
    default behavior

    use_csv=False will obtain new query return and overwrite existing
    CSV if one exists

    '''

    # check if CSV file already exists or use_csv=False
    if use_csv == False or isfile(f'{db_name}.csv') == False:
        # acquire data from database
        df = pd.read_sql(query, get_connection(db_name))
        # write acquired data to CSV file
        df.to_csv(f'{db_name}.csv', index=False)
        # drop any existing duplicates
        df = df.drop_duplicates()
        # replace whitespace with nan values
        df = df.replace(r'^\s*$', np.NaN, regex=True)
    else:
        # read into DataFrame from CSV file
        df = pd.read_csv(f'{db_name}.csv')

    return df


#################### Summarize Data ####################


def cols_with_null_rows(df):
    '''
    '''

    cols = list(df)
    cols.sort()
    missing_df = pd.DataFrame()
    for col in cols:
        rows_missing = df[col].isnull().sum()
        total_rows = df[col].shape[0]
        missing_row_dict = {'':col, 'num_rows_missing':f'{rows_missing:.0f}',
                    'pct_rows_missing':f'{(rows_missing / total_rows):.2%}'}
        missing_df = missing_df.append(missing_row_dict, ignore_index=True)
    missing_df = missing_df.set_index('')

    return missing_df


def rows_with_null_cols(df):
    '''
    '''
    
    num_cols_missing = df.isnull().sum(axis=1)
    total_cols = df.shape[1]
    pct_cols_missing = (num_cols_missing / total_cols)
    missing_df = pd.DataFrame({'num_cols_missing':num_cols_missing,
                    'pct_cols_missing':pct_cols_missing}).reset_index()\
                    .groupby(['num_cols_missing', 'pct_cols_missing']).count()\
                    .rename(columns={'index':'num_rows'}).reset_index()\
                    .set_index('num_cols_missing')

    return missing_df


def summarize(df):
    '''
    
    Takes in a single argument as a pandas DataFrame and outputs
    several statistics on passed DataFrame
    
    '''
    
    print('\n--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--\n')
    print('*** First Three Observations of DataFrame\n')
    print(df.head(3).T)
    print('\n--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--\n')
    print ('*** DataFame .info()\n')
    print(df.info())
    print('\n--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--\n')
    print('*** DataFrame .describe().T\n')
    print (df.describe().T)
    print('\n--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--~--\n')
    print('*** Value Counts for DataFrame Columns\n')
    cat_cols = [col for col in list(df) if df[col].dtype == 'O']
    num_cols = [col for col in list(df) if df[col].dtype != 'O']
    for col in list(df):
        if col in cat_cols:
            print(f'+ {df[col].name}\n\n{df[col].value_counts()}\n')
        else:
            print(f'+ {df[col].name}\n\n{df[col].value_counts(bins=10, sort=False)}\n')
