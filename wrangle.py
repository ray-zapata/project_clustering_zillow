#Z0096


# import standard libraries
import pandas as pd
import numpy as np

# import from other modules
import explore
import acquire
import prepare


#################### Wrangle Zillow ####################


# create variable to hold SQL query
query = '''
    SELECT *, properties_2017.id AS property_id
    FROM properties_2017
    INNER JOIN predictions_2017
        USING(parcelid)
    LEFT OUTER JOIN airconditioningtype
        USING(airconditioningtypeid)
    LEFT OUTER JOIN architecturalstyletype
        USING(architecturalstyletypeid)
    LEFT OUTER JOIN buildingclasstype
        USING(buildingclasstypeid)
    LEFT OUTER JOIN heatingorsystemtype
        USING(heatingorsystemtypeid)
    LEFT OUTER JOIN propertylandusetype
        USING(propertylandusetypeid)
    LEFT OUTER JOIN storytype
        USING(storytypeid)
    LEFT OUTER JOIN typeconstructiontype
        USING(typeconstructiontypeid)
    LEFT OUTER JOIN unique_properties
        USING(parcelid)
    WHERE
        transactiondate LIKE '2017%%' AND
        latitude IS NOT NULL AND
        longitude IS NOT NULL;'''


def get_single_units(df):
    '''
    '''

    # create list of single unit propertylandusedesc
    single_prop_types = ['Single Family Residential', 'Condominium',
                         'Mobile Home', 'Townhouse'
                         'Manufactured, Modular, Prefabricated Homes']
    # filter for most-likely single unit properties
    df = df[df.propertylandusedesc.isin(single_prop_types)]
    df = df[(df.bedroomcnt > 0) & (df.bedroomcnt <= 10)]
    df = df[(df.bathroomcnt > 0) & (df.bathroomcnt <= 10)]

    return df


def drop_zillow_nulls(df):
    '''
    '''

    # set drop unnecessary id columns
    df = df.drop(columns=['id', 'id.1'])
    # drop -typeid columns that are redundant to desc columns
    df = df.drop(columns=(df.filter(regex='typeid').columns))
    # drop regionid- columns that are not clearly defined or mislabeled
    df = df.drop(columns=(df.filter(regex='regionid').columns))
    # drop columns with no clear context, redundant values
    df = df.drop(columns=['assessmentyear', 'calculatedbathnbr',
                          'finishedsquarefeet12', 'propertycountylandusecode',
                          'propertylandusedesc', 'rawcensustractandblock',
                          'roomcnt'])
    # drop columns and rows missing more than 25% of total observations
    df = prepare.drop_null_values(df)
    # drop all rows with null values for any tax fields
    df = df[df.taxvaluedollarcnt.isnull() == False]
    df = df[df.landtaxvaluedollarcnt.isnull() == False]
    df = df[df.structuretaxvaluedollarcnt.isnull() == False]
    df = df[df.taxamount.isnull() == False]
    # drop the low-count of null rows rather than impute
    df = df[df.fullbathcnt.isnull() == False]
    df = df[df.yearbuilt.isnull() == False]
    df = df[df.calculatedfinishedsquarefeet.isnull() == False]
    df = df[df.censustractandblock.isnull() == False]

    return df


def fix_zillow_structure(df):
    '''
    '''

    # convert to drop float decimals
    df.fips = df.fips.astype(int)
    # replace fips numerical codes with string county names and rename
    df.fips = np.where(df.fips == 6037, 'Los Angeles', df.fips)
    df.fips = np.where(df.fips == '6059', 'Orange', df.fips)
    df.fips = np.where(df.fips == '6111', 'Ventura', df.fips)
    # rename column to reflect new values
    df = df.rename(columns=({'fips':'county'}))
    # convert columns to correct data type
    df.transactiondate = pd.to_datetime(df.transactiondate)
    df.bedroomcnt = df.bedroomcnt.astype(int)
    df.yearbuilt = df.yearbuilt.astype(int)
    # convert latitude and longitude from whole numbers to coords
    df.latitude = df.latitude / 1_000_000
    df.longitude = df.longitude / 1_000_000

    return df


def rename_zillow_cols(df):
    '''
    '''

    # rename columns
    col_dict = {'bathroomcnt':'bathrooms', 
                'bedroomcnt':'bedrooms', 
                'calculatedfinishedsquarefeet':'structure_square_feet',
                'censustractandblock':'census_tractcode',
                'fullbathcnt':'full_bathrooms',
                'landtaxvaluedollarcnt':'land_value_usd',
                'logerror':'log_error',
                'lotsizesquarefeet':'lot_square_feet',
                'parcelid':'parcel_id',
                'structuretaxvaluedollarcnt':'structure_value_usd',
                'taxamount':'tax_amount_usd',
                'taxvaluedollarcnt':'property_value_usd',
                'transactiondate':'transaction_date',
                'yearbuilt':'year_built'
               }
    df = df.rename(columns=col_dict)

    return df


def shed_zillow_outliers(df):
    '''
    '''

    # assign columns to remove IQR outliers from
    outlier_cols = ['land_value_usd', 'property_value_usd', 
                    'structure_square_feet', 'tax_amount_usd']
    # run function to remove rows with outlier values
    df = prepare.shed_iqr_outliers(df, col_list=outlier_cols)

    return df


def encode_variables(df):
    '''
    '''

    # encode county variable to seperate columns
    df = pd.get_dummies(df, columns=['county']).rename(columns={
                                            'county_Los Angeles':'la_county',
                                            'county_Orange':'orange_county',
                                            'county_Ventura':'ventura_county'})
    df['county'] = np.where(df.la_county == 1, 1, 0)
    df['county'] = np.where(df.orange_county == 1, 2, df.county)
    df['county'] = np.where(df.ventura_county == 1, 3, df.county)

    return df


def add_new_features(df):
    '''
    '''

    # add new features created from other variables
    df['acreage'] = df.lot_square_feet * 0.00002295682
    df['age'] = 2017 - df.year_built
    df['bedrooms_per_sqft'] = df.bedrooms / df.structure_square_feet
    df['room_count'] = df.bedrooms + df.bathrooms
    df['transaction_month'] = pd.DatetimeIndex(df.transaction_date).month

    return df


def add_clusters(train, validate, test):
    '''
    '''

    # create lat_long_clstr
    train, validate, test = explore.create_clusters(train, validate, test,
                        ['latitude', 'longitude'], 'lat_long', k=5)
    # create lot_rooms_clstr
    train, validate, test = explore.create_clusters(train, validate, test,
                        ['acreage', 'room_count'], 'lot_rooms', k=5)
    # create bed_sqft_age_clstr
    train, validate, test = explore.create_clusters(train, validate, test,
                        ['bedrooms_per_sqft', 'age'], 'bed_sqft_age', k=5)
    # create bed_sqft_age_clstr
    train, validate, test = explore.create_clusters(train, validate, test,
                        ['census_tractcode', 'structure_square_feet', 'age'],
                        'tract_size_age', k=5)

    return train, validate, test


def prep_zillow(query=query, clusters=True):
    '''
    '''

    # read in initial DataFrame
    df = acquire.get_sql(query, 'zillow')
    # store count of inital observations
    init_observ = df.shape[0]
    # remove duplicate properties keeping most recent sell date
    df = df.sort_values('transactiondate')\
           .drop_duplicates('parcelid', keep='last')
    # filter out properties not likely single unit
    df = get_single_units(df)
    # drop null values that not going to be imputed
    df = drop_zillow_nulls(df)
    # fix data types and structure issues
    df = fix_zillow_structure(df)
    # rename columns
    df = rename_zillow_cols(df)
    # remove outliers for certain columns using IQR
    df = shed_zillow_outliers(df)
    # reorganize columns alphabetically for readability
    cols = list(df)
    cols.sort()
    df = df[cols]

    return df


def wrangle_zillow(query=query, clusters=True):
    '''
    '''

    # read in initial DataFrame
    df = acquire.get_sql(query, 'zillow')
    # store count of inital observations
    init_observ = df.shape[0]
    # remove duplicate properties keeping most recent sell date
    df = df.sort_values('transactiondate')\
           .drop_duplicates('parcelid', keep='last')
    # filter out properties not likely single unit
    df = get_single_units(df)
    # drop null values that not going to be imputed
    df = drop_zillow_nulls(df)
    # fix data types and structure issues
    df = fix_zillow_structure(df)
    # rename columns
    df = rename_zillow_cols(df)
    # remove outliers for certain columns using IQR
    df = shed_zillow_outliers(df)
    # add new features to DataFrame
    df = add_new_features(df)
    # encode county variables
    df = encode_variables(df)
    # reorganize columns alphabetically for readability
    cols = list(df)
    cols.sort()
    df = df[cols]
    # split data into train, validate, test
    train, validate, test = prepare.split_data(df)
    # impute missing values from lot_square_feet column
    train, validate, test = prepare.impute_null_values(train, validate, test,
                                    col_list=['lot_square_feet', 'acreage'])
    # add clusters created in exploration if called
    if clusters == True:
        train, validate, test = add_clusters(train, validate, test)
    # split into X, y
    X_train, y_train, \
    X_validate, y_validate, \
    X_test, y_test = prepare.split_xy(train, validate, test, 'log_error')
    # print output percentages for data prep and split
    post_observ = df.shape[0]
    train_observ = X_train.shape[0]
    val_observ = X_validate.shape[0]
    test_observ = X_test.shape[0]
    x_observ = train_observ + val_observ + test_observ
    print(f'''
*----------------------------------------*
|  ***   Data Preparation Summary   ***  |
*----------------------------------------*
|                                        |
|       Initial Observations: {init_observ:,}     |
|      Prepared Observations: {post_observ:,}     |
|          Null Loss Percent: {1 - (post_observ / init_observ):.2%}     |
|                                        |
|       X_train Observations: {train_observ:,}     |
|           Percent of Total: {train_observ / init_observ:.0%}        |
|               Percent of X: {train_observ / x_observ:.0%}        |
|                                        |
|    X_validate Observations: {val_observ:,}     |
|           Percent of Total: {val_observ / init_observ:.0%}        |
|               Percent of X: {val_observ / x_observ:.0%}        |
|                                        |
|        X_test Observations: {test_observ:,}     |
|           Percent of Total: {test_observ / init_observ:.0%}        |
|               Percent of X: {test_observ / x_observ:.0%}        |
|                                        |
*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*''')

    return X_train, y_train, X_validate, y_validate, X_test, y_test