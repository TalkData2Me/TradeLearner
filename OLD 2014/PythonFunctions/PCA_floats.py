
# coding: utf-8

# In[ ]:

def PCA_floats(df=None,n_comps=None,whiten=None):
    from sklearn.decomposition import PCA
    print 'Original data size: ' + str(df.shape)
    cols = list(df.columns.values)
    to_pca = []
    base_fields = []
    
    for col in cols:
        if df[col].dtype == 'float':
            to_pca.append(col)
        else:
            base_fields.append(col)
    pca = PCA(n_components=n_comps,whiten=whiten)
    pca_df = pandas.DataFrame(pca.fit_transform(df[to_pca]))
    pca_df.rename(columns=lambda x: str(x).replace('0', 'Zero'), inplace=True)
    pca_df.rename(columns=lambda x: str(x).replace('1', 'One'), inplace=True)
    pca_df.rename(columns=lambda x: str(x).replace('2', 'Two'), inplace=True)
    pca_df.rename(columns=lambda x: str(x).replace('3', 'Three'), inplace=True)
    pca_df.rename(columns=lambda x: str(x).replace('4', 'Four'), inplace=True)
    pca_df.rename(columns=lambda x: str(x).replace('5', 'Five'), inplace=True)
    pca_df.rename(columns=lambda x: str(x).replace('6', 'Six'), inplace=True)
    pca_df.rename(columns=lambda x: str(x).replace('7', 'Seven'), inplace=True)
    pca_df.rename(columns=lambda x: str(x).replace('8', 'Eight'), inplace=True)
    pca_df.rename(columns=lambda x: str(x).replace('9', 'Nine'), inplace=True)
    df = pandas.merge(df[base_fields],pca_df,left_index=True,right_index=True)
    print 'PCA data size: ' + str(df.shape)
    return df

