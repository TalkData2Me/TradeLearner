
# coding: utf-8

# In[1]:

def package_data(db=None, ticker=None, start=None, end=None):
    con = sqlite3.connect(db)
    c = con.cursor()
    sql = "select asset_id from assets where ticker='%s'" % ticker #change this!
    c.execute(sql)
    id_list = c.fetchall()
    if len(id_list)==1:
        f_key = id_list[0][0]
    else:
        print 'Error: asset has %s IDs' % str(len(key_list))

    raw_quotes = quotes_historical_yahoo(ticker, start, end) #list of tuples
    data = []
    
    for quote in raw_quotes:
        date_raw = datetime.datetime.fromordinal(int(quote[0]))
        year, month, day = date_raw.year, date_raw.month, date_raw.day
        date_string = str(year)+'-'+str(month)+'-'+str(day)
        record = (f_key, quote[0], date_string, year, month, day, quote[1], quote[2], quote[3], quote[4], quote[5])
        data.append(record)
    
    headers = ('asset_id','gregorian_day','date_string','year','month','day','open','close','high','low','volume')
    
    return {'data':data, 'headers':headers}


# In[2]:

# write2sqlite() takes a given dictionary of tuples and writes them to a designated sqlite database table.

def write2sqlite(db=None, table_name=None, data_dict=None):
    header_string = ', '.join([header for header in data_dict['headers']])
    marks = len(data_dict['headers'])*'?,'
    marks_string = marks[:-1]
    con = sqlite3.connect(db)
    c = con.cursor()
    c.executemany('insert into ' + table_name + ' (' + header_string + ') '
                  'values (' + marks_string +')', data_dict['data'])
    con.commit()
    # don't forget to add 'date modified' field at some pt
    c.close()
    return


# In[3]:

# build_database() creates an sqlite database populated by stocks defined in the code below. 
# Change date1 to adjust how much price history you want.

def build_database(db=None, assets=None, start=None, end=None):
    con = sqlite3.connect(db)
    c = con.cursor()
    c.execute('''CREATE TABLE assets
    (asset_id integer not null primary key,
    ticker text,
    tag text)
    ''')
    
    c.execute('''CREATE TABLE prices
    (price_id integer not null primary key,
    asset_id integer not null,
    gregorian_day integer,
    date_string date,
    year integer,
    month integer,
    day integer,
    open real,
    close real,
    high real,
    low real,
    volume integer,
    FOREIGN KEY (asset_id) REFERENCES assets(asset_id))
    ''')
    
    con.commit()
    c.close()
    
    #add stocks to asset table
    write2sqlite(db=db, table_name='assets', data_dict=assets)
    
    #package price data and write to price table
    for asset in assets['data']:
        prices = package_data(db=db, ticker=asset[0], start=start, end=end)
        write2sqlite(db=db, table_name='prices', data_dict=prices)
    
    return


# In[4]:

def remove_existing_db(path=None):
    if os.path.exists(path) == True:
        os.remove(path)
        print 'old db removed'
    else:
        pass


# In[ ]:



