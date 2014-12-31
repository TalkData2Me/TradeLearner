
# coding: utf-8

# In[6]:

def window_data(df=None, prior_days=None):
    df = df.sort(['asset_id','gregorian_day'])
    df['index'] = df.index.values
    for n in prior_days:   # change these to reflect trading days per month, year, etc.
        df2 = df[['index', 'asset_id', 'open', 'high', 'low', 'close', 'volume']].copy()
        df2['index'] = df2['index']+n
        df = pandas.merge(df, df2, how='left', on=('asset_id','index'), left_on=None, right_on=None,
                      left_index=False, right_index=False, sort=True,
                      suffixes=('', '_m'+str(n)), copy=True)
        df2=None
    df = df.replace([numpy.inf, -numpy.inf, numpy.NINF,'',numpy.nan], numpy.nan).dropna(axis=0)
    return df


# In[4]:

def add_interactions(df=None):
    cols = list(df.columns.values)
    to_expand = []
    for col in cols:
        if df[col].dtype == 'float':
            to_expand.append(col)
    for coli in to_expand:
        for colj in to_expand:
            df[coli+'_'+colj] = (df[coli] - df[colj]) / df[colj]
    for col in to_expand:
        df = df.drop(col,1)
    return df


# In[5]:

def expnd_w_fctns(df=None):
    cols = list(df.columns.values)
    to_expand = []
    for col in cols:
        if df[col].dtype == 'float':
            to_expand.append(col)
    for col in to_expand:
        df[col+'_sqrd'] = df[col]**2
        df[col+'_cubd'] = df[col]**3
        df[col+'_cos'] = numpy.cos(df[col])
        df[col+'_sin'] = numpy.sin(df[col])
    return df


# In[ ]:



