
# coding: utf-8

# In[ ]:

def kmeans_cluster(X=None,y=None, n_clusters=None, n_init=None, max_iter=None, n_jobs=None):
    from sklearn import cluster
    
    km = cluster.KMeans(n_clusters=n_clusters, n_init=n_init, max_iter=max_iter, n_jobs=n_jobs)
    
    cols = list(X.columns.values)
    clusterable = []
    base_fields = []
    
    for col in cols:
        if X[col].dtype == 'float':
            clusterable.append(col)
        else:
            base_fields.append(col)
    
    km.fit(X[clusterable])
    clstr = pandas.DataFrame(km.predict(y[clusterable]))
    clstr.rename(columns=lambda x: str(x).replace('0', 'Cluster'), inplace=True)
    result = pandas.merge(y[base_fields],clstr,left_index=True,right_index=True)
    return result

