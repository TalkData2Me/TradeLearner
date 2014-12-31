
# coding: utf-8

# In[ ]:

def normalize(df=None,minimum=None,maximum=None):
    from sklearn import preprocessing
    cols = list(df.columns.values)
    to_norm = []
    base_fields = []
    df = df.replace([numpy.inf, -numpy.inf, numpy.NINF,'',numpy.nan], numpy.nan).dropna(axis=0)
    for col in cols:
        if df[col].dtype == 'float':
            to_norm.append(col)
        else:
            base_fields.append(col)
    min_max_scaler = preprocessing.MinMaxScaler(feature_range=(minimum, maximum))
    df = df.replace([numpy.inf, -numpy.inf, numpy.NINF,'',numpy.nan], numpy.nan).dropna(axis=0)
    norm_df = pandas.DataFrame(min_max_scaler.fit_transform(df[to_norm]))
    df = df.replace([numpy.inf, -numpy.inf, numpy.NINF,'',numpy.nan], numpy.nan).dropna(axis=0)
    norm_df.rename(columns=lambda x: str(x).replace('0', 'Zero'), inplace=True)
    norm_df.rename(columns=lambda x: str(x).replace('1', 'One'), inplace=True)
    norm_df.rename(columns=lambda x: str(x).replace('2', 'Two'), inplace=True)
    norm_df.rename(columns=lambda x: str(x).replace('3', 'Three'), inplace=True)
    norm_df.rename(columns=lambda x: str(x).replace('4', 'Four'), inplace=True)
    norm_df.rename(columns=lambda x: str(x).replace('5', 'Five'), inplace=True)
    norm_df.rename(columns=lambda x: str(x).replace('6', 'Six'), inplace=True)
    norm_df.rename(columns=lambda x: str(x).replace('7', 'Seven'), inplace=True)
    norm_df.rename(columns=lambda x: str(x).replace('8', 'Eight'), inplace=True)
    norm_df.rename(columns=lambda x: str(x).replace('9', 'Nine'), inplace=True)
    df = pandas.merge(df[base_fields],norm_df,left_index=True,right_index=True)
    df = df.replace([numpy.inf, -numpy.inf, numpy.NINF,'',numpy.nan], numpy.nan).dropna(axis=0)
    return df

